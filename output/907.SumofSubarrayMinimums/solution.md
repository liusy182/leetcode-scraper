<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-prevnext-array">Approach 1: Prev/Next Array</a></li>
<li><a href="#approach-2-maintain-stack-of-minimums">Approach 2: Maintain Stack of Minimums</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-prevnext-array">Approach 1: Prev/Next Array</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to count the number of subarrays <code>#(j)</code> for which <code>A[j]</code> is the <em>right-most</em> minimum.  Then, the answer will be <code>sum #(j) * A[j]</code>.  (We must say <em>right-most</em> so that we form disjoint sets of subarrays and do not double count any, as the minimum of an array may not be unique.)</p>
<p>This in turn brings us the question of knowing the smallest index <code>i &lt;= j</code> for which <code>A[i], A[i+1], ..., A[j]</code> are all <code>&gt;= A[j]</code>; and the largest index <code>k &gt;= j</code> for which <code>A[j+1], A[j+2], ..., A[k]</code> are all <code>&gt; A[j]</code>.</p>
<p><strong>Algorithm</strong></p>
<p>For example, if <code>A = [10, 3, 4, 5, _3_, 2, 3, 10]</code> and we would like to know <code>#(j = 4)</code> [the count of the second <code>3</code>, which is marked], we would find <code>i = 1</code> and <code>k = 5</code>.</p>
<p>From there, the actual count is <code>#(j) = (j - i + 1) * (k - j + 1)</code>, as there are <code>j - i + 1</code> choices <code>i, i+1, ..., j</code> for the left index of the subarray, and <code>k - j + 1</code> choices <code>j, j+1, ..., k</code> for the right index of the subarray.</p>
<p>Answering these queries (ie. determining <code>(i, k)</code> given <code>j</code>) is a classic problem that can be answered with a stack.  We'll focus on the problem of finding <code>i</code>: the problem of finding <code>k</code> is similar.</p>
<p><strong>Making a Prev Array</strong></p>
<p>The idea is to maintain <code>stack</code>, a monotone decreasing subsequence of <code>A</code> (actually, indices of <code>A</code> in implementation).  These represent candidate boundaries <code>i* - 1</code> for the next query, stored in increasing order of <code>A[i*]</code>.</p>
<p>Now considering <code>j</code> in increasing order, we can remove candidates for which <code>A[i*] &lt;= A[j]</code> in decreasing order of <code>i*</code>.</p>
<p>For example, if <code>A = [10, 5, 3, 7, 0, 4, 5, 2, 1, _8_]</code>, then when considering <code>j = 9</code> <code>(A[j] = 8)</code>, we have a stack of boundaries like <code>[-1, 0, 3, 6]</code> (representing <code>A[i*] = -inf, 10, 7, 5</code>).  We pop <code>6</code> and <code>3</code> from the stack, as <code>5 &lt;= 8</code> and <code>7 &lt;= 8</code>, and we get the answer boundary <code>i* - 1 = 0</code>.</p>
<p>Note that this process is linear, since we do a linear amount of pushes and pops of the stack in total.</p>
<p>This is quite difficult to figure out, but this type of technique occurs often in many other problems, so it is worth learning in detail.</p>
<iframe src="https://leetcode.com/playground/CMceXvyZ/shared" frameborder="0" width="100%" height="500" name="CMceXvyZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-maintain-stack-of-minimums">Approach 2: Maintain Stack of Minimums</h4>
<p><strong>Intuition</strong></p>
<p>For a specific <code>j</code>, let's try to count the minimum of each subarray <code>[i, j]</code>.  The intuition is that as we increment <code>j++</code>, these minimums may be related to each other.  Indeed, <code>min(A[i:j+1]) = min(A[i:j], A[j])</code>.</p>
<p>Playing with some array like <code>A = [1,7,5,2,4,3,9]</code>, with <code>j = 6</code> the minimum of each subarray <code>[i, j]</code> is <code>B = [1,2,2,2,3,3,9]</code>.   We can see that there are critical points <code>i = 0, i = 3, i = 5, i = 6</code> where a minimum is reached for the first time when walking left from <code>j</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's try to maintain an RLE (run length encoding) of these critical points <code>B</code>.  More specifically, for the above <code>(A, j)</code>, we will maintain <code>stack = [(val=1, count=1), (val=2, count=3), (val=3, count=2), (val=9, count=1)]</code>, that represents a run length encoding of the subarray minimums <code>B = [1,2,2,2,3,3,9]</code>.  For each <code>j</code>, we want <code>sum(B)</code>.  </p>
<p>As we increment <code>j</code>, we will have to update this stack to include the newest element <code>(val=x, count=1)</code>.  We need to pop off all values <code>&gt;= x</code> before, as the minimum of the associated subarray <code>[i, j]</code> will now be <code>A[j]</code> instead of what it was before.</p>
<p>At the end, the answer is the dot product of this stack: <script type="math/tex; mode=display">\sum\limits_{e\text{ } \in \text{ stack}} e\text{.val} * e\text{.count}</script>, which we also maintain on the side as the variable <code>dot</code>.</p>
<iframe src="https://leetcode.com/playground/yoG86DGx/shared" frameborder="0" width="100%" height="500" name="yoG86DGx"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approach 2 inspired by <a href="https://leetcode.com/aakarshmadhavan">@aakarshmadhavan</a>.</p>
          </div>
        
      </div>