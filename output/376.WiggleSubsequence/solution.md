<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-dynamic-programming-accepted">Approach #2  Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-3-linear-dynamic-programming-accepted">Approach #3 Linear Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-4-space-optimized-dynamic-programming-accepted">Approach #4 Space-Optimized Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-5-greedy-approach-accepted">Approach #5 Greedy Approach [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>We need to find the length of the longest wiggle subsequence. A wiggle subsequence consists of a subsequence with numbers which appears in alternating ascending / descending order.</p>
<h2 id="solution">Solution</h2>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p>Here, we can find the length of every possible wiggle subsequence and find the maximum length out of them. To implement this, we use a recursive function, <script type="math/tex; mode=display">\text{calculate}(\text{nums}, \text{index}, \text{isUp})</script> which takes the array <script type="math/tex; mode=display">\text{nums}</script>, the <script type="math/tex; mode=display">\text{index}</script> from which we need to find the length of the longest wiggle subsequence, boolean variable <script type="math/tex; mode=display">\text{isUp}</script> to tell whether we need to find an increasing wiggle or decreasing wiggle respectively. If the function <script type="math/tex; mode=display">\text{calculate}</script> is called after an increasing wiggle, we need to find the next decreasing wiggle with the same function. If the function <script type="math/tex; mode=display">\text{calculate}</script> is called after a decreasing wiggle, we need to find the next increasing wiggle with the same function.</p>
<iframe src="https://leetcode.com/playground/JXWefkVB/shared" frameborder="0" name="JXWefkVB" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n!)</script>. <script type="math/tex; mode=display">\text{calculate}()</script> will be called maximum <script type="math/tex; mode=display">n!</script> times.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Recursion of depth <script type="math/tex; mode=display">n</script> is used.</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-accepted">Approach #2  Dynamic Programming [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>To understand this approach, take two arrays for dp named <script type="math/tex; mode=display">up</script> and <script type="math/tex; mode=display">down</script>.</p>
<p>Whenever we pick up any element of the array to be a part of the wiggle subsequence, that element could be a part of a rising wiggle or a falling wiggle depending upon which element we have taken prior to it.</p>
<p>
<script type="math/tex; mode=display">up[i]</script> refers to the length of the longest wiggle subsequence obtained so far considering <script type="math/tex; mode=display">i^{th}</script> element as the last element of the wiggle subsequence and ending with a rising wiggle.</p>
<p>Similarly, <script type="math/tex; mode=display">down[i]</script> refers to the length of the longest wiggle subsequence obtained so far considering <script type="math/tex; mode=display">i^{th}</script> element as the last element of the wiggle subsequence and ending with a falling wiggle.</p>
<p>
<script type="math/tex; mode=display">up[i]</script> will be updated every time we find a rising wiggle ending with the <script type="math/tex; mode=display">i^{th}</script> element. Now, to find <script type="math/tex; mode=display">up[i]</script>, we need to consider the maximum out of all the previous wiggle subsequences ending with a falling wiggle i.e. <script type="math/tex; mode=display">down[j]</script>, for every <script type="math/tex; mode=display">j&lt;i</script> and <script type="math/tex; mode=display">nums[i]&gt;nums[j]</script>. Similarly, <script type="math/tex; mode=display">down[i]</script> will be updated.</p>
<iframe src="https://leetcode.com/playground/5DeX9SiP/shared" frameborder="0" name="5DeX9SiP" width="100%" height="360"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Loop inside a loop.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Two arrays of the same length are used for dp.</li>
</ul>
<hr>
<h4 id="approach-3-linear-dynamic-programming-accepted">Approach #3 Linear Dynamic Programming [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Any element in the array could correspond to only one of the three possible states:</p>
<ol>
<li>up position, it means <script type="math/tex; mode=display">nums[i] > nums[i-1]</script>
</li>
<li>down position, it means <script type="math/tex; mode=display">nums[i] < nums[i-1]</script>
</li>
<li>equals to position, <script type="math/tex; mode=display">nums[i] == nums[i-1]</script>
</li>
</ol>
<p>The updates are done as:</p>
<p>If <script type="math/tex; mode=display">nums[i] > nums[i-1]</script>, that means it wiggles up. The element before it must be a down position. So <script type="math/tex; mode=display">up[i] = down[i-1] + 1</script>, <script type="math/tex; mode=display">down[i]</script> remains the same as <script type="math/tex; mode=display">down[i-1]</script>.
If <script type="math/tex; mode=display">nums[i] < nums[i-1]</script>, that means it wiggles down. The element before it must be a up position. So <script type="math/tex; mode=display">down[i] = up[i-1] + 1</script>, <script type="math/tex; mode=display">up[i]</script> remains the same as <script type="math/tex; mode=display">up[i-1]</script>.
If <script type="math/tex; mode=display">nums[i] == nums[i-1]</script>, that means it will not change anything becaue it didn't wiggle at all. So both <script type="math/tex; mode=display">down[i]</script> and <script type="math/tex; mode=display">up[i]</script> remain the same as <script type="math/tex; mode=display">down[i-1]</script> and <script type="math/tex; mode=display">up[i-1]</script>.</p>
<p>At the end, we can find the larger out of <script type="math/tex; mode=display">up[length-1]</script> and <script type="math/tex; mode=display">down[length-1]</script> to find the max. wiggle subsequence length, where <script type="math/tex; mode=display">length</script> refers to the number of elements in the given array.</p>
<p>The process can be illustrated with the following example:</p>
<!--![Wiggle gif](https://leetcode.com/media/original_images/376_Wiggle_Subsequence.gif)-->

<p>!?!../Documents/376_Wiggle.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/iKGkFpFG/shared" frameborder="0" name="iKGkFpFG" width="100%" height="428"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Only one pass over the array length.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Two arrays of the same length are used for dp.</li>
</ul>
<hr>
<h4 id="approach-4-space-optimized-dynamic-programming-accepted">Approach #4 Space-Optimized Dynamic Programming [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>This approach relies on the same concept as <a href="https://leetcode.com/articles/wiggle-subsequence/#approach-3-linear-dynamic-programming-accepted">Approach #3</a>. But we can observe that in the DP approach, for updating elements <script type="math/tex; mode=display">up[i]</script> and <script type="math/tex; mode=display">down[i]</script>, we need only the elements <script type="math/tex; mode=display">up[i-1]</script> and <script type="math/tex; mode=display">down[i-1]</script>. Thus, we can save space by not using the whole array, but only the last elements.</p>
<iframe src="https://leetcode.com/playground/hUCEjR4D/shared" frameborder="0" name="hUCEjR4D" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Only one pass over the array length.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</li>
</ul>
<hr>
<h4 id="approach-5-greedy-approach-accepted">Approach #5 Greedy Approach [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We need not necessarily need dp to solve this problem. This problem is equivalent to finding the number of alternating max. and min. peaks in the array. Since, if we choose any other intermediate number to be a part of the current wiggle subsequence, the maximum length of that wiggle subsequence will always be less than or equal to the one obtained by choosing only the consecutive max. and min. elements.</p>
<p>This can be clarified by looking at the following figure:
<img alt="Wiggle Peaks" src="https://leetcode.com/media/original_images/376_Wiggle_Subsequence.PNG"></p>
<p>From the above figure, we can see that if we choose <strong>C</strong> instead of <strong>D</strong> as the 2nd point in the wiggle subsequence, we can't include the point <strong>E</strong>. Thus, we won't obtain the maximum length wiggle subsequence.</p>
<p>Thus, to solve this problem, we maintain a variable <script type="math/tex; mode=display">\text{prevdiff}</script>, where <script type="math/tex; mode=display">\text{prevdiff}</script> is used to indicate whether the current subsequence of numbers lies in an increasing or decreasing wiggle. If <script type="math/tex; mode=display">\text{prevdiff} > 0</script>, it indicates that we have found the increasing wiggle and are looking for a decreasing wiggle now. Thus, we update the length of the found subsequence when <script type="math/tex; mode=display">\text{diff}</script> (<script type="math/tex; mode=display">nums[i]-nums[i-1]</script>) becomes negative. Similarly, if <script type="math/tex; mode=display">\text{prevdiff} < 0</script>, we will update the count when <script type="math/tex; mode=display">\text{diff}</script> (<script type="math/tex; mode=display">nums[i]-nums[i-1]</script>) becomes positive.</p>
<p>When the complete array has been traversed, we get the required count, which represents the length of the longest wiggle subsequence.</p>
<iframe src="https://leetcode.com/playground/AqoaR5Ks/shared" frameborder="0" name="AqoaR5Ks" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We traverse the given array once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>