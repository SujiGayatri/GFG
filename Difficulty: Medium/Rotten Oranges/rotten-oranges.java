//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            int mat[][] = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) mat[i][j] = sc.nextInt();
            }
            Solution obj = new Solution();
            int ans = obj.orangesRotting(mat);
            System.out.println(ans);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    // Function to find minimum time required to rot all oranges.
    class Pair {
        int row, col, time;
        Pair(int row, int col, int time) {
            this.row = row;
            this.col = col;
            this.time = time;
        }
    }

    public int orangesRotting(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        Queue<Pair> queue = new LinkedList<>();
        int freshCount = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] == 2) {
                    queue.add(new Pair(i, j, 0)); 
                } else if (mat[i][j] == 1) {
                    freshCount++;
                }
            }
        }
        if (freshCount == 0) return 0;
        
        int timeElapsed = 0;
        int[] dRow = {-1, 1, 0, 0};
        int[] dCol = {0, 0, -1, 1};
        while (!queue.isEmpty()) {
            Pair curr = queue.poll();
            int r = curr.row;
            int c = curr.col;
            int time = curr.time;
            timeElapsed = time;
            
            for (int i = 0; i < 4; i++) {
                int newRow = r + dRow[i];
                int newCol = c + dCol[i];
                
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && mat[newRow][newCol] == 1) {
                    mat[newRow][newCol] = 2; 
                    freshCount--;
                    queue.add(new Pair(newRow, newCol, time + 1));
                }
            }
        }
        return freshCount == 0 ? timeElapsed : -1;
    }
}