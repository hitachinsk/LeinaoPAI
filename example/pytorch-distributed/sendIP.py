import sys
import os


# ---------------- 获取ip地址 ----------------

cmd = 'ifconfig > ifconfig.txt'
os.system(cmd)
with open ('ifconfig.txt', 'r') as fin:
    total = fin.readlines()

ifEth0 = False
for line in total:
    if ifEth0:
        tmp_arr = line.split(sep=' ')
        for str_value in tmp_arr:
            if str_value.startswith('addr'):
                local_address = str_value.split(sep=':')[1]
        break
    if line.startswith('eth0'):   # 我们取eth0的那个ip地址，即172打头的
        ifEth0 = True
print ("Node0_IP : ", local_address)

file_name = 'node0_ip.txt'
with open (file_name, 'wt') as fout:
    fout.write(local_address)


# ---------------- 获取各节点名称 ----------------

# 获取worker结点的任务名称以及数量
role_list_len = int(os.environ["PAI_JOB_TASK_ROLE_COUNT"])
role_list_str = os.environ["PAI_JOB_TASK_ROLE_LIST"]
role_list = role_list_str.split(',')

for ii in range(1, len(role_list)):
    # 任务名需要在后面添加“-0”
    worker_taskName = '%s-0' % role_list[ii]
    # 传输文件
    cmd = 'scp %s %s:/root' % (file_name, worker_taskName)
    os.system(cmd)

