<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-mathematical">Approach 1: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-mathematical">Approach 1: Mathematical</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <code>A</code> be the original array, and <code>B</code> be the array after all our modifications.  Towards trying to minimize <code>max(B) - min(B)</code>, let's try to minimize <code>max(B)</code> and maximize <code>min(B)</code> separately.</p>
<p>The smallest possible value of <code>max(B)</code> is <code>max(A) - K</code>, as the value <code>max(A)</code> cannot go lower.  Similarly, the largest possible value of <code>min(B)</code> is <code>min(A) + K</code>.  So the quantity <code>max(B) - min(B)</code> is at least <code>ans = (max(A) - K) - (min(A) + K)</code>.</p>
<p>We can attain this value (if <code>ans &gt;= 0</code>), by the following modifications:</p>
<ul>
<li>If <script type="math/tex; mode=display">A[i] \leq \min(A) + K</script>, then <script type="math/tex; mode=display">B[i] = \min(A) + K</script>
</li>
<li>Else, if <script type="math/tex; mode=display">A[i] \geq \max(A) - K</script>, then <script type="math/tex; mode=display">B[i] = \max(A) - K</script>
</li>
<li>Else, <script type="math/tex; mode=display">B[i] = A[i]</script>.</li>
</ul>
<p>If <code>ans &lt; 0</code>, the best answer we could have is <code>ans = 0</code>, also using the same modification.</p>
<iframe src="https://leetcode.com/playground/hn3nSh7u/shared" frameborder="0" width="100%" height="225" name="hn3nSh7u"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
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