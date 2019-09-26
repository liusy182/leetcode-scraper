<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-subtree-sum-and-count-accepted">Approach #1: Subtree Sum and Count [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-subtree-sum-and-count-accepted">Approach #1: Subtree Sum and Count [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>ans</code> be the returned answer, so that in particular <code>ans[x]</code> be the answer for node <code>x</code>.</p>
<p>Naively, finding each <code>ans[x]</code> would take <script type="math/tex; mode=display">O(N)</script> time  (where <script type="math/tex; mode=display">N</script> is the number of nodes in the graph), which is too slow.  This is the motivation to find out how <code>ans[x]</code> and <code>ans[y]</code> are related, so that we cut down on repeated work.</p>
<p>Let's investigate the answers of neighboring nodes <script type="math/tex; mode=display">x</script> and <script type="math/tex; mode=display">y</script>.  In particular, say <script type="math/tex; mode=display">xy</script> is an edge of the graph, that if cut would form two trees <script type="math/tex; mode=display">X</script> (containing <script type="math/tex; mode=display">x</script>) and <script type="math/tex; mode=display">Y</script> (containing <script type="math/tex; mode=display">y</script>).</p>
<p></p><center>
    <img src="../Figures/834/sketch1.png" alt="Tree diagram illustrating recurrence for ans[child]" style="width: 1000px;">
</center>
<p>Then, as illustrated in the diagram, the answer for <script type="math/tex; mode=display">x</script> in the entire tree, is the answer of <script type="math/tex; mode=display">x</script> on <script type="math/tex; mode=display">X</script>
<code>"x@X"</code>, plus the answer of <script type="math/tex; mode=display">y</script> on <script type="math/tex; mode=display">Y</script>
<code>"y@Y"</code>, plus the number of nodes in <script type="math/tex; mode=display">Y</script>
<code>"#(Y)"</code>.  The last part <code>"#(Y)"</code> is specifically because for any node <code>z in Y</code>, <code>dist(x, z) = dist(y, z) + 1</code>.</p>
<p>By similar reasoning, the answer for <script type="math/tex; mode=display">y</script> in the entire tree is <code>ans[y] = x@X + y@Y + #(X)</code>.  Hence, for neighboring nodes <script type="math/tex; mode=display">x</script> and <script type="math/tex; mode=display">y</script>, <code>ans[x] - ans[y] = #(Y) - #(X)</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Root the tree.  For each node, consider the subtree <script type="math/tex; mode=display">S_{\text{node}}</script> of that node plus all descendants.  Let <code>count[node]</code> be the number of nodes in <script type="math/tex; mode=display">S_{\text{node}}</script>, and <code>stsum[node]</code> ("subtree sum") be the sum of the distances from <code>node</code> to the nodes in <script type="math/tex; mode=display">S_{\text{node}}</script>.</p>
<p>We can calculate <code>count</code> and <code>stsum</code> using a post-order traversal, where on exiting some <code>node</code>, the <code>count</code> and <code>stsum</code> of all descendants of this node is correct, and we now calculate <code>count[node] += count[child]</code> and <code>stsum[node] += stsum[child] + count[child]</code>.</p>
<p>This will give us the right answer for the <code>root</code>: <code>ans[root] = stsum[root]</code>.</p>
<p>Now, to use the insight explained previously: if we have a node <code>parent</code> and it's child <code>child</code>, then these are neighboring nodes, and so <code>ans[child] = ans[parent] - count[child] + (N - count[child])</code>.  This is because there are <code>count[child]</code> nodes that are <code>1</code> easier to get to from <code>child</code> than <code>parent</code>, and <code>N-count[child]</code> nodes that are <code>1</code> harder to get to from <code>child</code> than <code>parent</code>.</p>
<p></p><center>
    <img src="../Figures/834/sketch2.png" alt="Tree diagram illustrating recurrence for ans[child]" style="height: 200px;">
</center>
<p>Using a second, pre-order traversal, we can update our answer in linear time for all of our nodes.</p>
<iframe src="https://leetcode.com/playground/u5mhW6AL/shared" frameborder="0" width="100%" height="500" name="u5mhW6AL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the graph.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>