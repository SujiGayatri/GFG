class Solution {
    boolean isBinary(String s) {
        // Your code here
        int cnt=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch!='1' && ch!='0'){
                return false;
            }
        }
        return true;
    }
}