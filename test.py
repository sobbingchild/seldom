
import os
import subprocess
 
# 用户输入可能来自于不可信的来源
user_input = input("Enter a command: ")
 
# 直接使用os模块执行命令，命令注入风险
os_command_injection(user_input):
    os.system(user_input)
 
# 使用subprocess模块执行命令，可以防止命令注入
subprocess_command_injection(user_input):
    subprocess.run(user_input, shell=True)


# 使用 \n 换行，\r 回车
text_with_newline = "这是第一行\n这是第二行"
text_with_carriage_return = "这是第一行\r这是第二行"
 
# 打印字符串，观察效果
print(text_with_newline)
print(text_with_carriage_return)


# 打开文件进行写入
with open('example.txt', 'w') as file:
    file.write("这是第一行\n这是第二行\n")
 
# 如果需要回车后再换行（在Windows中常见）
with open('example.txt', 'w') as file:
    file.write("这是第一行\r\n这是第二行\r\n")
 

from ldap3 import Server, Connection, ALL
 
# LDAP服务器地址
ldap_server = "ldap://your_ldap_server"
# 用户名和密码
ldap_username = "cn=admin,dc=example,dc=com"
ldap_password = "admin"
 
# 初始化LDAP服务器和连接对象
server = Server(ldap_server)
conn = Connection(server, user=ldap_username, password=ldap_password)
 
# 绑定到服务器
conn.bind()
 
# 要执行的LDAP搜索过滤器
search_filter = "(cn={username})"
search_scope = ALL
 
# 用户提供的输入
username = "user1"
 
# 使用参数绑定来避免LDAP注入
filter_params = [search_filter.format(username=username)]
 
# 执行搜索
conn.search(search_base='dc=example,dc=com',
            search_filter=filter_params,
            search_scope=search_scope,
            attributes=['uid', 'cn'])
 
# 获取搜索结果
response = conn.response
 
# 解除绑定
conn.unbind()
 
# 处理结果
for entry in response:
    print(entry)
import pickle
 
# 假设你有一个序列化的字节串
serialized_data = b'\x80\x03X\x04\x00\x00\x00spam'
 
# 反序列化
deserialized_data = pickle.loads(serialized_data)
 
print(deserialized_data)  # 输出: 'spam'
import json
 
# 假设你有一个JSON格式的字符串
json_data = '{"spam": 42}'
 
# 反序列化
deserialized_data = json.loads(json_data)
 
print(deserialized_data)  # 输出: {'spam': 42}


