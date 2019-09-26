<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-sliding-window-accepted">Approach #1: Sliding Window [Accepted]</a></li>
<li><a href="#approach-2-sorted-count-pairs-accepted">Approach #2: Sorted Count Pairs [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-sliding-window-accepted">Approach #1: Sliding Window [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to find the smallest left-most chunk.</p>
<p><strong>Algorithm</strong></p>
<p>Notice that if <script type="math/tex; mode=display">a_1, a_2, \dots, a_m</script> is a chunk, and <script type="math/tex; mode=display">a_1, a_2, \dots, a_n</script> is a chunk (<script type="math/tex; mode=display">m < n</script>), then <script type="math/tex; mode=display">a_{m+1}, a_{m+2}, \dots, a_n</script> is a chunk too.  This shows that a greedy approach produces the highest number of chunks.</p>
<p>We know the array <code>arr</code> should end up like <code>expect = sorted(arr)</code>.  If the count of the first <code>k</code> elements minus the count what those elements should be is zero everywhere, then the first <code>k</code> elements form a valid chunk.  We repeatedly perform this process.</p>
<p>We can use a variable <code>nonzero</code> to count the number of letters where the current count is non-zero.</p>
<iframe src="https://leetcode.com/playground/B8GKxQrY/shared" frameborder="0" width="100%" height="480" name="B8GKxQrY"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>arr</code></p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-sorted-count-pairs-accepted">Approach #2: Sorted Count Pairs [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, let's try to find the smallest left-most chunk, where we have some expectation <code>expect = sorted(arr)</code></p>
<p>If the elements were distinct, then it is enough to find the smallest <code>k</code> with <code>max(arr[:k+1]) == expect[k]</code>, as this must mean the elements of <code>arr[:k+1]</code> are some permutation of <code>expect[:k+1]</code>.</p>
<p>Since the elements are not distinct, this fails; but we can amend the cumulative multiplicity of each element to itself to make the elements distinct.</p>
<p><strong>Algorithm</strong></p>
<p>Instead of elements <code>x</code>, have counted elements <code>(x, count)</code> where <code>count</code> ranges from <code>1</code> to the total number of <code>x</code> present in <code>arr</code>.</p>
<p>Now <code>cur</code> will be the cumulative maximum of <code>counted[:k+1]</code>, where we expect a result of <code>Y = expect[k]</code>.  We count the number of times they are equal.</p>
<iframe src="https://leetcode.com/playground/jLmjinpa/shared" frameborder="0" width="100%" height="500" name="jLmjinpa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>arr</code></p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>