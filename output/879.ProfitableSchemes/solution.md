<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>We don't care about the profit of the scheme if it is <script type="math/tex; mode=display">\geq P</script>, because it surely will be over the threshold of profitability required.  Similarly, we don't care about the number of people required in the scheme if it is <script type="math/tex; mode=display">> G</script>, since we know the scheme will be too big for the gang to execute.</p>
<p>As a result, the bounds are small enough to use dynamic programming.  Let's keep track of <code>cur[p][g]</code>, the number of schemes with profitability <script type="math/tex; mode=display">p</script> and requiring <script type="math/tex; mode=display">g</script> gang members: except we'll say (without changing the answer) that all schemes that profit <em>at least</em> <code>P</code> dollars will instead profit <em>exactly</em> <code>P</code> dollars.</p>
<p><strong>Algorithm</strong></p>
<p>Keeping track of <code>cur[p][g]</code> as defined above, let's understand how it changes as we consider 1 extra crime that will profit <code>p0</code> and require <code>g0</code> gang members.  We will put the updated counts into <code>cur2</code>.</p>
<p>For each possible scheme with profit <code>p1</code> and group size <code>g1</code>, that scheme plus the extra crime (<code>p0, g0</code>) being considered, has a profit of <code>p2 = min(p1 + p0, P)</code>, and uses a group size of <code>g2 = g1 + g0</code>.</p>
<iframe src="https://leetcode.com/playground/gFHdtSWS/shared" frameborder="0" width="100%" height="500" name="gFHdtSWS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N * P * G)</script>, where <script type="math/tex; mode=display">N</script> is the number of crimes available to the gang.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(P * G)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>