print("Hello...! Welcome to Rushikesh's Projecct library")
# List
list=[1,10,2012,22.02,"hi","hroo",12]
print(len(list))   #this is length property 
print(list[0])      # Indexing
print(type(list))   #type of dataType
print(list[-1])     #reverse Indexing
print(list[2:5])    #this ru from index no. to index no.
list[1]="Rushi"     #Changing Element
list.insert(2,"Om")         #Insert new element on given position (position required)
list.append("Manav")        #Insert new eelement (position not required)
list.remove("hroo")        #remove element
list.pop(1)                 #remove element by index no.
del list[0]                 #deletes the element
no=[12,1,65,11,5,7]
no.sort()                  #sorting
no.sort(reverse=True)       #Reverse Sorting

print(no)

x=list+no
print(list)
print(x)