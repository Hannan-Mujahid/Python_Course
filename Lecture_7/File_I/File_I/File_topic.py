f = open("demo.txt", "r")
data = f.read()
print(data)


"""
again_write = input("Do you want to write again (y/n): ")
if again_write == 'y':
    f = open("demo.txt", "a")
    data = input("Enter your data: ")
    f.write(data)
    f.write("\n")
f.close()
"""
f.close()
f = open("demo.txt", "w")
f.write("I am Hannan Mujahid")
f.close()