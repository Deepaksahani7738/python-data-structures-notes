def mydata():
    name=("hii my name is tina")
    designation=("python developer")
    print(name)
    print(designation)
mydata()

hii my name is tina
python developer





def mytech():
    name=input("enter the city name: ")
   
    print(f"the name is: {name}")
    age=input("enter the age : ")
    print(f"the age is :{age}")
   
mytech()


enter the city name: mumbai
the name is: mumbai
enter the age : 23
the age is :23



def greet1():
    return "This is a function using return"
res=greet1()
print(res)

This is a function using return


country="india"
def mydata():
    name="devika"
    print(f'the name is : {name}')
    return(f'which city : {country}')
res=mydata()
print(res) 

the name is : devika
which city : india   
    


data=[10,20,30,40,50]
def mydata():
    print(f"the value is : {data}") ==>this is print statement
mydata()

the value is : [10, 20, 30, 40, 50]


data=[10,20,30,40,50]
def mydata():
    results=data
    return(f"the value is : {results}") ==>this is return statement
result=mydata()
print(result)

the value is : [10, 20, 30, 40, 50]



def mydata():
    name="deepak"
    last="sahani"
    def data():
        roll_no=45
        id=114
        def square():
            city="mumbai"
            live="kandivali"
            print(name)
            print(last)
            print(roll_no)
            print(id)
            print(city)
            print(live)
        square()
    data()
mydata()  


deepak
sahani
45
114
mumbai
kandivali  
            
            
            
            
def myinfo(*num):
    for i in num:
        print(i)
myinfo(4,5)

4
5


def mydata(name="deepak",city="pune",course="php"):
     print(name)
     print(city)
     print(course)
mydata()

deepak
pune
php



data=["tcs","mumbai","pune","nashik","banglore"]
val=[10,20,30,40]
from itertools import zip_longest
res1 = dict(zip_longest(data,val))
print(res1)

{'tcs': 10, 'mumbai': 20, 'pune': 30, 'nashik': 40, 'banglore': None}




addition=lambda num1,num2,num3,num4,num5,num6:num1+num2+num3+num4+num5+num6
res=addition(10,20,30,50,80,144)
print(res)

334

data=lambda num1:num1//2
result=data(10)
print(result)

5


myinfo=(10,20,30,40,50)
mydata=map(lambda num:num*2,myinfo)
res=tuple(mydata)
print(res)


(20, 40, 60, 80, 100)


myinfo=[10,20,30,40,50]
mydata=map(lambda num:num*2,myinfo)
res=list(mydata)
print(res)


[20, 40, 60, 80, 100] 


def data():
    name="Deepak"
    return(name)
res=data()
print(res)

Deepak

data=[10,20,30,40,50,60,70,80,90,100]
mydata=map(lambda num:num**2,data)
res=list(mydata)
print(res)

[100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000]

def data(*data):
    for i in data:
        print(i)
data(10,20)

10
20



def mydata(*date):
    
    
    print(date)
mydata(10,20,30)

(10, 20, 30)


a=[10,20,30]
data=map(lambda num:num*2,a)
res=tuple(data)
print(res)


(20, 40, 60)

def data(num1,num2):
    result=num1+num2
    return(result)
a=data(140,60)
print(a)

200

def data(a,b):
    res=a//b
    return(res)
b=data(20,2)
print(b)

10


def solo(p1,p2,p3):
    res=p1*p2//p3
    return(res)
r=solo(20,5,10)
print(r)

10


data=(10,20,30)
a=map(lambda num:num*2,data)
res=set(a)
print(res)

{40, 20, 60}

a=lambda num:num//2
res=(10)
print(res)

10


def data():
    name="rajshree"
    designation="python developer"
    print(f"he is name is : {name}")
    print(f"designation : {designation}")
    def mydata():
        city="mumbai"
        friends="Deepak","karan","lokesh"
        print(f"city : {city}")
        print(f"he's friends is this : {friends}")
        def a():
            city="mumbai"
            friends="Deepak","karan","lokesh"
            print(f"city : {city}")
            print(f"he's friends is this : {friends}")
            def b():
                city="mumbai"
                friends="Deepak","karan","lokesh"
                print(f"city : {city}")
                print(f"he's friends is this : {friends}")
                def c():
                    city="mumbai"
                    friends="Deepak","karan","lokesh"
                    print(f"city : {city}")
                    print(f"he's friends is this : {friends}")
                    def info(*num):
                        print(num)
                    info(20,30)
                c()
            b()
        a()
    mydata()
data()


he is name is : rajshree
designation : python developer
city : mumbai
he's friends is this : ('Deepak', 'karan', 'lokesh')
city : mumbai
he's friends is this : ('Deepak', 'karan', 'lokesh')
city : mumbai
he's friends is this : ('Deepak', 'karan', 'lokesh')
city : mumbai
he's friends is this : ('Deepak', 'karan', 'lokesh')
(20, 30)

     
data=[140,20,30,40,50]
mydata=map(lambda num:num//2,data)
res=list(mydata)
print(res)

[70, 10, 15, 20, 25]

data=("a","b","c","d","e","f")
a=(10,20,30,40,50,60)
result={k:v for k,v in zip(data,a)}
print(result)

{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

data=[[10,20,30,40,50],[1,32,45,60]]
for i in data:
     for j in i:
         print(j)

print(data[0][1])
print(data[1][0])

10
20
30
40
50
1
32
45
60
20
1

        









