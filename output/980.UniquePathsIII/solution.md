<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-backtracking-dfs">Approach 1: Backtracking DFS</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-backtracking-dfs">Approach 1: Backtracking DFS</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's try walking to each <code>0</code>, leaving an obstacle behind from where we walked.  After, we can remove the obstacle.</p>
<p>Given the input limits, this can work because bad paths tend to get stuck quickly and run out of free squares.</p>
<iframe src="https://leetcode.com/playground/bfNeazhV/shared" frameborder="0" width="100%" height="500" name="bfNeazhV"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(4^{R*C})</script>, where <script type="math/tex; mode=display">R, C</script> are the number of rows and columns in the grid.  (We can find tighter bounds, but such a bound is beyond the scope of this article.)</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(R*C)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <code>dp(r, c, todo)</code> be the number of paths starting from where we are (<code>r, c</code>), and given that <code>todo</code> is the set of empty squares we've yet to walk on.</p>
<p>We can use a similar approach to <em>Approach 1</em>, except we will memoize these states <code>(r, c, todo)</code> so as not to repeat work.</p>
<iframe src="https://leetcode.com/playground/KxYhLJfP/shared" frameborder="0" width="100%" height="500" name="KxYhLJfP"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(R * C * 2^{R*C})</script>, where <script type="math/tex; mode=display">R, C</script> are the number of rows and columns in the grid.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(R * C)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>