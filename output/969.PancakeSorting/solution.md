<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort-largest-to-smallest">Approach 1: Sort Largest to Smallest</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort-largest-to-smallest">Approach 1: Sort Largest to Smallest</h4>
<p><strong>Intuition</strong></p>
<p>We can place the largest element (in location <code>i</code>, 1-indexed) by flipping <code>i</code> to move the element to the first position, then <code>A.length</code> to move it to the last position.  Afterwards, the largest element is in the correct position, so we no longer need to pancake-flip by <code>A.length</code> or more.</p>
<p>We can repeat this process until the array is sorted.  Each move will use 2 flips per element.</p>
<p><strong>Algorithm</strong></p>
<p>First, sort the locations from largest value of A to smallest value of A.</p>
<p>For each element (from largest to smallest) with location <code>i</code>, we will first simulate where this element actually is, based on the pancake flips we have done.  For a pancake flip <code>f</code>, if <code>i &lt;= f</code>, then the element has moved from location <code>i</code> to <code>f+1 - i</code>.</p>
<p>After, we flip by <code>i</code> then <code>N--</code> to put this element in the correct position.</p>
<iframe src="https://leetcode.com/playground/kQvhoWDb/shared" frameborder="0" width="100%" height="412" name="kQvhoWDb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
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