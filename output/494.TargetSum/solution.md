<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</a></li>
<li><a href="#approach-3-2d-dynamic-programming">Approach 3: 2D Dynamic Programming</a></li>
<li><a href="#approach-4-1d-dynamic-programming">Approach 4: 1D Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>The brute force approach is based on recursion. We need to try to put both the <code>+</code> and <code>-</code> symbols at every location in the given <script type="math/tex; mode=display">nums</script> array and find out the assignments which lead to the required result <script type="math/tex; mode=display">S</script>.</p>
<p>For this, we make use of a recursive function <code>calculate(nums, i, sum, S)</code>, which returns the assignments leading to the sum <script type="math/tex; mode=display">S</script>, starting from the <script type="math/tex; mode=display">i^{th}</script> index onwards, provided the sum of elements upto the <script type="math/tex; mode=display">i^{th}</script> element is <script type="math/tex; mode=display">sum</script>. This function appends a <code>+</code> sign and a <code>-</code> sign both to the element at the current index and calls itself with the updated <script type="math/tex; mode=display">sum</script> as <script type="math/tex; mode=display">sum + nums[i]</script> and <script type="math/tex; mode=display">sum - nums[i]</script> repectively along with the updated current index as <script type="math/tex; mode=display">i+1</script>.  Whenver, we reach the end of the array, we compare the sum obtained with <script type="math/tex; mode=display">S</script>. If they are equal, we increment the <script type="math/tex; mode=display">count</script> value to be returned.</p>
<p>Thus, the function call <code>calculate(nums, 0, 0, S)</code> retuns the required no. of assignments.</p>
<iframe src="https://leetcode.com/playground/fM6wckj7/shared" frameborder="0" width="100%" height="327" name="fM6wckj7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^n)</script>. Size of recursion tree will be <script type="math/tex; mode=display">2^n</script>. <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</h4>
<p><strong>Algorithm</strong></p>
<p>It can be easily observed that in the last approach, a lot of redundant function calls could be made with the same value of <script type="math/tex; mode=display">i</script> as the current index and the same value of <script type="math/tex; mode=display">sum</script> as the current sum, since the same values could be obtained through multiple paths in the recursion tree. In order to remove this redundancy, we make use of memoization as well to store the results which have been calculated earlier.</p>
<p>Thus, for every call to <code>calculate(nums, i, sum, S)</code>, we store the result obtained in <script type="math/tex; mode=display">memo[i][sum + 1000]</script>. The factor of 1000 has been added as an offset to the <script type="math/tex; mode=display">sum</script> value to map all the <script type="math/tex; mode=display">sum</script>s possible to positive integer range. By making use of memoization, we can prune the search space to a good extent.</p>
<iframe src="https://leetcode.com/playground/VRUSdbty/shared" frameborder="0" width="100%" height="480" name="VRUSdbty"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(l*n)</script>. The <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">l*n</script> has been filled just once. Here, <script type="math/tex; mode=display">l</script> refers to the range of <script type="math/tex; mode=display">sum</script> and <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of recursion tree can go upto <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-2d-dynamic-programming">Approach 3: 2D Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>The idea behind this approach is as follows. Suppose we can find out the number of times a particular sum, say <script type="math/tex; mode=display">sum_i</script> is possible upto a particular index, say <script type="math/tex; mode=display">i</script>, in the given <script type="math/tex; mode=display">nums</script> array, which is given by say <script type="math/tex; mode=display">count_i</script>. Now, we can find out the number of times the sum <script type="math/tex; mode=display">sum_i + nums[i]</script> can occur easily as <script type="math/tex; mode=display">count_i</script>. Similarly, the number of times the sum <script type="math/tex; mode=display">sum_i - nums[i]</script> occurs is also given by <script type="math/tex; mode=display">count_i</script>. </p>
<p>Thus, if we know all the sums <script type="math/tex; mode=display">sum_j</script>'s which are possible upto the <script type="math/tex; mode=display">j^{th}</script> index by using various assignments, along with the corresponding count of assignments, <script type="math/tex; mode=display">count_j</script>, leading to the same sum, we can determine all the sums possible upto the <script type="math/tex; mode=display">(j+1)^{th}</script> index  along with the corresponding count of assignments leading to the new sums.</p>
<p>Based on this idea, we make use of a <script type="math/tex; mode=display">dp</script> to determine the number of assignments which can lead to the given sum. <script type="math/tex; mode=display">dp[i][j]</script> refers to the number of assignments which can lead to a sum of <script type="math/tex; mode=display">j</script> upto the <script type="math/tex; mode=display">i^{th}</script> index. To determine the number of assignments which can lead to a sum of <script type="math/tex; mode=display">sum + nums[i]</script> upto the <script type="math/tex; mode=display">(i+1)^{th}</script> index, we can use <script type="math/tex; mode=display">dp[i][sum + nums[i]] = dp[i][sum + nums[i]] + dp[i-1][sum]</script>. Similarly, <script type="math/tex; mode=display">dp[i][sum - nums[i]] = dp[i][sum + nums[i]] + dp[i-1][sum]</script>. We iterate over the <script type="math/tex; mode=display">dp</script> array in a rowwise fashion i.e. Firstly we obtain all the sums which are possible upto a particular index along with the corresponding count of assignments and then proceed for the next element(index) in the <script type="math/tex; mode=display">nums</script> array.</p>
<p>But, since the <script type="math/tex; mode=display">sum</script> can range from -1000 to +1000, we need to add an offset of 1000 to the sum indices (column number) to map all the sums obtained to positive range only. </p>
<p>At the end, the value of <script type="math/tex; mode=display">dp[n-1][S+1000]</script> gives us the required number of assignments. Here, <script type="math/tex; mode=display">n</script> refers to the number of elements in the <script type="math/tex; mode=display">nums</script> array.</p>
<p>The animation below shows the way various sums are generated along with the corresponding indices. The example assumes <script type="math/tex; mode=display">sum</script> values to lie in the range of -6 to +6 just for the purpose of illustration. This animation is inspired by <a href="https://leetcode.com/Chidong">@Chidong</a></p>
<p>!?!../Documents/494_Target_Sum.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/tSDYMR33/shared" frameborder="0" width="100%" height="327" name="tSDYMR33"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(l*n)</script>. The entire <script type="math/tex; mode=display">nums</script> array is travesed 2001(constant no.: <script type="math/tex; mode=display">l</script>) times. <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array. <script type="math/tex; mode=display">l</script> refers to the range of <script type="math/tex; mode=display">sum</script> possible.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(l*n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">l*n</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-1d-dynamic-programming">Approach 4: 1D Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>If we look closely at the last solution, we can observe that for the evaluation of the current row of <script type="math/tex; mode=display">dp</script>, only the values of the last row of <script type="math/tex; mode=display">dp</script> are needed. Thus, we can save some space by using a 1D DP array instead of a 2-D DP array. The only difference that needs to be made is that now the same <script type="math/tex; mode=display">dp</script> array will be updated for every row traversed. </p>
<p>Below code is inspired by <a href="https://leetcode.com/Chidong">@Chidong</a></p>
<iframe src="https://leetcode.com/playground/N6s9PiwM/shared" frameborder="0" width="100%" height="361" name="N6s9PiwM"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(l.n)</script>. The entire <script type="math/tex; mode=display">nums</script> array is traversed <script type="math/tex; mode=display">l</script> times. <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array. <script type="math/tex; mode=display">l</script> refers to the range of <script type="math/tex; mode=display">sum</script> possible.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>