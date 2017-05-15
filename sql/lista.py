def generatorImion(self):
names = []
with open("~/sql/imiona.txt") as file:
    for line in file:
        line = line.strip() 
        names.append(line)
return names

def generatorNazwisk(self):
names = []
with open("~/sql/nazwiska.txt") as file:
    for line in file:
        line = line.strip() 
        names.append(line)
return names

def generatorUlic(self):
names = []
with open("~/sql/ulice.txt") as file:
    for line in file:
        line = line.strip() 
        names.append(line)
return names
