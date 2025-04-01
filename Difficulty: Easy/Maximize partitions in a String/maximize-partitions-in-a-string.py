class Solution:
    def maxPartitions(self , s):
        # code here
        last_index = {char: i for i, char in enumerate(s)}  # Store last occurrence of each character
    
        partitions = 0
        max_end = -1
    
        for i, char in enumerate(s):
            max_end = max(max_end, last_index[char]) 
            if i == max_end: 
                partitions += 1
    
        return partitions


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends