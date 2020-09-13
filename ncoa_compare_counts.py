from ncoa_file_config import *

def other_counts(fileout):
    with open(fileout, 'r') as file_out1:
        counter =0
        for line in file_out1:
            if line[135] not in ('5','0'):
                print(line)
                counter = counter+1;
        print(" {} other than savings and pension records found in file {} ".format(counter,fileout))


def diff_counts(fileout , addresstype, doprint=False):    
    with open(fileout, 'r') as file_out1:
        addresstypestring = "savings"
        if addresstype == '5':
            addresstypestring = "pension"
        counter = 0;
        for line in file_out1:
            if line[135] == addresstype :
                if doprint :
                    print(" {} record type  is {}".format(addresstypestring,line))
                counter = counter+1;
            
        print(" {} {} records found diff output file {} ".format(counter,addresstypestring,fileout))

diff_counts(file_out_old,'5')
diff_counts(file_out_old,'0')
diff_counts(file_out_new,'5')
diff_counts(file_out_new ,'0',True)
#other_counts(file_out_old)
#other_counts(file_out_new)




