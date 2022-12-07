string = input("enter a string")

if len(string) > 10:
    print("string too long")
elif len(string) < 10:
    print("string not long enough")
result = ""
for i in range(0, len(string)):
    result = result + string[i]
    print(result)
