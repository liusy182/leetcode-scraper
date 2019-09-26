<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-row-and-column-maximums-accepted">Approach #1: Row and Column Maximums [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-row-and-column-maximums-accepted">Approach #1: Row and Column Maximums [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>The skyline looking from the top is <code>col_maxes = [max(column_0), max(column_1), ...]</code>.  Similarly, the skyline from the left is <code>row_maxes [max(row_0), max(row_1), ...]</code></p>
<p>In particular, each building <code>grid[r][c]</code> could become height <code>min(max(row_r), max(col_c))</code>, and this is the largest such height.  If it were larger, say <code>grid[r][c] &gt; max(row_r)</code>, then the part of the skyline <code>row_maxes = [..., max(row_r), ...]</code> would change.</p>
<p>These increases are also independent (none of them change the skyline), so we can perform them independently.</p>
<iframe src="https://leetcode.com/playground/ELQgWsrX/shared" frameborder="0" width="100%" height="395" name="ELQgWsrX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of rows (and columns) of the grid.  We iterate through every cell of the grid.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>row_maxes</code> and <code>col_maxes</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>