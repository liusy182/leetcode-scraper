<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-square-by-square">Approach 1: Square by Square</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-square-by-square">Approach 1: Square by Square</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to count the surface area contributed by <code>v = grid[i][j]</code>.</p>
<p>When <code>v &gt; 0</code>, the top and bottom surface contributes an area of 2.</p>
<p>Then, for each side (west side, north side, east side, south side) of the column at <code>grid[i][j]</code>, the neighboring cell with value <code>nv</code> means our square contributes <code>max(v - nv, 0)</code>.</p>
<p>For example, for <code>grid = [[1, 5]]</code>, the contribution at <code>grid[0][1]</code> is 2 + 5 + 5 + 5 + 4.  The 2 comes from the top and bottom side, the 5 comes from the north, east, and south side; and the 4 comes from the west side, of which 1 unit is covered by the adjacent column.</p>
<p><strong>Algorithm</strong></p>
<p>For each <code>v = grid[r][c] &gt; 0</code>, count <code>ans += 2</code>, plus <code>ans += max(v - nv, 0)</code> for each neighboring value <code>nv</code> adjacent to <code>grid[r][c]</code>.</p>
<iframe src="https://leetcode.com/playground/JqxzqTG3/shared" frameborder="0" width="100%" height="497" name="JqxzqTG3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of rows (and columns) in the <code>grid</code>.</p>
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