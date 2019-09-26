<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can think of any path (of nodes with the same values) as up to two arrows extending from it's root.</p>
<p>Specifically, the <em>root</em> of a path will be the unique node such that the parent of that node does not appear in the path, and an <em>arrow</em> will be a path where the root only has one child node in the path.</p>
<p>Then, for each node, we want to know what is the longest possible arrow extending left, and the longest possible arrow extending right?  We can solve this using recursion.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>arrow_length(node)</code> be the length of the longest arrow that extends from the <code>node</code>.  That will be <code>1 + arrow_length(node.left)</code> if <code>node.left</code> exists and has the same value as <code>node</code>.  Similarly for the <code>node.right</code> case.</p>
<p>While we are computing arrow lengths, each candidate answer will be the sum of the arrows in both directions from that node.  We record these candidate answers and return the best one.</p>
<iframe src="https://leetcode.com/playground/DjHbgZUi/shared" frameborder="0" name="DjHbgZUi" width="100%" height="428"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.  We process every node once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(H)</script>, where <script type="math/tex; mode=display">H</script> is the height of the tree.  Our recursive call stack could be up to <script type="math/tex; mode=display">H</script> layers deep.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>