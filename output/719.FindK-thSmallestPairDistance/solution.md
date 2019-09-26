<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-heap-time-limit-exceeded">Approach #1: Heap [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-binary-search-prefix-sum-accepted">Approach #2: Binary Search + Prefix Sum [Accepted]</a></li>
<li><a href="#approach-3-binary-search-sliding-window-accepted">Approach #3: Binary Search + Sliding Window [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-heap-time-limit-exceeded">Approach #1: Heap [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Sort the points.  For every point with index <code>i</code>, the pairs with indexes <code>(i, j)</code> [by order of distance] are <code>(i, i+1), (i, i+2), ..., (i, N-1)</code>.</p>
<p>Let's keep a heap of pairs, initially <code>heap = [(i, i+1) for all i]</code>, and ordered by distance (the distance of <code>(i, j)</code> is <code>nums[j] - nums[i]</code>.)  Whenever we use a pair <code>(i, x)</code> from our heap, we will add <code>(i, x+1)</code> to our heap when appropriate.</p>
<iframe src="https://leetcode.com/playground/haWM6KvQ/shared" frameborder="0" width="100%" height="500" name="haWM6KvQ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O((k+N) \log{N})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  As <script type="math/tex; mode=display">k = O(N^2)</script>, this is <script type="math/tex; mode=display">O(N^2 \log {N})</script> in the worst case.  The complexity added by our heap operations is either <script type="math/tex; mode=display">O((k+N) \log N)</script> in the Java solution, or <script type="math/tex; mode=display">O(k \log{N} + N)</script> in the Python solution because the <code>heapq.heapify</code> operation is linear time.  Additionally, we add <script type="math/tex; mode=display">O(N \log N)</script> complexity due to sorting.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used to store our <code>heap</code> of at most <code>N-1</code> elements.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-binary-search-prefix-sum-accepted">Approach #2: Binary Search + Prefix Sum [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's binary search for the answer.  It's definitely in the range <code>[0, W]</code>, where <code>W = max(nums) - min(nums)]</code>.  </p>
<p>Let <code>possible(guess)</code> be true if and only if there are <code>k</code> or more pairs with distance less than or equal to <code>guess</code>.  We will focus on evaluating our <code>possible</code> function quickly.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>prefix[v]</code> be the number of points in <code>nums</code> less than or equal to <code>v</code>.  Also, let <code>multiplicity[j]</code> be the number of points <code>i</code> with <code>i &lt; j and nums[i] == nums[j]</code>.  We can record both of these with a simple linear scan.</p>
<p>Now, for every point <code>i</code>, the number of points <code>j</code> with <code>i &lt; j</code> and <code>nums[j] - nums[i] &lt;= guess</code> is <code>prefix[x+guess] - prefix[x] + (count[i] - multiplicity[i])</code>, where <code>count[i]</code> is the number of ocurrences of <code>nums[i]</code> in <code>nums</code>.  The sum of this over all <code>i</code> is the number of pairs with distance <code>&lt;= guess</code>.  </p>
<p>Finally, because the sum of <code>count[i] - multiplicity[i]</code> is the same as the sum of <code>multiplicity[i]</code>, we could just replace that term with <code>multiplicity[i]</code> without affecting the answer.  (Actually, the sum of multiplicities in total will be a constant used in the answer, so we could precalculate it if we wanted.)</p>
<p>In our Java solution, we computed <code>possible = count &gt;= k</code> directly in the binary search instead of using a helper function.</p>
<iframe src="https://leetcode.com/playground/upbfbVHa/shared" frameborder="0" width="100%" height="500" name="upbfbVHa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(W + N \log{W} + N \log{N})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>, and <script type="math/tex; mode=display">W</script> is equal to <code>nums[nums.length - 1] - nums[0]</code>.  We do <script type="math/tex; mode=display">O(W)</script> work to calculate <code>prefix</code> initially.  The <script type="math/tex; mode=display">\log W</script> factor comes from our binary search, and we do <script type="math/tex; mode=display">O(N)</script> work inside our call to <code>possible</code> (or to calculate <code>count</code> in Java).  The final <script type="math/tex; mode=display">O(N\log N)</script> factor comes from sorting.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N+W)</script>, the space used to store <code>multiplicity</code> and <code>prefix</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-binary-search-sliding-window-accepted">Approach #3: Binary Search + Sliding Window [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #2</em>, let's binary search for the answer, and we will focus on evaluating our <code>possible</code> function quickly.</p>
<p><strong>Algorithm</strong></p>
<p>We will use a sliding window approach to count the number of pairs with distance <code>&lt;=</code> guess.  </p>
<p>For every possible <code>right</code>, we maintain the loop invariant: <code>left</code> is the smallest value such that <code>nums[right] - nums[left] &lt;= guess</code>.  Then, the number of pairs with <code>right</code> as it's right-most endpoint is <code>right - left</code>, and we add all of these up.</p>
<iframe src="https://leetcode.com/playground/UD6QK4gU/shared" frameborder="0" width="100%" height="429" name="UD6QK4gU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N \log{W} + N \log{N})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>, and <script type="math/tex; mode=display">W</script> is equal to <code>nums[nums.length - 1] - nums[0]</code>.  The <script type="math/tex; mode=display">\log W</script> factor comes from our binary search, and we do <script type="math/tex; mode=display">O(N)</script> work inside our call to <code>possible</code> (or to calculate <code>count</code> in Java).  The final <script type="math/tex; mode=display">O(N\log N)</script> factor comes from sorting.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.  No additional space is used except for integer variables.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>