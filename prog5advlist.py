# List Sorting

# Sort in alpha numeric order default it is ascending


my_list = ['banana', 'orange', 'apple', 'guava']
my_list1 = [90, 400, 200 , 20 , 10 , 50]
my_list.sort()

print(my_list)
print(my_list1)

# sort in descending order

my_list2 = [90, 400, 200 , 20 , 10 , 50 ]
my_list2.sort(reverse = True)
print(my_list2)

my_list3 = [90, 400, 200 , 20 , 10 , 50 ]
my_list3.sort(reverse = False)
print(my_list3)



# Case Insensitive sorting
# by default sort() is case-sensitive
# all the capital letters will be sorted before lowercase letters
my_list4 = ['banana', 'Orange', 'Apple', 'guava' ]

my_list4.sort(key = str.lower)

print(my_list4)


# reverses the order of a list
my_list5 = ['banana', 'orange', 'apple', 'guava' ]

my_list5.reverse()

print(my_list5)

# Copying the list

list1 = [10,20,30,40] #original list

list2 = list1.copy() #copy list
list2 = list(list1) #another way for copying of the list
print(list2)

list2.pop()
print(list1)
print(list2)



