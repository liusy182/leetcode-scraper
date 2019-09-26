<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-reverse-time-and-union-find-accepted">Approach #1: Reverse Time and Union-Find [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-reverse-time-and-union-find-accepted">Approach #1: Reverse Time and Union-Find [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The problem is about knowing information about the connected components of a graph as we cut vertices.  In particular, we'll like to know the size of the "roof" (component touching the top edge) between each cut.  Here, a cut refers to the erasure of a vertex.</p>
<p>As we may know, a useful data structure for joining connected components is a disjoint set union structure.  The key idea in this problem is that we can use this structure if we work in reverse: instead of looking at the graph as a series of sequential cuts, we'll look at the graph after all the cuts, and reverse each cut.</p>
<p><strong>Algorithm</strong></p>
<p>We'll modify our typical disjoint-set-union structure to include a <code>dsu.size</code> operation, that tells us the size of this component.  The way we do this is whenever we make a component point to a new parent, we'll also send it's size to that parent.</p>
<p>We'll also include <code>dsu.top</code>, which tells us the size of the "roof", or the component connected to the top edge.  We use an <em>ephemeral</em> "source" node with label <code>R * C</code> where all nodes on the top edge (with row number <code>0</code>) are connected to the source node.</p>
<p>For more information on DSU, please look at <em>Approach #2</em> in the <a href="https://leetcode.com/articles/redundant-connection/">article here</a>.</p>
<p>Next, we'll introduce <code>A</code>, the grid after all the cuts have happened, and initialize our disjoint union structure on the graph induced by <code>A</code> (nodes are grid squares with a brick; edges between 4-directionally adjacent nodes).</p>
<p>After, if we get an cut at <code>(r, c)</code> but the original <code>grid[r][c]</code> was always <code>0</code>, then we couldn't have had a meaningful cut - the number of dropped bricks is <code>0</code>.</p>
<p>Otherwise, we'll look at the size of the new roof after adding this brick at <code>(r, c)</code>, and compare them to find the number of dropped bricks.</p>
<p>Since we were working in reverse time order, we should reverse our working answer to arrive at our final answer.</p>
<iframe src="https://leetcode.com/playground/vKx7cbxE/shared" frameborder="0" width="100%" height="500" name="vKx7cbxE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N*Q*\alpha(N * Q))</script>, where <script type="math/tex; mode=display">N = R*C</script> is the number of grid squares, <script type="math/tex; mode=display">Q</script> is the length of <code>hits</code>, and <script type="math/tex; mode=display">\alpha</script> is the <em>Inverse-Ackermann function</em>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>