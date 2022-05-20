#Comparing strings
'A' == 'A'
'A' == 'a'
'a' != 'A'
'abc' <= 'abc'
'Abc' > 'abc'
#sting slices
A = 'Hello_world'
print(A[4:7])
print(A[3:])
print(A[:8])
print(A[4:1:-1])
print(A[9:11])
print(A[::])
print(A[::-1])
A.capitalize() #capitalize first letter
# A.find(w,i,j) #finds a between ith and jth index
A.isalpha() #ture,if there are only space in string(at least one).
A.isdigit()
A.isalnum()
A.isspace()
A.islower()
A.isupper()
A.istitle()
A.lower()
A.upper()
A.title()
len(A)
