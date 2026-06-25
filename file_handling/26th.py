# f = open("file.txt")
# print(f.read())
# f.close()

# using with statement we don't need to close the file manually 

with open("file.txt",encoding="utf8") as f:
    print(f.read())

    # file will be closed automatically by with statement