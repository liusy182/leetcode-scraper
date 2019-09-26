<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-simulation-accepted">Approach #1: Simulation [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-simulation-accepted">Approach #1: Simulation [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's work on simulating one turn of the process.  We can repeat this as necessary while there are still infected regions.</p>
<p><strong>Algorithm</strong></p>
<p>Though the implementation is long, the algorithm is straightforward.  We perform the following steps:</p>
<ul>
<li>
<p>Find all viral regions (connected components), additionally for each region keeping track of the frontier (neighboring uncontaminated cells), and the perimeter of the region.</p>
</li>
<li>
<p>Disinfect the most viral region, adding it's perimeter to the answer.</p>
</li>
<li>
<p>Spread the virus in the remaining regions outward by 1 square.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/VFSzJzRe/shared" frameborder="0" width="100%" height="500" name="VFSzJzRe"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O((R*C)^{\frac{4}{3}})</script> where <script type="math/tex; mode=display">R, C</script> is the number of rows and columns.  After time <script type="math/tex; mode=display">t</script>, viral regions that are alive must have size at least <script type="math/tex; mode=display">t^2 + (t-1)^2</script>, so the total number removed across all time is <script type="math/tex; mode=display">\Omega(t^3) \leq R*C</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(R*C)</script> in additional space.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>