class Hotel():
    def __init__(self, name, age=0, phone=000):
        self.name = name
        self.age = age
        self.phone = phone

    def addStuff(self, wname, id):
        self.wname = wname 
        self.id = id 
        self.age = 23
    
    def addGuest(self, gname, gage, phone): 
        self.gname = gname 
        self.gage = gage 
        self.phone = phone
        
        
    def printAllStuffs(self):
        print("Name:", self.wname)
        print("age", self.age)
        print("phone:", self.phone)

    def printAllGuest(self):
        print("name:", self.gname)
        print("age", self.gage)
        print("phone:", self.phone) 


h = Hotel("Lakeshore")
h.addStuff("Adam", 26)
print("=================================")
print(h.printAllStuffs())
print("=================================")
h.addGuest("Carol", 35, "123")
print("=================================")
print(h.printAllGuest())
print("=================================")
h.addGuest("Diana", 32 , "431")
print("=================================")
print(h.printAllGuest())