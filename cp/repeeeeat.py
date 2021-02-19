# Add a char n times in a string
print("Enter total inputs:")
for _ in range(int(input())):
    print("Enter String")
    str = input()
    print("Enter letter")
    letter = input()
    print("Enter Repititions")
    repeat = int(input())

    print(str[:len(str)//2]+(letter*repeat)+str[len(str)//2+1:])
