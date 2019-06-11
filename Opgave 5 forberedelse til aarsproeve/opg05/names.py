godkendteFornavnePiger = 0
godkendteFornavneDrenge = 0
pigerB = []
drenge4 = 0
with open("godkendte-pigenavne-1988.txt", "r") as f:
    for line in f:
        godkendteFornavnePiger += 1
        print(line.strip())
        if line[0] == "B":
            pigerB.append(line.strip())

with open("godkendte-drengenavne-1988.txt", "r") as m:
    for line in m:
        godkendteFornavneDrenge +=1
        #print(line.strip())
        if len(line) == 5:
            drenge4 +=1
'''
print("----------------")
print("Der er ",godkendteFornavnePiger, "godkendte fornavne til piger")
print("Der er ",godkendteFornavneDrenge, "godkendte fornavne til drenge")
print("Der er ",drenge4, "godkendte drenge navne på 4 bogstaver")

print("---------------")
print("Følgende pigenavne starter med b:")
for i in range(0,len(pigerB)):
    print(pigerB[i])
'''
