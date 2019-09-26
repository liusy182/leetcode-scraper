<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>There is a clear recursion available: the final cost <code>f[i]</code> to climb the staircase from some step <code>i</code> is <code>f[i] = cost[i] + min(f[i+1], f[i+2])</code>.  This motivates <em>dynamic programming</em>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's evaluate <code>f</code> backwards in order.  That way, when we are deciding what <code>f[i]</code> will be, we've already figured out <code>f[i+1]</code> and <code>f[i+2]</code>.</p>
<p>We can do even better than that.  At the <code>i</code>-th step, let <code>f1, f2</code> be the old value of <code>f[i+1]</code>, <code>f[i+2]</code>, and update them to be the new values <code>f[i], f[i+1]</code>.  We keep these updated as we iterate through <code>i</code> backwards.  At the end, we want <code>min(f1, f2)</code>.</p>
<iframe src="https://leetcode.com/playground/R8h7KgV3/shared" frameborder="0" width="100%" height="242" name="R8h7KgV3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>cost</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>f1, f2</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>