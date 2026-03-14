marks ={
 "palak":98,
 "mitali":92,
 "om":76
}

print(marks)
print(marks["om"])
print(marks.get("om")) #both are same but the only diff is that get method does not give error if key is not present it shows none 


print(marks.items()) # print key value pairs and items
print(marks.keys())  # print keys
print(marks.values()) #print values
marks.update({"mitali":98}) # update the value , not changed becoz dictionary is mutable

print(marks.pop("palak"))  #pop method removes the key value pair and returns the value of the removed key
print(marks)

print(marks.popitem()) #popitem method removes the last inserted key value pair and returns it as tuple


