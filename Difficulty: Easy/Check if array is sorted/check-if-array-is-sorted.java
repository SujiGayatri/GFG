//{ Driver Code Starts
import java.util.*;


// } Driver Code Ends
// User function Template for Java

class Solution {
    public boolean arraySortedOrNot(int[] arr) {
        // code here
        int[] sorted=new int[arr.length];
        for(int i=0;i<arr.length;i++){
            sorted[i]=arr[i];
        }
        Arrays.sort(arr);
        int c=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==sorted[i]){
                c+=1;
            }
        }
        return c==arr.length?true:false;
    }
}

//{ Driver Code Starts.

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = Integer.parseInt(scanner.nextLine());

        while (t-- > 0) {
            String line = scanner.nextLine();
            String[] numStrings = line.split(" ");
            int arr[] = new int[numStrings.length];
            for (int i = 0; i < arr.length; i++)
                arr[i] = Integer.parseInt(numStrings[i]);
            Solution ob = new Solution();
            boolean ans = ob.arraySortedOrNot(arr);
            System.out.println(ans ? "true" : "false");
            System.out.println("~");
        }
        scanner.close();
    }
}
// } Driver Code Ends