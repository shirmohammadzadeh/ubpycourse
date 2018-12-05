import os
import sys
list_file = []
list_file.extend(sys.argv[1:])
for i in list_file:
    os.system("potrace -b svg -b pdf {0} -o {1}.pdf".format(i,i[:-4]))
    print('Completed Successfully!')
