<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-single-pass-accepted">Approach #2 Single Pass [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p>The simplest method is to create a actual 2-D array of size <script type="math/tex; mode=display">m</script>x<script type="math/tex; mode=display">n</script>(<script type="math/tex; mode=display">arr</script>), perform all the operations one by one on the given range of elements, and then count the number of maximum elements. Now, we know that all the operations performed always include the element at index <script type="math/tex; mode=display">(0,0)</script>. Thus, the element <script type="math/tex; mode=display">arr[0][0]</script> will always be the maximum. After performing all the operations, we can count the number of elements equal to <script type="math/tex; mode=display">arr[0][0]</script> to get the required count of the maximum elements.</p>
<iframe src="https://leetcode.com/playground/awQVAxR8/shared" frameborder="0" name="awQVAxR8" width="100%" height="411"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(x*m*n)</script>. Array is updated <script type="math/tex; mode=display">x</script> times, where <script type="math/tex; mode=display">x</script> represents number of times operation is preformed i.e. <script type="math/tex; mode=display">ops.length</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. Array of size <script type="math/tex; mode=display">m*n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-single-pass-accepted">Approach #2 Single Pass [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>As per the given problem statement, all the operations are performed on a rectangular sub-matrix of the initial all 0's <script type="math/tex; mode=display">M</script> matrix. The upper left corner of each such rectangle is given by the index <script type="math/tex; mode=display">(0, 0)</script> and the lower right corner for an operation <script type="math/tex; mode=display">[i, j]</script> is given by the index <script type="math/tex; mode=display">(i, j)</script>. </p>
<p>The maximum element will be the one on which all the operations have been performed. The figure below shows an example of two operations being performed on the initial <script type="math/tex; mode=display">M</script> array. </p>
<p><img alt="Range_Addition" src="../Figures/598_Range_Addition2.PNG"></p>
<p>From this figure, we can observe that the maximum elements will be the ones which lie in the intersection region of the rectangles representing the operations. Further, we can observe that to count the number of elements lying in this intersection region, we don't actually need to perform the operations, but we need to determine the lower right cornerof the intersecting region only. This corner is given by <script type="math/tex; mode=display">\big(x, y\big) = \big(\text{min}(op[0], \text{min}(op[1])\big)</script>, where <script type="math/tex; mode=display">\text{min}(op[i])</script> reprsents the minimum value of <script type="math/tex; mode=display">op[i]</script> from among all the <script type="math/tex; mode=display">op[i]</script>'s in the given set of operations.</p>
<p>Thus, the resultant count of elements lying in the intersection is given by: <script type="math/tex; mode=display">x</script>x<script type="math/tex; mode=display">y</script>.</p>
<iframe src="https://leetcode.com/playground/eUWGJ45b/shared" frameborder="0" name="eUWGJ45b" width="100%" height="224"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(x)</script>. Single traversal of all operations is done. <script type="math/tex; mode=display">x</script> refers to the number of operations.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>