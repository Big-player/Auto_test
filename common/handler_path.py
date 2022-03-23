import os
def ab_path(filename):
    # 传入文件相对于项目顶级目录的文件路径，给出当前文件的绝对路径
    s=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(s, filename)




