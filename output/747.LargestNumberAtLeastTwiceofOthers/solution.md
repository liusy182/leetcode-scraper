<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-linear-scan-accepted">Approach #1: Linear Scan [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-linear-scan-accepted">Approach #1: Linear Scan [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Scan through the array to find the unique largest element <code>m</code>, keeping track of it's index <code>maxIndex</code>.</p>
<p>Scan through the array again.  If we find some <code>x != m</code> with <code>m &lt; 2*x</code>, we should return <code>-1</code>.</p>
<p>Otherwise, we should return <code>maxIndex</code>.</p>
<iframe src="https://leetcode.com/playground/j3xuZ4yh/shared" frameborder="0" width="100%" height="293" name="j3xuZ4yh"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by our <code>int</code> variables.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>