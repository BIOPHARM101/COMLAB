def run():
    Name = input("Name : ")
    Year = input("age : ")
    Year1 = int(Year)
    Since = 2565-Year1
    Since1 = Since%100
    Since2 = str(Since1)

    print("Name: "+Name)
    print("Age : "+Year)
    print(Name+Since2+"@chula.ac.th")

run()