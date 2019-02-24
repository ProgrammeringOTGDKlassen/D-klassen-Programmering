liste = [1, 2]

lenList = len(liste)-1
print(lenList)

for i in range(0, lenList):
    print("Dette er i {}".format(i))
    s = liste[i]
    t = liste[i+1]
    print("Dette er s {}".format(s))
    print("Dette er t {}".format(s))


