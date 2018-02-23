#!
#Python编程快速上手 第6章 6.7实践项目

def  printTable(tableData):
    #定义存储每列长度的列表
    colWidths=[0]*len(tableData)
    #保持每列中的最大字符串长度
    for i in range(len(tableData)):
        colWidths[i]=max([len(j) for j in tableData[i]])
    #外圈 for 语句，按列数迭代
    for i in range(len(tableData[0])):
        prn_s = ' '
        #内区 for 语句，按行数跌打
        for j in range(len(colWidths)):
            if j == 0 :
                prn_s += tableData[j][i].rjust(colWidths[j],'-')
            else:
                prn_s += tableData[j][i].ljust(colWidths[j],'-')
            prn_s += ' '
        print(prn_s)


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
    



                
