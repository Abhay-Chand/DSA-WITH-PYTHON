#O(1) SPACE COMPLEXCITY
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i,i+1)
    return 0

def pair_sum(a,b):
    return (a+b)

pair_sum_sequence(10)
pair_sum(2,9)
