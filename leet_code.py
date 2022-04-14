# Arrays
# Remove duplicates

def removeDuplicates(nums):
    if not nums:
        return 0
    elif len(nums):
        return 1
    pos = 0
    unic = nums[pos]
    lenght = len(nums)
    while True:
        print(pos)
        if nums[pos + 1] == unic:
            nums.pop(pos + 1)
            lenght = len(nums)
        else:
            pos += 1
            unic = nums[pos]
        if lenght == 1 or pos == lenght - 1:
            break
        print(nums)
    return len(nums)


# rotate k times
# def rotate(nums, k: int):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#
#     if len(nums) not in [0, 1]:
#         if k == 0:
#             return nums
#         else:
#             return rotate(nums[1:] + [nums[0]], k - 1)

def rotate(nums, k):

    """
    Do not return anything, modify nums in-place instead.
    """
    print(id(nums))

    def rotate1(x):
        print(id(x))
        return x[1:] + [x[0]]

    lenght = len(nums)

    if lenght not in [0, 1]:
        for i in range(k):
            nums = rotate1(nums)
            print(nums)

# 3Summ
def threeSum(nums):
    res = []
    i = 0
    while True:
        if i == 1:
            break
        # for i in range(len(nums)):
        _res = []
        array_i = nums.copy()
        first = array_i.pop(i-1)
        i -= 1
        for j in range(len(array_i) - 1):
            array_j = array_i.copy()
            second = array_j.pop(j)
            i -= 1
            for third in array_j:
                if first + second + third == 0:
                    _res = [first, second, third]
                    _res.sort()
                    print(_res)
                    if _res not in res:
                        res.append(_res)


    return res






def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        zero_pos = []
        if 0 in matrix[i]:
            for j in range(n):
                if matrix[i][j] != 0:
                    pass
        pass

        """
        Do not return anything, modify matrix in-place instead.
        """


if __name__ == '__main__':
    matrix = [
              [0,1,2,0],
              [3,4,5,2],
              [1,3,1,5]
             ]
    setZeroes(matrix)

    # print(threeSum([-1,0,1,2,-1,-4]))

