<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-deque">Approach 1: Deque</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-deque">Approach 1: Deque</h4>
<p><strong>Intuition</strong></p>
<p>Consider all the nodes numbered first by level and then left to right.  Call this the "number order" of the nodes.</p>
<p>At each insertion step, we want to insert into the node with the lowest number (that still has 0 or 1 children).</p>
<p>By maintaining a <code>deque</code> (double ended queue) of these nodes in number order, we can solve the problem.  After inserting a node, that node now has the highest number and no children, so it goes at the end of the deque.  To get the node with the lowest number, we pop from the beginning of the deque.</p>
<p><strong>Algorithm</strong></p>
<p>First, perform a breadth-first search to populate the <code>deque</code> with nodes that have 0 or 1 children, in number order.</p>
<p>Now when inserting a node, the parent is the first element of <code>deque</code>, and we add this new node to our <code>deque</code>.</p>
<iframe src="https://leetcode.com/playground/vJC78XQe/shared" frameborder="0" width="100%" height="500" name="vJC78XQe"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  The preprocessing is <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.  Each insertion operation thereafter is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N_{\text{cur}})</script> space complexity, when the size of the tree during the current insertion operation is <script type="math/tex; mode=display">N_{\text{cur}}</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>