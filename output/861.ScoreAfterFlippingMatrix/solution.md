<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-greedy">Approach 2: Greedy</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>Notice that a <code>1</code> in the <script type="math/tex; mode=display">i</script>th column from the right, contributes <script type="math/tex; mode=display">2^i</script> to the score.</p>
<p>Say we are finished toggling the rows in some configuration.  Then for each column, (to maximize the score), we'll toggle the column if it would increase the number of <code>1</code>s.</p>
<p>We can brute force over every possible way to toggle rows.</p>
<p><strong>Algorithm</strong></p>
<p>Say the matrix has <code>R</code> rows and <code>C</code> columns.</p>
<p>For each <code>state</code>, the transition <code>trans = state ^ (state-1)</code> represents the rows that must be toggled to get into the state of toggled rows represented by (the bits of) <code>state</code>.</p>
<p>We'll toggle them, and also maintain the correct column sums of the matrix on the side.</p>
<p>Afterwards, we'll calculate the score.  If for example the last column has a column sum of <code>3</code>, then the score is <code>max(3, R-3)</code>, where <code>R-3</code> represents the score we get from toggling the last column.</p>
<p>In general, the score is increased by <code>max(col_sum, R - col_sum) * (1 &lt;&lt; (C-1-c))</code>, where the factor <code>(1 &lt;&lt; (C-1-c))</code> is the power of <code>2</code> that each <code>1</code> contributes.</p>
<p>Note that this approach may not run in the time allotted.</p>
<iframe src="https://leetcode.com/playground/RqkiosdE/shared" frameborder="0" width="100%" height="500" name="RqkiosdE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^R * R * C)</script>, where <script type="math/tex; mode=display">R, C</script> is the number of rows and columns in the matrix.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(C)</script> in additional space complexity.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy">Approach 2: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>Notice that a <code>1</code> in the <script type="math/tex; mode=display">i</script>th column from the right, contributes <script type="math/tex; mode=display">2^i</script> to the score.</p>
<p>Since <script type="math/tex; mode=display">2^n > 2^{n-1} + 2^{n-2} + \cdots + 2^0</script>, maximizing the left-most digit is more important than any other digit.  Thus, the rows should be toggled such that the left-most column is either all <code>0</code> or all <code>1</code> (so that after toggling the left-most column [if necessary], the left column is all <code>1</code>.)</p>
<p><strong>Algorithm</strong></p>
<p>If we toggle rows by the first column (<code>A[r][c] ^= A[r][0]</code>), then the first column will be all <code>0</code>.</p>
<p>Afterwards, the base score is <code>max(col, R - col)</code> where <code>col</code> is the column sum; and <code>(1 &lt;&lt; (C-1-c))</code> is the power of 2 that each <code>1</code> in that column contributes to the score.</p>
<iframe src="https://leetcode.com/playground/2SApjxHH/shared" frameborder="0" width="100%" height="276" name="2SApjxHH"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(R * C)</script>, <script type="math/tex; mode=display">R, C</script> is the number of rows and columns in the matrix.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script> in additional space complexity.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>