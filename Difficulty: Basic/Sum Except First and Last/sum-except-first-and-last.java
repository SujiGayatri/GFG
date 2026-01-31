class Solution {
    int sumExceptFirstLast(int[] arr) {
        // your code here
        int s=0;
        for(int i=1;i<arr.length-1;i++){
            s+=arr[i];
        }
        return s;
    }
}