f = open("file.txt","r",encoding="utf-8") #utf is for emoji 

lines =f.readlines()

print(lines, type(lines))

f.close()