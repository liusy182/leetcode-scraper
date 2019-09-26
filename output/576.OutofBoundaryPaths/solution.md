<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-recursion-with-memoization-accepted">Approach #2 Recursion with memoization [Accepted]</a></li>
<li><a href="#approach-3-dynamic-programming-accepted">Approach #3 Dynamic Programming [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>In the brute force approach, we try to take one step in every direction and decrement the number of pending moves for each step taken. Whenever we reach out of the boundary while taking the steps, we deduce that one extra path is available to take the ball out. </p>
<p>In order to implement the same, we make use of a recursive function <code>findPaths(m,n,N,i,j)</code> which takes the current number of moves(<script type="math/tex; mode=display">N</script>) along with the current position(<script type="math/tex; mode=display">(i,j)</script> as some of the parameters and returns the number of moves possible to take the ball out with the current pending moves from the current position. Now, we take a step in every direction and update the corresponding indices involved along with the current number of pending moves. </p>
<p>Further, if we run out of moves at any moment, we return a 0 indicating that the current set of moves doesn't take the ball out of boundary.</p>
<iframe src="https://leetcode.com/playground/Q7b3GKsJ/shared" frameborder="0" name="Q7b3GKsJ" width="100%" height="224"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(4^n)</script>. Size of recursion tree will be <script type="math/tex; mode=display">4^n</script>. Here, <script type="math/tex; mode=display">n</script> refers to the number of moves allowed.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursion-with-memoization-accepted">Approach #2 Recursion with memoization [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the brute force approach, while going through the various branches of the recursion tree, we could reach the same position with the same number of moves left. </p>
<p>Thus, a lot of redundant function calls are made with the same set of parameters leading to a useless increase in runtime. We can remove this redundancy by making use of a memoization array, <script type="math/tex; mode=display">memo</script>. <script type="math/tex; mode=display">memo[i][j][k]</script> is used to store the number of possible moves leading to a path out of the boundary if the current position is given by the indices <script type="math/tex; mode=display">(i, j)</script> and number of moves left is <script type="math/tex; mode=display">k</script>. </p>
<p>Thus, now if a function call with some parameters is repeated, the <script type="math/tex; mode=display">memo</script> array will already contain valid values corresponding to that function call resulting in pruning of the search space.</p>
<iframe src="https://leetcode.com/playground/o22neiZb/shared" frameborder="0" name="o22neiZb" width="100%" height="411"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n*N)</script>. We need to fill the <script type="math/tex; mode=display">memo</script> array once with dimensions <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">N</script>. Here, <script type="math/tex; mode=display">m</script>, <script type="math/tex; mode=display">n</script> refer to the number of rows and columns of the given grid respectively. <script type="math/tex; mode=display">N</script> refers to the total number of allowed moves.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n*N)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">m*n*N</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming-accepted">Approach #3 Dynamic Programming [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>The idea behind this approach is that if we can reach some position in <script type="math/tex; mode=display">x</script> moves, we can reach all its adjacent positions in <script type="math/tex; mode=display">x+1</script> moves. Based on this idea, we make use of a 2-D <script type="math/tex; mode=display">dp</script> array to store the number of ways in which a particular position can be reached. <script type="math/tex; mode=display">dp[i][j]</script> refers to the number of ways the position corresponding to the indices <script type="math/tex; mode=display">(i,j)</script> can be reached given some particular number of moves.</p>
<p>Now, if the current <script type="math/tex; mode=display">dp</script> array stores the number of ways the various positions can be reached by making use of <script type="math/tex; mode=display">x-1</script> moves, in order to determine the number of ways the position <script type="math/tex; mode=display">(i,j)</script> can be reached by making use of <script type="math/tex; mode=display">x</script> moves, we need to update the corresponding <script type="math/tex; mode=display">dp</script> entry as <script type="math/tex; mode=display">dp[i][j] = dp[i-1][j] + dp[i+1][j] + dp[i][j-1] + dp[i][j+1]</script> taking care of boundary conditions. This happens because we can reach the index <script type="math/tex; mode=display">(i,j)</script> from any of the four adjacent positions and the total number of ways of reaching the index <script type="math/tex; mode=display">(i,j)</script> in <script type="math/tex; mode=display">x</script> moves is the sum of the ways of reaching the adjacent positions in <script type="math/tex; mode=display">x-1</script> moves. </p>
<p>But, if we alter the <script type="math/tex; mode=display">dp</script> array, now some of the entries will correspond to <script type="math/tex; mode=display">x-1</script> moves and the updated ones will correspond to <script type="math/tex; mode=display">x</script> moves. Thus, we need to find a way to tackle this issue. So, instead of updating the <script type="math/tex; mode=display">dp</script> array for the current(<script type="math/tex; mode=display">x</script>) moves, we make use of a temporary 2-D array <script type="math/tex; mode=display">temp</script> to store the updated results for <script type="math/tex; mode=display">x</script> moves, making use of the results obtained for <script type="math/tex; mode=display">dp</script> array corresponding to <script type="math/tex; mode=display">x-1</script> moves. After all the entries for all the positions have been considered for <script type="math/tex; mode=display">x</script> moves, we update the <script type="math/tex; mode=display">dp</script> array based on <script type="math/tex; mode=display">temp</script>. Thus, <script type="math/tex; mode=display">dp</script> now contains the entries corresponding to <script type="math/tex; mode=display">x</script> moves.</p>
<p>Thus, we start off by considering zero move available for which we make an initial entry of <script type="math/tex; mode=display">dp[x][y] = 1</script>(<script type="math/tex; mode=display">(x,y)</script> is the initial position), since we can reach only this position in zero move. Then, we increase the number of moves to 1 and update all the <script type="math/tex; mode=display">dp</script> entries appropriately. We do so for all the moves possible from 1 to N. </p>
<p>In order to update <script type="math/tex; mode=display">count</script>, which indicates the total number of possible moves which lead an out of boundary path, we need to perform the update only when we reach the boundary. We update the count as <script type="math/tex; mode=display">count = count + dp[i][j]</script>, where <script type="math/tex; mode=display">(i,j)</script> corresponds to one of the boundaries. But, if <script type="math/tex; mode=display">(i,j)</script> is simultaneously a part of multiple boundaries, we need to add the <script type="math/tex; mode=display">dp[i][j]</script> factor multiple times(same as the number of boundaries to which <script type="math/tex; mode=display">(i,j)</script> belongs).</p>
<p>After we are done with all the <script type="math/tex; mode=display">N</script> moves, <script type="math/tex; mode=display">count</script> gives the required result.</p>
<p>The following animation illustrates the process:</p>
<p>!?!../Documents/576_Boundary_Paths.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/MvuV89Mf/shared" frameborder="0" name="MvuV89Mf" width="100%" height="513"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(N*m*n)</script>. We need to fill the <script type="math/tex; mode=display">dp</script>$ array with dimensions <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script>
<script type="math/tex; mode=display">N</script> times. Here <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script> refers to the size of the grid and <script type="math/tex; mode=display">N</script> refers to the number of moves available.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. <script type="math/tex; mode=display">dp</script> and <script type="math/tex; mode=display">temp</script> array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script> are used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>