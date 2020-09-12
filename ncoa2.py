print ("comparing files...")
with open('C:\\data\\ENV3\\NCOA\\new\\NcoaFileExtractboth20200912.txt', 'r') as file1:
    with open('C:\\data\\ENV3\\NCOA\\old\\NcoaFileExtractboth20200911.txt', 'r') as file2:
        difference_new = set(file1).difference(file2)
        difference_old = set(file2).difference(file1)

#print(difference)
difference_new.discard('\n')
difference_old.discard('\n')

with open('C:\\data\\ENV3\\NCOA\\ncoa_diff_out_new1.txt', 'w') as file_out1:
    for line in difference_new:
        file_out1.write(line)

with open('C:\\data\\ENV3\\NCOA\\ncoa_diff_out_old1.txt', 'w') as file_out2:
    for line in difference_old:
        file_out2.write(line)
