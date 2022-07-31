str1=str(input("enter a string: "))
def reverse():
    reverse=""   
    for i in str1:
        reverse = i + reverse
    print("Reverse of the string: ",reverse)
 
print("The original string is: ",str1)
 
reverse()