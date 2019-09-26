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
<p>The robot can only move either down or right.
Hence any cell in the first row can only be reached from the cell left to it.</p>
<p></p><center>
<p>!?!../Documents/63_Unique_Paths_2_1.json:500,415!?!</p>
<p></p></center>
<p>And, any cell in the first column can only be reached from the cell above it.</p>
<p></p><center>
<p>!?!../Documents/63_Unique_Paths_2_2.json:500,415!?!</p>
<p></p></center>
<p>For any other cell in the grid, we can reach it either from the cell to left of it or the cell above it.</p>
<p>If any cell has an obstacle, we won't let that cell contribute to any path.</p>
<p>We will be iterating the array from left-to-right and top-to-bottom. Thus, before reaching any cell we would have the number of ways of reaching the predecessor cells. This is what makes it a <code>Dynamic Programming</code> problem. We will be using the <code>obstacleGrid</code> array as the DP array thus not utilizing any additional space.</p>
<p><code>Note:</code> As per the question, cell with an obstacle has a value <code>1</code>. We would use this value to make sure if a cell needs to be included in the path or not. After that we can use the same cell to store the number of ways to reach that cell.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>If the first cell i.e. <code>obstacleGrid[0,0]</code> contains <code>1</code>, this means there is an obstacle in the first cell. Hence the robot won't be able to make any move and we would return the number of ways as <code>0</code>.</li>
<li>Otherwise, if <code>obstacleGrid[0,0]</code> has a <code>0</code> originally we set it to <code>1</code> and move ahead.</li>
<li>Iterate the first row. If a cell originally contains a <code>1</code>, this means the current cell has an obstacle and shouldn't contribute to any path. Hence, set the value of that cell to <code>0</code>. Otherwise, set it to the value of previous cell i.e. <code>obstacleGrid[i,j] = obstacleGrid[i,j-1]</code></li>
<li>Iterate the first column. If a cell originally contains a <code>1</code>, this means the current cell has an obstacle and shouldn't contribute to any path. Hence, set the value of that cell to <code>0</code>. Otherwise, set it to the value of previous cell i.e. <code>obstacleGrid[i,j] = obstacleGrid[i-1,j]</code></li>
<li>Now, iterate through the array starting from cell <code>obstacleGrid[1,1]</code>. If a cell originally doesn't contain any obstacle then the number of ways of reaching that cell would be the sum of number of ways of reaching the cell above it and number of ways of reaching the cell to the left of it.
    <pre>
    obstacleGrid[i,j] = obstacleGrid[i-1,j] + obstacleGrid[i,j-1]</pre></li>
<li>If a cell contains an obstacle set it to <code>0</code> and continue. This is done to make sure it doesn't contribute to any other path.</li>
</ol>
<p>Following is the animation to explain the algorithm's steps:
</p><center>
<p>!?!../Documents/63_Unique_Paths_2_3.json:500,415!?!</p>
<p></p></center>
<p><br></p>
<iframe src="https://leetcode.com/playground/bmmKXqeu/shared" frameborder="0" width="100%" height="500" name="bmmKXqeu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(M \times N)</script>. The rectangular grid given to us is of size <script type="math/tex; mode=display">M \times N</script> and we process each cell just once.  </li>
<li>Space Complexity: <script type="math/tex; mode=display">O(1)</script>. We are utilizing the <code>obstacleGrid</code> as the DP array. Hence, no extra space.</li>
</ul>
<p><br><br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>