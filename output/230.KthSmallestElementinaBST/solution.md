<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#how-to-traverse-the-tree">How to traverse the tree</a></li>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-iteration">Approach 2: Iteration</a></li>
<li><a href="#follow-up">Follow up</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="how-to-traverse-the-tree">How to traverse the tree</h4>
<p>There are two general strategies to traverse a tree:</p>
<ul>
<li>
<p><em>Depth First Search</em> (<code>DFS</code>)</p>
<p>In this strategy, we adopt the <code>depth</code> as the priority, so that one
would start from a root and reach all the way down to certain leaf,
and then back to root to reach another branch.</p>
<p>The DFS strategy can further be distinguished as
<code>preorder</code>, <code>inorder</code>, and <code>postorder</code> depending on the relative order
among the root node, left node and right node.</p>
</li>
<li>
<p><em>Breadth First Search</em> (<code>BFS</code>)</p>
<p>We scan through the tree level by level, following the order of height,
from top to bottom. The nodes on higher level would be visited before
the ones with lower levels.</p>
</li>
</ul>
<p>On the following figure the nodes are numerated in the order you visit them,
please follow <code>1-2-3-4-5</code> to compare different strategies.</p>
<p><img alt="postorder" src="../Figures/230/bfs_dfs.png"></p>
<blockquote>
<p>To solve the problem, one could use the property of BST : inorder traversal of BST
is an array sorted in the ascending order. </p>
</blockquote>
<p><br> 
<br></p>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p>It's a very straightforward approach with <script type="math/tex; mode=display">\mathcal{O}(N)</script> 
time complexity.
The idea is to build an inorder traversal of BST which is 
an array sorted in the ascending order. 
Now the answer is the <code>k - 1</code>th element of this array. </p>
<p><img alt="bla" src="../Figures/230/inorder.png"></p>
<iframe src="https://leetcode.com/playground/8B2Y2ArK/shared" frameborder="0" width="100%" height="293" name="8B2Y2ArK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> to build a traversal. </li>
<li>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> to keep an inorder traversal.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-iteration">Approach 2: Iteration</h4>
<p>The above recursion could be converted into iteration, 
with the help of stack. This way one could speed up the solution 
because there is no need to build the entire inorder traversal,
and one could stop after the kth element.</p>
<p><img alt="bla" src="../Figures/230/iteration.png"></p>
<iframe src="https://leetcode.com/playground/Z2JBGMv5/shared" frameborder="0" width="100%" height="361" name="Z2JBGMv5"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(H + k)</script>, where <script type="math/tex; mode=display">H</script> is a tree height.
This complexity is defined by the stack, which contains at least <script type="math/tex; mode=display">H + k</script> elements, since before
starting to pop out one has to go down to a leaf. This results in 
<script type="math/tex; mode=display">\mathcal{O}(\log N + k)</script> for the balanced tree and 
<script type="math/tex; mode=display">\mathcal{O}(N + k)</script> for completely unbalanced tree with all
 the nodes in the left subtree. </li>
<li>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(H + k)</script>, the same as for time complexity, 
<script type="math/tex; mode=display">\mathcal{O}(N + k)</script> in the worst case,
 and <script type="math/tex; mode=display">\mathcal{O}(\log N + k)</script> in the average case.
<br>
<br></li>
</ul>
<hr>
<h4 id="follow-up">Follow up</h4>
<blockquote>
<p>What if the BST is modified (insert/delete operations) 
often and you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?</p>
</blockquote>
<p><a href="https://leetcode.com/articles/insert-into-a-bst/">Insert</a> 
and <a href="https://leetcode.com/articles/delete-node-in-a-bst/">delete</a> 
in a BST were discussed last week, the time complexity of these 
operations is <script type="math/tex; mode=display">\mathcal{O}(H)</script>, where <script type="math/tex; mode=display">H</script> is a height of binary tree,
and <script type="math/tex; mode=display">H = \log N</script> for the balanced tree.</p>
<p>Hence without any optimisation insert/delete + search of kth element has 
<script type="math/tex; mode=display">\mathcal{O}(2H + k)</script> complexity. 
How to optimise that? </p>
<p>That's a design question, 
basically we're asked to implement a structure 
which contains a BST inside and
optimises the following operations :</p>
<ul>
<li>
<p>Insert</p>
</li>
<li>
<p>Delete</p>
</li>
<li>
<p>Find kth smallest</p>
</li>
</ul>
<p>Seems like a database description, isn't it? 
Let's use here the same logic as for <a href="https://leetcode.com/articles/lru-cache/">LRU cache</a>
design, and combine an indexing structure (we could keep BST here)
with a double linked list. </p>
<p>Such a structure would provide:</p>
<ul>
<li>
<p>
<script type="math/tex; mode=display">\mathcal{O}(H)</script> time for the insert and delete.</p>
</li>
<li>
<p>
<script type="math/tex; mode=display">\mathcal{O}(k)</script> for the search of kth smallest.</p>
</li>
</ul>
<p><img alt="bla" src="../Figures/230/linked_list2.png"></p>
<p>The overall time complexity for insert/delete + search of kth smallest
is <script type="math/tex; mode=display">\mathcal{O}(H + k)</script> instead of <script type="math/tex; mode=display">\mathcal{O}(2H + k)</script>. </p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity for insert/delete + search of kth smallest: 
<script type="math/tex; mode=display">\mathcal{O}(H + k)</script>, where <script type="math/tex; mode=display">H</script> is a tree height.
<script type="math/tex; mode=display">\mathcal{O}(\log N + k)</script> in the average case,
<script type="math/tex; mode=display">\mathcal{O}(N + k)</script> in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> to keep the linked list.</p>
</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>