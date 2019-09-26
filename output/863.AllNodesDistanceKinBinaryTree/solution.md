<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-annotate-parent">Approach 1: Annotate Parent</a></li>
<li><a href="#approach-2-percolate-distance">Approach 2: Percolate Distance</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-annotate-parent">Approach 1: Annotate Parent</h4>
<p><strong>Intuition</strong></p>
<p>If we know the parent of every node <code>x</code>, we know all nodes that are distance <code>1</code> from <code>x</code>.  We can then perform a breadth first search from the <code>target</code> node to find the answer.</p>
<p><strong>Algorithm</strong></p>
<p>We first do a depth first search where we annotate every node with information about it's parent.</p>
<p>After, we do a breadth first search to find all nodes a distance <code>K</code> from the <code>target</code>.</p>
<iframe src="https://leetcode.com/playground/ySaDMJzK/shared" frameborder="0" width="100%" height="500" name="ySaDMJzK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-percolate-distance">Approach 2: Percolate Distance</h4>
<p><strong>Intuition</strong></p>
<p>From <code>root</code>, say the <code>target</code> node is at depth <code>3</code> in the left branch.  It means that any nodes that are distance <code>K - 3</code> in the right branch should be added to the answer.</p>
<p><strong>Algorithm</strong></p>
<p>Traverse every <code>node</code> with a depth first search <code>dfs</code>.  We'll add all nodes <code>x</code> to the answer such that <code>node</code> is the node on the path from <code>x</code> to <code>target</code> that is closest to the <code>root</code>.</p>
<p>To help us, <code>dfs(node)</code> will return the distance from <code>node</code> to the <code>target</code>.  Then, there are 4 cases:</p>
<ul>
<li>
<p>If <code>node == target</code>, then we should add nodes that are distance <code>K</code> in the subtree rooted at <code>target</code>.</p>
</li>
<li>
<p>If <code>target</code> is in the left branch of <code>node</code>, say at distance <code>L+1</code>, then we should look for nodes that are distance <code>K - L - 1</code> in the right branch.</p>
</li>
<li>
<p>If <code>target</code> is in the right branch of <code>node</code>, the algorithm proceeds similarly.</p>
</li>
<li>
<p>If <code>target</code> isn't in either branch of <code>node</code>, then we stop.</p>
</li>
</ul>
<p>In the above algorithm, we make use of the auxillary function <code>subtree_add(node, dist)</code> which adds the nodes in the subtree rooted at <code>node</code> that are distance <code>K - dist</code> from the given <code>node</code>.</p>
<iframe src="https://leetcode.com/playground/4h24GtWA/shared" frameborder="0" width="100%" height="500" name="4h24GtWA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
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