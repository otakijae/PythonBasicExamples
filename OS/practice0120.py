import os
from datetime import *
#print(dir(os))
print(os.getcwd())
os.chdir("/Users/jaehyukshin/Desktop/module")
print(os.getcwd())
print(os.listdir())
'''
os.mkdir("testfolder")

with open("test.txt", "wt") as f:
    s="Hi Jae"
    f.write(s)

os.rename("test.txt", "testRenamed.txt")
os.rename("testfolder", "testfolderRenamed")
'''
print(os.stat("testRenamed.txt"))
print(os.stat("testfolderRenamed").st_size)

#from datetime import *
mod_time = os.stat("testRenamed.txt").st_mtime
print(mod_time)
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, fnames in os.walk("/Users/jaehyukshin/Desktop/module"):
    print("Current Path : ", dirpath)
    print("Directories : ", dirnames)
    print("Files : ", fnames)
    print("\n")
    
print(os.environ)
print("")
print(os.environ.get('HOME'))
fpath = os.path.join(os.environ.get('HOME'), 'desktop/text.txt')
print(fpath)

with open(fpath, 'w') as f:
	f.write("python is good. We can do everything!")
