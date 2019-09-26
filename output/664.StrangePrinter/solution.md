<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>It is natural to consider letting <code>dp(i, j)</code> be the answer for printing <code>S[i], S[i+1], ..., S[j]</code>, but proceeding from here is difficult.  We need the following sequence of deductions:</p>
<ul>
<li>
<p>Whatever turn creates the final print of <code>S[i]</code> might as well be the first turn, and also there might as well only be one print, since any later prints on interval <code>[i, k]</code> could just be on <code>[i+1, k]</code>.</p>
</li>
<li>
<p>Say the first print is on <code>[i, k]</code>.  We can assume <code>S[i] == S[k]</code>, because if it wasn't, we could print up to the last occurrence of <code>S[i]</code> in <code>[i, k]</code> for the same result.</p>
</li>
<li>
<p>When correctly printing everything in <code>[i, k]</code> (with <code>S[i] == S[k]</code>), it will take the same amount of steps as correctly printing everything in <code>[i, k-1]</code>.  This is because if <code>S[i]</code> and <code>S[k]</code> get completed in separate steps, we might as well print them first in one step instead.</p>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>With the above deductions, the algorithm is straightforward.</p>
<p>To compute a recursion for <code>dp(i, j)</code>, for every <code>i &lt;= k &lt;= j</code> with <code>S[i] == S[k]</code>, we have some candidate answer <code>dp(i, k-1) + dp(k+1, j)</code>, and we take the minimum of these candidates.  Of course, when <code>k = i</code>, the candidate is just <code>1 + dp(i+1, j)</code>.</p>
<p>To avoid repeating work, we memoize our intermediate answers <code>dp(i, j)</code>.</p>
<iframe src="https://leetcode.com/playground/L3mAUr9w/shared" frameborder="0" width="100%" height="378" name="L3mAUr9w"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^3)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>s</code>.  For each of <script type="math/tex; mode=display">O(N^2)</script> possible states representing a subarray of <code>s</code>, we perform <script type="math/tex; mode=display">O(N)</script> work iterating through <code>k</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the size of our <code>memo</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>