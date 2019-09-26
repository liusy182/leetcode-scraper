<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
<li><a href="#approach-2-greedy">Approach 2: Greedy</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to cover every node, starting from the top of the tree and working down.  Every node considered must be covered by a camera at that node or some neighbor.</p>
<p>Because cameras only care about local state, we can hope to leverage this fact for an efficient solution.  Specifically, when deciding to place a camera at a node, we might have placed cameras to cover some subset of this node, its left child, and its right child already.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>solve(node)</code> be some information about how many cameras it takes to cover the subtree at this node in various states.  There are essentially 3 states:</p>
<ul>
<li>[State 0] Strict subtree:  All the nodes below this node are covered, but not this node.</li>
<li>[State 1] Normal subtree:  All the nodes below and including this node are covered, but there is no camera here.</li>
<li>[State 2] Placed camera:  All the nodes below and including this node are covered, and there is a camera here (which may cover nodes above this node).</li>
</ul>
<p>Once we frame the problem in this way, the answer falls out:</p>
<ul>
<li>To cover a strict subtree, the children of this node must be in state 1.</li>
<li>To cover a normal subtree without placing a camera here, the children of this node must be in states 1 or 2, and at least one of those children must be in state 2.</li>
<li>To cover the subtree when placing a camera here, the children can be in any state.</li>
</ul>
<iframe src="https://leetcode.com/playground/4oJtky7i/shared" frameborder="0" width="100%" height="480" name="4oJtky7i"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(H)</script>, where <script type="math/tex; mode=display">H</script> is the height of the given tree.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy">Approach 2: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>Instead of trying to cover every node from the top down, let's try to cover it from the bottom up - considering placing a camera with the deepest nodes first, and working our way up the tree.</p>
<p>If a node has its children covered and has a parent, then it is strictly better to place the camera at this node's parent.</p>
<p><strong>Algorithm</strong></p>
<p>If a node has children that are not covered by a camera, then we must place a camera here.  Additionally, if a node has no parent and it is not covered, we must place a camera here.</p>
<iframe src="https://leetcode.com/playground/Zhw2ojEo/shared" frameborder="0" width="100%" height="500" name="Zhw2ojEo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(H)</script>, where <script type="math/tex; mode=display">H</script> is the height of the given tree.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>