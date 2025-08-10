org_list = []   #An empty list
for i in range(1,11):   #runs from 1 - 10
    org_list.append(i)  #appends each number from 1 - 10 to the empty list
print("Orginal list:",org_list) 
ext_list = org_list[:5]     #extract the first five elements using slicing
print("Extracted first five elements:",ext_list)        
rev_list = ext_list[::-1]       #reversing the first five elements using slicing
print("Reversed extracted elements:",rev_list)     
