# Implementation of Linear Search Algorithm

def linear_search(arr,n):

    """
    linear search implementation
    """
    for i in range(0,len(arr)):
        if arr[i] == n:
            return i
    return None

def call_linear_search():
    arr = input("Input the number with space as separation").split()
    # arr = arr.split()
    n = input("Input no to search:")
    result = linear_search(arr,n)
    if result == None:
        print(f"{n} is no present")
    else:
        print(f"{n} is present in list at index={result}")


# Program to find largest element in an Array

def largest_element(arr):
    """
    find largest element from array
    """
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def call_largest_element():
    arr1 = [10, 20, 4]
    arr2 = [20, 10, 20, 4, 100]

    res1 = largest_element(arr1)
    res2 = largest_element(arr2)

    print(f"largest element in array = {res1}")
    print(f"largest element in array = {res2}")


# Find second largest element in an array

def second_largest_element(arr):
    """
    to find secodn largest element from the arr

    param: 
        arr : input array 

    return:
        result : second largest number
    """
    len_arr =  len(arr)
    largest = -1
    second_largest = -1

    for i in range(len_arr):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i]> second_largest:
            second_largest = arr[i]
    
    return second_largest

def call_second_element():
    arr1 = [12, 35, 1, 10, 34, 1]
    arr2 = [10, 5, 10]
    arr3 = [10,10,10]

    result1 = second_largest_element(arr1)
    result2 = second_largest_element(arr2)
    result3 = second_largest_element(arr3)

    print(f"Second Largest element in arr = {result1}")
    print(f"Second Largest element in arr = {result2}")
    print(f"Second Largest element in arr = {result3}")


# Find the largest three distinct elements in an array
def three_largest_element(arr):
    """
    to find three largest distinct element from the array

    param: 
        arr : input array 

    return:
        result : three largest distict element
    """
    if len(arr) >= 3:
        first_item = float('-inf')
        second_item = float('-inf')
        third_item = float('-inf')

        for i in range(len(arr)):
            if arr[i] > first_item:
                first_item, second_item, third_item = arr[i], first_item, second_item
            elif arr[i] > second_item and arr[i] != first_item:
                second_item, third_item = arr[i], second_item
            elif arr[i] > third_item and arr[i] != first_item and arr[i] != second_item:
                third_item = arr[i]

        return first_item, second_item, third_item
    else: 
        arr.sort()
        arr =list(set(arr))
        return arr

def call_three_largest_element():
    arr1 = [10, 4, 3, 50, 23, 90]
    arr2 = [6, 8, 9, 2, 1, 10]
    arr3 = [10, 9, 9]
    arr4 = [10, 10]
    arr5 = []

    res1 = three_largest_element(arr1)
    res2 = three_largest_element(arr2)
    res3 = three_largest_element(arr3)
    res4 = three_largest_element(arr4)
    res5 = three_largest_element(arr5)

    print(f"result for the three largest element from the array = {res1}")
    print(f"result for the three largest element from the array = {res2}")
    print(f"result for the three largest element from the array = {res3}")
    print(f"result for the three largest element from the array = {res4}")
    print(f"result for the three largest element from the array = {res5}")
    
# Leaders in an array
def find_leader(arr):
    """
    param:
        arr (list) : input array 
    
    return: 
        result (int): leader in array
    """
    leader_element_arr = [] 
    max= 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            max = arr[i]
            leader_element_arr.append(arr[i])
    leader_element_arr.sort(reverse=True)
    return leader_element_arr


def call_find_leader():
    arr1 = [16, 17, 4, 3, 5, 2]
    result1 =  find_leader(arr1)
    print(f"Leader from arr = {result1}")
    
    arr2 = [1, 2, 3, 4, 5, 2]
    result2 =  find_leader(arr2)
    print(f"Leader from arr = {result2}")


if __name__ == "__main__":
    call_find_leader()
    # call_largest_element()
    # call_second_element()
    # call_three_largest_element()