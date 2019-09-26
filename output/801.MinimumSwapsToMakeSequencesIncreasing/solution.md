<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The cost of making both sequences increasing up to the first <code>i</code> columns can be expressed in terms of the cost of making both sequences increasing up to the first <code>i-1</code> columns.  This is because the only thing that matters to the <code>i</code>th column is whether the previous column was swapped or not.  This makes dynamic programming an ideal choice.</p>
<p>Let's remember <code>n1</code> (<code>natural1</code>), the cost of making the first <code>i-1</code> columns increasing and not swapping the <code>i-1</code>th column; and <code>s1</code> (<code>swapped1</code>), the cost of making the first <code>i-1</code> columns increasing and swapping the <code>i-1</code>th column.</p>
<p>Now we want candidates <code>n2</code> (and <code>s2</code>), the costs of making the first <code>i</code> columns increasing if we do not swap (or swap, respectively) the <code>i</code>th column.</p>
<p><strong>Algorithm</strong></p>
<p>For convenience, say <code>a1 = A[i-1], b1 = B[i-1]</code> and <code>a2 = A[i], b2 = B[i]</code>.</p>
<p>Now, if <code>a1 &lt; a2</code> and <code>b1 &lt; b2</code>, then it is allowed to have both of these columns natural (unswapped), or both of these columns swapped.  This possibility leads to <code>n2 = min(n2, n1)</code> and <code>s2 = min(s2, s1 + 1)</code>.</p>
<p>Another, (not exclusive) possibility is that <code>a1 &lt; b2</code> and <code>b1 &lt; a2</code>.  This means that it is allowed to have exactly one of these columns swapped.  This possibility leads to <code>n2 = min(n2, s1)</code> or <code>s2 = min(s2, n1 + 1)</code>.</p>
<p>Note that it is important to use two if statements separately, because both of the above possibilities might be possible.</p>
<p>At the end, the optimal solution must leave the last column either natural or swapped, so we take the minimum number of swaps between the two possibilities.</p>
<iframe src="https://leetcode.com/playground/KT3yuKkz/shared" frameborder="0" width="100%" height="395" name="KT3yuKkz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>