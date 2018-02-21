#mcb console
import sys,pyperclip,shelve

#get the run args
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcb_file = shelve.open('mcb_con')
    mcb_file[sys.argv[2]]=pyperclip.paste()
    mcb_file.close()
elif len(sys.argv)>=2 and sys.argv[1].lower()=='list':
    print('McbConsole have saved:')
    mcb_file = shelve.open('mcb_con')
    print(list(mcb_file.keys()))
    mcb_file.close()
else:
    print('Run args is wrong.')


    
