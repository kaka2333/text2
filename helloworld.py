'''


print("hello world")
x = "123"
print(x)
total = "11" + \
        "22"
print(total)
# ni hao a
x = 123
x = y = z = 999
x, y, z = 1, 2, 3
print(x, y, z)
x = '123'
print(x * 2)
print(x[2])
print('1' in x)
print("My %s old is %d" % ('zara', 21))

a = 5
b = 10
print(a // b)

# 这是单行注释

# conding=utf-8
print('中文')
print(type(a))

age = 10
print("%d岁" % age)

name = 'zjq'
QQ = 1412885221
phone = 15230562026

print("名字：%s" % name)
print("QQ:%d" % QQ)
print("Phone:%d" % phone)

# password = input()
# print("password:"+password)
print(9 / 2)
print(9 // 2)
print(9 % 2)

if age >= 2:
    print('11')
else:
    print('22')

if age < 11:
    print("age:%d" % age)
elif age > 11:
    print("age : 11")
else:
    print("ddd")

'''

'''
这是多行注释
'''

'''
a = True
b = False
if a and b:
    print("正确")
else:
    print("错误")
'''
'''
import random

player = input("请输入：剪刀(0)  石头(1)  布(2):")
player = int(player)

computer = random.randint(0, 2)

print("player:%d,computer:%d" % (player, computer))
'''
'''
i = 1
while i < 5:
    print("这是第%d次" % i)
    i += 1

i = 100
s = 0
while i >= 1:
    s += i
    i -= 1
print(s)

i = 1
while i < 6:
    s = 1
    while s <= i:
        print("*", end=" ")
        s += 1
    print("\n")
    i += 1

i = 1
while i < 10:
    m = 1
    while m <= i:
        print("%d * %d = %d" % (m, i, m * i), end=" ")
        m += 1
    print("\n")
    i += 1
'''

'''
i = 1
while i <= 10:
    if i > 5:
        for num in range(i, 10):
            print("*", end=" ")
    elif i <= 5:
        for num in range(0, i):
            print("*", end=" ")
    print("\n")
    i += 1

for q in range(1, 1):
    print("11111")
'''

'''
name = 'zhangjq sad asd'
print(name[1: 5])
print(name[::-1])
print(name[1:-1])
print(name.count('z'))
print(name.replace('z', 'Z'))
print(name.title())
print(name.strip())
print(name.partition('sad'))
print(name.split(' '))
print('asdsad'.isalpha())
li = ["aa", "bb", "cc"]
print("22".join(li))
'''

'''
name = ["zs", 'ls', 22]
for i in name:
    print(i)

print(len(name))
name.append("ww")
print(name[3])

age = [12, 13, 14]
name.append(age)
name.extend(age)
name.insert(1, "QQ")
del name[2]
name.remove('ww')
name.pop()

age.sort(reverse=True)
for i in age:
    print(i)
for i in name:
    print(i, end=" ")
print('\n')
print("QQ" in name)
print(name.index('QQ', 1, 3))

info = {"name": 'zs', 'age': 13, 'sex': 'man'}
print(info['name'])
print(info['age'])
print(info.get('age'))
info['id'] = '01'
del info['id']
print(info.get('id'))
print(len(info))
print(info.keys())
print(info.values())
print('name' in info.keys())

for i in info.values():
    print(i)
for item in info.items():
    print(item)
for key,value in info.items():
    print("key:%s,value:%s"%(key,value))
'''

'''
print([1, 2] + [3, 4])
print(len([1, 2, 3, 4]))
print(max([1, 2, 3, 4, 46, 5]))

def demo():
    print("demo")


demo()


def add(a, b):
    print("%d" % (a + b))


'''"用来完成对2个数求和"'''

add(1, 2)


def add2(a, b):
    return a + b


c = 100


def demo(a):
    for i in range(0, a):
        print("*****")


demo(2)

'''

'''
递归

def demo(a):
    if a > 1:
        return a * demo(a - 1)
    elif a == 1:
        return 1


print(demo(5))
'''

'''
文件
f = open("D://1.txt", 'w')
f.write('hello world')
f.close()

f = open("D://1.txt")
read = f.read(2)
print(read)
print(f.read())
f.close()

f = open("D://1.txt")
read = f.readlines()
print(type(read))
print(read)
for i in read:
    print(i)
f.close()
'''

'''
拷贝文件
oldName = 'D://1.txt'
oldFile = open(oldName, 'r')
if oldFile:
    # print(oldName.find('.'))
    # print(oldName[oldName.find('.'):])
    # print(oldName[:oldName.find('.')])
    index = oldName.find('.')
    prefix = oldName[:index]
    suffix = oldName[index:]
    # list = oldName.split('.')
    # for i in list:
    #     print(i)
    newName=prefix+"副本"+suffix
    newFile=open(newName,'w')
    oldLines=oldFile.readlines()
    for i in oldLines:
        newFile.write(i)
oldFile.close()
newFile.close()

'''

'''
f = open("D://1.txt", 'r')
str = f.read(5)
print(str)
tell = f.tell()
print(tell)

f.seek(4, 0)
print(f.read(5))
print(tell)

'''

