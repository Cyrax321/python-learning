#lists
items=["bread","pasta","fruits","veggies"]
print(items)
print(items[0])
print(items[1],items[2])

#changing the value of the list
items[0]="chocolate"
print(items)

print(items[0:2]) #prints the first two elements of the list
print(items[-1]) #prints the last element of the list

items.append("butter") #adds the element to the end of the list
print(items)
items.insert(1,'jam') #adds the element at the specified index
print(items)

#concatenating lists
food=["chicken","mutton","fish"]
bathroom=["soap","shampoo","toothpaste"]
all_items=food+bathroom #concatenates the two lists
print(all_items)

#to find length of items
print(len(items)) #prints the length of the list


#to check weather items exists in the list

print("chicken" in items) #prints true if the element is present in the list
print("chicken " in all_items) #prints false if the element is not present in the list
print("muttton" in all_items)   #prints false if the element is not present in the list
print("soap" in bathroom) #prints true if the element is present in the list