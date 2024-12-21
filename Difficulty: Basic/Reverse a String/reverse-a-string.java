//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class Driver {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());

        while (t-- > 0) {
            String str = read.readLine();
            System.out.println(new Solution().reverseString(str));

            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public static String reverseString(String s) {
        // code here
        // String rev="";
        // char ch;
        // for(int i=0;i<s.length();i++){
        //     ch=s.charAt(i);
        //     rev=ch+rev;
        // }
        // return rev;
        StringBuilder rev= new StringBuilder();
        for(int i=s.length()-1;i>=0;i--){
            rev.append(s.charAt(i));
        }
        return rev.toString();
    }
}