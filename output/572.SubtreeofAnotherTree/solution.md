<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-preorder-traversal-accepted">Approach #1 Using Preorder Traversal [Accepted]</a></li>
<li><a href="#approach-2-by-comparison-of-nodes-accepted">Approach #2 By Comparison of Nodes  [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-preorder-traversal-accepted">Approach #1 Using Preorder Traversal [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We can find the preorder traversal of the given tree <script type="math/tex; mode=display">s</script> and <script type="math/tex; mode=display">t</script>, given by, say <script type="math/tex; mode=display">s_{preorder}</script> and <script type="math/tex; mode=display">t_{preorder}</script> respectively(represented in the form of a string). Now, we can check if <script type="math/tex; mode=display">t_{preorder}</script> is a substring of <script type="math/tex; mode=display">s_{preorder}</script>. </p>
<p>But, in order to use this approach, we need to treat the given tree in a different manner. Rather than assuming a <script type="math/tex; mode=display">null</script> value for the childern of the leaf nodes, we need to treat the left and right child as a <script type="math/tex; mode=display">lnull</script> and <script type="math/tex; mode=display">rnull</script> value respectively. This is done to ensure that the <script type="math/tex; mode=display">t_{preorder}</script> doesn't become a substring of <script type="math/tex; mode=display">s_{preorder}</script> even in cases when <script type="math/tex; mode=display">t</script> isn't a subtree of <script type="math/tex; mode=display">s</script>. </p>
<p>You can also note that we've added a '#' before every considering every value. If this isn't done, the trees of the form <code>s:[23, 4, 5]</code> and <code>t:[3, 4, 5]</code> will also give a true result since the preorder string of the <code>t("23 4 lnull rull 5 lnull rnull")</code> will be a substring of the preorder string of <code>s("3 4 lnull rull 5 lnull rnull")</code>. Adding a '#' before the node's value solves this problem.</p>
<p align="center"><img alt="Preorder_null" src="../Figures/572_Subtree_1.PNG"></p>
<p align="center"><img alt="Preorder_lnull_rnull" src="../Figures/572_Subtree_2.PNG"></p>
<iframe src="https://leetcode.com/playground/cagXWqSv/shared" frameborder="0" name="cagXWqSv" width="100%" height="513"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m^2+n^2+m*n)</script>. A total of <script type="math/tex; mode=display">n</script> nodes of the tree <script type="math/tex; mode=display">s</script> and <script type="math/tex; mode=display">m</script> nodes of tree <script type="math/tex; mode=display">t</script> are traversed. Assuming string concatenation takes <script type="math/tex; mode=display">O(k)</script> time for strings of length <script type="math/tex; mode=display">k</script> and <code>indexOf</code> takes <script type="math/tex; mode=display">O(m*n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(max(m,n))</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script> for tree <script type="math/tex; mode=display">t</script> and <script type="math/tex; mode=display">m</script> for tree <script type="math/tex; mode=display">s</script> in worst case.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-by-comparison-of-nodes-accepted">Approach #2 By Comparison of Nodes  [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of creating an inorder traversal, we can treat every node of the given tree <script type="math/tex; mode=display">t</script> as the root, treat it as a subtree and compare the corresponding subtree with the given subtree <script type="math/tex; mode=display">s</script> for equality. For checking the equality, we can compare the all the nodes of the two subtrees. </p>
<p>For doing this, we make use a function <code>traverse(s,t)</code> which traverses over the given tree <script type="math/tex; mode=display">s</script> and treats every node as the root of the subtree currently being considered. It also checks the two subtrees currently being considered for their equality. In order to check the equality of the two subtrees, we make use of <code>equals(x,y)</code> function, which takes <script type="math/tex; mode=display">x</script> and <script type="math/tex; mode=display">y</script>, which are the roots of the two subtrees to be compared as the inputs and returns True or False depending on whether the two are equal or not. It compares all the nodes of the two subtrees for equality. Firstly, it checks whether the roots of the two trees for equality and then calls itself recursively for the left subtree and the right subtree.</p>
<p>The follwowing animation depicts an abstracted view of the process:</p>
<p>!?!../Documents/572_Subtree.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/A6ipy4aH/shared" frameborder="0" name="A6ipy4aH" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. In worst case(skewed tree) <code>traverse</code> function takes <script type="math/tex; mode=display">O(m*n)</script> time. </p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script>. <script type="math/tex; mode=display">n</script> refers to the number of nodes in <script type="math/tex; mode=display">s</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>