<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-pointers">Approach 1: Two Pointers</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-pointers">Approach 1: Two Pointers</h4>
<p><strong>Algorithm</strong></p>
<p>Since the array is already sorted, we can keep two pointers <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script>, where <script type="math/tex; mode=display">i</script> is the slow-runner while <script type="math/tex; mode=display">j</script> is the fast-runner. As long as <script type="math/tex; mode=display">nums[i] = nums[j]</script>, we increment <script type="math/tex; mode=display">j</script> to skip the duplicate.</p>
<p>When we encounter <script type="math/tex; mode=display">nums[j] \neq nums[i]</script>, the duplicate run has ended so we must copy its value to <script type="math/tex; mode=display">nums[i + 1]</script>. <script type="math/tex; mode=display">i</script> is then incremented and we repeat the same process again until <script type="math/tex; mode=display">j</script> reaches the end of array.</p>
<iframe src="https://leetcode.com/playground/p8jPfpcx/shared" frameborder="0" width="100%" height="242" name="p8jPfpcx"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complextiy : <script type="math/tex; mode=display">O(n)</script>.
Assume that <script type="math/tex; mode=display">n</script> is the length of array. Each of <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> traverses at most <script type="math/tex; mode=display">n</script> steps.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>