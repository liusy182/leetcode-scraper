<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Starting from a rooted tree with <code>N-1</code> edges and <code>N</code> vertices, let's enumerate the possibilities for the added "redundant" edge.  If there is no loop, then either one vertex must have two parents (or no edge is redundant.)  If there is a loop, then either one vertex has two parents, or every vertex has one parent.</p>
<p>In the first two cases, there are only two candidates for deleting an edge, and we can try removing the last one and seeing if that works.  In the last case, the last edge of the cycle can be removed: for example, when <code>1-&gt;2-&gt;3-&gt;4-&gt;1-&gt;5</code>, we want the last edge (by order of occurrence) in the cycle <code>1-&gt;2-&gt;3-&gt;4-&gt;1</code> (but not necessarily <code>1-&gt;5</code>).</p>
<p><strong>Algorithm</strong></p>
<p>We'll first construct the underlying graph, keeping track of edges coming from nodes with multiple parents.  After, we either have 2 or 0 <code>candidates</code>.</p>
<p>If there are no candidates, then every vertex has one parent, such as in the case <code>1-&gt;2-&gt;3-&gt;4-&gt;1-&gt;5</code>.  From any node, we walk towards it's parent until we revisit a node - then we must be inside the cycle, and any future seen nodes are part of that cycle.  Now we take the last edge that occurs in the cycle.</p>
<p>Otherwise, we'll see if the graph induced by <code>parent</code> is a rooted tree.  We again take the <code>root</code> by walking from any node towards the parent until we can't, then we perform a depth-first search on this <code>root</code>.  If we visit every node, then removing the last of the two edge candidates is acceptable, and we should.  Otherwise, we should remove the first of the two edge candidates.</p>
<p>In our solution, we use <code>orbit</code> to find the result upon walking from a node <code>x</code> towards it's parent repeatedly until you revisit a node or can't walk anymore.  <code>orbit(x).node</code> (or <code>orbit(x)[0]</code> in Python) will be the resulting node, while <code>orbit(x).seen</code> (or <code>orbit(x)[1]</code>) will be all the nodes visited.</p>
<iframe src="https://leetcode.com/playground/sHSf6pyj/shared" frameborder="0" width="100%" height="500" name="sHSf6pyj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the number of vertices (and also the number of edges) in the graph.  We perform a depth-first search.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the size of the graph.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>