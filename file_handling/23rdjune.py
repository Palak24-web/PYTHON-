f = open("file.txt","r",encoding="utf-8") #utf is for emoji 

# line1 =f.readline()
# print(line1, type(line1))

# line2 =f.readline()
# print(line2, type(line2))

# line3 =f.readline()
# print(line3, type(line3))

# line4 =f.readline()
# print(line4, type(line4))

# line5 =f.readline()
# print(line5, type(line5)) #it will print empty string if no line is present

  #or we can use loop also like:



line=f.readline()
while line!="":
    print(line)
    line=f.readline()
f.close()