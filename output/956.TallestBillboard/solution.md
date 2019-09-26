<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
<li><a href="#approach-2-meet-in-the-middle">Approach 2: Meet in the Middle</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>For each rod <code>x</code>, we can write <code>+x</code>, <code>-x</code>, or <code>0</code>.  Our goal is to write <code>0</code> using the largest sum of positive terms.  For writings that have a sum of <code>0</code>, let's call the sum of the positive terms written the <em>score</em>.  For example, <code>+1 +2 +3 -6</code> has a score of <code>6</code>.</p>
<p>Since <code>sum(rods)</code> is bounded, it suggests to us to use that fact it in some way.  Indeed, if we already wrote some sum in the first few terms, it doesn't matter how we got it.  For example, with <code>rods = [1,2,2,3]</code>, we could arrive at a sum of <code>3</code> in 3 different ways, but the effective score is <code>3</code>.  This upper-bounds the number of states we have to consider to <code>10001</code>, as there are only this many possible sums in the interval <code>[-5000, 5000]</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>dp[i][s]</code> be the largest score we can get using <code>rods[j]</code> <code>(j &gt;= i)</code>, after previously writing a sum of <code>s</code> (that isn't included in the score).  For example, with <code>rods = [1,2,3,6]</code>, we might have <code>dp[1][1] = 5</code>, as after writing <code>1</code>, we could write <code>+2 +3 -6</code> with the remaining <code>rods[i:]</code> for a score of <code>5</code>.</p>
<p>In the base case, <code>dp[rods.length][s]</code> is <code>0</code> when <code>s == 0</code>, and <code>-infinity</code> everywhere else.  The recursion is <code>dp[i][s] = max(dp[i+1][s], dp[i+1][s-rods[i]], rods[i] + dp[i+1][s+rods[i]])</code>.</p>
<iframe src="https://leetcode.com/playground/w65ZpeRa/shared" frameborder="0" width="100%" height="480" name="w65ZpeRa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NS)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>rods</code>, and <script type="math/tex; mode=display">S</script> is the maximum of <script type="math/tex; mode=display">\sum \text{rods}[i]</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(NS)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-meet-in-the-middle">Approach 2: Meet in the Middle</h4>
<p><strong>Intuition</strong></p>
<p>Typically, the complexity of brute force can be reduced with a "meet in the middle" technique.  As applied to this problem, we have <script type="math/tex; mode=display">3^N</script> possible states, from writing either <code>+x</code>, <code>-x</code>, or <code>0</code> for each rod <code>x</code>, and we want to make this brute force faster.</p>
<p>What we can do is write the first and last <script type="math/tex; mode=display">3^{N/2}</script> states separately, and attempt to combine them.  For example, if we have rods <code>[1, 3, 5, 7]</code>, then the first two rods create up to nine states: <code>[0+0, 0+3, 0-3, 1+0, 1+3, 1-3, -1+0, -1+3, -1-3]</code>, and the last two rods also create nine states.</p>
<p>We will store each state as the sum of positive terms, and the sum of absolute values of the negative terms.  For example, <code>+1 +2 -3 -4</code> becomes <code>(3, 7)</code>.  Let's also call the difference <code>3 - 7</code> to be the <em>delta</em> of this state, so this state has a delta of <code>-4</code>.</p>
<p>Our high level goal is to combine states with deltas that sum to <code>0</code>.  The score of a state will be the sum of the positive terms, and we want the highest score.  Note that for each delta, we only care about the state that has the highest score.</p>
<p><strong>Algorithm</strong></p>
<p>Split the rods into two halves: left and right.</p>
<p>For each half, use brute force to compute the reachable states as defined above.  Then, for each state, record the delta and the maximum score.</p>
<p>Now, we have a left and right halves with <code>[(delta, score)]</code> information.  We'll find the largest total score, with total delta <code>0</code>.</p>
<iframe src="https://leetcode.com/playground/b3NRJoz4/shared" frameborder="0" width="100%" height="500" name="b3NRJoz4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(3^{N/2})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>rods</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(3^{N/2})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>