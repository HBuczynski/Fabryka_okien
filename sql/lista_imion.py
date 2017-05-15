def generatorImion(self):
names = []
with open("~/sql/imiona.txt") as file:
    for line in file:
        line = line.strip() 
        names.append(line)
return names
