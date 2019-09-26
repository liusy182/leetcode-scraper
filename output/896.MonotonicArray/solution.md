<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-pass">Approach 1: Two Pass</a></li>
<li><a href="#approach-2-one-pass">Approach 2: One Pass</a></li>
<li><a href="#approach-3-one-pass-simple-variant">Approach 3: One Pass (Simple Variant)</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-pass">Approach 1: Two Pass</h4>
<p><strong>Intuition</strong></p>
<p>An array is <em>monotonic</em> if it is monotone increasing, or monotone decreasing.  Since <code>a &lt;= b</code> and <code>b &lt;= c</code> implies <code>a &lt;= c</code>, we only need to check adjacent elements to determine if the array is monotone increasing (or decreasing, respectively).  We can check each of these properties in one pass.</p>
<p><strong>Algorithm</strong></p>
<p>To check whether an array <code>A</code> is monotone increasing, we'll check <code>A[i] &lt;= A[i+1]</code> for all <code>i</code>.  The check for monotone decreasing is similar.</p>
<iframe src="https://leetcode.com/playground/45YrvCAw/shared" frameborder="0" width="100%" height="344" name="45YrvCAw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-one-pass">Approach 2: One Pass</h4>
<p><strong>Intuition</strong></p>
<p>To perform this check in one pass, we want to handle a stream of comparisons from <script type="math/tex; mode=display">\{-1, 0, 1\}</script>, corresponding to <code>&lt;</code>, <code>==</code>, or <code>&gt;</code>.  For example, with the array <code>[1, 2, 2, 3, 0]</code>, we will see the stream <code>(-1, 0, -1, 1)</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Keep track of <code>store</code>, equal to the first non-zero comparison seen (if it exists.)  If we see the opposite comparison, the answer is <code>False</code>.</p>
<p>Otherwise, every comparison was (necessarily) in the set <script type="math/tex; mode=display">\{-1, 0\}</script>, or every comparison was in the set <script type="math/tex; mode=display">\{0, 1\}</script>, and therefore the array is monotonic.</p>
<iframe src="https://leetcode.com/playground/qcBYT2JK/shared" frameborder="0" width="100%" height="310" name="qcBYT2JK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-one-pass-simple-variant">Approach 3: One Pass (Simple Variant)</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>To perform this check in one pass, we want to remember if it is monotone increasing or monotone decreasing.</p>
<p>It's monotone increasing if there aren't some adjacent values <code>A[i], A[i+1]</code> with <code>A[i] &gt; A[i+1]</code>, and similarly for monotone decreasing.</p>
<p>If it is either monotone increasing or monotone decreasing, then <code>A</code> is monotonic.</p>
<iframe src="https://leetcode.com/playground/FnWYKTw8/shared" frameborder="0" width="100%" height="293" name="FnWYKTw8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
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