<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-solve-the-equation">Approach 1: Solve the Equation</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-solve-the-equation">Approach 1: Solve the Equation</h4>
<p><strong>Intuition</strong></p>
<p>If Alice swaps candy <code>x</code>, she expects some specific quantity of candy <code>y</code> back.</p>
<p><strong>Algorithm</strong></p>
<p>Say Alice and Bob have total candy <script type="math/tex; mode=display">S_A, S_B</script> respectively.</p>
<p>If Alice gives candy <script type="math/tex; mode=display">x</script>, and receives candy <script type="math/tex; mode=display">y</script>, then Bob receives candy <script type="math/tex; mode=display">x</script> and gives candy <script type="math/tex; mode=display">y</script>.  Then, we must have</p>
<p>
<script type="math/tex; mode=display">
S_A - x + y = S_B - y + x
</script>
</p>
<p>for a fair candy swap.  This implies</p>
<p>
<script type="math/tex; mode=display">
y = x + \frac{S_B - S_A}{2}
</script>
</p>
<p>Our strategy is simple.  For every candy <script type="math/tex; mode=display">x</script> that Alice has, if Bob has candy <script type="math/tex; mode=display">y = x + \frac{S_B - S_A}{2}</script>, we return <script type="math/tex; mode=display">[x, y]</script>.  We use a <code>Set</code> structure to check whether Bob has the desired candy <script type="math/tex; mode=display">y</script> in constant time.</p>
<iframe src="https://leetcode.com/playground/WryKmFvR/shared" frameborder="0" width="100%" height="361" name="WryKmFvR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(A\text{.length} + B\text{.length})</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(B\text{.length})</script>, the space used by <code>setB</code>.  (We can improve this to <script type="math/tex; mode=display">\min(A\text{.length}, B\text{.length})</script> by using an if statement.)
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>