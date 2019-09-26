<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-union-find">Approach 1: Union-Find</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-union-find">Approach 1: Union-Find</h4>
<p><strong>Intuition</strong></p>
<p>To find the number of components in a graph, we can use either depth-first search or union find.  The main difficulty with this problem is in specifying the graph.</p>
<p>One "brute force" way to specify the graph is to associate each grid square with 4 nodes (north, south, west, and east), representing 4 triangles inside the square if it were to have both slashes.  Then, we can connect all 4 nodes if the grid square is <code>" "</code>, and connect two pairs if the grid square is <code>"/"</code> or <code>"\"</code>.  Finally, we can connect all neighboring nodes (for example, the east node of the square at <code>grid[0][0]</code> connects with the west node of the square at <code>grid[0][1]</code>).</p>
<p>This is the most straightforward approach, but there are other approaches that use less nodes to represent the underlying information.</p>
<p><strong>Algorithm</strong></p>
<p>Create <code>4*N*N</code> nodes, one for each grid square, and connect them as described above.  After, we use a union find structure to find the number of connected components.</p>
<p>We will skip the explanation of how a DSU structure is implemented.  Please refer to <a href="https://leetcode.com/problems/redundant-connection/solution/">https://leetcode.com/problems/redundant-connection/solution/</a> for a tutorial on DSU.</p>
<iframe src="https://leetcode.com/playground/jdYrnNjc/shared" frameborder="0" width="100%" height="500" name="jdYrnNjc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N * N * \alpha(N))</script>, where <script type="math/tex; mode=display">N</script> is the length of the grid, and <script type="math/tex; mode=display">\alpha</script> is the Inverse-Ackermann function (if we were to use union-find by rank.)</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N * N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>