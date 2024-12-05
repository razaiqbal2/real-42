fruit=["mango","apple","melon","watermelon","orange"]

#indexing
print(fruit[1],"is rich with iron")

#length
print("the length of list is",len(fruit))

#slicing
print("sliced list is ",fruit[1:5])

#append
fruit.append("cherry")
print("the updated version of list is",fruit)

#remove
fruit.remove("melon")
print("the updation after removal in list", fruit)

#sort
fruit.sort()
print("sorted a list ",fruit)

#reverse
fruit.reverse()
print("Reversed list",fruit)