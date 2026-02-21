#Empty Tuple
from operator import index


my_tuple = ()
print(my_tuple)

#Tuple with integers
my_tuple = (1, 2, 3)
print(my_tuple)
#Tuple with mixed data types
my_tuple = (1, "Hello", 3.14)

#nested Tuble
my_tuple =("mouse",[8,4,6],(1,2,3))
print(my_tuple)

#Accessing Tuble elements using indexing
my_tuple = ("p","e","r","m","i","t")
print(my_tuple[0])
print(my_tuple[5])
#nested Tuble
n_tuple = ("mouse",[8,4,6],(1,2,3))

#nested index
print(n_tuple[0][3])
print (n_tuple[1][1])

 #slicing 
print(my_tuple[1:4])

 #Interacting with Tuble  

for letter in (my_tuple):
    print("Hello", letter)
 
