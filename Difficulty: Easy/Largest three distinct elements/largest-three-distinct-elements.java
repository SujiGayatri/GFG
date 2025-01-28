//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());

        while (tc-- > 0) {
            String s[] = br.readLine().split(" ");
            int arr[] = new int[s.length];

            for (int i = 0; i < arr.length; i++) arr[i] = Integer.parseInt(s[i]);

            Solution obj = new Solution();
            int ans[] = obj.getThreeLargest(arr);

            for (int i : ans) {
                System.out.print(i + " ");
            }
            System.out.println();
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    public int[] getThreeLargest(int arr[]) {
        // code here
        Arrays.sort(arr);
        int n=arr.length,j=0;
        for(int i=1;i<n;i++){
            if(arr[i]!=arr[j]){
                j++;
                arr[j]=arr[i];
            }
        }
        int[] res=Arrays.copyOf(arr,j+1);
        int x=res.length;
        if( x==2) {
            return new int[]{res[x-1],res[x-2]};
        }
        else if(x==1){
            return new int[]{res[x-1]};
        }
        return new int[]{res[x-1],res[x-2],res[x-3]};
        
    }
}