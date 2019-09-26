<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-breadth-first-search">Approach 1: Breadth First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-breadth-first-search">Approach 1: Breadth First Search</h4>
<p><strong>Intuition</strong></p>
<p>This problem reduces to two smaller problems: representing the "location" of each node as a <code>(depth, position)</code> pair, and formalizing what it means for nodes to all be left-justified.</p>
<p>If we have say, 4 nodes in a row with depth 3 and positions 0, 1, 2, 3; and we want 8 new nodes in a row with depth 4 and positions 0, 1, 2, 3, 4, 5, 6, 7; then we can see that the rule for going from a node to its left child is <code>(depth, position) -&gt; (depth + 1, position * 2)</code>, and the rule for going from a node to its right child is <code>(depth, position) -&gt; (depth + 1, position * 2 + 1)</code>.  Then, our row at depth <script type="math/tex; mode=display">d</script> is completely filled if it has <script type="math/tex; mode=display">2^{d-1}</script> nodes, and all the nodes in the last level are left-justified when their positions take the form <code>0, 1, ...</code> in sequence with no gaps.</p>
<p>A cleaner way to represent depth and position is with a code: <code>1</code> will be the root node, and for any node with code <code>v</code>, the left child will be <code>2*v</code> and the right child will be <code>2*v + 1</code>.  This is the scheme we will use.  Under this scheme, our tree is complete if the codes take the form <code>1, 2, 3, ...</code> in sequence with no gaps.</p>
<p><strong>Algorithm</strong></p>
<p>At the root node, we will associate it with the code <code>1</code>.  Then, for each node with code <code>v</code>, we will associate its left child with code <code>2 * v</code>, and its right child with code <code>2 * v + 1</code>.</p>
<p>We can find the codes of every node in the tree in "reading order" (top to bottom, left to right) sequence using a breadth first search.  (We could also use a depth first search and sort the codes later.)</p>
<p>Then, we check that the codes are the sequence <code>1, 2, 3, ...</code> with no gaps.  Actually, we only need to check that the last code is correct, since the last code is the largest value.</p>
<iframe src="https://leetcode.com/playground/JXyfvuSS/shared" frameborder="0" width="100%" height="480" name="JXyfvuSS"></iframe>

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