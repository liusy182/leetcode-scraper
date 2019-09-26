<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</a></li>
<li><a href="#approach-3-dynamic-programming">Approach 3: Dynamic Programming</a></li>
<li><a href="#approach-4-dynamic-programming-with-binary-search">Approach 4: Dynamic Programming with Binary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>The simplest approach is to try to find all increasing subsequences and then returning the maximum length of longest increasing subsequence. In order to
do this, we make use of a recursive function <script type="math/tex; mode=display">\text{lengthofLIS}</script> which returns the length of the LIS possible from the current element(corresponding to <script type="math/tex; mode=display">curpos</script>)
 onwards(including the current element). Inside each function call, we consider two cases:</p>
<ol>
<li>
<p>The current element is larger than the previous element included in the LIS. In this case, we can include the current element in the LIS. Thus, we find out the
length of the LIS obtained by including it. Further, we also find out the length of LIS possible by not including the current element in the LIS. The value returned
by the current function call is, thus, the maximum out of the two lengths.</p>
</li>
<li>
<p>The current element is smaller than the previous element included in the LIS. In this case, we can't include the current element in the LIS. Thus, we find out only
the length of the LIS possible by not including the current element in the LIS, which is returned by the current function call.</p>
</li>
</ol>
<iframe src="https://leetcode.com/playground/UoMzWLi7/shared" frameborder="0" width="100%" height="361" name="UoMzWLi7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^n)</script>. Size of recursion tree will be <script type="math/tex; mode=display">2^n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^2)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n * n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</h4>
<p><strong>Algorithm</strong></p>
<p>In the previous approach, many recursive calls had to made again and again with the same parameters. This redundancy can be eliminated by storing the results obtained for
a particular call in a 2-d memoization array <script type="math/tex; mode=display">memo</script>. <script type="math/tex; mode=display">memo[i][j]</script> represents the length of the LIS possible using <script type="math/tex; mode=display">nums[i]</script> as the previous element considered to
be included/not included in the LIS, with <script type="math/tex; mode=display">nums[j]</script> as the current element considered to be included/not included in the LIS. Here, <script type="math/tex; mode=display">nums</script> represents the given array.</p>
<iframe src="https://leetcode.com/playground/GSwVQjkr/shared" frameborder="0" width="100%" height="480" name="GSwVQjkr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Size of recursion tree can go upto <script type="math/tex; mode=display">n^2</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^2)</script>. <script type="math/tex; mode=display">memo</script> array of <script type="math/tex; mode=display">n*n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming">Approach 3: Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>This method relies on the fact that the longest increasing subsequence possible upto the <script type="math/tex; mode=display">i^{th}</script>  index in a given array is independent of the elements coming
later on in the array. Thus, if we know the length of the LIS upto <script type="math/tex; mode=display">i^{th}</script> index, we can figure out the length of the LIS possible by including the <script type="math/tex; mode=display">(i+1)^{th}</script> element
based on the elements with indices <script type="math/tex; mode=display">j</script> such that <script type="math/tex; mode=display">0 \leq j \leq (i + 1)</script>.</p>
<p>We make use of a <script type="math/tex; mode=display">dp</script> array to store the required data. <script type="math/tex; mode=display">dp[i]</script> represents the length of the longest increasing subsequence possible considering the array elements upto the <script type="math/tex; mode=display">i^{th}</script>
index only ,by necessarily including the <script type="math/tex; mode=display">i^{th}</script> element. In order to find out <script type="math/tex; mode=display">dp[i]</script>, we need to try to append the current element(<script type="math/tex; mode=display">nums[i]</script>) in every possible increasing subsequences upto the <script type="math/tex; mode=display">(i-1)^{th}</script>
index(including the <script type="math/tex; mode=display">(i-1)^{th}</script> index), such that the new sequence formed by adding the current element is also an increasing subsequence. Thus, we can easily determine
<script type="math/tex; mode=display">dp[i]</script> using:  </p>
<p>
<script type="math/tex; mode=display">dp[i] = \text{max}(dp[j]) + 1, \forall 0\leq j < i</script>
</p>
<p>At the end, the maximum out of all the <script type="math/tex; mode=display">dp[i]</script>'s to determine the final result.</p>
<p>
<script type="math/tex; mode=display">LIS_{length}= \text{max}(dp[i]), \forall 0\leq i < n</script>
</p>
<p>The following animation illustrates the method:</p>
<!--![LIS](../Figures/300_LIS1.gif)-->

