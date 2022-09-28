"""
dict 客户端
发起请求，接受结果，呈现数据
"""
from socket import *
import sys

# 服务器地址
ADDR = ("127.0.0.1", 8889)


# 查询单词
def do_query(sockfd, name):
    while True:
        word = input("单词：").strip()  # 去除空格
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        sockfd.send(msg.encode())
        # 无论是否查询到单词，都进行打印
        result = sockfd.recv(1024)
        print(result.decode())


# 历史记录
def do_history(sockfd, name):
    msg = "H " + name
    sockfd.send(msg.encode())
    # 接受历史记录
    while True:
        # 每次接受一个
        data = sockfd.recv(1024).decode()
        if data == "##":
            break
        print(data)


# 二级界面
def second(sockfd, name):
    while True:
        print("""
        ===========Query=============
        1.查单词   2.历史记录  3.注销          
        =============================
        """)
        cmd = input("请输入命令：")
        if cmd == "1":
            do_query(sockfd, name)
        elif cmd == "2":
            do_history(sockfd, name)
        elif cmd == "3":
            pass


# 发送注册请求
def do_register(sockfd):
    name = input("Name:")
    passwd = input("Passwd:")
    passwd_ = input("Passwd again:")
    # 做一些输入的基本验证
    if passwd != passwd_ or "" in name or "" in passwd:
        print("用户名或密码错误")
        return
    msg = "R %s %s" % (name, passwd)
    sockfd.send(msg.encode())  # 发送请求
    # 等待结果
    result = sockfd.recv(128).decode()
    if result == "OK":
        print("注册成功")
    else:
        print("注册失败")


# 发送登陆请求
def do_login(sockfd):
    name = input("Name:")
    passwd = input("Passwd:")
    msg = "L %s %s" % (name, passwd)
    sockfd.send(msg.encode())  # 发送请求
    # 等待结果
    result = sockfd.recv(128).decode()
    if result == "OK":
        print("登录成功")
        second(sockfd, name)  # 进入二级界面
    else:
        print("登录失败")


# 启动函数
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.connect(ADDR)

    # 进入一级界面
    while True:
        print("""
        ===========welcome===========
        1.注册        2.登录    3.退出
        =============================
        """)

        cmd = input("请输入命令：")
        # sockfd.send(cmd.encode())
        if cmd == "1":
            do_register(sockfd)
        elif cmd == "2":
            do_login(sockfd)
        elif cmd == "3":
            sockfd.send(b"E")
            sys.exit("谢谢使用")
        else:
            print("请输入正确的命令：1,2 or 3")


if __name__ == '__main__':
    main()
