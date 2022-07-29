lst=[]
num=int(input("Enter the number of digits in the list: "))
for n in range(num):
        series= int(input("Enter the numbers you want in the list:"))
        lst.append(series)

def addition():
        sum=0
        i=0
        while i<num:
                sum += lst[i]
                i+=1
        print("Sum of the numbers in the list: ",sum)

print("Entered list: ",lst)
addition()
