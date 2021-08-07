n = int(input("Enter the number of students: "))
list1 = []
for i in range(n):
    name = input() 
    list1.append(name)
# makes a tuple from the list of names
tuple1 = tuple(list1)
findName = input("Enter name to find: ")
#   part (a) a user defined function to search
def userDefinedSearch():
     #loops through every element of tuple
    for item in tuple1:
         #if any element is equal to what we are finding
        if item==findName:
            #announce item found
            print("Name found") 
            return #return from the function
    #this statement is reached only if the element is not found
    print("Name not found")

#calling user defined function
userDefinedSearch()

# part (b) built in function
# index() returns the first index where element is found
# the return value will be either 0 or more than 0 if the element is present in the tuple 
if tuple1.index(findName) >=0 :
    print("Name found")
else:
    print("Name not found")
