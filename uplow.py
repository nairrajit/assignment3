#Calculate the Upper and Lower case

str1=str(input("Enter a string: "))

def case():
    lchr=0
    uchr=0
    for lowcase in str1:
        if lowcase in "abcdefghijklmnopqrstuvwxyz":
            lchr+=1
    print("Number of lower case characters: ", lchr)
    for uppcase in str1:
        if uppcase in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uchr+=1
    print("Number of upper case characters: ", uchr)

print("Original string you entered: ", str1)
case()
