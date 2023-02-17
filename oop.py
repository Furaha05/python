class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and i'm {self.age} years old")

class restaurants:
    def __init__(self,type,name,year):
        self.type=type
        self.name=name
        self.year=year
    def hello_me(self):
        print(f"This is a {self.type} and its called {self.name}, first opened in the year {self.year}")
#creating an object
myobj=students("Temina",4)
myobj2=students("Foi",22)
myobj3=students("Furaha",18)
myobj=restaurants("Chinese","Hongshii" ,2002)
myobj12=restaurants("mexican","Kabale",2019)
myobj=musicians("UK", "RNB", 23, 12)
myobj.hello_me()
myobj2.hello_me()
myobj3.hello_me()
myobj.hello_me()
myobj12.hello_me()

class musicians:
    def __init__(self,country,songtype,age,numberofalbums):
        self.country=country
        self.songtype=songtype
        self.age=age
        self.numberofalbums=numberofalbums
    def music(self):
        print(f"Singer is from {self.country} and sings {self.songtype}. She is {self.age} years old, and has released {self.numberofalbums} albums")
myobj=musicians("UK", "RNB", 23, 12)
myobj12.music()