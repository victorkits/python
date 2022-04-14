def solution(A):
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(i, N):
            if A[i] != A[j]:
                result = max(result, j - i)
    return result


def solution1(arr):
    max = 0
    for i, elem in enumerate(arr):
        if
        pass


if __name__ == '__main__':
    print(solution([4,6,2,2,6,6,4]))
