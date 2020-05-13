import os
from elasticsearch import Elasticsearch
from helk_info import HELK_IP
import json
import re
from multiprocessing import Pool
import time

POOL_SIZE = 10

def getItemList():
    item_list = []
    procedure_dir = 'dst_procedures'
    for procedure in os.listdir(procedure_dir):
        procedure_path = procedure_dir + '/' + procedure
        search_doc = ""
        tactic = ""
        technique = ""
        tech_code = ""

        for id, line in enumerate(open(procedure_path)):
            if id == 0:
                search_doc = eval(line.strip())
            if re.match('tactic', line):
                # 用eval可以去掉python字符串两端的引号
                tactic = eval(line.split('=')[1].strip())
            elif re.match('technique', line):
                technique = eval(line.split('=')[1].strip())
            elif re.match('procedure', line):
                procedure = eval(line.split('=')[1].strip())
            elif re.match('tech_code', line):
                tech_code = eval(line.split('=')[1].strip())

        item = (search_doc, tactic, technique, procedure, tech_code)
        item_list.append(item)
    return item_list
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

def exec_rule(item):
    es = Elasticsearch(HELK_IP + ':9200')
    search_doc = item[0]
    res = es.search(index="logs-endpoint-winevent-*",body=search_doc)
    count = res['hits']['total']['value']
    tactic = item[1]
    technique = item[2]
    procedure = item[3]
    tech_code = item[4]

    action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }
    print(count)
    es.index(index="represent_1",body = action, id = procedure)

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
    main()






