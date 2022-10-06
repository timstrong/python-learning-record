'''
import os
val = os.system("cat /etc/passwd>>/dev/null")
print(val)

val = os.popen('df -h')
print(val.read())
val.close()



#import subprocess  #允许创建进程，可以指定输入输出，错误输出管道，CompletedProcess(args='df', returncode=0
#val = subprocess.run("df") #等待命令执行完成返回包含执行结果的，CompletedProcess(args='df', returncode=0
#print(val)

#val = subprocess.run(["df","-Th"])
#print(val)

#val = subprocess.call(["df","-Th"])#执行命令，返回命令执行状态，功能和os.system()类似
#print(val)

#val = subprocess.call("cat /proc/cpuinfo | grep 'processor'",shell=True)
#print(val)

#val = subprocess.check_call("cat /proc/cpuinfo | grep 'processor'",shell=True) #执行命令，执行成功返回命令执行状态，执行不成功抛出异常
#print(val)

from subprocess import Popen,PIPE 

def excute_cmd(cmd):
    pobj = Popen(cmd,
        stdin = PIPE,
        stdout = PIPE,
        stderr = PIPE,
        shell = True
        )
    stdout,stderr = pobj.communicate()
    if pobj.returncode != 0:
        return("异常",pobj.returncode,stderr)
    return(pobj.returncode,stdout.decode().split('\n'))

re = excute_cmd(['ls','-l'])
print(re)



#

#
#文件读写：
#
#打开 open(file_name,accessmode_mode='r')
#
#filename:文件名
#
#accessmode_mode='r':打开方式： r 读方式打开，文件存在
#
#                            w 写方式打开，文件不存在创建，存在清空
#
#                            a 追加方式打开
#
#                            b 二级制的方式方式打开
#
#                            + 读写#

#
#操作
#
#    读：read() readline() for
#
#    写：write() writelines()#

#
#关闭
#
#    close()#


from datetime import datetime
import imp
import os
from collections import Counter

c = Counter()
print(c)
with open(os.path.expanduser("~/.bash_history"),'r+') as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]] +=1

c_cmd = c.most_common(5)
print(c_cmd)

import os
import socket
import psutil
import datetime

def boot_time():
    datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return dict(boot_time=boot_time)

def cpu_info():
    cpu_count = psutil.cpu_count()
    return dict(cpu_count=cpu_count)

def disk_info():
    disk_usa_p = psutil.disk_usage('/')
    disk_per = disk_usa_p.percent
    return dict(disk_per = disk_per)

def collect_mon_info():
    info = {}
    #开机时间
    info.update(boot_time())
    #CPU使用
    info.update(cpu_info())
    #磁盘使用
    info.update(disk_info())
    #内存使用
    print(info)

def main():
    hostname=socket.gethostname()
    collect_mon_info()

if __name__ == '__main__':
    main()

'''

import pexpect
val=pexpect.run('ls')
print(val)
