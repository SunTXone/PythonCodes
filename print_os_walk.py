import os,sys
targetDir = r'D:\Access 2007 Bible'
if len(sys.argv)>=2 and os.path.isdir(sys.argv[1]):
        targetDir = sys.argv[1]
        
os.chdir(targetDir)
nCount = 0
for strc,strp,strf in os.walk(os.getcwd()):
        nCount += 1
        print('-'*20 +str(nCount) + '-'*20)
        print('Os_CurrentDir:{}'.format(os.getcwd()))
        print('当前目录：{}'.format(strc))
        print('子文件夹：{}'.format(strp))
        print('文件集  ：{}'.format(strf))
