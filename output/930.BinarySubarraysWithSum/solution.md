<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-index-of-ones">Approach 1: Index of Ones</a></li>
<li><a href="#approach-2-prefix-sums">Approach 2: Prefix Sums</a></li>
<li><a href="#approach-3-three-pointer">Approach 3: Three Pointer</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-index-of-ones">Approach 1: Index of Ones</h4>
<p><strong>Intuition</strong></p>
<p>Say we number the <code>1</code>s in <code>A</code>: <script type="math/tex; mode=display">(x_1, x_2, \cdots, x_n)</script> with <script type="math/tex; mode=display">A[x_i] = 1</script>.</p>
<p>Then, if we have a subarray of sum <script type="math/tex; mode=display">S</script>, it has to use the ones <script type="math/tex; mode=display">x_i, x_{i+1}, \cdots, x_{i+S-1}</script>.  For each <script type="math/tex; mode=display">i</script>, we can count the number of such subarrays individually.</p>
<p><strong>Algorithm</strong></p>
<p>In general, the number of such subarrays (for <script type="math/tex; mode=display">i</script>) is <script type="math/tex; mode=display">(x_i - x_{i-1}) * (x_{i+S} - x_{i+S-1})</script>.</p>
<p>For example, if <script type="math/tex; mode=display">S = 2</script>, then in <code>A = [1,0,1,0,1,0,0,1]</code>, let's count the number of subarrays <code>[i, j]</code> that use the middle two <code>1</code>s.  There are 2 choices for the <code>i</code> <code>(i = 1, 2)</code> and 3 choices for the <code>j</code> <code>(j = 4, 5, 6)</code>.</p>
<p>The corner cases are when <script type="math/tex; mode=display">S = 0</script>, <script type="math/tex; mode=display">i = 1</script>, or <script type="math/tex; mode=display">i+S = n+1</script>. We can handle these gracefully.</p>
<iframe src="https://leetcode.com/playground/xeXqLmYy/shared" frameborder="0" width="100%" height="500" name="xeXqLmYy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-prefix-sums">Approach 2: Prefix Sums</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>P[i] = A[0] + A[1] + ... + A[i-1]</code>.  Then <code>P[j+1] - P[i] = A[i] + A[i+1] + ... + A[j]</code>, the sum of the subarray <code>[i, j]</code>.</p>
<p>Hence, we are looking for the number of <code>i &lt; j</code> with <code>P[j] - P[i] = S</code>.</p>
<p><strong>Algorithm</strong></p>
<p>For each <code>j</code>, let's count the number of <code>i</code> with <code>P[j] = P[i] + S</code>.  This is analogous to counting the number of subarrays ending in <code>j</code> with sum <code>S</code>.</p>
<p>It comes down to counting how many <code>P[i] + S</code> we've seen before.  We can keep this count on the side to help us find the final answer.</p>
<iframe src="https://leetcode.com/playground/nAHXHKUL/shared" frameborder="0" width="100%" height="344" name="nAHXHKUL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-three-pointer">Approach 3: Three Pointer</h4>
<p><strong>Intuition</strong></p>
<p>For each <code>j</code>, let's try to count the number of <code>i</code>'s that have the subarray <code>[i, j]</code> equal to <code>S</code>.</p>
<p>It is easy to see these <code>i</code>'s form an interval <code>[i_lo, i_hi]</code>, and each of <code>i_lo</code>, <code>i_hi</code> are increasing with respect to <code>j</code>.  So we can use a "two pointer" style approach.</p>
<p><strong>Algorithm</strong></p>
<p>For each <code>j</code> (in increasing order), let's maintain 4 variables:</p>
<ul>
<li><code>sum_lo</code> : the sum of subarray <code>[i_lo, j]</code></li>
<li><code>sum_hi</code> : the sum of subarray <code>[i_hi, j]</code></li>
<li><code>i_lo</code> : the smallest <code>i</code> so that <code>sum_lo &lt;= S</code></li>
<li><code>i_hi</code> : the largest <code>i</code> so that <code>sum_hi &lt;= S</code></li>
</ul>
<p>Then, (provided that <code>sum_lo == S</code>), the number of subarrays ending in <code>j</code> is <code>i_hi - i_lo + 1</code>.</p>
<p>As an example, with <code>A = [1,0,0,1,0,1]</code> and <code>S = 2</code>, when <code>j = 5</code>, we want <code>i_lo = 1</code> and <code>i_hi = 3</code>.</p>
<iframe src="https://leetcode.com/playground/7oyzRqG8/shared" frameborder="0" width="100%" height="480" name="7oyzRqG8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>