<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#tree-definition">Tree definition</a></li>
<li><a href="#intuition">Intuition</a></li>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-iteration">Approach 2: Iteration</a></li>
<li><a href="#approach-3-inorder-traversal">Approach 3: Inorder traversal</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="tree-definition">Tree definition</h4>
<p>First of all, here is the definition of the <code>TreeNode</code> which we would use.</p>
<iframe src="https://leetcode.com/playground/W2qazBuk/shared" frameborder="0" width="100%" height="225" name="W2qazBuk"></iframe>

<p><br>
<br></p>
<hr>
<h4 id="intuition">Intuition</h4>
<p>On the first sight, the problem is trivial. Let's traverse the tree
and check at each step if <code>node.right.val &gt; node.val</code> and 
<code>node.left.val &lt; node.val</code>. This approach would even work for some
trees 
<img alt="compute" src="../Figures/98/98_not_bst.png"></p>
<p>The problem is this approach will not work for all cases. 
Not only the right child should be larger than the node 
but all the 
elements in the right subtree. Here is an example :</p>
<p><img alt="compute" src="../Figures/98/98_not_bst_3.png"></p>
<p>That means one should keep both upper 
and lower limits for each node while traversing the tree, 
and compare the node value not
with children values but with these limits.
<br>
<br></p>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p>The idea above could be implemented as a recursion.
One compares the node value with its upper and lower limits
if they are available. Then one repeats the same 
step recursively for left and right subtrees. </p>
<p>!?!../Documents/98_LIS.json:1000,462!?!</p>
<iframe src="https://leetcode.com/playground/VeZZvEw8/shared" frameborder="0" width="100%" height="412" name="VeZZvEw8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> since we visit each node exactly once. </li>
<li>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> since we keep up to the entire tree.</li>
</ul>
<p><br>
<br></p>
<hr>
<h4 id="approach-2-iteration">Approach 2: Iteration</h4>
<p>The above recursion could be converted into iteration, 
with the help of stack. DFS would be better than BFS since 
it works faster here.</p>
<iframe src="https://leetcode.com/playground/VFyKF5Jv/shared" frameborder="0" width="100%" height="500" name="VFyKF5Jv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> since we visit each node exactly once. </li>
<li>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> since we keep up to the entire tree.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-3-inorder-traversal">Approach 3: Inorder traversal</h4>
<p><strong>Algorithm</strong></p>
<p>Let's use the order of nodes in the 
<a href="https://leetcode.com/articles/binary-tree-inorder-traversal/">inorder traversal</a> 
<code>Left -&gt; Node -&gt; Right</code>.</p>
<p><img alt="postorder" src="../Figures/145_transverse.png"></p>
<p>Here the nodes are enumerated in the order you visit them, 
and you could follow <code>1-2-3-4-5</code> to compare different strategies.</p>
<p><code>Left -&gt; Node -&gt; Right</code> order of inorder traversal 
means for BST that each element should be smaller 
than the next one.</p>
<p>Hence the algorithm with <script type="math/tex; mode=display">\mathcal{O}(N)</script> time complexity 
and <script type="math/tex; mode=display">\mathcal{O}(N)</script> space complexity could be simple:</p>
<ul>
<li>
<p>Compute inorder traversal list <code>inorder</code>.</p>
</li>
<li>
<p>Check if each element in <code>inorder</code> is smaller than the next one.</p>
</li>
</ul>
<p><img alt="postorder" src="../Figures/98/98_bst_inorder.png"></p>
<blockquote>
<p>Do we need to keep the whole <code>inorder</code> traversal list? </p>
</blockquote>
<p>Actually, no. The last added inorder element is enough 
to ensure at each step that the tree is BST (or not).
Hence one could merge both steps into one and
reduce the used space.</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/xWskyKv3/shared" frameborder="0" width="100%" height="429" name="xWskyKv3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> in the worst case
when the tree is BST or the "bad" element is a rightmost leaf.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> to keep <code>stack</code>.</p>
</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>