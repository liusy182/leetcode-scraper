<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth First Search</h4>
<p><strong>Intuition</strong></p>
<p>If the leaf of a tree has 0 coins (an excess of -1 from what it needs), then we should push a coin from its parent onto the leaf.  If it has say, 4 coins (an excess of 3), then we should push 3 coins off the leaf.  In total, the number of moves from that leaf to or from its parent is <code>excess = Math.abs(num_coins - 1)</code>.  Afterwards, we never have to consider this leaf again in the rest of our calculation.</p>
<p><strong>Algorithm</strong></p>
<p>We can use the above fact to build our answer.  Let <code>dfs(node)</code> be the <em>excess</em> number of coins in the subtree at or below this <code>node</code>: namely, the number of coins in the subtree, minus the number of nodes in the subtree.  Then, the number of moves we make from this node to and from its children is <code>abs(dfs(node.left)) + abs(dfs(node.right))</code>.  After, we have an excess of <code>node.val + dfs(node.left) + dfs(node.right) - 1</code> coins at this node.</p>
<iframe src="https://leetcode.com/playground/9mtBQnVp/shared" frameborder="0" width="100%" height="327" name="9mtBQnVp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(H)</script>, where <script type="math/tex; mode=display">H</script> is the height of the tree.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>