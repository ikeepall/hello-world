def new_file(file_name):
    file = open(file_name, "w")
    print('pls input content. Input":w"only will save and exit')
    while True:
        write_some = input()        
        if write_some !=":w":
            file.write(write_some)
        else:
            break
        file.close()
        
file_name = input('pls input your file name')
new_file(file_name)