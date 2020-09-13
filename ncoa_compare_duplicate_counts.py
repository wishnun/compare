from ncoa_file_config import *
        
def dups_old(duplicates):
    counter = 0
    olds = set()
    with open(ncoafile_old, 'r') as inF:    
        for line in inF:
            custid = line[140:148]
            olds.add(custid)
        difference = duplicates.difference(olds)
        print(" with in those {} duplicates  {} custids do not find old file".format(len(duplicates), len(difference)))


def duplicate_counts(file): 
    records = set()   
    duplicates = set()
    with open(file, 'r') as ncoafile:
        counter = 0
        oldcounter = 0
        linenumber = 1        
        for line in ncoafile:
            custid = line[140:148]            
            if custid in records :
               #print(" custid {} is duplicate in line number {} ".format(custid,linenumber))              
               counter = counter+1        
               duplicates.add(custid)       
            else :
                records.add(custid)
            linenumber = linenumber+1
            
        print(" {} duplicate records found  file {} ".format(counter,file))
    #print(" {} new file duplicates that are found in old file {} ".format(oldcounter,file_out_old))
    dups_old(duplicates)

duplicate_counts(ncoafile_new)

#duplicate_counts(ncoafile_old)
#print(test1('123'))




