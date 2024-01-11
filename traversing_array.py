import array 
my_array = array.array('i',[1,2,3,4,5,6,7])
my_array1 = array.array('d',[1.3,1.2,1.5,1.6,1.8])
#print(my_array)
#print(my_array1)

def traverse_array(array):
    for i in array:
        print(i)
        
traverse_array(my_array)
traverse_array(my_array1)