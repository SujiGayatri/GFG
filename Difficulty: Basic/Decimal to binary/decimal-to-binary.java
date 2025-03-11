//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int test = sc.nextInt();
        while (test-- > 0) {
            int n = sc.nextInt();
            Solution obj = new Solution();
            System.out.println(obj.decToBinary(n));
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    static String decToBinary(int n) {
        // code here
        String s="";
        long x=(int)(Math.log(n)/Math.log(2));
        for(long i=x;i>=0;i--){
            if((n & (1<<i))>0){
                s+=1;
            }
            else{
                s+=0;
            }
        }
        return s;
    }
}