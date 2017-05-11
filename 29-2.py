def file_read(file,line):
    print("%s file content of %s lines is as following:"%(file,line))
    f = open(file)
    line_num = int(line)
    fl = f.readlines()
    for i in range(line_num):
        print(fl[i])
        
file = input('pls input file name')
line = input('pls input number line')

file_read(file,line)        