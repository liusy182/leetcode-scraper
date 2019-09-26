<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's check every 3x3 grid individually.  For each grid, all numbers must be unique and between 1 and 9; plus every row, column, and diagonal must have the same sum.</p>
<p><strong>Extra Credit</strong></p>
<p>We could also include an <code>if grid[r+1][c+1] != 5: continue</code> check into our code, helping us skip over our <code>for r... for c...</code> for loops faster.  This is based on the following observations:</p>
<ul>
<li>The sum of the grid must be 45, as it is the sum of the distinct values from 1 to 9.</li>
<li>Each horizontal and vertical line must add up to 15, as the sum of 3 of these lines equals the sum of the whole grid.</li>
<li>The diagonal lines must also sum to 15, by definition of the problem statement.</li>
<li>Adding the 12 values from the four lines that cross the center, these 4 lines add up to 60; but they also add up to the entire grid (45), plus 3 times the middle value.  This implies the middle value is 5.</li>
</ul>
<iframe src="https://leetcode.com/playground/6yuMDRxQ/shared" frameborder="0" width="100%" height="500" name="6yuMDRxQ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(R*C)</script>, where <script type="math/tex; mode=display">R, C</script> are the number of rows and columns in the given <code>grid</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>