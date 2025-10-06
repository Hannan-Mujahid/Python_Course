f = open("demo.txt", "r")
data = f.read()
print(data)

again_wright = input("Do you want to write again (y/n): ")
if again_wright == 'y':
    f = open("demo.txt", "a")
    data = input("Enter your data: ")
    f.write(data)
    f.write("\n")
f.close()
# f.close()