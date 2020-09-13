import sys

fileextension='.txt'
basedir='c:\\data\\ENV3\\NCOA\\'
newdir='new\\'
olddir='old\\'
filepath_new = basedir+newdir
filepath_old = basedir+olddir
filename_new = 'NcoaFileExtractboth20200912'
filename_old=  'NcoaFileExtractboth20200911'
ncoafile_new = filepath_new+filename_new+fileextension
ncoafile_old = filepath_old+filename_old+fileextension
fileoutpath = basedir
file_out_new=fileoutpath+filename_new+"_diff_out"+fileextension
file_out_old=fileoutpath+filename_old+"_diff_out"+fileextension


print(" ** NEW NCOA FILE -> ncoafile_new = "+ncoafile_new)
print(" ** OLD NCOA FILE -> ncoafile_new = "+ncoafile_old)
print(" ** OUTPUT FILE for records that new query did NOT pull when compare to old query = "+file_out_old)
print(" ** OUTPUT FILE for records that new query DID pull when compare to old query = "+file_out_new)