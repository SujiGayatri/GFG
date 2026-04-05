#User function Template for python3

def find4Numbers( A, N, X):
    # return true or false
    A.sort()
    for i in range(N - 3):
        for j in range(i + 1, N - 2):
            left = j + 1
            right = N - 1
            while left < right:
                total = A[i] + A[j] + A[left] + A[right]
                if total==X:
                    return True
                elif total < X:
                    left += 1
                else:
                    right -= 1
    return False