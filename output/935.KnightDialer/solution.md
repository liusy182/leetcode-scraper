<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>f(start, n)</code> be the number of ways to dial an <code>n</code> digit number, where the knight starts at square <code>start</code>.  We can create a recursion, writing this in terms of <code>f(x, n-1)</code>'s.</p>
<p><strong>Algorithm</strong></p>
<p>By hand or otherwise, have a way to query what moves are available at each square.  This implies the exact recursion for <code>f</code>.  For example, from <code>1</code> we can move to <code>6, 8</code>, so <code>f(1, n) = f(6, n-1) + f(8, n-1)</code>.</p>
<p>After, let's keep track of <code>dp[start] = f(start, n)</code>, and update it for each n from <code>1, 2, ..., N</code>.</p>
<p>At the end, the answer is <code>f(0, N) + f(1, N) + ... + f(9, N) = sum(dp)</code>.</p>
<iframe src="https://leetcode.com/playground/EirthMi4/shared" frameborder="0" width="100%" height="463" name="EirthMi4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>.</p>
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