#list-mutable
import colorsys


L=list('power')
print(L)
#L=list(input('Enter elements:'))
#print(L)
#appending elements
L=[2,3,5]
#L[3]=12
L.append(12)
#deleting elements
del L[2] #delets elements at index 2
del L[1:4] #delets slice of 1:4 i.e 1,2,3 indices
del L #delets the whole list.
#extending elements
L=[2,5,17]
L.extend((21,'hi',[1,2,3]))
#updating elemts
L[1]=2
print(L)
#making a ture copy
color=['red','blue','green']
L2=colors #error
L2=list(colors)

#List-functions
#insert method
L.insert(<pos>,<items>)
#pop method
L.pop(<index>) #delets and returns elements at<index>
L.pop() #delets and returns last elements
#remove method
L.remove(<value>) #removes the first occurence of <value>
#clear method
L.clear() #clears the whole list, [], this remains
#count method
L.count(<item>) #count the <item> and returns
#reverse method
L.reverse() #reverses the whole list.
#sort method
L.sort() #sorts the list in ascending order.
L.sort(reverse=Ture) #sorts the list in descending order
