
class Solution {
    public int countOfElements(int x, List<Integer> arr) {
        // Code here
        int cnt=0;
        for(int i=0;i<arr.size();i++){
            if(arr.get(i)<=x){
                cnt++;
            }
        }
        return cnt;
    }
}