import array

my_array = array.array('i',[1,2,3,4,5])
print(my_array)
my_array.insert(0,6) # when we have to insert element in  zero index
print(my_array)
my_array.insert(3,10) #when we have to insert element in middle index
print(my_array)
my_array.insert(7,50) #when we have to insert element in end of the index
print(my_array)

# here my_array is array and when we insert element using '.insert(index where we have to that element,inserting number)'
#if we put index number greater than actual index then element will insert at end.
# time complexity for worst case is :O(N) 
# Space complexity for worst case is :O(1) 