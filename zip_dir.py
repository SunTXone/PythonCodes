#将指定目录（文件）压入指定压缩文件
#不压缩空文件夹

#参数1：压缩后的目标文件；参数2：要压缩的文件夹（文件）

import sys,os,zipfile

assert len(sys.argv)==3,'参数输入错误'
zfileName = sys.argv[1]
if os.path.exists(sys.argv[2]):
    zfile = zipfile.ZipFile(zfileName,'a')
    if os.path.isdir(sys.argv[2]):
        #
        for dirC,blank,fileset in os.walk(sys.argv[2]):
            if len(fileset)>0 :
                for tfile in fileset:
                    print('Zipping the file:'+dirC+'\\'+tfile)
                    zfile.write(dirC+'\\'+tfile)
    else:
        print('Zipping the file:'+sys.argv[2])
        zfile.write(sys.argv[2])
    zfile.close()
else:
    print('文件夹不存在！')

    
         
     
        
