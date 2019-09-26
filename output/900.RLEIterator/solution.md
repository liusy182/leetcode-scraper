<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-store-exhausted-position-and-quantity">Approach 1: Store Exhausted Position and Quantity</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-store-exhausted-position-and-quantity">Approach 1: Store Exhausted Position and Quantity</h4>
<p><strong>Intuition</strong></p>
<p>We can store an index <code>i</code> and quantity <code>q</code> which represents that <code>q</code> elements of <code>A[i]</code> (repeated <code>A[i+1]</code> times) are exhausted.</p>
<p>For example, if we have <code>A = [1,2,3,4]</code> (mapping to the sequence <code>[2,4,4,4]</code>) then <code>i = 0, q = 0</code> represents that nothing is exhausted; <code>i = 0, q = 1</code> represents that <code>[2]</code> is exhausted, <code>i = 2, q = 1</code> will represent that we have currently exhausted <code>[2, 4]</code>, and so on.</p>
<p><strong>Algorithm</strong></p>
<p>Say we want to exhaust <code>n</code> more elements.  There are currently <code>D = A[i] - q</code> elements left to exhaust (of value <code>A[i+1]</code>).</p>
<p>If <code>n &gt; D</code>, then we should exhaust all of them and continue: <code>n -= D; i += 2; q = 0</code>.</p>
<p>Otherwise, we should exhaust some of them and return the current element's value: <code>q += D; return A[i+1]</code>.</p>
<iframe src="https://leetcode.com/playground/YThfYaPX/shared" frameborder="0" width="100%" height="480" name="YThfYaPX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + Q)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">Q</script> is the number of calls to <code>RLEIterator.next</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>