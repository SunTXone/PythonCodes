#将指定目录（文件）压入指定压缩文件
#不压缩空文件夹

#参数1：目标压缩文件；参数2：要压缩的文件夹（文件）

#2018-2-8,测试，按要求输入已可以有效压缩文件夹或文件
#         存在问题，当指定要求压缩的文件夹包含生产的压缩文件时，无法执行


import sys,os,zipfile

assert len(sys.argv)==3,'参数输入错误'
zfileName = sys.argv[1]

#print('压缩文件名：{}'.format(zfileName))
if os.path.exists(sys.argv[2]):
    zfile = zipfile.ZipFile(zfileName,'a')
    if os.path.isdir(sys.argv[2]):
        #
        for dirC,blank,fileset in os.walk(sys.argv[2]):
            #【2018-2-8】排除包目标压缩文件包含在要压缩的文件的可能性
            #     方法：判断目标文件的路径与当前浏览路径是否相符，如相符则将压缩文件名从文件名集中剔除
            if os.path.abspath(os.path.dirname(zfileName)).lower() == os.path.abspath(dirC).lower():
                if os.path.basename(zfileName) in fileset:
                    fileset.remove(os.path.basename(zfileName))
            #处理剔除目标文件结束
            if len(fileset)>0 :
                for tfile in fileset:
                    tfile = dirC+'\\'+tfile
                    print('Zipping the file:'+tfile)
                    zfile.write(tfile)
    else:
        print('Zipping the file:'+sys.argv[2])
        zfile.write(sys.argv[2])
    zfile.close()
else:
    print('文件夹[{}]不存在！'.format(sys.argv[2]))

    
         
     
        
