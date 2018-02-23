# Python 核心编程第二版（中文）11.2.4 一个例子
# 儿童算数游戏

from operator import add,sub
from random import randint,choice

"""
    全局变量有:一个包含了运算符和与其相关联的函数的集合(字典)，一个决定在给出正解之前，
用户有多少次机会尝试给出答案的整型变量。
    函数字典的键值是运算符的符号，程序通过查字典找到合适的算术函数。
"""
ops = {'+':add,'-':sub}
MAXTRIES = 2

"""
doprob()函数是应用程序的核心引擎。该函数随机选择一个操作并生成两个操作数，同时为了
避免减法问题中的负数问题，将这两个算子按大到下进行排序。然后用这些值调用一个数学函数，
计算出正确的解。接着用一个等式来提示用户输入并给用户三次机会来输入一个正确的答案。
"""
def doprob():
    op = choice('+-')
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse = True)
    ans = ops[op](*nums)  #利用ops字典和op变量、nums列表将ans变成函数变量
    pr = '%d %s %d = '%(nums[0],op,nums[1])
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:#使用input代替raw_input
                print('correct')
                break
            if oops == MAXTRIES:
                print('answer\n%s%d'%(pr,ans))
            else:
                print('incorrent... try again')
                oops += 1 #计数输入答案错误次数，如果次数等于MAXTRIES后，每次都提示正确答案
        except (KeyboardInterrupt,EOFError,ValueError):
            print('invalid input... try again')

"""
程序的主入口是 main()，如果直接运行脚本，程序将自顶向下的运行。如果被作为模块导入，
导入者要么调用 doprob()函数来开始执行，要么调用 main()来进入程序控制。main()简单地调用
doprob()使用户与脚本的主要功能进行交互, 并负责提示用户退出或者尝试下一个问题。
"""
def main():
    while True:
        doprob()
        try:
            opt = input('Again?[y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt,EOFError):
            break

if __name__ == '__main__':
    main()

    
