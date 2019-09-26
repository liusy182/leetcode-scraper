<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dfs-accepted">Approach #1: DFS [Accepted]</a></li>
<li><a href="#approach-2-union-find-accepted">Approach #2: Union-Find [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-dfs-accepted">Approach #1: DFS [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each edge <code>(u, v)</code>, traverse the graph with a depth-first search to see if we can connect <code>u</code> to <code>v</code>.  If we can, then it must be the duplicate edge.</p>
<iframe src="https://leetcode.com/playground/W7EXu5ND/shared" frameborder="0" name="W7EXu5ND" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script> where <script type="math/tex; mode=display">N</script> is the number of vertices (and also the number of edges) in the graph.  In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.  The current construction of the graph has at most <script type="math/tex; mode=display">N</script> nodes.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-union-find-accepted">Approach #2: Union-Find [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>If we are familiar with a Disjoint Set Union (DSU) data structure, we can use this in a straightforward manner to solve the problem: we simply find the first edge occurring in the graph that is already connected.  The rest of this explanation will focus on the details of implementing DSU.</p>
<p>A DSU data structure can be used to maintain knowledge of the connected components of a graph, and query for them quickly.  In particular, we would like to support two operations:</p>
<ul>
<li>
<p><code>dsu.find(node x)</code>, which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component, and:</p>
</li>
<li>
<p><code>dsu.union(node x, node y)</code>, which draws an edge <code>(x, y)</code> in the graph, connecting the components with id <code>find(x)</code> and <code>find(y)</code> together.</p>
</li>
</ul>
<p>To achieve this, we keep track of <code>parent</code>, which remembers the <code>id</code> of a smaller node in the same connected component.  If the node is it's own parent, we call this the <em>leader</em> of that connected component.</p>
<p>A naive implementation of a DSU structure would look something like this:</p>
<p><em>Psuedocode</em></p>
<iframe src="https://leetcode.com/playground/sCjT3wyq/shared" frameborder="0" name="sCjT3wyq" width="100%" height="190"></iframe>

<p>We use two techniques to improve the run-time complexity: <em>path compression</em>, and <em>union-by-rank</em>.</p>
<ul>
<li>
<p>Path compression involves changing the <code>x = parent[x]</code> in the <code>find</code> function to <code>parent[x] = find(parent[x])</code>.  Basically, as we compute the correct leader for x, we should remember our calculation.</p>
</li>
<li>
<p>Union-by-rank involves distributing the workload of <code>find</code> across leaders evenly.  Whenever we <code>dsu.union(x, y)</code>, we have two leaders <code>xr, yr</code> and we have to choose whether we want <code>parent[x] = yr</code> or <code>parent[y] = xr</code>.  We choose the leader that has a higher following to pick up a new follower.<br>
Specifically, the meaning of <code>rank</code> is that there are less than <code>2 ^ rank[x]</code> followers of <code>x</code>.  This strategy can be shown to give us better bounds for how long the recursive loop in <code>dsu.find</code> could run for.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/tFfjEuXo/shared" frameborder="0" name="tFfjEuXo" width="100%" height="515"></iframe>

<p><em>Alternate Implementation of DSU without Union-By-Rank</em>
<iframe src="https://leetcode.com/playground/DzMVxYRc/shared" frameborder="0" name="DzMVxYRc" width="100%" height="207"></iframe></p>
<iframe src="https://leetcode.com/playground/YgdvM9bJ/shared" frameborder="0" name="YgdvM9bJ" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N\alpha(N)) \approx O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of vertices (and also the number of edges) in the graph, and <script type="math/tex; mode=display">\alpha</script> is the <em>Inverse-Ackermann</em> function.  We make up to <script type="math/tex; mode=display">N</script> queries of <code>dsu.union</code>, which takes (amortized) <script type="math/tex; mode=display">O(\alpha(N))</script> time.  Outside the scope of this article, it can be shown why <code>dsu.union</code> has <script type="math/tex; mode=display">O(\alpha(N))</script> complexity, what the Inverse-Ackermann function is, and why <script type="math/tex; mode=display">O(\alpha(N))</script> is approximately <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.  The current construction of the graph (embedded in our <code>dsu</code> structure) has at most <script type="math/tex; mode=display">N</script> nodes.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>