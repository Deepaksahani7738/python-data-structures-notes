# All file modes in Python

with open("mydata.txt","w") as create_file:
    for x in range(10):
        create_file.write("hello world\n")
        
 
        
with open("secret data.txt","w") as file:
    file.write("hii my name is deepak\n")
    file.write("he is a good python developer\n")
    file.write("they are complete python module\n")
    file.write("they are good coder \n")
    file.write("this is a amazing tools of python\n")
    file.write("vs code is a good for beginners\n")

with open("secret data.txt","a") as f_data:
    f_data.write("mumbai is a big city\n")
    f_data.write("there are lots of open source to learn python\n")
    f_data.write("reactjs is a good framework\n")


data=["mumbai","pune","chennai","hydrabad","gorakhpur","banarash","gujrat"]

with open("city.txt","w") as d:
    for item in data:
        d.write(item +"\n")


with open("mydata.txt","r") as create_file:
    data=create_file.read()
    print(data)

    
with open("secret data.txt","r") as f:
    res=f.read()
    print(res)  



with open("city.txt","r") as a:
    res=a.read()
    print(res)
    
    

    
    
# this is write , append and read mode in python 
    
with open("myinfo.txt","w") as data:
    data.write("he is a good coder\n")
    
 
    
with open("myinfo.txt","a") as toodle:
    toodle.write("happy new year 2023 !")

    

with open(r"myinfo.txt","r") as f:
    print(f.read())
    

# this is write and read mode in python

with open("ctc_file.txt","w+") as data:
    data.write("mango is a good fruit as compare to grapes !")
    
with open(r"ctc_file.txt","r") as f:
    print(f.read())  
    
    

# this is a read and write mode in python
    
    
with open("attrib.txt","r+") as d:
    d.write("amazing python")
    
    
with open(r"attrib.txt","r") as f:
    print(f.read())
    

# file handling of python !
# write binary and read binary mode in python

data_file=[10,20,30,40,50,60,70,80,90,100]

import pickle
with open("view_tech.txt","wb") as data:
    pickle.dump(data_file,data)
    
with open("view_tech.txt","rb") as file:
    res=pickle.load(file)
    print(res)
    
    
    
    
import os

res=os.listdir(r"C:\Users\ARVIND\OneDrive\Desktop\File Handling in Python")
for item in res:
    print(item)

# Handling the Current Working Directory

import os
result=os.listdir(r"C:\Users\ARVIND\Downloads")
print(result)


import os

result=os.listdir(r"C:\Users\ARVIND\Downloads\python-notes")
for item in result:
    print(item)


import os
cwd=os.getcwd()
print(f" Current Working Directory: {cwd} ")

#

#  opens the file in binary format for reading  in python

with open(r"C:\Users\ARVIND\OneDrive\Pictures\deepak.image.png","rb") as data:
    print(data.read())



with open(r"C:\Users\ARVIND\OneDrive\Desktop\Loops in Python\Loops in Python.py","rb") as data:
    res=data.read()
    print(res)
    

with open(r"C:\Users\ARVIND\OneDrive\Desktop\Loops in Python\Loops in Python.py","r") as f:
    print(f.read())


with open(r"C:\Users\ARVIND\OneDrive\Desktop\Regex in Python\snippets.txt","rb") as f:
    print(f.read())
    