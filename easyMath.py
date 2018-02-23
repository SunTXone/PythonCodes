# Python 核心编程第二版（中文）11.2.4 一个例子
# 儿童算数游戏

from operator import add,sub
from random import randint,choice

ops = {'+':add,'-':sub}
MAXTRIES = 2

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
                oops += 1 #??
        except(KeyboardInterrupt,EOFError,ValueError):
            print('invalid input... try again'

def main():
    while True:
        doprob()
        try:
            opt = input('Again?[y]').lower()
            if opt and opt[0] == 'n':
                break
            except (KeyboardInterrupt,EOFError):
                break

    if __name__ == '__main__'
        main()

    
