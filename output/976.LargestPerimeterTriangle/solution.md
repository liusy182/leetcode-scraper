<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort">Approach 1: Sort</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort">Approach 1: Sort</h4>
<p><strong>Intuition</strong></p>
<p>Without loss of generality, say the sidelengths of the triangle are <script type="math/tex; mode=display">a \leq b \leq c</script>.  The necessary and sufficient condition for these lengths to form a triangle of non-zero area is <script type="math/tex; mode=display">a + b > c</script>.</p>
<p>Say we knew <script type="math/tex; mode=display">c</script> already.  There is no reason not to choose the largest possible <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> from the array.  If <script type="math/tex; mode=display">a + b > c</script>, then it forms a triangle, otherwise it doesn't.</p>
<p><strong>Algorithm</strong></p>
<p>This leads to a simple algorithm:  Sort the array.  For any <script type="math/tex; mode=display">c</script> in the array, we choose the largest possible <script type="math/tex; mode=display">a \leq b \leq c</script>:  these are just the two values adjacent to <script type="math/tex; mode=display">c</script>.  If this forms a triangle, we return the answer.</p>
<iframe src="https://leetcode.com/playground/2RjnrKEg/shared" frameborder="0" width="100%" height="208" name="2RjnrKEg"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
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