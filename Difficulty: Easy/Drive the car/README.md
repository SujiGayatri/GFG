<h2><a href="https://www.geeksforgeeks.org/problems/drive-the-car2541/1?page=5&category=Arrays&difficulty=Easy&status=unsolved&sortBy=submissions">Drive the car</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18.6667px;">Given an array <strong>arr[]</strong> where each element represents the length of a sub-track, and an integer <strong>k </strong>representing the maximum distance a car can travel on any sub-track. </span></p>
<ul>
<li><span style="font-size: 18.6667px;">You may add petrol to increase the car's maximum travel distance. </span></li>
<li><span style="font-size: 18.6667px;"><strong>Each unit</strong> of petrol increases this maximum distance by <strong>1</strong> kilometer for all sub-tracks.</span></li>
</ul>
<p><span style="font-size: 18.6667px;">Determine the <strong>minimum </strong>units of petrol required so that the car can travel through every sub-track. If the car can already cover all sub-tracks with its initial capacity, return<strong> -1</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [2, 5, 4, 5, 2], k = 7
<strong>Output: </strong>-1
<strong>Explanation: </strong>No extra petrol required, as k is greater than all the elemnts in the array hence <strong>-1</strong>.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 6, 3, 5, 2], k = 4
<strong>Output: </strong>2
<strong>Explanation: </strong></span><span style="font-size: 18.6667px;">The longest sub-track has length 6, while the car can travel only 4 kilometers. To cover every sub-track, the car's maximum travel distance must be increased from 4 to 6. Since each unit of petrol increases the maximum travel distance by 1 kilometer, 2 units of petrol are required.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup></span><br><span style="font-size: 14pt;">1 ≤ k,&nbsp;</span><span style="font-size: 18.6667px;">arr[i]</span><span style="font-size: 18.6667px;"> </span><span style="font-size: 14pt;">&nbsp;≤ 10</span><sup>9</sup></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;