<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-breadth-first-search">Approach 1: Breadth-First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-breadth-first-search">Approach 1: Breadth-First Search</h4>
<p><strong>Intuition</strong></p>
<p>Every turn, the rotting spreads from each rotting orange to other adjacent oranges.  Initially, the rotten oranges have 'depth' 0 [as in the spanning tree of a graph], and every time they rot a neighbor, the neighbors have 1 more depth.  We want to know the largest possible depth.</p>
<p><strong>Algorithm</strong></p>
<p>We can use a breadth-first search to model this process.  Because we always explore nodes (oranges) with the smallest depth first, we're guaranteed that each orange that becomes rotten does so with the lowest possible depth number.</p>
<p>We should also check that at the end, there are no fresh oranges left.</p>
<iframe src="https://leetcode.com/playground/8S5VkeTc/shared" frameborder="0" width="100%" height="500" name="8S5VkeTc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of cells in the grid.</p>
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