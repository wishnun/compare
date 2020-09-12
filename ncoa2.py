print ("comparing files...")
with open('1.txt', 'r') as file1:
    with open('2.txt', 'r') as file2:
        difference_new = set(file1).difference(file2)
        difference_old = set(file2).difference(file1)

#print(difference)
difference_new.discard('\n')
difference_old.discard('\n')

with open('n1.txt', 'w') as file_out1:
    for line in difference_new:
        file_out1.write(line)

with open('n2.txt', 'w') as file_out2:
    for line in difference_old:
        file_out2.write(line)
