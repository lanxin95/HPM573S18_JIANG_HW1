#Problem 4: Lists and Mutability
yours=["Yale", "MIT", "Berkeley"]
mine=["Stanford", "SJTU", "Yale"]
ours1 = mine + yours

ours2 = []
ours2.append(mine)
ours2.append(yours)

#1. Print ours1 and ours2. Describe how ours1 and ours2 differ from each other.
print(ours1)
print(ours2)
#Ours1: "+ operator" combines the two lists, yours and mine, together, and creates a new list ours1. It concatenates the elements from yours and mine to the new list.
#Ours2: "append" mutates the list and adds the list "mine" as the element to the end of the list mine. Thus, ours2 is a list with the elements of two lists.

#2. Change the second element of yours to something else and again print ours1 and ours2. Explain why changing yours would changes ours2 but not ours1.2.
yours[1]="Harvard"
print(ours1)
print(ours2)
#Because a list is an object in memory, and it is mutable. By using a key phrase to change an object,such as append here, any variable points to that object will be affected.
#Thus, changing the element in yours would also influence ours2.