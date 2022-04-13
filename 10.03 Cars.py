import csv

class Car:
    def __init__(self,year,make,speed=0):
        self.year = year
        self.make = make
        self.speed = speed

    def accelarate(self,value):
        self.speed = self.speed + value

    def brake(self,value):
        self.speed = self.speed + value

if __name__ == "__main__":
    flag = True
    changes = []
    with open('10.03 Cars.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if flag:
                car = Car(year=row[0],make=(row[1]).strip())
                flag = False
                continue
            changes.append(int(row[0]))
    print('Make: ',car.make)
    print('Year: ',car.year)
    print("\nChange\tSpeed")
    for change in changes:
        if change>0:
            car.accelarate(change)
        else:
            car.brake(change)
        print(f"{change}\t{car.speed}")