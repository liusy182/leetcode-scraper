<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sliding-window">Approach 1: Sliding Window</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sliding-window">Approach 1: Sliding Window</h4>
<p><strong>Intuition</strong></p>
<p>For convenience, let's denote subarrays by tuples: <code>(i,j) = [A[i], A[i+1], ..., A[j]]</code>, and call a subarray <em>valid</em> if it has <code>K</code> different integers.</p>
<p>For each <code>j</code>, let's consider the set <script type="math/tex; mode=display">S_j</script> of all <code>i</code> such that the subarray <code>(i, j)</code> is valid.</p>
<p>Firstly, <script type="math/tex; mode=display">S_j</script> must be a contiguous interval.  If <code>i1 &lt; i2 &lt; i3</code>, <code>(i1,j)</code> and <code>(i3,j)</code> are valid, but <code>(i2,j)</code> is not valid, this is a contradiction because <code>(i2,j)</code> must contain more than <code>K</code> different elements [as <code>(i3,j)</code> contains <code>K</code>], but <code>(i1,j)</code> [which is a superset of <code>(i2,j)</code>] only contains <code>K</code> different integers.</p>
<p>So now let's write <script type="math/tex; mode=display">S_j</script> as intervals: <script type="math/tex; mode=display">S_j = [\text{left1}_j, \text{left2}_j]</script>.</p>
<p>The second observation is that the endpoints of these intervals must be monotone increeasing - namely, <script type="math/tex; mode=display">\text{left1}_j</script> and <script type="math/tex; mode=display">\text{left2}_j</script> are monotone increasing.  With similar logic to the above, we could construct a proof of this fact, but the intuition is that after adding an extra element to our subarrays, they are already valid, or we need to shrink them a bit to keep them valid.</p>
<p><strong>Algorithm</strong></p>
<p>We'll maintain two sliding windows, corresponding to <script type="math/tex; mode=display">\text{left1}_j</script> and <script type="math/tex; mode=display">\text{left2}_j</script>.  Each sliding window will be able to count how many different elements there are in the window, and add and remove elements in a queue-like fashion.</p>
<iframe src="https://leetcode.com/playground/MkaZoDQt/shared" frameborder="0" width="100%" height="500" name="MkaZoDQt"></iframe>

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