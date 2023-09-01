def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) #this is a example of O(n^2)
print_items(20)
#it doesn't matter either there is N^2 or N^3 orN^N this will always be complexity of O(n^2)