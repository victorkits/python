# arr[] = 64 25 12 22 11
#
# // Find the minimum element in arr[0...4]
# // and place it at beginning
# 11 25 12 22 64
#
# // Find the minimum element in arr[1...4]
# // and place it at beginning of arr[1...4]
# 11 12 25 22 64
#
# // Find the minimum element in arr[2...4]
# // and place it at beginning of arr[2...4]
# 11 12 22 25 64
#
# // Find the minimum element in arr[3...4]
# // and place it at beginning of arr[3...4]
# 11 12 22 25 64

arr = [64, 25, 12, 22, 11]


def main(array):
    new_arr = []
    for pos in range(len(array)):
        print(array)
        a = min(array)
        # min(array)
        print(a)
        pos = array.index(a)
        array.pop(pos)
        new_arr.append(a)

    print(new_arr)




# ================ implementation of Selection
# Time complexity O(n**2)

def sort():
    import sys

    A = [64, 25, 12, 22, 11]

    # Traverse through all array elements
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]

    # Driver code to test above
    print("Sorted array")
    for i in range(len(A)):
        print("%d" % A[i], end=" ")


if __name__ == '__main__':
    main(arr)
