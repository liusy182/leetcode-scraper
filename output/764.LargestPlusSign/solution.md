<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each possible center, find the largest plus sign that could be placed by repeatedly expanding it.
We expect this algorithm to be <script type="math/tex; mode=display">O(N^3)</script>, and so take roughly <script type="math/tex; mode=display">500^3 = (1.25) * 10^8</script> operations.  This is a little bit too big for us to expect it to run in time.</p>
<iframe src="https://leetcode.com/playground/pVcrm4PA/shared" frameborder="0" width="100%" height="412" name="pVcrm4PA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^3)</script>, as we perform two outer loops (<script type="math/tex; mode=display">O(N^2)</script>), plus the inner loop involving <code>k</code> is <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(\text{mines.length})</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>How can we improve our bruteforce?  One way is to try to speed up the inner loop involving <code>k</code>, the order of the candidate plus sign.
If we knew the longest possible arm length <script type="math/tex; mode=display">L_u, L_l, L_d, L_r</script> in each direction from a center, we could know the order <script type="math/tex; mode=display">\min(L_u, L_l, L_d, L_r)</script> of a plus sign at that center.  We could find these lengths separately using dynamic programming.</p>
<p><strong>Algorithm</strong></p>
<p>For each (cardinal) direction, and for each coordinate <code>(r, c)</code> let's compute the <code>count</code> of that coordinate: the longest line of <code>'1'</code>s starting from <code>(r, c)</code> and going in that direction.
With dynamic programming, it is either 0 if <code>grid[r][c]</code> is zero, else it is <code>1</code> plus the count of the coordinate in the same direction.
For example, if the direction is left and we have a row like <code>01110110</code>, the corresponding count values are <code>01230120</code>, and the integers are either 1 more than their successor, or 0.
For each square, we want <code>dp[r][c]</code> to end up being the minimum of the 4 possible counts.  At the end, we take the maximum value in <code>dp</code>.</p>
<iframe src="https://leetcode.com/playground/JxbvtwM9/shared" frameborder="0" width="100%" height="500" name="JxbvtwM9"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, as the work we do under two nested for loops is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the size of <code>dp</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>