'''
import os

# os.rename("D://1副本.txt","D://1.txt")
# os.remove("D://2.txt")
# os.mkdir("D://练习")
# print(os.getcwd(),
# os.listdir("D://"))
# os.rmdir("D://练习")

list = os.listdir("D://test")
print(list)
for i in list:
    if '练习' == i.split('.')[0].split('-')[0]:
        print(i)
        if i.index('.') > 0:
            os.rename("D://test//" + i, 'D://test//新' + i)

'''

'''

class Car:
    def __init__(self):
        self.color = 'yellow'
        self.name = 'ben'

    def com(self, people):
        print(self.name)
        print("1213")
        print(people)


class People:
    def __init__(self):
        self.name = 'zs'
        self.sex = 'man'

    def __str__(self):
        return self.name + ',' + self.sex


people=People()

BWM = Car()
print(BWM.color)
print(BWM.name)
BWM.com(people)


class Dog:
    def __init__(self, name):
        self.__name = name
        print('__init__方法被调用')

    # def __del__(self):
    #     print('__del__方法被调用')
    #     print('%s马上del掉了' % self.getname())
    #
    # def getname(self):
    #     return self.__name

    def eat(self):
        print("狗吃肉")


# erha = Dog('erha')
# del erha


class Dog2(Dog):
    def __init__(self):
        self.__name = 'jinmao'
        self.__age = 3

    def run(self):
        print('paobu')


jinmao = Dog2()
jinmao.run()
jinmao.eat()



'''

'''

class A:
    def __init__(self):
        self.name='zs'
        self.age=10
    def test(self):
        print('A')


class B:
    def test(self):
        print('B')


class C(A, B):
    pass

c=C()
c.test()
print(c.age)
print(c.name)


class A:
    name = 'zs'

a=A()
print(A.name)
print(a.name)
a.name='ls'
print(A.name)
print(a.name)
A.name='ls'
print(A.name)
print(a.name)
del a.name
print(A.name)
print(a.name)
class A:
    name = 'zs'

    @classmethod
    def method1(cls):
        cls.name = 'ls'

    @staticmethod
    def method2():
        A.name = 'ss'


a = A()
print(a.name)
print(A.name)
A.method1()
print(A.name)

class Car:
    def move(self):
        print('车移动')

    def stop(self):
        print('车停止')


class CarStore:
    def order(self):
        car = Car()
        car.move()
        car.stop()


buyCar = CarStore()
buyCar.order()

class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = Singleton(18, 'ls')
b = Singleton(20, 'zs')

print(id(a))
print(id(b))

a.age = 18
print(b.age)


#单利模式
class Singleton2(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton2, cls).__new__(cls)
        return cls.instance


ob1 = Singleton2()
ob2 = Singleton2()

print(id(ob1))
print(id(ob2))

#异常捕获，抛出
try:
    print('begin__')
    open('F://1.txt', 'r')
    print('end__')
except IOError as result:
    print('error')
    print(result)

#自定义异常
class ShortInputException(Exception):
    def __init__(self):
        print('自定义异常')


def main():
    try:
        raise ShortInputException()
    except ShortInputException as result:
        result
    else:
        print('没有异常发生')
    finally:
        print('最终————')


main()


import test

test.test1()
test.test2()
a=test.Test()
a.test1()
a.test2()

b = re.findall('[\d]', "abc33")
print(str(b))

'''

'''
#爬小说
url = 'http://www.book.com.tw/18_18949/8703377.html'
response = urllib.request.urlopen(url)
content = response.read()
text_soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
alltext = text_soup.find_all('div', id='content')
text_list = alltext[0].get_text()
# text_list = re.sub(r'(/s*<br/>)+', '', alltext)
# text_list = str(alltext[0]).split(r'<div id="content">')[1].split(r'</div>')[0].split(r'<br/>')
file = open('D://1.txt', 'w', encoding='utf-8')
file.write('\t第一章\n\n')
for i in text_list:
    # print(i)
    file.write(i)
file.close()

# soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
# soup_list = soup.find_all('div', class_='box_con')
# print(soup_list[1])
# result = soup_list[1].find_all('a', href=re.compile(r'/%s/\w+' % url.split(r'/')[3]))
# for i in result:
#     url_path=i['href']
#     url_join=urljoin(url,url_path)
#     print(url_join)
# print(result)

info = {"11": '22', '22': '33', '44': 'ww'}
# list = info.items()
# del list[0:2]
print('ww' in info.values())

def f(x):
        return x * x


    list2 = [1, 2, 3, 4, 5, 6, 7]
    # text_list = map(f, list2)
    # text_list=reduce(f,list2)
    # print(list(text_list))

    a = range(0, 10)
    print(type(a))
    print(a)
    
    
    #filter过滤器
    # 生成一个奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


if __name__ == "__main__":
    print(primes())
    # 打印1000以内的素数:
    for n in primes():
        if n < 100:
            print(n)
        else:
            break
    
    '''
if __name__ == '__main__':
    def sum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum


    # print(sum(1, 2, 3, 4, 5, 6))

    def lazy_sum(*args):
        def sum():
            sum = 0
            for i in args:
                sum += i
            return sum

        return sum


    # print(lazy_sum(1, 2, 3, 4, 5, 6))

    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i * i

            fs.append(f)
        return fs


    # 因为循环产生了3个函数对象，所以需要3个变量接
    f1, f2, f3 = count()

    import logging


    # @log
    def log():
        print('2222')

    @log
    def now():
        print('2018-8-31')

    now()

