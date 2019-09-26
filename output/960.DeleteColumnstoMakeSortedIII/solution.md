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
<p><strong>Intuition and Algorithm</strong></p>
<p>This is a tricky problem that is hard to build an intuition about.</p>
<p>First, lets try to find the number of columns to keep, instead of the number to delete.  At the end, we can subtract to find the desired answer.</p>
<p>Now, let's say we must keep the first column <code>C</code>.  The next column <code>D</code> we keep must have all rows lexicographically sorted (ie. <code>C[i] &lt;= D[i]</code>), and we can say that we have deleted all columns between <code>C</code> and <code>D</code>.</p>
<p>Now, we can use dynamic programming to solve the problem in this manner.  Let <code>dp[k]</code> be the number of columns that are kept in answering the question for input <code>[row[k:] for row in A]</code>.  The above gives a simple recursion for <code>dp[k]</code>.</p>
<iframe src="https://leetcode.com/playground/dYqmP2Pc/shared" frameborder="0" width="100%" height="395" name="dYqmP2Pc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N * W^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">W</script> is the length of each word in <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(W)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>