import os
import re
from multiprocessing import Pool

POOL_SIZE = 10


def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename)
    (shortname,extension) = os.path.splitext(tempfilename)
    #filepath是文件所在的目录（最后没有 /），shortname是去除最后一个. 所得到的文件名
    return filepath,shortname,extension

'''
    根据src_procedures目录下的procedure文件，创建modify_procedures目录下的procedure文件

'''
def work_func(procedure_path):
    _, shortname, extension = jwkj_get_filePath_fileName_fileExt(procedure_path)
    procedure_name = shortname
    procedure = shortname + extension

    w_str = "import json\n"
    tactic_line = ""
    technique_line = ""
    procedure_line = ""
    tech_code_line = ""

    for line in open(procedure_path):
        w_str += line

        if(re.match("tactic", line)):
            tactic_line = line
        
        elif(re.match("technique", line)):
            technique_line = line
        
        elif(re.match("procedure", line)):
            procedure_line = line
        
        elif(re.match("tech_code", line)):
            tech_code_line = line
 
    
    w_str += "json_str = json.dumps(doc)\n" + \
            "with open(\"dst_procedures/" + procedure + "\", \"w\", encoding=\"gbk\") as f:\n" + \
                "\tf.write(json_str" + "+\"\\n\")\n" + \
                "\tf.write("+"\'"+tactic_line.strip()+"\\n\'"+")\n" + \
                "\tf.write("+"\'"+technique_line.strip()+"\\n\'"+")\n" + \
                "\tf.write(\'procedure = "+"\""+procedure_name+"\"\\n\'"+")\n" + \
                "\tf.write("+"\'"+tech_code_line.strip()+"\\n\'"+")\n"
    

    with open("modify_procedures/" + procedure, "w") as f:
        f.write(w_str)

def main():
    src_procedure_dir = 'src_procedures'

    procedure_list = []
    for procedure in os.listdir(src_procedure_dir):
        procedure_path = src_procedure_dir + '/' + procedure
        procedure_list.append(procedure_path)

    with Pool(POOL_SIZE) as pool:
        results = pool.map(work_func, procedure_list)
    
    # 遍历执行 modify_procedures 目录下的procedures文件
    modify_procedure_dir = "modify_procedures"
    for procedure in os.listdir(modify_procedure_dir):
        modify_procedure_path = modify_procedure_dir+ "/" +"\"" + procedure + "\""
        os.system("python " + modify_procedure_path)

if __name__ == "__main__":
    main()








                
                


                


        





