def binary_search(sps, n): 
    sps = [1,2,3,4,5,6,7,8,9,12,17,19,23,28,33,35,39,40,47,46,56,66,67,90]
    left = -1 
    right = len(sps) 
    while right > left + 1: 
        middle = (left + right) // 2 
        if sps[middle] >= n: 
            right = middle 
        else: 
            left = middle 
    return right

print(binary_search(sps=[1,2,3,4,5,6,7,8,9,12,17,19,23,28,33,35,39,40,47,46,56,66,67,90] , n=40))





def buble_sort (list):

    done = False
    while not done:
        done = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                done = False
    print(list)
print(buble_sort(list = [33,67,12,59,90,77,35,45]))