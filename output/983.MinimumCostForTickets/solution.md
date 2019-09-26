<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming-day-variant">Approach 1: Dynamic Programming (Day Variant)</a></li>
<li><a href="#approach-2-dynamic-programming-window-variant">Approach 2: Dynamic Programming (Window Variant)</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming-day-variant">Approach 1: Dynamic Programming (Day Variant)</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each day, if you don't have to travel today, then it's strictly better to wait to buy a pass.  If you have to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or 30-day pass.</p>
<p>We can express those choices as a recursion and use dynamic programming.  Let's say <code>dp(i)</code> is the cost to fulfill your travel plan from day <code>i</code> to the end of the plan.  Then, if you have to travel today, your cost is:</p>
<p>
<script type="math/tex; mode=display">
\text{dp}(i) = \min(\text{dp}(i+1) + \text{costs}[0], \text{dp}(i+7) + \text{costs}[1], \text{dp}(i+30) + \text{costs}[2])
</script>
</p>
<iframe src="https://leetcode.com/playground/vQP5W3UT/shared" frameborder="0" width="100%" height="500" name="vQP5W3UT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(W)</script>, where <script type="math/tex; mode=display">W = 365</script> is the maximum numbered day in your travel plan.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(W)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-window-variant">Approach 2: Dynamic Programming (Window Variant)</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in <em>Approach 1</em>, we only need to buy a travel pass on a day we intend to travel.</p>
<p>Now, let <code>dp(i)</code> be the cost to travel from day <code>days[i]</code> to the end of the plan.  If say, <code>j1</code> is the largest index such that <code>days[j1] &lt; days[i] + 1</code>, <code>j7</code> is the largest index such that <code>days[j7] &lt; days[i] + 7</code>, and <code>j30</code> is the largest index such that <code>days[j30] &lt; days[i] + 30</code>, then we have:</p>
<p>
<script type="math/tex; mode=display">
\text{dp}(i) = \min(\text{dp}(j1) + \text{costs}[0], \text{dp}(j7) + \text{costs}[1], \text{dp}(j30) + \text{costs}[2])
</script>
</p>
<iframe src="https://leetcode.com/playground/NtqEyFYA/shared" frameborder="0" width="100%" height="500" name="NtqEyFYA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of unique days in your travel plan.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>