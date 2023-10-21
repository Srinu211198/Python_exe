
with open("test.txt",'r') as fp:
    lines=fp.readlines()
file_name = "new_test.txt"
with open(file_name,'w') as nf:
    count = 0
    for line in lines:
        if count == 4:
            count +=1
            continue
        else:
            nf.write(line)
        count +=1