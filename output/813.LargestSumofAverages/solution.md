<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The best score partitioning <code>A[i:]</code> into at most <code>K</code> parts depends on answers to paritioning <code>A[j:]</code> (<code>j &gt; i</code>) into less parts.  We can use dynamic programming as the states form a directed acyclic graph.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>dp(i, k)</code> be the best score partioning <code>A[i:]</code> into at most <code>K</code> parts.</p>
<p>If the first group we partition <code>A[i:]</code> into ends before <code>j</code>, then our candidate partition has score <code>average(i, j) + dp(j, k-1))</code>, where <code>average(i, j) = (A[i] + A[i+1] + ... + A[j-1]) / (j - i)</code> (floating point division).  We take the highest score of these, keeping in mind we don't necessarily need to partition - <code>dp(i, k)</code> can also be just <code>average(i, N)</code>.</p>
<p>In total, our recursion in the general case is <code>dp(i, k) = max(average(i, N), max_{j &gt; i}(average(i, j) + dp(j, k-1)))</code>.</p>
<p>We can calculate <code>average</code> a little bit faster by remembering prefix sums.  If <code>P[x+1] = A[0] + A[1] + ... + A[x]</code>, then <code>average(i, j) = (P[j] - P[i]) / (j - i)</code>.</p>
<p>Our implementation showcases a "bottom-up" style of dp.  Here at loop number <code>k</code> in our outer-most loop, <code>dp[i]</code> represents <code>dp(i, k)</code> from the discussion above, and we are calculating the next layer <code>dp(i, k+1)</code>.  The end of our second loop <code>for i = 0..N-1</code> represents finishing the calculation of the correct value for <code>dp(i, t)</code>, and the inner-most loop performs the calculation <code>max_{j &gt; i}(average(i, j) + dp(j, k))</code>.</p>
<iframe src="https://leetcode.com/playground/Eem7Vreg/shared" frameborder="0" width="100%" height="378" name="Eem7Vreg"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(K * N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>dp</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>