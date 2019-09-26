<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Prune children of the tree recursively.  The only decisions at each node are whether to prune the left child or the right child.</p>
<p><strong>Algorithm</strong></p>
<p>We'll use a function <code>containsOne(node)</code> that does two things: it tells us whether the subtree at this <code>node</code> contains a <code>1</code>, and it also prunes all subtrees not containing <code>1</code>.</p>
<p>If for example, <code>node.left</code> does not contain a one, then we should prune it via <code>node.left = null</code>.</p>
<p>Also, the parent needs to be checked.  If for example the tree is a single node <code>0</code>, the answer is an empty tree.</p>
<iframe src="https://leetcode.com/playground/oKrtTG2C/shared" frameborder="0" width="100%" height="293" name="oKrtTG2C"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.  We process each node once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(H)</script>, where <script type="math/tex; mode=display">H</script> is the height of the tree.  This represents the size of the implicit call stack in our recursion.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>