# coding:utf-8
# import paramiko
#
# # 建立一个sshclient对象
# ssh = paramiko.SSHClient()
# # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 调用connect方法连接服务器
# ssh.connect(hostname='192.168.2.129', port=22, username='super', password='super')
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df -hl')
# # 结果放到stdout中，如果有错误将放到stderr中
# print(stdout.read().decode())
# # 关闭连接
# ssh.close()




# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     filename='./log.log',
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#                     #datefmt='%a, %d %b %Y %H:%M:%S')
#                     # filename='log.log',
#                     # filemode='w')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')







import logging
import os
FILE=os.getcwd()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename = os.path.join(FILE,'log.txt'),
                    filemode='a')
logging.info('msg')
logging.debug('msg2')