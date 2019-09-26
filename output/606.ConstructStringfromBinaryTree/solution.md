<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</a></li>
<li><a href="#approach-2-iterative-method-using-stack-accepted">Approach #2 Iterative Method Using stack [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</h4>
<p>This solution is very simple. We simply need to do the preorder traversal of the given Binary Tree. But, along with this, we need to make use of braces at appropriate positions. But, we also need to make sure that we omit the unnecessary braces. To do the preorder traversal, we make use of recursion. We print the current node and call the same given function for the left and the right children of the node in that order(if they exist). For every node encountered, the following cases are possible.</p>
<p>Case 1: Both the left child and the right child exist for the current node. In this case, we need to put the braces <code>()</code> around both the left child's preorder traversal output and the right child's preorder traversal output.</p>
<p>Case 2: None of the left or the right child exist for the current node. In this case, as shown in the figure below, considering empty braces for the null left and right children is redundant. Hence, we need not put braces for any of them.</p>
<p align="center"><img alt="No_child" src="../Figures/606/606_Case2.PNG"></p>
<p>Case 3: Only the left child exists for the current node. As the figure below shows, putting empty braces for the right child in this case is unnecessary while considering the preorder traversal. This is because the right child will always come after the left child in the preorder traversal. Thus, omitting the empty braces for the right child also leads to same mapping between the string and the binary tree.</p>
<p align="center"><img alt="Left_child" src="../Figures/606/606_Case3.PNG"></p>
<p>Case 4: Only the right child exists for the current node. In this case, we need to consider the empty braces for the left child. This is because, during the preorder traversal, the left child needs to be considered first. Thus, to indicate that the child following the current node is a right child we need to put a pair of empty braces for the left child. </p>
<p align="center"><img alt="Right_child" src="../Figures/606/606_Case4.PNG"></p>
<p>Just by taking care of the cases, mentioned above, we can obtain the required output string.</p>
<iframe src="https://leetcode.com/playground/AQ3oFiCv/shared" frameborder="0" name="AQ3oFiCv" width="100%" height="411"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The preorder traversal is done over the <script type="math/tex; mode=display">n</script> nodes of the given Binary Tree.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script> in case of a skewed tree.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-iterative-method-using-stack-accepted">Approach #2 Iterative Method Using stack [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In order to solve the given problem, we can also make use of a <script type="math/tex; mode=display">stack</script>. To see how to do it, we'll go through the implementation and we'll also look at the idea behind each step.</p>
<p>We make use of a <script type="math/tex; mode=display">stack</script> onto which various nodes of the given tree will be pushed during the process. The node at the top of the <script type="math/tex; mode=display">stack</script> represents the current node to be processed. Whenever a node has been processed once, it is marked as visited. The reasoning behind this will be discussed soon. </p>
<p>We start off by pushing the root of the binary tree onto the <script type="math/tex; mode=display">stack</script>. Now, the root acts as the current node. For every current node encountered, firstly, we check if it has not been visited already. If not, we add it to the set of visited nodes. </p>
<p>Since, for the preorder traversal, we know, we need to process the nodes in the order current-left-right. Thus, we add a <code>(</code> followed by the current node to the string <script type="math/tex; mode=display">s</script> to be returned. </p>
<p>Now, if both the left and the right children of the current node exist, we need to process them in the order left-right. To do so, we need to push them onto the <script type="math/tex; mode=display">stack</script> in the reverse order, so that when they are picked up later on, their order of processing gets corrected.</p>
<p>Since we've already added <script type="math/tex; mode=display">(current\_node</script> to the string <script type="math/tex; mode=display">s</script>, if only the right child of the current node exists, as discussed in case 4 in the last approach, we need to put a <code>()</code> in <script type="math/tex; mode=display">s</script> representing the null left node. We need not push anything onto the <script type="math/tex; mode=display">stack</script> for the left node and we can directly add the <code>()</code> to <script type="math/tex; mode=display">s</script> for this. But, we still need to push the right child onto the <script type="math/tex; mode=display">stack</script> for future processing. </p>
<p>If only the left child exists, we need not consider the right child at all, as discussed in case 3 in the last approach. We can continue the process by just pushing the left child onto the <script type="math/tex; mode=display">stack</script>.</p>
<p>Now, we need to note that even when a node is being processed, if it has not already been visited, it isn't popped off from the <script type="math/tex; mode=display">stack</script>. But, if a node that has already been processed(i.e. its children have been considered already), it is popped off from the <script type="math/tex; mode=display">stack</script> when encountered again. Such a situation will occur for a node only when the preorder traversal of both its left and right sub-trees has been completely done. Thus, we need to add a <code>)</code> to mark the end of the preorder traversal of the current node as well.</p>
<p>Thus, at the end, we get the required pre-order traversal in the substring <script type="math/tex; mode=display">s(1:n-1)</script>. Here, <script type="math/tex; mode=display">n</script> represents the length of <script type="math/tex; mode=display">s</script>. This is because, we need not put the parentheses(redundant) at the outermost level.</p>
<p>The following animation better depicts the process.</p>
<p>!?!../Documents/Construct_Binary_Tree_stack.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/qvqkT2qU/shared" frameborder="0" name="qvqkT2qU" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">n</script> nodes are pushed and popped in a stack.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">stack</script> size can grow upto <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>