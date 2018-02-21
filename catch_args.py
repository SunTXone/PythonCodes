# for catch args with this program
import sys
print('Args Numbers:{}\n'.format(len(sys.argv)))
for i in range(len(sys.argv)):
    print('Args[{0}] is "{1}".'.format(i,sys.argv[i]))
    

       
