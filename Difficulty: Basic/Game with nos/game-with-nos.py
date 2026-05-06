#User function Template for python3

def game_with_number (arr,  n) : 
    #Complete the function
    for i in range(n - 1):
        arr[i] = arr[i] ^ arr[i + 1]
    return arr