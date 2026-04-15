def remAnagram(s1,s2):
    #code here
    freq1 = [0] * 26
    freq2 = [0] * 26
    for ch in s1:
        freq1[ord(ch) - ord('a')] += 1
    for ch in s2:
        freq2[ord(ch) - ord('a')] += 1
    deletions = 0
    for i in range(26):
        deletions += abs(freq1[i] - freq2[i])
    return deletions