<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort">Approach 1: Sort</a></li>
<li><a href="#approach-2-two-pointer">Approach 2: Two Pointer</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort">Approach 1: Sort</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Create an array of the squares of each element, and sort them.</p>
<iframe src="https://leetcode.com/playground/mVRPMKjB/shared" frameborder="0" width="100%" height="242" name="mVRPMKjB"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pointer">Approach 2: Two Pointer</h4>
<p><strong>Intuition</strong></p>
<p>Since the array <code>A</code> is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.</p>
<p>For example, with <code>[-3, -2, -1, 4, 5, 6]</code>, we have the negative part <code>[-3, -2, -1]</code> with squares <code>[9, 4, 1]</code>, and the positive part <code>[4, 5, 6]</code> with squares <code>[16, 25, 36]</code>.  Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.</p>
<p><strong>Algorithm</strong></p>
<p>We can use two pointers to read the positive and negative parts of the array - one pointer <code>j</code> in the positive direction, and another <code>i</code> in the negative direction.</p>
<p>Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.</p>
<iframe src="https://leetcode.com/playground/h7YnwCLs/shared" frameborder="0" width="100%" height="500" name="h7YnwCLs"></iframe>

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
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>