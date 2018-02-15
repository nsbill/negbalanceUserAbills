#!/usr/bin/env python3
import sys
sys.path.insert(0, '/app/db')
from mysql_select import query_with_users, update_with_user
import subprocess

user = query_with_users()
print(user)
for ng in user:
    connect_info = ng.get('connect_info')
    cmd_ns = 'cmd_ns{nas}'.format(nas = ng.get('nas_id'))
    PIPE = subprocess.PIPE
    if str('cmd_ns1') == str(cmd_ns):
       cmd_ns1 = 'ssh -p2222 remoteUser@IP_ADDRESS \'/usr/local/bin/sudo /usr/sbin/ngctl shutdown {connect_info}'.format(connect_info = connect_info) +':\''
       p = subprocess.Popen(cmd_ns1, shell = True)
       p.wait()
       update_with_user(ng.get('uid'))
    elif str('cmd_ns2') == str(cmd_ns2):
       cmd_ns2 = 'ssh -p22222 remoteUSER@IP_ADDRESS \'/usr/local/bin/sudo /usr/sbin/ngctl shutdown {connect_info}'.format(connect_info = connect_info) +':\''
       p = subprocess.Popen(cmd_ns2, shell = True)
       p.wait()
       update_with_user(ng.get('uid'))
    else:
        print('good')
