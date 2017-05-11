def file_read(file,line):
    
    f = open(file)
   
    (begin,end) = line.split(":")
    if begin == " ":
        begin = '1'
    if end == " ":
        end = '-1'
        
    if begin == '1' and end == '-1':
        cont = 'beginning to end '
    elif begin == '1' and end != '-1':
        cont = 'beginning to line %s '%end
    elif begin != '1' and end == '-1':
        cont = 'line %s to end '%begin
    elif begin != '1' and end != '-1':
        cont = 'line %s to line %s '%(begin,end)
    
    print('The content of ' + cont + 'is as following')
    
    begin = (int(begin)) -1
    end = int(end)
    lines = end - begin
    
    if lines < 0:
        print(f.read())
        
    else:
        for j in range(lines):
            print(f.readline())

    
    f.close()
    
file = input('pls input file name')
line = input('pls input line, format is as 13:15 or  :13 or 13: ')

file_read(file,line)       