<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If a chain of length <code>k</code> ends at some <code>pairs[i]</code>, and <code>pairs[i][1] &lt; pairs[j][0]</code>, we can extend this chain to a chain of length <code>k+1</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Sort the pairs by first coordinate, and let <code>dp[i]</code> be the length of the longest chain ending at <code>pairs[i]</code>.  When <code>i &lt; j</code> and <code>pairs[i][1] &lt; pairs[j][0]</code>, we can extend the chain, and so we have the candidate answer <code>dp[j] = max(dp[j], dp[i] + 1)</code>.</p>
<iframe src="https://leetcode.com/playground/5RAj49MD/shared" frameborder="0" width="100%" height="378" name="5RAj49MD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>pairs</code>.  There are two for loops, and <script type="math/tex; mode=display">N^2</script> dominates the sorting step.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script> for sorting and to store <code>dp</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can greedily add to our chain.  Choosing the next addition to be the one with the lowest second coordinate is at least better than a choice with a larger second coordinate.</p>
<p><strong>Algorithm</strong></p>
<p>Consider the pairs in increasing order of their <em>second</em> coordinate.  We'll try to add them to our chain.  If we can, by the above argument we know that it is correct to do so.</p>
<iframe src="https://leetcode.com/playground/imd3oEYD/shared" frameborder="0" width="100%" height="242" name="imd3oEYD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N \log N)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.  The complexity comes from the sorting step, but the rest of the solution does linear work.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.  The additional space complexity of storing <code>cur</code> and <code>ans</code>, but sorting uses <script type="math/tex; mode=display">O(N)</script> space.  Depending on the implementation of the language used, sorting can sometimes use less space.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>