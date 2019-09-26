<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-with-set">Approach 1: Brute Force with Set</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-with-set">Approach 1: Brute Force with Set</h4>
<p><strong>Intuition</strong></p>
<p>Every Fibonacci-like subsequence has each two adjacent terms determine the next expected term.  For example, with <code>2, 5</code>, we expect that the sequence must continue <code>7, 12, 19, 31</code>, etc.</p>
<p>We can use a <code>Set</code> structure to determine quickly whether the next term is in the array <code>A</code> or not.  Because of the exponential growth of these terms, there are at most 43 terms in any Fibonacci-like subsequence that has maximum value <script type="math/tex; mode=display">\leq 10^9</script>.</p>
<p><strong>Algorithm</strong></p>
<p>For each starting pair <code>A[i], A[j]</code>, we maintain the next expected value <code>y = A[i] + A[j]</code> and the previously seen largest value <code>x = A[j]</code>.  If <code>y</code> is in the array, then we can then update these values <code>(x, y) -&gt; (y, x+y)</code>.</p>
<p>Also, because subsequences are only fibonacci-like if they have length 3 or more, we must perform the check <code>ans &gt;= 3 ? ans : 0</code> at the end.</p>
<iframe src="https://leetcode.com/playground/HWTGNbV2/shared" frameborder="0" width="100%" height="500" name="HWTGNbV2"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2 \log M)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">M</script> is the maximum value of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by the set <code>S</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>Think of two consecutive terms <code>A[i], A[j]</code> in a fibonacci-like subsequence as a single node <code>(i, j)</code>, and the entire subsequence is a path between these consecutive nodes.  For example, with the fibonacci-like subsequence <code>(A[1] = 2, A[2] = 3, A[4] = 5, A[7] = 8, A[10] = 13)</code>, we have the path between nodes <code>(1, 2) &lt;-&gt; (2, 4) &lt;-&gt; (4, 7) &lt;-&gt; (7, 10)</code>.</p>
<p>The motivation for this is that two nodes <code>(i, j)</code> and <code>(j, k)</code> are connected if and only if <code>A[i] + A[j] == A[k]</code>, and we needed this amount of information to know about this connection.  Now we have a problem similar to <em>Longest Increasing Subsequence</em>.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>longest[i, j]</code> be the longest path ending in <code>[i, j]</code>.  Then <code>longest[j, k] = longest[i, j] + 1</code> if <code>(i, j)</code> and <code>(j, k)</code> are connected.  Since <code>i</code> is uniquely determined as <code>A.index(A[k] - A[j])</code>, this is efficient: we check for each <code>j &lt; k</code> what <code>i</code> is potentially, and update <code>longest[j, k]</code> accordingly.</p>
<iframe src="https://leetcode.com/playground/vEtztLgc/shared" frameborder="0" width="100%" height="463" name="vEtztLgc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N \log M)</script>, where <script type="math/tex; mode=display">M</script> is the largest element of <code>A</code>.  We can show that the number of elements in a subsequence is bounded by <script type="math/tex; mode=display">O(\log \frac{M}{a})</script> where <script type="math/tex; mode=display">a</script> is the minimum element in the subsequence.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>