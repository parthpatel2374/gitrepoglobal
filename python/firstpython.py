import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="Arth",
  password="password"
)
print(mydb)






"""
cont from python mysql...

import matplotlib.pyplot as plt
import numpy as np
#xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
plt.plot(xpoints, ypoints)
print(matplotlib.__version__)
cont from libs...

import os
#os.rmdir("delfolder")
os.rmdir("/Users/parthpatel/Desktop/gitrepoglobal/python/delfolder")
if os.path.exists("/Users/parthpatel/Desktop/gitrepoglobal/python/newmodule.txt"):
    os.remove("/Users/parthpatel/Desktop/gitrepoglobal/python/newmodule.txt")
else:
    print("file not exists")
f = open("file1.txt", "w")
f.write("some text is being written in this file.")
f.close()
f = open("file1.txt", "r")
print(f.read())
f.close()
f1 = open("file1.txt", "x")
f2 = open("module.txt", "x")
if(f2):
    print("both files open")
f1.close()
f2.close()
f =open("module.txt", "a")
f.write("now there is more content.")
f.close()
f = open("module.txt", "r")
print(f.read())
f.close()
for x in f:
    print(x)
f.close()
f = open("/Users/parthpatel/Desktop/gitrepoglobal/python/newmodule.txt", "r")
print(f.readline())
mybike = "There is my bike named {name}. It has {number} tyres, and two {sound}."
print(mybike.format(name="gorbik", sound="horns", number=2))
name = input()
print("his name is",name)
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
try:
    print(x)
except:
    print("something else went wrong")
finally:
    print("the 'try except' is finished")
try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")
except NameError:
    print("x is not defined")
import camelcase
c= camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, separators=(". ", "= "), sort_keys=True))
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
x ={
    "name" : "Parth",
    "surname" : "patel",
    "age" : 20,
    "license" : "no"
}
y= json.dumps(x)
print(y)
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
import newmodule
newmodule.greet("parth")
a = newmodule.person1["country"]
print(a)
b = dir(newmodule)
print(b)
cont from iterators....

class person:
    def __init__(self, fnam, lnam):
        self.fname=fnam
        self.lname=lnam
    a=100
    def printname(self):
        print(self.fname, self.lname)
class student(person):
    def __init__(self, fnam, lnam):
        super().__init__(fnam, lnam)
x=person("parth", "patel")
x.printname()
x=student("vrund", "patel")
x.printname()
print(x.a)
class mclass:
    def __init__(self, a, b):  
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a} {self.b}"
    def println(self):
        return self.a*self.b
obj = mclass(10, 20)
print(obj.a)
print(obj.b)
print(obj.println())
print(obj)
def myfin(x):
  return lambda a: a*x    
myfun = myfin(10)
print(myfun(10))
def myfun(x):
    return 5+x
print(myfun(20))
  for x in fruits:
    print(x)
frut=["apple", "banna", "mango"]
myfun(frut)
  print("this is "+state["maharashtra"]+" fruit.")
myfun(kashmir="apple", maharashtra="sugarcane", gujarat="mango")
  print("this is "+fruits[1]+" fruit.")
myfun("apple", "banna", "mango")
    print("hellow from this function.")
cont from functions...

for x in range(5, 30, 5):
    print(x)
else:
    print("this is the end")
fruits=["apple", "banna", "mango"]
for x in fruits:
    print(x)
    if(x=="banna"):
        continue    
for x in "banna":
    print(x)
i=1
while i<10:
    i+=1
    print(i)
else:
    print("i is now >10")
print(i)
    if(i%2==0):
        continue
a=200
b=33
if b>a:
    pass
print("this has passed")
print("a = ", a) if(a>b) else print("b = ", b)
if a>b: print("a = ", a)
if a<b:
    print("a = ", a)
elif(a==b):
    print("a&b = ", a, b)
else:
    print("b = ", b)
cont from functions.....

fruit={
 
	"mango":{
    "season":"summer",
    "color":"yellow",
    "price":120
    },
	"apple":{
    "season":"all",
    "color":"red",
    "price":70
    },
	"grape":{
    "season":"summer",
    "color":"green&black",
    "price":100
	},
	"watermellon":{
    "season":"summer",
    "color":"green",
    "price":20
    } 

}
print(fruit["mango"]["color"]) 
mango={
    "season":"summer",
    "color":"yellow",
    "price":120
    },
apple={
    "season":"all",
    "color":"red",
    "price":70
    },
grape={
    "season":"summer",
    "color":"green&black",
    "price":100
	},
watermellon={
    "season":"summer",
    "color":"green",
    "price":20
    } 

fruit={
    "wateremellon":watermellon,
    "mango":mango,
    "apple":apple,
    "grape":grape,
}
mango=dict(fruit)
print(mango)
for x in fruit.keys():
  print(x)
for x in fruit.values():
  print(x)
for x in fruit.items():
  print(x)
fruit.clear()
del fruit
fruit.pop("color")
fruit.popitem()
fruit.update({"color":"redish yellow", "price":120})
fruit["season"]="monsoon"
x = dictfruit.keys()
x = dictfruit.values()
x = dictfruit.items()
x = dictfruit.get("name")
print(dictfruit["price/kg"])
a=set(("apple", "banna", "mango", True, 2, 3))
a.remove(True)
print(a) 
b={1, 2, 3}
a.intersection_update(b)
b.discard(4)
c=a.symmetric_difference(b)
a.symmetric_difference_update(b)
c=a.intersection(b)
c=a.union(b)
a.update(b)
print(c) 
for x in thisset:
newset={"fruits", "numbers"}
thisset.pop()
del thisset
thisset.clear()
thisset.add("orange")
mytuple=tuple((1, "apple", "cherry", "berry", 5.34, 5, 5))
print(x)
x=round(mytuple[4])
thistuple=("crush", "boy", "fucks", "girl")
newtuple=thistuple*2
print(newtuple)
mytuple+=thistuple
for x in mytuple:
	print(x)
for i in range(len(mytuple)):
	print(mytuple[i])
(number1, *fruitred, number2)=mytuple
print(number1)
print(number2)
print(fruitred)
oneitem=("crush", )
mytuple += oneitem
y=list(mytuple)
y[2]="banna"
x=tuple(y)
print(x)
print(mytuple[:3])
print(mytuple[3:])
print(type(mytuple))
print(oneitem)
print(len(mytuple))
cont from tuples...

thislist=[1, 6, 4, 3, 5, 2]
cpylist=thislist.copy()
list1=thislist+cpylist
print(list1)
cpylist.append(100)
print(thislist)
print(cpylist)
thislist.extend(cpylist)
print(thislist)
thislist.sort(reverse=True)
print(thislist)
newlist=[x for x in thislist if x<5]
print(thislist)
print(newlist)
cont from loop list...

thislist.clear()
print(thislist)
del thislist[2]
thislist.pop()
thislist.pop(3)
thislist.remove(2)
print(thislist)
del thislist
print(thislist)
fruits=["apple", "banna", "mango"]
thislist.extend(fruits)
fruits.extend(thislist)
print(thislist)
print(fruits)
thislist.append(4)
print(thislist)
thislist.insert(1, 1.5)
print(thislist)
print(thislist[1:2])
print(len(thislist))
print(thislist[-3])
print(thislist)
print(type(thislist))
x=8
y=(x<<2)
z=(x>>2)
print(y,z)
print(bool("hellp"))
print(bool(15))
cont from python booleans...

a = "Hi I am the \"\n\" #creator"
print(a)
px=18
vx=19
kx=20
y="My name is Pth, I am {2} years old."
"My friend Vnd is {1} years old."
"And another friend Ktn is {0} years old."
print(y.format(kx, vx, px))
print(x.replace('H', 'P'))
print(x.split(" "))
print(x.strip())
print(x.lower())
print(x.upper())
print(y[-5: -0])
print(y[-5:])
print(y[:-5])
print(y[4:])
print(y[:4])
print(y[0:4])
print(len(y))
for y in "Hello Python":
	print(y)
x= "Hello Python, how are your learning experience going"
"so far!I am happy to talk with you again,"
"hello world is world universal favourite tags one of the"
"i mean!"
y='Hello Python'
print(x)
print(y)
x=int(5.25)
print(x)
x=5
y="John"
print(x, y)
x="Python "
y="is "
z="awesome."
print(x+y+z)
if(5>2):
	print("hi world")
this print is commented!!!
print("Hello, World!")
"""