import os, shutil
import datetime


#从本机上传至服务器端


def backupfile(src_path, dst_path):
    if not os.path.exists(src_path):
        return
    dir_file_list = os.listdir(src_path) #获取所有目录，文件
    for name in dir_file_list:
        print(name)
        if name == 'RECYCLER' \
                or name == 'Thumbs.db'\
                or name == 'System Volume Information'\
                or name == '来文来电':
            pass
        else:
            abs_path = os.path.join(src_path,name) #拼接绝对路径
            if os.path.isfile(abs_path):
                #print('这是文件%s'%abs_path)
                start_time = datetime.datetime.now()
                print(start_time, " 开始复制……")
                print('源文件是：',abs_path)
                back_path = os.path.join(dst_path, src_path[20:])#abs_path[20:]去掉前面的‘\\192.168.3.222\服务器\’
                print('目标文件夹：',back_path)
                if not os.path.exists(back_path):
                    os.makedirs(back_path)
                back_file = back_path + '\\' + name
                print('目标文件', back_file)
                shutil.copyfile(abs_path, back_file)
                print(abs_path, ' => ', back_file, 'copy done!')

            if os.path.isdir(abs_path):
                #print('这是目录%s'%abs_path)
                backupfile(abs_path,dst_path)  #如果是目录，则继续递归执行函数




if __name__ == "__main__":
    src_path = r'\\192.168.3.222\服务器'
    dst_path = r'd:\backupfile'
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    backupfile(src_path,dst_path)
