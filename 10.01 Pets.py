class Pet ():
    def __init__(self):
        self.Name=""
        self.Type=""
        self.Age=0

petsfile = open("10.01 Pets.txt")   
x = petsfile.readline() 
y = x.split(",")
myPet1 = Pet()
myPet1.Name = y[0].strip()
myPet1.Type = y[1].strip()
myPet1.Age = int(y[2].strip())

x = petsfile.readline()
y = x.split(",")
myPet2 = Pet()
myPet2.Name = y[0].strip()
myPet2.Type = y[1].strip()
myPet2.Age = int(y[2].strip())

x = petsfile.readline()
y = x.split(",")
myPet3 = Pet()
myPet3.Name = y[0].strip()
myPet3.Type = y[1].strip()
myPet3.Age = int(y[2].strip())

petsfile.close()
print("{:>8s}{:>8s}{:>8s}".format("Name","Type","Age"))
print("{:>8s}{:>8s}{:>8d}".format(myPet1.Name,myPet1.Type,myPet1.Age))
print("{:>8s}{:>8s}{:>8d}".format(myPet2.Name,myPet2.Type,myPet2.Age))
print("{:>8s}{:>8s}{:>8d}".format(myPet3.Name,myPet3.Type,myPet3.Age))