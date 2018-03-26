'''
  第一一个学生类
'''


# 第一一个空的类
class Student():
    # 一个空类，pass
    pass


mingyue = Student()


# 定义个类，来描述python的学生
class PythonStudent():
    # None给不确定的值赋值
    name = None
    age = 18
    course = "python"

    # 需要注意
    # 1、def doHomework的缩进层级
    # 2、系统默认由一个self参数
    @staticmethod
    def doHomework():
        print("I 在做作业")
        return None


yueyue = PythonStudent()
print(yueyue.age)
print(yueyue.course)
