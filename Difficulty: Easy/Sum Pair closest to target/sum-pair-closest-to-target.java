//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            String line = br.readLine();
            String[] tokens = line.split(" ");

            ArrayList<Integer> array = new ArrayList<>();

            for (String token : tokens) {
                array.add(Integer.parseInt(token));
            }

            int[] arr = new int[array.size()];
            int idx = 0;
            for (int i : array) arr[idx++] = i;

            int target = Integer.parseInt(br.readLine());

            Solution ob = new Solution();
            List<Integer> res = ob.sumClosest(arr, target);
            if (res.isEmpty()) {
                System.out.print("[]");
            } else {
                for (Integer num : res) {
                    System.out.print(num + " ");
                }
            }
            System.out.println();
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public List<Integer> sumClosest(int[] arr, int target) {
        // code here
        List<Integer> res=new ArrayList<>();
        Arrays.sort(arr);
        int l=0,r=arr.length-1;
        int cl=Integer.MAX_VALUE;
        while(l<r){
            int s=arr[l]+arr[r];
            int diff=Math.abs(target-s);
            if(diff<cl){
                cl=diff;
                res.clear();
                res.add(arr[l]);
                res.add(arr[r]);
            }
            if(s<target){
                l++;
            }
            else{
                r--;
            }
        }
        return res;
    }
}