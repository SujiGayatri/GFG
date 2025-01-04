//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        while (t-- > 0) {
            String[] arr1Str = sc.nextLine().split(" ");
            int[] arr = Arrays.stream(arr1Str).mapToInt(Integer::parseInt).toArray();
            int target = Integer.parseInt(sc.nextLine());

            Solution ob = new Solution();
            int ans = ob.countTriplets(arr, target);
            System.out.println(ans);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    public int countTriplets(int[] arr, int target) {
        // Code Here
        int n=arr.length;
        int c=0;
        for(int i=0;i<n-2;i++){
            int l=i+1,r=n-1;
            while(l<r){
                int sum=arr[i]+arr[l]+arr[r];
                if(sum==target){
                    c++;
                    int tl=l+1;
                    int tr=r-1;
                    while(tl<r && arr[tl]==arr[l]) 
                    {  
                        c++;
                        tl++;
                    }
                    while(l<tr && arr[tr]==arr[r])
                    {
                        c++;
                        tr--;
                    }
                    l++;
                    r--;
                }
                else if(sum<target){
                    l++;
                }
                else{
                    r--;
                }
            }
        }
        return c;
    }
}