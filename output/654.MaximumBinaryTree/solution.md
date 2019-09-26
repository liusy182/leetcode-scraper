<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursive-solution">Approach 1: Recursive Solution</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursive-solution">Approach 1: Recursive Solution</h4>
<p>The current solution is very simple. We make use of a function <code>construct(nums, l, r)</code>, which returns the maximum binary tree consisting of numbers within the indices <script type="math/tex; mode=display">l</script> and <script type="math/tex; mode=display">r</script> in the given <script type="math/tex; mode=display">nums</script> array(excluding the <script type="math/tex; mode=display">r^{th}</script> element).</p>
<p>The algorithm consists of the following steps:</p>
<ol>
<li>
<p>Start with the function call <code>construct(nums, 0, n)</code>. Here, <script type="math/tex; mode=display">n</script> refers to the number of elements in the given <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Find the index, <script type="math/tex; mode=display">max_i</script>, of the largest element in the current range of indices <script type="math/tex; mode=display">(l:r-1)</script>. Make this largest element, <script type="math/tex; mode=display">nums[max\_i]</script> as the local root node.</p>
</li>
<li>
<p>Determine the left child using <code>construct(nums, l, max_i)</code>. Doing this recursively finds the largest element in the subarray left to the current largest element.</p>
</li>
<li>
<p>Similarly, determine the right child using <code>construct(nums, max_i + 1, r)</code>.</p>
</li>
<li>
<p>Return the root node to the calling function.</p>
</li>
</ol>
<iframe src="https://leetcode.com/playground/WgEZm2za/shared" frameborder="0" width="100%" height="429" name="WgEZm2za"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. The function <code>construct</code> is called <script type="math/tex; mode=display">n</script> times. At each level of the recursive tree, we traverse over all the <script type="math/tex; mode=display">n</script> elements to find the maximum element.  In the average case, there will be a <script type="math/tex; mode=display">\log n</script> levels leading to a complexity of <script type="math/tex; mode=display">O\big(n\log n\big)</script>. In the worst case, the depth of the recursive tree can grow upto <script type="math/tex; mode=display">n</script>, which happens in the case of a sorted <script type="math/tex; mode=display">nums</script> array, giving a complexity of <script type="math/tex; mode=display">O(n^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The size of the <script type="math/tex; mode=display">set</script> can grow upto <script type="math/tex; mode=display">n</script> in the worst case. In the average case, the size will be <script type="math/tex; mode=display">\log n</script> for <script type="math/tex; mode=display">n</script> elements in <script type="math/tex; mode=display">nums</script>, giving an average case complexity of <script type="math/tex; mode=display">O(\log n)</script>
</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>