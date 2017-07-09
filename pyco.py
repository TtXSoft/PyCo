import pickle
import sys
print('PyCo Compiler: Opening file '+sys.argv[1])
text = open(sys.argv[1],'r').read()
print('PyCo Compiler: Writing compiled code to '+sys.argv[2])
pickle.dump(text,open(sys.argv[2],'wb'))
print('PyCo Compiler: Creating Bootstrap')
bt = open('start.py','a')
bt.write('import pickle\n')
bt.write('exec(pickle.load(open("'+sys.argv[2]+'","rb")))')
bt.close()
print('PyCo Compiler: All done')
print('Info: Open your app by running start.py')
