<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-paint-deepest-nodes">Approach 1: Paint Deepest Nodes</a></li>
<li><a href="#approach-2-recursion">Approach 2: Recursion</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-paint-deepest-nodes">Approach 1: Paint Deepest Nodes</h4>
<p><strong>Intuition</strong></p>
<p>We try a straightforward approach that has two phases.</p>
<p>The first phase is to identify the nodes of the tree that are deepest.  To do this, we have to annotate the depth of each node.  We can do this with a depth first search.</p>
<p>Afterwards, we will use that annotation to help us find the answer:</p>
<ul>
<li>
<p>If the <code>node</code> in question has maximum depth, it is the answer.</p>
</li>
<li>
<p>If both the left and right child of a <code>node</code> have a deepest descendant, then the answer is this parent <code>node</code>.  </p>
</li>
<li>
<p>Otherwise, if some child has a deepest descendant, then the answer is that child.</p>
</li>
<li>
<p>Otherwise, the answer for this subtree doesn't exist.</p>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>In the first phase, we use a depth first search <code>dfs</code> to annotate our nodes.</p>
<p>In the second phase, we also use a depth first search <code>answer(node)</code>, returning the answer for the subtree at that <code>node</code>, and using the rules above to build our answer from the answers of the children of <code>node</code>.</p>
<p>Note that in this approach, the <code>answer</code> function returns answers that have the deepest nodes of the <em>entire</em> tree, not just the subtree being considered.</p>
<iframe src="https://leetcode.com/playground/BShzUaRJ/shared" frameborder="0" width="100%" height="500" name="BShzUaRJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursion">Approach 2: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>We can combine both depth first searches in <em>Approach #1</em> into an approach that does both steps in one pass.  We will have some function <code>dfs(node)</code> that returns both the answer for this subtree, and the distance from <code>node</code> to the deepest nodes in this subtree.</p>
<p><strong>Algorithm</strong></p>
<p>The <code>Result</code> (on some subtree) returned by our (depth-first search) recursion will have two parts:
<em> <code>Result.node</code>: the largest depth node that is equal to or an ancestor of all the deepest nodes of this subtree.
</em> <code>Result.dist</code>: the number of nodes in the path from the root of this subtree, to the deepest node in this subtree.</p>
<p>We can calculate these answers disjointly for <code>dfs(node)</code>:</p>
<ul>
<li>
<p>To calculate the <code>Result.node</code> of our answer:</p>
<ul>
<li>
<p>If one <code>childResult</code> has deeper nodes, then <code>childResult.node</code> will be the answer.</p>
</li>
<li>
<p>If they both have the same depth nodes, then <code>node</code> will be the answer.</p>
</li>
</ul>
</li>
<li>
<p>The <code>Result.dist</code> of our answer is always 1 more than the largest <code>childResult.dist</code> we have.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/QAN4y6ev/shared" frameborder="0" width="100%" height="500" name="QAN4y6ev"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.</p>
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