l = [5, 5, 5, 5, 5]
print(len(l))

print("Number entering program!")
n = int(input("Enter the elements you want to enter:"))


inputList = []

for i in range(n):
    temp = int(input("Enter number"))
    inputList.append(temp)

outputList = [x for x in inputList if x % 2 == 0]

for i in range(len(outputList)):
    print(outputList[i])


# list=[]
# tuple=()
# set={}
# dictionary={key:value}
