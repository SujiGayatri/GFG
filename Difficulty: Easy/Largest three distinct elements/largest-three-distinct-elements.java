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
        int x=arr.length,j=0;
        for(int i=1;i<x;i++){
            if(arr[i]!=arr[j]){
                j++;
                arr[j]=arr[i];
            }
        }
        int[] res=Arrays.copyOf(arr,j+1);
        int l=res.length;
        if(l==2){
            return new int[]{res[l-1],res[l-2]};
        }
        else if(l==1){
            return new int[]{res[l-1]};
        }
        return new int[]{res[l-1],res[l-2],res[l-3]};
    }
}