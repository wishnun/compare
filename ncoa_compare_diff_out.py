from ncoa_file_config import *

def diff_out(file_1, file_2,fileout):
    print("comparing "+file_1 +" to "+file_2+" records exist in new but not in old "+fileout)
    with open(file_1, 'r') as file1:
        with open(file_2, 'r') as file2:
            difference = set(file1).difference(file2)
    difference.discard('\n')
    with open(fileout, 'w') as file_out1:
        for line in difference:
            file_out1.write(line)

diff_out(ncoafile_new,ncoafile_old,file_out_new)
diff_out(ncoafile_old,ncoafile_new,file_out_old)




