<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>trim(node)</code> be the desired answer for the subtree at that node.  We can construct the answer recursively.</p>
<p><strong>Algorithm</strong></p>
<p>When <script type="math/tex; mode=display">\text{node.val > R}</script>, we know that the trimmed binary tree must occur to the left of the node. Similarly, when <script type="math/tex; mode=display">\text{node.val < L}</script>, the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.</p>
<iframe src="https://leetcode.com/playground/8eWsgDRM/shared" frameborder="0" name="8eWsgDRM" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the total number of nodes in the given tree.  We visit each node at most once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.  Even though we don't explicitly use any additional memory, the call stack of our recursion could be as large as the number of nodes in the worst case.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>