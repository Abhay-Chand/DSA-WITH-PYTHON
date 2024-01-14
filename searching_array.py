import array 

arry1 = array.array("i",[1,2,3,4,5,6])
arry2 = array.array("d",[1.2,3.2,5.2,0.6,6.5,5.5])
def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target :
            return i
    return ("not found")
print(linear_search(arry1,4))