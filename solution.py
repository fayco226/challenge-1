string = input("enter a string")

if len(string) > 10:
    print("string too long")
elif len(string) < 10:
    print("string not long enough")
result = ""
for i in string:
    result = result + i
    print(result)
