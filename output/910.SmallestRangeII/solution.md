<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-linear-scan">Approach 1: Linear Scan</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-linear-scan">Approach 1: Linear Scan</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Smallest Range I</em>, smaller <code>A[i]</code> will choose to increase their value ("go up"), and bigger <code>A[i]</code> will decrease their value ("go down").</p>
<p><strong>Algorithm</strong></p>
<p>We can formalize the above concept: if <code>A[i] &lt; A[j]</code>, we don't need to consider when <code>A[i]</code> goes down while <code>A[j]</code> goes up.  This is because the interval <code>(A[i] + K, A[j] - K)</code> is a subset of <code>(A[i] - K, A[j] + K)</code> (here, <code>(a, b)</code> for <code>a &gt; b</code> denotes <code>(b, a)</code> instead.)</p>
<p>That means that it is never worse to choose <code>(up, down)</code> instead of <code>(down, up)</code>.  We can prove this claim that one interval is a subset of another, by showing both <code>A[i] + K</code> and <code>A[j] - K</code> are between <code>A[i] - K</code> and <code>A[j] + K</code>.</p>
<p>For sorted <code>A</code>, say <code>A[i]</code> is the largest <code>i</code> that goes up.  Then <code>A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K</code> are the only relevant values for calculating the answer: every other value is between one of these extremal values.</p>
<iframe src="https://leetcode.com/playground/cCvupdgy/shared" frameborder="0" width="100%" height="310" name="cCvupdgy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of the <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>, plus the space used by the builtin sorting algorithm.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>