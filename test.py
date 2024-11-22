
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
