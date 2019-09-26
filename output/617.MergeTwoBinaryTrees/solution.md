<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</a></li>
<li><a href="#approach-2-iterative-method-accepted">Approach #2 Iterative Method [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</h4>
<p>We can traverse both the given trees in a preorder fashion. At every step, we check if the current node exists(isn't null) for both the trees. If so, we add the values in the current nodes of both the trees and update the value in the current node of the first tree to reflect this sum obtained. At every step, we also call the original function <code>mergeTrees()</code> with the left children and then with the right children of the current nodes of the two trees. If at any step, one of these children happens to be null, we return the child of the other tree(representing the corresponding child subtree) to be added as a child subtree to the calling parent node in the first tree. At the end, the first tree will represent the required resultant merged binary tree.</p>
<p>The following animation illustrates the process.</p>
<p>!?!../Documents/617_Merge_Trees_Recursion.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/d9nZDPEJ/shared" frameborder="0" name="d9nZDPEJ" width="100%" height="428"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m)</script>. A total of <script type="math/tex; mode=display">m</script> nodes need to be traversed. Here, <script type="math/tex; mode=display">m</script> represents the minimum number of nodes from the two given trees.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">m</script> in the case of a skewed tree. In average case, depth will be <script type="math/tex; mode=display">O(logm)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-iterative-method-accepted">Approach #2 Iterative Method [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the current approach, we again traverse the two trees, but this time we make use of a <script type="math/tex; mode=display">stack</script> to do so instead of making use of recursion. Each entry in the <script type="math/tex; mode=display">stack</script> strores data in the form <script type="math/tex; mode=display">[node_{tree1}, node_{tree2}]</script>. Here, <script type="math/tex; mode=display">node_{tree1}</script> and <script type="math/tex; mode=display">node_{tree2}</script> are the nodes of the first tree and the second tree respectively.</p>
<p>We start off by pushing the root nodes of both the trees onto the <script type="math/tex; mode=display">stack</script>. Then, at every step, we remove a node pair from the top of the stack. For every node pair removed, we add the values corresponding to the two nodes and update the value of the corresponding node in the first tree. Then, if the left child of the first tree exists, we push the left child(pair) of both the trees onto the stack. If the left child of the first tree doesn't exist, we append the left child(subtree) of the second tree to the current node of the first tree. We do the same for the right child pair as well. </p>
<p>If, at any step, both the current nodes are null, we continue with popping the next nodes from the <script type="math/tex; mode=display">stack</script>.</p>
<p>The following animation depicts the process.</p>
<p>!?!../Documents/617_Merge_Trees_Stack.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/v2TK7i2x/shared" frameborder="0" name="v2TK7i2x" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We traverse over a total of <script type="math/tex; mode=display">n</script> nodes. Here, <script type="math/tex; mode=display">n</script> refers to the smaller of the number of nodes in the two trees.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of stack can grow upto <script type="math/tex; mode=display">n</script> in case of a skewed tree.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>