import array 
my_array = array.array('i',[13,21,32,43,55,63,])
my_array1 = array.array('d',[1.2,1.3,1.4,1.8,1.9,1.6])
print(my_array)
my_array1.insert(2,2)
print(my_array1)
def access_element(array,index):
    if index >= len(array):
        print("there is not any element on this index")
    else:
        print(array[index])
access_element(my_array,3)