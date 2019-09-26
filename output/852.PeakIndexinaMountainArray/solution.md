<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-linear-scan">Approach 1: Linear Scan</a></li>
<li><a href="#approach-2-binary-search">Approach 2: Binary Search</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-linear-scan">Approach 1: Linear Scan</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>The mountain increases until it doesn't.  The point at which it stops increasing is the peak.</p>
<iframe src="https://leetcode.com/playground/wnFAmS4Z/shared" frameborder="0" width="100%" height="174" name="wnFAmS4Z"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-binary-search">Approach 2: Binary Search</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>The comparison <code>A[i] &lt; A[i+1]</code> in a mountain array looks like <code>[True, True, True, ..., True, False, False, ..., False]</code>: 1 or more boolean <code>True</code>s, followed by 1 or more boolean <code>False</code>.  For example, in the mountain array <code>[1, 2, 3, 4, 1]</code>, the comparisons <code>A[i] &lt; A[i+1]</code> would be <code>True, True, True, False</code>.</p>
<p>We can binary search over this array of comparisons, to find the largest index <code>i</code> such that <code>A[i] &lt; A[i+1]</code>.  For more on <em>binary search</em>, see the <a href="https://leetcode.com/explore/learn/card/binary-search/">LeetCode explore topic here.</a></p>
<iframe src="https://leetcode.com/playground/FoZ3SCRk/shared" frameborder="0" width="100%" height="276" name="FoZ3SCRk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>