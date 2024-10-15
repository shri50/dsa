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
    arr = input("Input the number with space as separation").split()
    # arr = arr.split()
    result = largest_element(arr)
    print(f"Largest element in arr = {result}")


# Find second largest element in an array

def second_largest_element(arr):
    """
    to find secodn largest element from the arr

    param: 
        arr : input array 

    return:
        result : second largest number
    """

    max = arr[i]
    second_largest = arr[i]

    for 

if __name__ == "__main__":
    call_largest_element()