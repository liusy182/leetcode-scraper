<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>We have to put the words into a row, where each word may overlap the previous word.  This is because no word is contained in any word.</p>
<p>Also, it is sufficient to try to maximize the total overlap of the words.</p>
<p>Say we have put some words down in our row, ending with word <code>A[i]</code>.  Now say we put down word <code>A[j]</code> as the next word, where word <code>j</code> hasn't been put down yet.  The overlap increases by <code>overlap(A[i], A[j])</code>.</p>
<p>We can use dynamic programming to leverage this recursion.  Let <code>dp(mask, i)</code> be the total overlap after putting some words down (represented by a bitmask <code>mask</code>), for which <code>A[i]</code> was the last word put down.  Then, the key recursion is <code>dp(mask ^ (1&lt;&lt;j), j) = max(overlap(A[i], A[j]) + dp(mask, i))</code>, where the <code>j</code>th bit is not set in mask, and <code>i</code> ranges over all bits set in <code>mask</code>.</p>
<p>Of course, this only tells us what the maximum overlap is for each set of words.  We also need to remember each choice along the way (ie. the specific <code>i</code> that made <code>dp(mask ^ (1&lt;&lt;j), j)</code> achieve a minimum) so that we can reconstruct the answer.</p>
<p><strong>Algorithm</strong></p>
<p>Our algorithm has 3 main components:</p>
<ul>
<li>Precompute <code>overlap(A[i], A[j])</code> for all possible <code>i, j</code>.</li>
<li>Calculate <code>dp[mask][i]</code>, keeping track of the "<code>parent</code>" <code>i</code> for each <code>j</code> as described above.</li>
<li>Reconstruct the answer using <code>parent</code> information.</li>
</ul>
<p>Please see the implementation for more details about each section.</p>
<iframe src="https://leetcode.com/playground/bMRiuMrv/shared" frameborder="0" width="100%" height="500" name="bMRiuMrv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2 (2^N + W))</script>, where <script type="math/tex; mode=display">N</script> is the number of words, and <script type="math/tex; mode=display">W</script> is the maximum length of each word.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N (2^N + W))</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>