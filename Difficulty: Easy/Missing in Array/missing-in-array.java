class Solution {
    int missingNum(int arr[]) {
        // code here
        Arrays.sort(arr);
        int n=arr.length+1;
        long s=0;
        for(long i:arr){
            s+=i;
        }
        long x=(long) n*(n+1)/2;
        return (int)(x-s);
    }
}