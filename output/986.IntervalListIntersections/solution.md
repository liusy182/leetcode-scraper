<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-merge-intervals">Approach 1: Merge Intervals</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-merge-intervals">Approach 1: Merge Intervals</h4>
<p><strong>Intuition</strong></p>
<p>In an interval <code>[a, b]</code>, call <code>b</code> the "endpoint".</p>
<p>Among the given intervals, consider the interval <code>A[0]</code> with the smallest endpoint.  (Without loss of generality, this interval occurs in array <code>A</code>.)</p>
<p>Then, among the intervals in array <code>B</code>, <code>A[0]</code> can only intersect one such interval in array <code>B</code>.  (If two intervals in <code>B</code> intersect <code>A[0]</code>, then they both share the endpoint of <code>A[0]</code> -- but intervals in <code>B</code> are disjoint, which is a contradiction.)</p>
<p><strong>Algorithm</strong></p>
<p>If <code>A[0]</code> has the smallest endpoint, it can only intersect <code>B[0]</code>.  After, we can discard <code>A[0]</code> since it cannot intersect anything else.</p>
<p>Similarly, if <code>B[0]</code> has the smallest endpoint, it can only intersect <code>A[0]</code>, and we can discard <code>B[0]</code> after since it cannot intersect anything else.</p>
<p>We use two pointers, <code>i</code> and <code>j</code>, to virtually manage "discarding" <code>A[0]</code> or <code>B[0]</code> repeatedly.</p>
<iframe src="https://leetcode.com/playground/ZoFMccAy/shared" frameborder="0" width="100%" height="463" name="ZoFMccAy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(M + N)</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>A</code> and <code>B</code> respectively.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(M + N)</script>, the maximum size of the answer.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>