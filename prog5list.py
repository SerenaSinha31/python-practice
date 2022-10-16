listItems = [10,20,30,40]
listItems1 = [10,20,30,40, 'apples', 'oranges']
listItems = [10,20,30,40, 40, 30]

print(listItems1[4])
print(listItems)
print(type(listItems))


listOne1 = ['abcd', 40, True, 60, 'oranges']
print(listOne1)


#creating a list through constructor

listOne = list((10,20,30))
listTwo = [10,20,30]
print(listOne)
print(listTwo)

list3= [10,20,30,40,50]

print(list3[-2])

# search will start at index 2(include) and end at index 5(not included)
print(list3[2:5])

print(list3[:4])

print(list3[2:])

# change the list items

list4 = [30,60,10,20,80]

list4[1] = 90
list4[4] = 'hello'
#change a range of list items
list4[2:3] = ["hi", "hello"]
print(list4)

# insert items

list5 = [10,20,30]

list5.insert(2, 40)
print(list5)

# append items
# for adding the item at the end of the list
list6 = [10,20,30]
list6.append(40)
list6.append(50)
list6.append(60)
print(list6)

#extend a list
# To append or to add elements from another list into the current list we use extend()
#you can add or append any kined of iterable objects like tuples, sets, dictionaries etc.

list7 = [10,20,30]
list8 = [40,50,60]
tuple = (50,60)
list7.extend(list8)
print(list7)
print(list8)
list7.extend(tuple)
print(list7)

# remove a specified item from the list
# remove()

myList = ['john', 'peter', 'raj']
myList.remove('raj')
print(myList)

#remove item from specified index using del keyword

my_List = ['john', 'peter', 'raj']

del my_List[0]
# del myList
print(my_List)

#empty the list

myList2 = ['john', 'peter', 'raj']
myList2.clear()
print(myList2)





