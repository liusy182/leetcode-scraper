<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-longest-common-subsequence-time-limit-exceeded">Approach #1 Using Longest Common Subsequence [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-longest-common-subsequence-with-memoization-accepted">Approach #2 Longest Common Subsequence with Memoization [Accepted]</a></li>
<li><a href="#approach-3-using-longest-common-subsequence-dynamic-programming-accepted">Approach #3 Using Longest Common Subsequence- Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-4-without-using-lcs-dynamic-programmming-accepted">Approach #4 Without using LCS Dynamic Programmming [Accepted]:</a></li>
<li><a href="#approach-5-1-d-dynamic-programming-accepted">Approach #5 1-D Dynamic Programming [Accepted]:</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-longest-common-subsequence-time-limit-exceeded">Approach #1 Using Longest Common Subsequence [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>In order to determine the minimum number of delete operations needed, we can make use of the length of the longest common sequence among the two given strings <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>, say given by <script type="math/tex; mode=display">lcs</script>. If we can find this <script type="math/tex; mode=display">lcs</script> value, we can easily determine the required result as <script type="math/tex; mode=display">m + n - 2*lcs</script>. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the length of the two given strings <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>.</p>
<p>The above equation works because in case of complete mismatch(i.e. if the two strings can't be equalized at all), the total number of delete operations required will be <script type="math/tex; mode=display">m + n</script>. Now, if there is a common sequence among the two strings of length <script type="math/tex; mode=display">lcs</script>, we need to do <script type="math/tex; mode=display">lcs</script> lesser deletions in both the strings leading to a total of <script type="math/tex; mode=display">2lcs</script> lesser deletions, which then leads to the above equation.</p>
<p>In order to find the length of the longest common sequence, we make use of a recursive function <code>lcs(s1,s2,i,j)</code> which returns the length of the longest common sequence among the strings <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script> considering their lengths upto <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> respectively. For evaluating the function, we check if the characters <script type="math/tex; mode=display">s1[m-1]</script> and <script type="math/tex; mode=display">s2[n-1]</script> for equality. If they match, we can consider the corresponding strings upto 1 lesser lengths since the last characters have already been considered and add 1 to the result to be returned for strings of 1 lesser lengths. Thus, we make the function call <code>lcs(s1, s2, i-1, j-1)</code>. </p>
<p>If the last characters don't match, we have two options, either we can consider the second last character of <script type="math/tex; mode=display">s1</script> and the last character of <script type="math/tex; mode=display">s2</script>, or we can consider the second last character of <script type="math/tex; mode=display">s2</script> and the last character of <script type="math/tex; mode=display">s1</script>. We need to consider the larger result obtained out of the two considerations for getting the required length. </p>
<p>Thus, the function call <code>lcs(s1,s2,m,n)</code> returns the required <script type="math/tex; mode=display">lcs</script> value.</p>
<iframe src="https://leetcode.com/playground/QCLZ3ajV/shared" frameborder="0" name="QCLZ3ajV" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^{max(m,n)})</script>. Size of recursion tree will be <script type="math/tex; mode=display">2^(m+n)</script>. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the lengths of <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script> respectively.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\text{max}(m,n))</script>. The depth of the recursion tree will go upto <script type="math/tex; mode=display">\text{max}(m,n)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-longest-common-subsequence-with-memoization-accepted">Approach #2 Longest Common Subsequence with Memoization [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We can observe that in the last approach, while determining the <script type="math/tex; mode=display">lcs</script> value, a lot of redundant function calls are made, since the same <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> values to be used for the function calls could be obtained going through many different paths. We can remove this redundancy by making use of a <script type="math/tex; mode=display">memo</script> array to store the value to be returned for these function calls if they have been called once with the corresponding parameters. Thus, <script type="math/tex; mode=display">memo[i][j]</script> is used to store the result for the function call <code>lcs(s1,s2,i,j)</code>.</p>
<p>Thus, by returning the already stored values from the <script type="math/tex; mode=display">memo</script> array, we can prune the search space to a great extent.</p>
<iframe src="https://leetcode.com/playground/dPT69gpC/shared" frameborder="0" name="dPT69gpC" width="100%" height="377"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script> needs to be filled once. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the length of the strings <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script> respectively.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script> is used. Also, The depth of the recursion tree will go upto <script type="math/tex; mode=display">\text{max}(m,n)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-longest-common-subsequence-dynamic-programming-accepted">Approach #3 Using Longest Common Subsequence- Dynamic Programming [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Another method to obtain the value of <script type="math/tex; mode=display">lcs</script> is to make use of Dynamic Programming. We'll look at the implemenation and carry-on alongside the idea behind it.</p>
<p>We make use of a 2-D <script type="math/tex; mode=display">dp</script>, in which <script type="math/tex; mode=display">dp[i][j]</script> represents the length of the longest common subsequence among the strings <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script> considering their lengths upto <script type="math/tex; mode=display">(i-1)^{th}</script> index and <script type="math/tex; mode=display">(j-1)^{th}</script> index only respectively. We fill the <script type="math/tex; mode=display">dp</script> array in row-by-row order.</p>
<p>In order to fill the entry for <script type="math/tex; mode=display">dp[i][j]</script>, we can have two cases:</p>
<ol>
<li>
<p>The characters <script type="math/tex; mode=display">s1[i-1]</script> and <script type="math/tex; mode=display">s2[j-1]</script> match with each other. In this case, the entry for <script type="math/tex; mode=display">dp[i][j]</script> will be one more than the entry obtained for the strings considering their lengths upto one lesser index, since the matched character adds one to the length of LCS formed till the current indices. Thus, the <script type="math/tex; mode=display">dp[i][j]</script> entry is updated as <script type="math/tex; mode=display">dp[i][j] = 1 + dp[i-1][j-1]</script>. Note that <script type="math/tex; mode=display">dp[i-1][j-1]</script> has been used because the matched character belongs to both <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>.</p>
</li>
<li>
<p>The characters <script type="math/tex; mode=display">s1[i-1]</script> and <script type="math/tex; mode=display">s2[j-1]</script> don't match with each other. In this case, we can't increment the current entry as compared to entries corresponding to the previous indices, but we need to replicate the previous entry again to indicate that the length of LCS upto the current indices also remains the same. But, which entry to pick up? Now, since the current character hasn't matched, we have got two options. We can remove the current character from consideration from either <script type="math/tex; mode=display">s1</script> or <script type="math/tex; mode=display">s2</script> and use the corresponding <script type="math/tex; mode=display">dp</script> entries given by <script type="math/tex; mode=display">dp[i-1][j]</script> and <script type="math/tex; mode=display">dp[i][j-1]</script> respectively. Since we are considering the length of LCS upto the current indices we need to pick up the larger entry out of these two to update the current <script type="math/tex; mode=display">dp</script> entry.</p>
</li>
</ol>
<p>At the end, again, we obtain the number of deletions required as <script type="math/tex; mode=display">m + n - 2*dp[m][n]</script>, where <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the lengths of <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>. <script type="math/tex; mode=display">dp[m][n]</script> now refers to the length of LCS among the two given strings.</p>
<p>!?!../Documents/583_Delete1.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/xQZCgSyw/shared" frameborder="0" name="xQZCgSyw" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. We need to fill in the <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script>. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the lengths of <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-without-using-lcs-dynamic-programmming-accepted">Approach #4 Without using LCS Dynamic Programmming [Accepted]:</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of finding the length of LCS and then determining the number of deletions required, we can make use of Dynamic Programming to directly determine the number of deletions required till the current indices of the strings.</p>
<p>In order to do so, we make use of a 2-D <script type="math/tex; mode=display">dp</script> array. Now, <script type="math/tex; mode=display">dp[i][j]</script> refers to the number of deletions required to equalize the two strings if we consider the strings' length upto <script type="math/tex; mode=display">(i-1)^{th}</script> index and <script type="math/tex; mode=display">(j-1)^{th}</script> index for <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script> respectively. Again, we fill in the <script type="math/tex; mode=display">dp</script> array in a row-by-row order. Now, in order to fill the entry for <script type="math/tex; mode=display">dp[i][j]</script>, we need to consider two cases only:</p>
<ol>
<li>
<p>The characters <script type="math/tex; mode=display">s1[i-1]</script> and <script type="math/tex; mode=display">s2[j-1]</script> match with each other. In this case, we need to replicate the entry corresponding to <script type="math/tex; mode=display">dp[i-1][j-1]</script> itself. This is because, the matched character doesn't need to be deleted from any of the strings.</p>
</li>
<li>
<p>The characters <script type="math/tex; mode=display">s1[i-1]</script> and <script type="math/tex; mode=display">s2[j-1]</script> don't match with each other. In this case, we need to delete either the current character of <script type="math/tex; mode=display">s1</script> or <script type="math/tex; mode=display">s2</script>. Thus, an increment of 1 needs to be done relative to the entries corresponding to the previous indices. The two options available at this moment are <script type="math/tex; mode=display">dp[i-1][j]</script> and <script type="math/tex; mode=display">dp[i][j-1]</script>. Since, we are keeping track of the minimum number of deletions required, we pick up the minimum out of these two values.</p>
</li>
</ol>
<p>At the end, <script type="math/tex; mode=display">dp[m][n]</script> gives the required minimum number of deletions. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the lengths of <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>.</p>
<p>!?!../Documents/583_Delete2.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/aPU8b3Fd/shared" frameborder="0" name="aPU8b3Fd" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. We need to fill in the <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script>. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the lengths of <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-5-1-d-dynamic-programming-accepted">Approach #5 1-D Dynamic Programming [Accepted]:</h4>
<p><strong>Algorithm</strong></p>
<p>We can observe that in the last approach, in order to update the current <script type="math/tex; mode=display">dp</script> entries, we need only the values of the previous row of <script type="math/tex; mode=display">dp</script>. Thus, rather than using a 2-D array, we can do the same job by making use of a 1-D <script type="math/tex; mode=display">dp</script> array.</p>
<p>Thus, now, <script type="math/tex; mode=display">dp[i]</script> refers to the number of deletions that need to be made in order to equalize the strings <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script> if we consider string <script type="math/tex; mode=display">s1</script> upto the <script type="math/tex; mode=display">(i-1)^{th}</script> index and string <script type="math/tex; mode=display">s2</script> upto the last to current index of <script type="math/tex; mode=display">s2</script>. </p>
<p>Now, we make the updations for the current row in an array <script type="math/tex; mode=display">temp</script> of the same size as <script type="math/tex; mode=display">dp</script>, and use the <script type="math/tex; mode=display">dp</script> entries as if they correspond to the previous row's entries. When, the whole <script type="math/tex; mode=display">temp</script> array has been filled, we copy it the <script type="math/tex; mode=display">dp</script> array so that <script type="math/tex; mode=display">dp</script> array now reflects the new row's entries.</p>
<iframe src="https://leetcode.com/playground/jfeuFUeS/shared" frameborder="0" name="jfeuFUeS" width="100%" height="360"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. We need to fill in the <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script>, <script type="math/tex; mode=display">m</script> times. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the lengths of <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">s2</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>