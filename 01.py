# # def multiole_attacks(count):
# #     for i  in range(count):
# #         print("拜泉")
# #         print("上课")
# #         print("奖金")
# #         print("上班")
# # multiole_attacks(3)
# # multiole_attacks(10)
# # list01 = [2,3,4,56]
# # list02 = ["a","b","c","d"]
# #
# # for item in list01:
# #     print(item,end=" ")
# # print()
# # for item in list02:
# #     print(item,end=" ")
# #
# # def print_single_list(list_target):
# #     for item in list_target:
# #         print(item, end=" ")
# #     print()
# # print_single_list(list01)
# #
# # print_single_list(list02)
# #
# # """
# #     返回值
# #     def 函数名():
# #       函数体
# #       return 数据 # 返回 结果
# #
# # """
# # def usd_to_rmb(usd):
# #     """
# #
# #     """
# #
# #     rmb = float(usd)*7.1465
# #     return rmb
# # rmb = usd_to_rmb("20")
# # print(rmb)
# # def funco01(p1,p2,p3):
# #     print(p1)
# #     print(p2)
# #     print(p3)
# #
# # funco01(1,2,3)
# # # funco01(p1=1,p2=2,p3=3)
# # funco01(p2=2)
# # def funco01(p1, p2, p3):
# #     print(p1)
# #     print(p2)
# #     print(p3)
# #
# #
# # dict04 = {"p1": 1, "p2": 2, "p3": 3}
# # funco01(**dict04)
# # # funco01(1, 2, 3)
# # # str02 = "123"
# # # tuple03 = (1, 2, 3)
# # # funco01(*list01)
# # def fun02(*p1):
# #     print(p1)
# #
# #
# # fun02()
# # fun02(1, 2, 3)
# # def funco01(*args):
# #     #形参中只有一个*
# #     #只支持位置实参
# #     print(p1)
# # funco01()
# # funco01(1,2,3)
# #
# #实参必须是关键字
#
# # print(10,20,30)
# # def func04(*args, **kwargs):
# #     print(args)
# #     print(kwargs)
# # def func02(p1,p2 = "",*args,p3 = 0, **kwargs):
# #     print(p1)
# #     print(p2)
# #     print(args)
# #     print(p3)
# # #     print(kwargs)
# # class Phone:
# #     """
# #
# #     """
# # def change_odd_one(list_target):
# #     for i in range(len(list_target)):
# #         if list_target[i] % 2:
# #             list_target[i] = 1
# #
# #
# # list01 = [3, 4, 5, 6, 7, 8, 9]
# # change_odd_one(list01)
# # print(list01)
# # """
# # 倒序删除
# # """
# #
# #
# # def change_odd_one(list_target):
# #     for i in range(len(list_target) - 1, -1, -1):
# #         if list_target[i] % 2:
# #             del list_target[i]
# #
# #
# # list01 = [3, 4, 5, 6, 7, 8, 9]
# # change_odd_one(list01)
# # # # print(list01)
# # class wife:
# #     def __init__(self,name="",age=""):
# #         self.name = name
# #         self.age = age
# #
# #     @property
# #     def age(self):
# #         return self.__age
# #
# #     @age.setter
# #     def age(self, value):
# #         if 25 <= value <= 30:
# #             self.__age = value
# #         else:
# #             raise Exception("不行")
# #
# #
# # w01 = wife("双儿",25)
# # print(w01.name)
# # print(w01.age)
# #
# # list_merge = [2, 0, 2, 0]
# #
# #
# #
# # def zero_to_end():
# #     for i in range(len(list_merge)):
# #         if list_merge[i] == 0:
# #             del list_merge[i]
# #             list_merge.append(0)
# #
# #
# # zero_to_end()
# # print(list_merge)
# # def merge():
# #     for i in range(len(list_merge) - 1):
# #         if list_merge[i] == list_merge[i + 1]:
# #             list_merge[i] += list_merge[i + 1]
# #             del list_merge[i + 1]
# #             list_merge.append(0)
# # merge()
# # print(list_merge)
# """
#   1.玩家攻击敌人，敌人受伤（播放动画）
#   2.玩家（攻击力）攻击敌人（血量），敌人受伤（播放动画，血量减少）
#   3.敌人（攻击力）还能攻击玩家（血量）
#     玩家受伤（碎屏，血量减少）
# """
#
#
# # class Player:
# #     def __init__(self, atk=0):
# #         self.atk = atk
# #
# #     def attack(self, Enemy):
# #         print("玩家攻击敌人")
# #         Enemy.damage()
# #
# #
# # class Enemy:
# #     def __init__(self, hp=""):
# #         self.hp = hp
# #
# #     def damage(self, value):
# #         print("播放受伤动画")
# #         self.hp -= value
# #         print("敌人血量是"，self.hp)
# #
# # p01 = player(50)
# # e01 = Enemy(100)
# # p01.attack(e01)
# # class Person:
# #     def __init__(self, name=""):
# #         self.name = name
# #     def teach(self,other,skill):
# #         print(self.name,"在教",other.name,skill)
# #
# #
# #     def work(self):
# #
# #
# # zwi = Person("张无忌")
# # zm = Person("赵敏")
# # zwj.teach(zm,"九阳神功")
# # zm.teach(zwj,"玉女心经")
# # zwj.work(5000)
# # zm.work(10000)
# # list_merge = [2, 0, 2, 0]
# #
# #
# #
# # def zero_to_end():
# #     for i in range(len(list_merge)):
# #         if list_merge[i] == 0:
# #             del list_merge[i]
# #             list_merge.append(0)
# #
# #
# #
# # def merge():
# #     for i in range(len(list_merge) - 1):
# #         if list_merge[i] == list_merge[i + 1]:
# #             list_merge[i] += list_merge[i + 1]
# #             del list_merge[i + 1]
# #             list_merge.append(0)
# # map = [
# #     [2,2,8,16]
# #     [4,2,0,2]
# #     [2,4,2,4]
# #     [0,4,0,4]
# # ]
# # def move_lsft():
# #     global list_merge
# #     for line in map:
# #         list_merge =line
# #         merge()
# #
# # def move_right():
# #     global list_merge
# #     for line in map:
# #         list_merge = line[::-1]
# #         line[::-1] = list_merge
# # """
# # 手雷爆炸
# #
# # """
# # #---------架构师-------
# # # class Grenade:
# # #     def explode(self,target):
# # #         print("手雷爆炸")
# # #         target.damage()
# # # class AttackTarget:
# # #     def damage(self):
# # #         pass
# # #
# # # #---------程序-------
# # # class Enemy(AttackTarget):
# # #     def damage(self):
# # #         print("敌人受伤")
# # #
# # #
# # # class Player(AttackTarget):
# # #     def damage(self):
# # #         print("玩家受伤")
# # #
# g01 = Grenade()
# e01 = Enemy()
# p01 = Player()
# # g01.explode(p01)
# list_merge = [2, 0, 2, 0]
#
#
#
# def zero_to_end():
#     for i in range(len(list_merge)):
#         if list_merge[i] == 0:
#             del list_merge[i]
#             list_merge.append(0)
#
#
#
# def merge():
#     for i in range(len(list_merge) - 1):
#         if list_merge[i] == list_merge[i + 1]:
#             list_merge[i] += list_merge[i + 1]
#             del list_merge[i + 1]
#             list_merge.append(0)
# map = [
#     [2,2,8,16]
#     [4,2,0,2]
#     [2,4,2,4]
#     [0,4,0,4]
# ]
# def move_lsft():
#     global list_merge
#     for line in map:
#         list_merge =line
#         merge()
#
# def move_right():
#     global list_merge
#     for line in map:
#         list_merge = line[::-1]
#         line[::-1] = list_merge
#
