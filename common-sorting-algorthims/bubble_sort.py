# Bubble sort, O(n**2), in-place algorithim.
# array = [3, 2, 1, 0]
# the idea is two have two loops:
# the outerloop (iteration loop) represents the # of unsorted elements, here we have 4 elements. You do the iteration 3 times
# the inner loop compares every two adjacent elements (1,2) / (2,3) / (3,4)
# thus the inner loop that compares each two adjacent elements together and then swaps them if element2<element1
# see here: j = 0 (first run), compare: 3-2 , 3-1, 3-0 --> i = 0,1,2 (inner loop)
# j = 1 (second run), compare 2-1, 1-0 --> i = 0,1 (inner loop)
# j = 2 (third run - last), compare 1-0 --> i = 0 
# notice j elements are 3 len(array) - 1: 0,1,2  (3 iterations)

arr = [20, 35, -15, 7, 55, 1, -22]


def bubble_sort(arr):
    iterations = len(arr) -1 # because when you reach the last element... theres's nothing to compare it with. 
    for j in range(iterations):
        for i in range(iterations - j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                #the else block is redundant, but makes the code easier to read. Always make sure your code is readable. Don't be a smartass with oneliners.
                continue
    return arr # in case the input was not a variable but a list []

bubble_sort(arr)
print(arr)
print(bubble_sort([4,3,2,1]))


