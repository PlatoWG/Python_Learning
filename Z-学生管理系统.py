#定义一个空列表，保存学生信息
from pip._internal.utils.misc import enum

stu_list = []

#0、打印功能菜单
def show_menu():
    print("学生管理系统".center(20))
    print("0、显示菜单")
    print("1、添加学生信息")
    print("2、删除学生信息")
    print("3、修改学生信息")
    print("4、查询学生信息")
    print("5、显示所有学生信息")
    print("6、保存所有学生信息到文件")
    print("10、退出学生管理系统")

#1、添加学生函数
def add_stu():
    print("请输入学生信息")
    stu_name = input("1、姓名:")
    stu_age = int(input("2、年龄:"))
    stu_sex = input("3、性别:")
    stu_dir = {}
    stu_dir["name"] = stu_name
    stu_dir["age"] = stu_age
    stu_dir["sex"] = stu_sex

    stu_list.append(stu_dir)
#2、删除学生信息函数
def del_stu():
    stu_index = int(input("请输入要删除的学生学号:"))
    if stu_index > 0 and stu_index <= len(stu_list):
        stu_no = stu_index - 1
        stu_del = stu_list.pop(stu_no)
        print("%s信息已删除"%stu_del.get("name"))
    else:
        print("输入错误，学号不在已保存学生信息范围内！")

#3、修改学生信息函数
def modify_stu():
    stu_index = int(input("请输入要修改的学生学号:"))
    #判断输入的学号是否在已存在的学生信息范围内
    if stu_index > 0 and stu_index <= len(stu_list):
        stu_no = stu_index - 1
        stu_name = input("1、修改后的姓名:")
        stu_age = int(input("2、修改后的年龄:"))
        stu_sex = input("3、修改后的性别:")
        stu_dir = {}
        stu_dir["name"] = stu_name
        stu_dir["age"] = stu_age
        stu_dir["sex"] = stu_sex
        stu_list[stu_no] = stu_dir
        print("%s信息已修改"%stu_list[stu_no].get("name"))
    else:
        print("输入错误，学号不在可修改的学生信息范围内！")

#4、查询学生信息函数
def search_stu():
    search_name = input("请输入要查询的学生姓名:")
    for stu_index,stu_info in enumerate(stu_list):
        if search_name == stu_info.get("name"):
            stu_no = stu_index + 1
            print("_____________%s学生信息_____________" % stu_info.get("name"))
            print("学号:%d" % stu_no)
            print("姓名:%s" % stu_info.get("name"))
            print("年龄:%d" % stu_info.get("age"))
            print("性别:%s" % stu_info.get("sex"))
        else:
            print("未查询到%s学生信息"%search_name)
            break


#5、显示所有学生信息函数
def show_stu():
    for stu_index,stu_info in enumerate(stu_list):
        stu_info = dict(stu_info)
        print("_____________%s学生信息_____________" % stu_info.get("name"))
        stu_no = stu_index + 1
        print("学号:%d" % stu_no)
        print("姓名:%s" % stu_info.get("name"))
        print("年龄:%d" % stu_info.get("age"))
        print("性别:%s" % stu_info.get("sex"))

#6、保存数据到文件
def save_list():
    stu_file = open("stu_list.txt","w",encoding="utf-8")
    stu_file.write(str(stu_list))
    print("学生信息已保存到stu_list.txt")
    stu_file.close()

#7、启动程序读取数据文件
def load_list():
    stu_file = open("stu_list.txt","r",encoding="utf-8")
    stu_content = stu_file.read()
    stu_infos = eval(stu_content)
    stu_list.extend(stu_infos)
    print("学生信息已读取到列表")
    stu_file.close()




#先显示菜单
load_list()

while True:
    action = int(input("请输入操作功能序号，[0]显示功能菜单:"))
    if action == 0:
        show_menu()
    elif action == 1:
        add_stu()
    elif action == 2:
        del_stu()
    elif action == 3:
        modify_stu()
    elif action == 4:
        search_stu()
    elif action == 5:
        show_stu()
    elif action == 6:
        save_list()
    elif action == 10:
        save_list()
        exit()
    else:
        print("非法输入")