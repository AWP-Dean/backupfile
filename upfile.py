import os, shutil
import time


#从本机上传至服务器端


def backupfile(src_path, dst_path):
    if not os.path.exists(src_path):
        return
    dir_file_list = os.listdir(src_path) #获取所有目录，文件
    for name in dir_file_list:
        if name == '~$2019.xlsx':
            pass
        else :
            srcfile_path = os.path.join(src_path, name)
            backfile_path = os.path.join(dst_path, name)
            loggerprint('源文件：%s'%(srcfile_path))
            loggerprint('目标文件:%s'%(backfile_path))
            shutil.copyfile(srcfile_path, backfile_path)
            loggerprint('%s => %s copy done!'%(srcfile_path,backfile_path))

def time1():
    return time.strftime("%Y-%m-%d",time.localtime())

def currenttime():
    return time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())

def loggerprint(str):
	filepath = r'C:\Users\Administrator\Desktop\来文来电\\logger\\'
	filename = time1() + '.txt'
	log = open(filepath + filename, 'a',newline='')
	print(currenttime(), file=log)
	print('\r\n', file=log)
	print(str, file=log)
	print('\r\n',file=log)
	log.close()


if __name__ == "__main__":
    dst_path = r'\\192.168.3.222\服务器\来文来电'
    src_path = r'C:\Users\Administrator\Desktop\来文来电'
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    backupfile(src_path,dst_path)
