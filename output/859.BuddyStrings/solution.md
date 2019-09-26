<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-enumerate-cases">Approach 1: Enumerate Cases</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-enumerate-cases">Approach 1: Enumerate Cases</h4>
<p><strong>Intuition</strong></p>
<p>Let's say <code>i</code> is <em>matched</em> if <code>A[i] == B[i]</code>, otherwise <code>i</code> is <em>unmatched</em>.  A buddy string has almost all matches, because a swap only affects two indices.</p>
<p>If swapping <code>A[i]</code> and <code>A[j]</code> would demonstrate that <code>A</code> and <code>B</code> are buddy strings, then <code>A[i] == B[j]</code> and <code>A[j] == B[i]</code>.  That means among the four free variables <code>A[i], A[j], B[i], B[j]</code>, there are only two cases: either <code>A[i] == A[j]</code> or not.</p>
<p><strong>Algorithm</strong></p>
<p>Let's work through the cases.</p>
<p>In the case <code>A[i] == A[j] == B[i] == B[j]</code>, then the strings <code>A</code> and <code>B</code> are equal.  So if <code>A == B</code>, we should check each index <code>i</code> for two matches with the same value.</p>
<p>In the case <code>A[i] == B[j], A[j] == B[i], (A[i] != A[j])</code>, the rest of the indices match.  So if <code>A</code> and <code>B</code> have only two unmatched indices (say <code>i</code> and <code>j</code>), we should check that the equalities <code>A[i] == B[j]</code> and <code>A[j] == B[i]</code> hold.</p>
<iframe src="https://leetcode.com/playground/3ce2yPsD/shared" frameborder="0" width="100%" height="500" name="3ce2yPsD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code> and <code>B</code>.</p>
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