<p>!?!../Documents/300_LIS.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/EVGvmMas/shared" frameborder="0" width="100%" height="412" name="EVGvmMas"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Two loops of <script type="math/tex; mode=display">n</script> are there.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-dynamic-programming-with-binary-search">Approach 4: Dynamic Programming with Binary Search</h4>
<p><strong>Algorithm</strong></p>
<p>In this approach, we scan the array from left to right. We also make use of a <script type="math/tex; mode=display">dp</script> array initialized with all 0's. This <script type="math/tex; mode=display">dp</script> array is meant to store the
increasing subsequence formed by including the currently encountered element.
 While traversing the <script type="math/tex; mode=display">nums</script> array, we keep on filling the <script type="math/tex; mode=display">dp</script> array with
the elements encountered so far. For the element corresponding to the <script type="math/tex; mode=display">j^{th}</script> index (<script type="math/tex; mode=display">nums[j]</script>),
 we determine its correct position in the <script type="math/tex; mode=display">dp</script> array(say <script type="math/tex; mode=display">i^{th}</script> index) by making use of Binary Search(which can be used since the
  <script type="math/tex; mode=display">dp</script> array is storing increasing subsequence) and also insert it at the correct position. An important point to be noted is that for Binary Search, we consider
  only that portion of the <script type="math/tex; mode=display">dp</script> array in which we have made the updates by inserting some elements at their correct positions(which remains always sorted).
  Thus, only the elements upto the <script type="math/tex; mode=display">i^{th}</script> index
  in the <script type="math/tex; mode=display">dp</script> array can determine the position of the current element in it.
  Since, the element enters its correct position(<script type="math/tex; mode=display">i</script>) in an ascending order in the <script type="math/tex; mode=display">dp</script> array, the
  subsequence formed so far in it is surely an increasing subsequence. Whenever this position index <script type="math/tex; mode=display">i</script> becomes equal to the length of the LIS formed so far(<script type="math/tex; mode=display">len</script>),
  it means, we need to update the <script type="math/tex; mode=display">len</script> as <script type="math/tex; mode=display">len = len + 1</script>.</p>
<p>Note: <script type="math/tex; mode=display">dp</script> array does not result in longest increasing subsequence, but length of <script type="math/tex; mode=display">dp</script> array will give you length of LIS.</p>
<p>Consider the example:</p>
<p>input: [0, 8, 4, 12, 2]</p>
<p>dp: [0]</p>
<p>dp: [0, 8]</p>
<p>dp: [0, 4]</p>
<p>dp: [0, 4, 12]</p>
<p>dp: [0 , 2, 12] which is not the longest increasing subsequence, but length of <script type="math/tex; mode=display">dp</script> array results in length of Longest Increasing Subsequence.</p>
<iframe src="https://leetcode.com/playground/Kbvq2W3R/shared" frameborder="0" width="100%" height="344" name="Kbvq2W3R"></iframe>

<p>Note: Arrays.binarySearch() method returns index of the search key, if it is contained in the array, else it returns (-(insertion point) - 1). The insertion point is the point at which the key would be inserted into the array: the index of the first element greater than the key, or a.length if all elements in the array are less than the specified key.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n\log n)</script>. Binary search takes <script type="math/tex; mode=display">\log n</script> time and it is called <script type="math/tex; mode=display">n</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>