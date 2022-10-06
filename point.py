


#pexpect练习
import pexpect

host = '127.0.0.1'
user = 'kylin'
password = 'qwer1234'

#链接服务器
logfile = open('logfile.txt','wb+')
child = pexpect.spawn('/usr/bin/ssh',[user+'@'+host])
child.logfile = logfile
child.expect("password: ")
child.sendline(password)
child.expect("$")
child.sendline("touch /home/kylin/done.txt")
#下载本地文件
child.sendline("scp kylin@localhost:/home/kylin/test.qqq /home/kylin/test/")
child.expect("password: ")
child.sendline("qwer1234")
child.expect("#")
#执行监控脚本