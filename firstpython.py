








"""
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