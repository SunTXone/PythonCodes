# 测试 collatz 队列

#定义 collatz 函数，她有一个参数 number
def collatz(number):
    if number%2 == 0 :
        returnNumber=number//2
    else:
        returnNumber=3*number+1

    print(returnNumber)
    return returnNumber
try :
    num=int(input('Enter number:'))
    print(num)
    while num!=1:
        num=collatz(num)
        #print(num)

except ValueError:
    print('You must input a integer!')

    
