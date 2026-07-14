<h2><a href="https://www.geeksforgeeks.org/problems/total-traversal-time/1?page=2&category=Arrays&difficulty=Easy&status=unsolved&sortBy=submissions">Total Traversal Time</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 14pt;">Given two arrays <strong>arr[]</strong> and <strong>penalty[]</strong> of size n, where each element in arr[] lies in the range <strong>[0, n-1]</strong>, traverse the array from <strong>left to right</strong> and compute the total time taken.</span></p>
<ul>
<li><span style="font-size: 14pt;">If an element appears for the first time, it takes <strong>1</strong> second to move forward.</span></li>
<li><span style="font-size: 14pt;">If an element has appeared <strong>before</strong>, it takes <strong>penalty[arr[i]]</strong> seconds to move forward.</span></li>
</ul>
<p><span style="font-size: 14pt;">Return the <strong>total time</strong> required to traverse the entire array.</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 2, 3, 3], penalty[] = [1, 2, 3, 4]
<strong>Output: </strong>6
<strong>Explanation:
</strong></span><span style="font-size: 18px;"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/927789/Web/Other/blobid0_1777972163.png" width="249" height="108"><br>For i = 0, traversal time = 0 second since this is the start point.  
For i = 1, traversal time = 1 second 
For i = 2, traversal time = 1 second 
For i = 3, traversal time = penalty[arr[3]]  = penalty[3] = 4
Total = 0+1+1+4 = 6 </span></pre>
<pre><span style="font-size: 18px;"><span style="font-family: Arial;"><strong>Input: </strong>arr[] = [6, 6, 1, 8, 1, 1, 3, 1], penalty[] = [8, 4, 1, 5, 2, 8, 9, 3]<strong>
Output: </strong>35<strong>
Explanation:
</strong></span></span><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/927789/Web/Other/blobid1_1777972177.png" width="424" height="116"><br><span style="font-size: 14pt;">For i = 0, traversal time = 0 second since this is the start point.
For i = 1, traversal time = penalty[arr[1]] = penalty[6] = 9
For i = 2, traversal time = 1 second
For i = 3, traversal time = 1 second
For i = 4, traversal time = penalty[arr[4]] = penalty[1] = 4
For i = 5, traversal time = penalty[arr[5]] = penalty[1] = 4
For i = 6, traversal time = 1 second
For i = 7, traversal time = penalty[arr[7]] = penalty[1] = 4
Total = 0 + 9 + 1 + 1 + 4 + 4 + 1 + 4 = 24</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n ≤ 10<sup>5</sup><br>0 ≤ arr[i] ≤ n-1<br>1 ≤ penalty[i] ≤ 10<sup>4</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Hash</code>&nbsp;<code>Data Structures</code>&nbsp;