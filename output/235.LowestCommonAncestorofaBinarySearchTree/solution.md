<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursive-approach">Approach 1: Recursive Approach</a></li>
<li><a href="#approach-2-iterative-approach">Approach 2: Iterative Approach</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>We can solve this using the approaches to find <a href="https://leetcode.com/articles/lowest-common-ancestor-of-a-binary-tree/">LCA in a binary tree</a>.</p>
<p>But, binary search tree's property could be utilized, to come up with a better algorithm.</p>
<p>Lets review properties of a BST:</p>
<blockquote>
<ol>
<li>Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value.</li>
<li>Right subtree of a node N contains nodes whose values are greater than node N's value.</li>
<li>Both left and right subtrees are also BSTs.</li>
</ol>
</blockquote>
<h4 id="approach-1-recursive-approach">Approach 1: Recursive Approach</h4>
<p><strong>Intuition</strong></p>
<p>Lowest common ancestor for two nodes <code>p</code> and <code>q</code> would be the last ancestor node common to both of them. Here <code>last</code> is defined in terms of the depth of the node. The below diagram would help in understanding what <code>lowest</code> means.</p>
<p></p><center>
<img src="../Figures/235/235_LCA_Binary_1.png" width="600">
</center>
<p>Note: One of <code>p</code> or <code>q</code> would be in the left subtree and the other in the right subtree of the LCA node.</p>
<p>Following cases are possible:
</p><center>
<img src="../Figures/235/235_LCA_Binary_2.png" width="600">
</center>
<p><strong>Algorithm</strong></p>
<ol>
<li>Start traversing the tree from the root node.</li>
<li>If both the nodes <code>p</code> and <code>q</code> are in the right subtree, then continue the search with right subtree starting step 1.</li>
<li>If both the nodes <code>p</code> and <code>q</code> are in the left subtree, then continue the search with left subtree starting step 1.</li>
<li>If both step 2 and step 3 are not true, this means we have found the node which is common to node <code>p</code>'s and <code>q</code>'s subtrees.
and hence we return this common node as the LCA.</li>
</ol>
<iframe src="https://leetcode.com/playground/A7ZULghS/shared" frameborder="0" width="100%" height="497" name="A7ZULghS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>. This is because the maximum amount of space utilized by the recursion stack would be <script type="math/tex; mode=display">N</script> since the height of a skewed BST could be <script type="math/tex; mode=display">N</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-iterative-approach">Approach 2: Iterative Approach</h4>
<p><strong>Algorithm</strong></p>
<p>The steps taken are also similar to approach 1. The only difference is instead of recursively calling the function, we traverse down the tree iteratively. This is possible without using a stack or recursion since we don't need to backtrace to find the LCA node. In essence of it the problem is iterative, it just wants us to find the split point. The point from where <code>p</code> and <code>q</code> won't be part of the same subtree or when one is the parent of the other.</p>
<iframe src="https://leetcode.com/playground/PfXQUZfN/shared" frameborder="0" width="100%" height="500" name="PfXQUZfN"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity : <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.</p>
</li>
<li>
<p>Space Complexity : <script type="math/tex; mode=display">O(1)</script>.
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>