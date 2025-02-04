//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = inputLine.length;
            int[] arr = new int[n];

            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            t--;

            System.out.println(new Solution().findsum(arr) == true ? "true" : "false");
        }
    }
}
// } Driver Code Ends


class Solution {
    // Function to check whether there is a subarray present with 0-sum or not.
    static boolean findsum(int arr[]) {
        // Your code here
        // for(int i=0;i<arr.length;i++){
        //     int s=arr[i];
        //     for(int j=i+1;j<arr.length;j++){
        //         if(s==0){
        //             return true;
        //         }
        //         s+=arr[j];
        //     }
        // }
        HashSet<Integer> prefix=new HashSet<>();
        int s=0;
        for(int i:arr){
            s+=i;
            if(s==0 ||prefix.contains(s)){
                return true;
            }
            prefix.add(s);
        }
        return false;
    }
}