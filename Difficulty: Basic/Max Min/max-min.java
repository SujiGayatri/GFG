// User function Template for Java

class Solution {
    public static int findSum(int A[], int N) {
        // code here
        int min1=A[0];
        int max1=A[0];
        for(int i=0;i<A.length;i++){
            if(A[i]<min1){
                min1=A[i];
            }
            if(A[i]>max1){
                max1=A[i];
            }
        }
        
        return min1+max1;
    }
}
