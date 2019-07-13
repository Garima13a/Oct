import libarchive.public as la

import glob
import os

y=[]




#searchDir = input('What directory do you want me to look in?')

searchDir = '/home/garima/Music/Garima/trial.7z'
searchDirAbs = os.path.abspath(searchDir)

#path = input('In which directory do you want your files saved?')
path = '/home/garima/Music/Garima' + '/'


#create dir med

name1 = path + 'med'
if not os.path.exists(name1):
    os.mkdir(name1)
    print("Directory " , name1 ,  " Created ")
else:
    print("Directory " , name1 ,  " already exists")

#create dir final

name2 = path + 'final'
if not os.path.exists(name2):
    os.mkdir(name2)
    print("Directory " , name2 ,  " Created ")
else:
    print("Directory " , name2 ,  " already exists")

#zipfile extractor


def extractor(direc,path):
    with la.file_reader(direc) as e:
        for entry in e:
            with open(path + '/' + str(entry.pathname), 'wb+') as f:
                for block in entry.get_blocks():
                    f.write(block)


#extract all files from original single file containing all 7z files
extractor(searchDir,name1)

#list names in array
for x in os.listdir(name1):
    y.append(x)
print(y)


#iterate through array to extract files
for i in y:
    print(i)
    for j in i:
        if not os.path.exists(name2+ '/' + 'patient'+ i):
            os.mkdir(name2+ '/' + 'patient'+i)
            print("Directory ", name2+ '/' + 'patient'+i, " Created ")
        else:
            print("Directory ", name2+ '/' + 'patient'+i, " already exists")
        extractor(name1 + '/' + i, name2+ '/' + 'patient'+i)






