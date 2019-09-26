<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-single-scan-accepted">Approach #1 Single Scan [Accepted]</a></li>
<li><a href="#approach-2-optimized-accepted">Approach #2 Optimized [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-single-scan-accepted">Approach #1 Single Scan [Accepted]</h4>
<p>The solution is very simple. We can find out the extra maximum number of flowers, <script type="math/tex; mode=display">count</script>, that can be planted for the given <script type="math/tex; mode=display">flowerbed</script> arrangement. To do so, we can traverse over all the elements of the <script type="math/tex; mode=display">flowerbed</script> and find out those elements which are 0(implying an empty position). For every such element, we check if its both adjacent positions are also empty. If so, we can plant a flower at the current position without violating the no-adjacent-flowers-rule. For the first and last elements, we need not check the previous and the next adjacent positions respectively.</p>
<p>If the <script type="math/tex; mode=display">count</script> obtained is greater than or equal to <script type="math/tex; mode=display">n</script>, the required number of flowers to be planted, we can plant <script type="math/tex; mode=display">n</script> flowers in the empty spaces, otherwise not.</p>
<iframe src="https://leetcode.com/playground/Dbm5A5CN/shared" frameborder="0" name="Dbm5A5CN" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. A single scan of the <script type="math/tex; mode=display">flowerbed</script> array of size <script type="math/tex; mode=display">n</script> is done.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-optimized-accepted">Approach #2 Optimized [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of finding the maximum value of <script type="math/tex; mode=display">count</script> that can be obtained, as done in the last approach, we can stop the process of checking the positions for planting the flowers as soon as <script type="math/tex; mode=display">count</script> becomes equal to <script type="math/tex; mode=display">n</script>. Doing this leads to an optimization of the first approach. If <script type="math/tex; mode=display">count</script> never becomes equal to <script type="math/tex; mode=display">n</script>, <script type="math/tex; mode=display">n</script> flowers can't be planted at the empty positions.</p>
<iframe src="https://leetcode.com/playground/GtCBiouS/shared" frameborder="0" name="GtCBiouS" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. A single scan of the <script type="math/tex; mode=display">flowerbed</script> array of size <script type="math/tex; mode=display">n</script> is done.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>