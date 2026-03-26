#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        vote_count = {}
        for name in arr:
            vote_count[name] = vote_count.get(name, 0) + 1
        max_votes = 0
        winner_name = ""
        for i in vote_count:
            if vote_count[i] > max_votes:
                max_votes = vote_count[i]
                winner_name = i
            elif vote_count[i] == max_votes:
                if i < winner_name:
                    winner_name = i
        return [winner_name, str(max_votes)]