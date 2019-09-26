<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth-First Search</a></li>
<li><a href="#approach-2-union-find">Approach 2: Union-Find</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth-First Search</h4>
<p><strong>Intuition</strong></p>
<p>Let's say two stones are connected by an edge if they share a row or column, and define a connected component in the usual way for graphs: a subset of stones so that there doesn't exist an edge from a stone in the subset to a stone not in the subset.  For convenience, we refer to a <em>component</em> as meaning a connected component.</p>
<p>The main insight is that we can always make moves that reduce the number of stones in each component to 1.</p>
<p>Firstly, every stone belongs to exactly one component, and moves in one component do not affect another component.</p>
<p>Now, consider a spanning tree of our component.  We can make moves repeatedly from the leaves of this tree until there is one stone left.</p>
<p><strong>Algorithm</strong></p>
<p>To count connected components of the above graph, we will use depth-first search.</p>
<p>For every stone not yet visited, we will visit it and any stone in the same connected component.  Our depth-first search traverses each node in the component.</p>
<p>For each component, the answer changes by <code>-1 + component.size</code>.</p>
<iframe src="https://leetcode.com/playground/vFbGLUPW/shared" frameborder="0" width="100%" height="500" name="vFbGLUPW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>stones</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-union-find">Approach 2: Union-Find</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach 1</em>, we will need to consider components of an underlying graph.  A "Disjoint Set Union" (DSU) data structure is ideal for this.</p>
<p>We will skip the explanation of how a DSU structure is implemented.  Please refer to <a href="https://leetcode.com/problems/redundant-connection/solution/">https://leetcode.com/problems/redundant-connection/solution/</a> for a tutorial on DSU.</p>
<p><strong>Algorithm</strong></p>
<p>Let's connect row <code>i</code> to column <code>j</code>, which will be represented by <code>j+10000</code>.  The answer is the number of components after making all the connections.</p>
<p>Note that for brevity, our <code>DSU</code> implementation does not use union-by-rank.  This makes the asymptotic time complexity larger.</p>
<iframe src="https://leetcode.com/playground/hhTCv59W/shared" frameborder="0" width="100%" height="500" name="hhTCv59W"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>stones</code>.  (If we used union-by-rank, this can be <script type="math/tex; mode=display">O(N * \alpha(N))</script>, where <script type="math/tex; mode=display">\alpha</script> is the Inverse-Ackermann function.)</p>
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