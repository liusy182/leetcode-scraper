<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-greedy-wrong-answer">Approach #1: Greedy [Wrong Answer]</a></li>
<li><a href="#approach-2-dynamic-programming-top-down-accepted">Approach #2: Dynamic Programming (Top Down) [Accepted]</a></li>
<li><a href="#approach-3-dynamic-programming-bottom-up-accepted">Approach #3: Dynamic Programming (Bottom Up) [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-greedy-wrong-answer">Approach #1: Greedy [Wrong Answer]</h4>
<p><strong>Intuition</strong></p>
<p>Let's find the most cherries we can pick up with one path, pick them up, then find the most cherries we can pick up with a second path on the remaining field.</p>
<p>Though a counter example might be hard to think of, this approach fails to find the best answer to this case:</p>
<div class="codehilite"><pre><span></span><span class="mi">11100</span>
<span class="mo">00101</span>
<span class="mi">10100</span>
<span class="mo">00100</span>
<span class="mo">00111</span>
</pre></div>


<p><strong>Algorithm</strong></p>
<p>We can use dynamic programming to find the most number of cherries <code>dp[i][j]</code> that can be picked up from any location <code>(i, j)</code> to the bottom right corner.  This is a classic question very similar to <a href="https://leetcode.com/problems/minimum-path-sum/description/">Minimum Path Sum</a>, refer to the link if you are not familiar with this type of question.</p>
<p>After, we can find an first path that maximizes the number of cherries taken by using our completed <code>dp</code> as an oracle for deciding where to move.  We'll choose the move that allows us to pick up more cherries (based on comparing <code>dp[i+1][j]</code> and <code>dp[i][j+1]</code>).</p>
<p>After taking the cherries from that path (and removing it from the grid), we'll take the cherries again.</p>
<iframe src="https://leetcode.com/playground/UVn8oEww/shared" frameborder="0" width="100%" height="500" name="UVn8oEww"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>grid</code>.  Our dynamic programming consists of two for-loops of length <code>N</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the size of <code>dp</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-top-down-accepted">Approach #2: Dynamic Programming (Top Down) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Instead of walking from end to beginning, let's reverse the second leg of the path, so we are only considering two paths from the beginning to the end.</p>
<p>Notice after <code>t</code> steps, each position <code>(r, c)</code> we could be, is on the line <code>r + c = t</code>.  So if we have two people at positions <code>(r1, c1)</code> and <code>(r2, c2)</code>, then <code>r2 = r1 + c1 - c2</code>.  That means the variables <code>r1, c1, c2</code> uniquely determine 2 people who have walked the same <code>r1 + c1</code> number of steps.  This sets us up for dynamic programming quite nicely.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>dp[r1][c1][c2]</code> be the most number of cherries obtained by two people starting at <code>(r1, c1)</code> and <code>(r2, c2)</code> and walking towards <code>(N-1, N-1)</code> picking up cherries, where <code>r2 = r1+c1-c2</code>.</p>
<p>If <code>grid[r1][c1]</code> and <code>grid[r2][c2]</code> are not thorns, then the value of <code>dp[r1][c1][c2]</code> is <code>(grid[r1][c1] + grid[r2][c2])</code>, plus the maximum of <code>dp[r1+1][c1][c2]</code>, <code>dp[r1][c1+1][c2]</code>, <code>dp[r1+1][c1][c2+1]</code>, <code>dp[r1][c1+1][c2+1]</code> as appropriate.  We should also be careful to not double count in case <code>(r1, c1) == (r2, c2)</code>.</p>
<p>Why did we say it was the maximum of <code>dp[r+1][c1][c2]</code> etc.?  It corresponds to the 4 possibilities for person 1 and 2 moving down and right:</p>
<ul>
<li>Person 1 down and person 2 down: <code>dp[r1+1][c1][c2]</code>;</li>
<li>Person 1 right and person 2 down: <code>dp[r1][c1+1][c2]</code>;</li>
<li>Person 1 down and person 2 right: <code>dp[r1+1][c1][c2+1]</code>;</li>
<li>Person 1 right and person 2 right: <code>dp[r1][c1+1][c2+1]</code>;</li>
</ul>
<iframe src="https://leetcode.com/playground/BbN9rraL/shared" frameborder="0" width="100%" height="500" name="BbN9rraL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>grid</code>.  Our dynamic programming has <script type="math/tex; mode=display">O(N^3)</script> states.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^3)</script>, the size of <code>memo</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming-bottom-up-accepted">Approach #3: Dynamic Programming (Bottom Up) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Like in <em>Approach #2</em>, we have the idea of dynamic programming.</p>
<p>Say <code>r1 + c1 = t</code> is the <code>t</code>-th layer.  Since our recursion only references the next layer, we only need to keep two layers in memory at a time.</p>
<p><strong>Algorithm</strong></p>
<p>At time <code>t</code>, let <code>dp[c1][c2]</code> be the most cherries that we can pick up for two people going from <code>(0, 0)</code> to <code>(r1, c1)</code> and <code>(0, 0)</code> to <code>(r2, c2)</code>, where <code>r1 = t-c1, r2 = t-c2</code>.  Our dynamic program proceeds similarly to <em>Approach #2</em>.</p>
<iframe src="https://leetcode.com/playground/SAAR75Ui/shared" frameborder="0" width="100%" height="500" name="SAAR75Ui"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>grid</code>.  We have three for-loops of size <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the sizes of <code>dp</code> and <code>dp2</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Solution 3 inspired by <a href="https://leetcode.com/contest/weekly-contest-61/ranking">@uwi</a>.</p>
          </div>
        
      </div>