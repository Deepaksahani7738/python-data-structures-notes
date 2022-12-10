mydata=open(r"C:\Users\ARVIND\OneDrive\Desktop\deepak sahani\functional.py.txt","r")
print(mydata.read())
mydata.close()
    
def mydata():
    name="karan"
    return(name)
res=mydata()
print(res)


for num in range(10):
    print(num,end="\t")
print()



i=0
while i<15:
    i+=1
    j=0
    while j<6:
        j+=1
        print("*",end=" ")
    print("\n")


for i in range(1,6):
    print(i,end=' ')
    for j in range(1,5):
        print(j,end=' ')
    print("\n")
    
for i in range(1,6):
    print("*",end=' ')
    for j in range(1,5):
        print("*",end=' ')
    print("\n")


for i in range(1,10):
    for j in range (i+1):
        print("*",end='\t ')
    print("\n")
        
for i in range(1,10):
    for j in range (i+1):
        print("*",end='  ')
    print("\n")
        
for i in range(10,0,-1):
    for j in range(i+1):
        print("*",end=' ')
    print("\n")

for i in range(10,0,-1):
    for j in range(5,0,-1):
        print("*",end=" ")
    print("\n")

def mydata():
    for i in range(10,0,-2):
        for j in range(i+1):
            print(j,end=" ")
        print('\n')
mydata()

def mydata():
    for i in range(10,0,-1):
        for j in range(i+1):
            print(j,end=" ")
        print('\n')
mydata()

data=int(input("enter the even and odd numbers"))
if data%2==0:
    print("even")
else:("odd num")


i=0
while i<10:
    i+=1
    j=0
    while j<10:
        j+=1
        print("*",end=" ")
    print("\n")
    
    
i=0
for i in range(10):
    i+=1
    j=0
    for j in range(10):
        j+=1
        print("*",end=" ")
    print("\n")


for i in range(10,0,-1):
    for j in range(i+1):
         print("*",end=' ')
    print('\n')
for k in range(1,11):
    for m in range(k+1):
        print("*",end=' ')
    print('\n')


i=0
for i in range(10,0,-1):
    i+=1
    j=0
    for j in range(i+1):
        j+=1
        print(j,end=' ')
    print('\n')
i=0
for i in range(1,11):
    i+=1
    j=0
    for j in range(i+1):
        j+=1
        print(j,end=' ')
    print('\n')