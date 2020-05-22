import os
import re
from multiprocessing import Pool

POOL_SIZE = 10

def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename)
    (shortname,extension) = os.path.splitext(tempfilename)
    #filepath是文件所在的目录（最后没有 /），shortname是去除最后一个. 所得到的文件名
    return filepath,shortname,extension

def work_func(step_path):

    _, shortname, extension = jwkj_get_filePath_fileName_fileExt(step_path)

    file_name = shortname + extension

    contains_search_doc_a = False
    contains_search_doc_b = False
    contains_search_doc_c = False
    tab_flag = False
    w_str = "import json\n"

    for line in open(step_path, 'r', encoding='utf-8'):
        w_str += line

        if(re.match("search_doc_a", line.strip())):
            contains_search_doc_a = True
        
        if(re.match("search_doc_b", line.strip())):
            contains_search_doc_b = True
        
        if(re.match("search_doc_c", line.strip())):
            contains_search_doc_c = True
        
        if(re.match("for id in range", line.strip())):
            tab_flag = True

        if(re.match("es.index", line.strip())):
            break

    if("info" in file_name):
        with open("mordor_empire_modify/" + file_name, "w", encoding="utf-8") as f:
            f.write(w_str)
        return

    if(tab_flag):
        w_str += "  with open(\"mordor_empire_dst/\" + eval_step + \".yml\", \"w\") as f:\n"

        if(contains_search_doc_a):
            w_str +="    search_doc_a = json.dumps(search_doc_a)\n" + \
        "    f.write(\"search_doc_a : \" + search_doc_a+\"\\n\")\n"
        if(contains_search_doc_b):
            w_str += "    search_doc_b = json.dumps(search_doc_b)\n" + \
        "    f.write(\"search_doc_b : \" + search_doc_b+\"\\n\")\n"
        if(contains_search_doc_c):
            w_str += "    search_doc_c = json.dumps(search_doc_c)\n" + \
        "    f.write(\"search_doc_c : \" + search_doc_c+\"\\n\")\n"
        
        w_str += "    f.write(\"tactic : \" + tactic+\"\\n\")\n" + \
        "    f.write(\"technique : \" + technique+\"\\n\")\n" + \
        "    f.write(\"tech_code : \" + tech_code+\"\\n\")\n" + \
        "    f.write(\"eval_phase : \" + eval_phase+\"\\n\")\n" + \
        "    f.write(\"eval_step : \" + eval_step+\"\\n\")\n" 
    else:
        w_str += "with open(\"mordor_empire_dst/\" + eval_step + \".yml\", \"w\") as f:\n"
        if(contains_search_doc_a):
            w_str +="\tsearch_doc_a = json.dumps(search_doc_a)\n" + \
        "\tf.write(\"search_doc_a : \" + search_doc_a+\"\\n\")\n"
        if(contains_search_doc_b):
            w_str += "\tsearch_doc_b = json.dumps(search_doc_b)\n" + \
        "\tf.write(\"search_doc_b : \" + search_doc_b+\"\\n\")\n"
        if(contains_search_doc_c):
            w_str += "\tsearch_doc_c = json.dumps(search_doc_c)\n" + \
        "\tf.write(\"search_doc_c : \" + search_doc_c+\"\\n\")\n"
        
        w_str += "\tf.write(\"tactic : \" + tactic+\"\\n\")\n" + \
        "\tf.write(\"technique : \" + technique+\"\\n\")\n" + \
        "\tf.write(\"tech_code : \" + tech_code+\"\\n\")\n" + \
        "\tf.write(\"eval_phase : \" + eval_phase+\"\\n\")\n" + \
        "\tf.write(\"eval_step : \" + eval_step+\"\\n\")\n" 


    with open("mordor_empire_modify/" + file_name, "w", encoding="utf-8") as f:
        f.write(w_str)

def main():
    mordor_empire_src = 'mordor_empire_src'

    step_list = []
    for step in os.listdir(mordor_empire_src):
        step_path = mordor_empire_src + '/' + step
        step_list.append(step_path)

    with Pool(POOL_SIZE) as pool:
        results = pool.map(work_func, step_list)
    
    # 遍历执行 modify_procedures 目录下的procedures文件
    mordor_empire_modify = "mordor_empire_modify"
    for step in os.listdir(mordor_empire_modify):
        modify_step_path = mordor_empire_modify+ "/" +"\"" + step + "\""
        os.system("python " + modify_step_path)

if __name__ == "__main__":
    main()








                
                


                


        





