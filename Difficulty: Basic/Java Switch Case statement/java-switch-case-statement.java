// User function Template for Java

class Solution {
    static double switchCase(int choice, List<Double> arr) {
        // code here
        double ans=0;
        switch (choice){
            case 1:{
                ans=Math.PI*arr.get(0)*arr.get(0);
                break;
            }
            case 2:{
                ans=arr.get(0)*arr.get(1);
                break;
            }
        }
        return ans;
    }
}