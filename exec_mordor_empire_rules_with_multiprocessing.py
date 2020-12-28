import os
from elasticsearch import Elasticsearch
from helk_info import HELK_IP
import json
import re
from multiprocessing import Pool
import time
import hashlib
import yaml
from functools import cmp_to_key
import datetime

POOL_SIZE = 10


def hash(search_doc_list, tactic, technique, tech_code, eval_phase, eval_step):
    hash_str = ""
    for doc_dict in search_doc_list:
        doc_str = json.dumps(doc_dict)
        hash_str += doc_str
    hash_str += tactic + technique + tech_code + eval_phase + eval_step

    md5 = hashlib.md5()
    md5.update(hash_str.encode('UTF-8'))
    return md5.hexdigest()


def getTimeStamp(jsonobj):
    return datetime.datetime.strptime(jsonobj['_source']['@timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')


def getTimeDifference(jsonobjA, jsonobjB):
    timeA = getTimeStamp(jsonobjA)
    timeB = getTimeStamp(jsonobjB)
    if timeA.__gt__(timeB):
        return (timeA - timeB).seconds
    else:
        return (timeB - timeA).seconds


# 定义时间比较器，用于排序
def cmp_datetime(a, b):
    a_datetime = getTimeStamp(a)
    b_datetime = getTimeStamp(b)

    if a_datetime.__gt__(b_datetime):
        return 1
    elif a_datetime.__lt__(b_datetime):
        return -1
    else:
        return 0


def getItemList():

    item_list = []
    step_dir = 'mordor_empire_dst'

    for step in os.listdir(step_dir):
        step_path = step_dir + '/' + step
        f = open(step_path)
        item = yaml.safe_load(f)

        search_doc_a = ""
        search_doc_b = ""
        search_doc_c = ""
        search_doc_list = []
        if ("search_doc_a" in item.keys()):
            search_doc_a = item["search_doc_a"]
        if ("search_doc_b" in item.keys()):
            search_doc_b = item["search_doc_b"]
        if ("search_doc_c" in item.keys()):
            search_doc_c = item["search_doc_c"]

        tactic = item["tactic"]
        technique = item["technique"]
        tech_code = item["tech_code"]
        eval_phase = item["eval_phase"]
        eval_step = item["eval_step"]

        if (search_doc_a is not ""):
            search_doc_list.append(search_doc_a)
        if (search_doc_b is not ""):
            search_doc_list.append(search_doc_b)
        if (search_doc_c is not ""):
            search_doc_list.append(search_doc_c)

        item = (search_doc_list, tactic, technique, tech_code, eval_phase, eval_step)
        item_list.append(item)

    return item_list


def exec_rule(item):
    search_doc_list = item[0]
    tactic = item[1]
    technique = item[2]
    tech_code = item[3]
    eval_phase = item[4]
    eval_step = item[5]
    es = Elasticsearch(HELK_IP + ':9200', timeout=30)

    count = 0

    rule_count = len(search_doc_list)

    if (rule_count == 3):
        search_doc_a = search_doc_list[0]
        search_doc_b = search_doc_list[1]
        search_doc_c = search_doc_list[2]
        res_a = es.search(index="logs-endpoint-winevent-*", body=search_doc_a)
        res_b = es.search(index="logs-endpoint-winevent-*", body=search_doc_b)
        res_c = es.search(index="logs-endpoint-winevent-*", body=search_doc_c)

        list_a = res_a["hits"]["hits"]
        list_b = res_b["hits"]["hits"]
        list_c = res_c["hits"]["hits"]

        # 对list_a、list_b、list_c 列表分别按照时间先后排序
        list_a.sort(key=cmp_to_key(cmp_datetime))
        list_b.sort(key=cmp_to_key(cmp_datetime))
        list_c.sort(key=cmp_to_key(cmp_datetime))

        # 当找到一组匹配的记录时，用来跳过当前的a_doc和b_doc.
        match_a_b_c = False

        for a_doc in list_a:
            for b_doc in list_b:
                if (getTimeDifference(a_doc, b_doc) <= 1):
                    for c_doc in list_c:

                        if (getTimeDifference(a_doc, c_doc) <= 1 and getTimeDifference(b_doc, c_doc) <= 1):
                            count = count + 1
                            match_a_b_c = True
                            list_b.remove(b_doc)
                            list_c.remove(c_doc)
                if match_a_b_c:
                    match_a_b_c = False
                    break    

    elif (rule_count == 2):

        search_doc_a = search_doc_list[0]
        search_doc_b = search_doc_list[1]
        res_a = es.search(index="logs-endpoint-winevent-*", body=search_doc_a)
        res_b = es.search(index="logs-endpoint-winevent-*", body=search_doc_b)

        list_a = res_a["hits"]["hits"]
        list_b = res_b["hits"]["hits"]

        # 对list_a、list_b、list_c 列表分别按照时间先后排序
        list_a.sort(key=cmp_to_key(cmp_datetime))
        list_b.sort(key=cmp_to_key(cmp_datetime))

        for a_doc in list_a:
            for b_doc in list_b:
                if (getTimeDifference(a_doc, b_doc) <= 1):
                    count = count + 1
                    list_b.remove(b_doc)
                    # 当找到匹配的记录后, 跳过当前的a_doc 和 b_doc
                    break

    elif (rule_count == 1):

        search_doc_c = search_doc_list[0]
        res_c = es.search(index="logs-endpoint-winevent-*", body=search_doc_c)

        count = res_c['hits']['total']['value']

    print(count)

    action = {
        "Tactic": tactic,
        "Technique": technique,
        "Tech_code": tech_code,
        "EvalStep": eval_step,
        "EvalPhase": eval_phase,
        "EventCount": count,
    }

    doc_id = hash(search_doc_list, tactic, technique, tech_code, eval_phase, eval_step)

    es.index(index="represent_7", body=action, id=doc_id)


def main():
    item_list = getItemList()
    start_time = time.time()
    with Pool(POOL_SIZE) as pool:
        results = pool.map(exec_rule, item_list)
    end_time = time.time()

    # 当线程池大小为1时，用时44.5s； 当线程池大小为10时， 用时10.8s。说明线程池确实有用
    use_time = end_time - start_time
    print(use_time)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)

