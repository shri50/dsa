# Implementation of Linear Search Algorithm

def linear_search(arr,n):

    """
    linear search implementation
    """
    for i in range(0,len(arr)):
        if arr[i] == n:
            return i
    return None

if __name__ == "__main__":
    arr = input("Input the number with space as separation").split()
    # arr = arr.split()
    n = input("Input no to search:")
    result = linear_search(arr,n)
    if result == None:
        print(f"{n} is no present")
    else:
        print(f"{n} is present in list at index={result}")