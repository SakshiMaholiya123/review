import csv
t=(10,20,30)
tot=sum(t)
avg=tot/len(t)

with open("python_fundamentals/data.csv","w") as file:
    writer=csv.writer(file)
    
    writer.writerow(["values","sum","average"])
    writer.writerow([t,tot,avg])

with open("python_fundamentals/data.csv","r") as file:
    reader=csv.reader(file)
    for i in reader:
        print(i)