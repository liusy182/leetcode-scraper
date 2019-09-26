<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursive-approach">Approach 1: Recursive Approach</a></li>
<li><a href="#approach-2-iterative-using-parent-pointers">Approach 2: Iterative using parent pointers</a></li>
<li><a href="#approach-3-iterative-without-parent-pointers">Approach 3: Iterative without parent pointers</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>First the given nodes <code>p</code> and <code>q</code> are to be searched in a binary tree and then their lowest common ancestor is to be found. We can resort to a normal tree traversal to search for the two nodes. Once we reach the desired nodes <code>p</code> and <code>q</code>, we can backtrack and find the lowest common ancestor.</p>
<p></p><center>
<img src="../Figures/236/236_LCA_Binary_1.png" width="600">
</center>
<h4 id="approach-1-recursive-approach">Approach 1: Recursive Approach</h4>
<p><strong>Intuition</strong></p>
<p>The approach is pretty intuitive. Traverse the tree in a depth first manner. The moment you encounter either of the nodes <code>p</code> or <code>q</code>, return some boolean flag. The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would then be the node for which both the subtree recursions return a <code>True</code> flag. It can also be the node which itself is one of <code>p</code> or <code>q</code> and for which one of the subtree recursions returns a <code>True</code> flag.</p>
<p>Let us look at the formal algorithm based on this idea.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Start traversing the tree from the root node.</li>
<li>If the current node itself is one of <code>p</code> or <code>q</code>, we would mark a variable <code>mid</code> as <code>True</code> and continue the search for the other node in the left and right branches.</li>
<li>If either of the left or the right branch returns <code>True</code>, this means one of the two nodes was found below.</li>
<li>If at any point in the traversal, any two of the three flags <code>left</code>, <code>right</code> or <code>mid</code> become <code>True</code>, this means we have found the lowest common ancestor for the nodes <code>p</code> and <code>q</code>.</li>
</ol>
<p>Let us look at a sample tree and we search for the lowest common ancestor of two nodes <code>9</code> and <code>11</code> in the tree.</p>
<p></p><center>
<p>!?!../Documents/236_LCA_Binary_Tree_1.json:770,460!?!</p>
<p></p></center>
<p>Following is the sequence of nodes that are followed in the recursion:</p>
<pre>
1 --&gt; 2 --&gt; 4 --&gt; 8
BACKTRACK 8 --&gt; 4
4 --&gt; 9 (ONE NODE FOUND, return True)
BACKTRACK 9 --&gt; 4 --&gt; 2
2 --&gt; 5 --&gt; 10
BACKTRACK 10 --&gt; 5
5 --&gt; 11 (ANOTHER NODE FOUND, return True)
BACKTRACK 11 --&gt; 5 --&gt; 2

2 is the node where we have left = True and right = True and hence it is the lowest common ancestor.
</pre>

<iframe src="https://leetcode.com/playground/xy87wUjj/shared" frameborder="0" width="100%" height="500" name="xy87wUjj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>. This is because the maximum amount of space utilized by the recursion stack would be <script type="math/tex; mode=display">N</script> since the height of a skewed binary tree could be <script type="math/tex; mode=display">N</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-iterative-using-parent-pointers">Approach 2: Iterative using parent pointers</h4>
<p><strong>Intuition</strong></p>
<p>If we have parent pointers for each node we can traverse back from <code>p</code> and <code>q</code> to get their ancestors. The first common node we get during this traversal would be the LCA node. We can save the parent pointers in a dictionary as we traverse the tree.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Start from the root node and traverse the tree.</li>
<li>Until we find <code>p</code> and <code>q</code> both, keep storing the parent pointers in a dictionary.</li>
<li>Once we have found both <code>p</code> and <code>q</code>, we get all the ancestors for <code>p</code> using the parent dictionary and add to a set called <code>ancestors</code>.</li>
<li>Similarly, we traverse through ancestors for node <code>q</code>. If the ancestor is present in the ancestors set for <code>p</code>, this means this is the first ancestor common between <code>p</code> and <code>q</code> (while traversing upwards) and hence this is the LCA node.</li>
</ol>
<iframe src="https://leetcode.com/playground/CVzZroWp/shared" frameborder="0" width="100%" height="500" name="CVzZroWp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity : <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.</p>
</li>
<li>
<p>Space Complexity : <script type="math/tex; mode=display">O(N)</script>. In the worst case space utilized by the stack, the parent pointer dictionary and the ancestor set, would be <script type="math/tex; mode=display">N</script> each, since the height of a skewed binary tree could be <script type="math/tex; mode=display">N</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-iterative-without-parent-pointers">Approach 3: Iterative without parent pointers</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, we come across the LCA during the backtracking process. We can get rid of the backtracking process itself. In this approach we always have a pointer to the probable LCA and the moment we find both the nodes we return the pointer as the answer.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Start with root node.</li>
<li>Put the <code>(root, root_state)</code> on to the stack. <code>root_state</code> defines whether one of the children or both children of <code>root</code> are left for traversal.</li>
<li>While the stack is not empty, peek into the top element of the stack represented as <code>(parent_node, parent_state)</code>.</li>
<li>Before traversing any of the child nodes of <code>parent_node</code> we check if the <code>parent_node</code> itself is one of <code>p</code> or <code>q</code>.</li>
<li>First time we find either of <code>p</code> or <code>q</code>, set a boolean flag called <code>one_node_found</code> to <code>True</code>. Also start keeping track of the lowest common ancestors by keeping a note of the top index of the stack in the variable <code>LCA_index</code>. Since all the current elements of the stack are ancestors of the node we just found.</li>
<li>The second time <code>parent_node == p or parent_node == q</code> it means we have found both the nodes and we can return the <code>LCA node</code>.</li>
<li>Whenever we visit a child of a <code>parent_node</code> we push the <code>(parent_node, updated_parent_state)</code> onto the stack. We update the state of the parent since a child/branch has been visited/processed and accordingly the state changes.</li>
<li>A node finally gets popped off from the stack when the state becomes <code>BOTH_DONE</code> implying both left and right subtrees have been pushed onto the stack and processed. If <code>one_node_found</code> is <code>True</code> then we need to check if the top node being popped could be one of the ancestors of the found node. In that case we need to reduce <code>LCA_index</code> by one. Since one of the ancestors was popped off.</li>
</ol>
<blockquote>
<p>Whenever both <code>p</code> and <code>q</code> are found, <code>LCA_index</code> would be pointing to an index in the stack which would contain all the common ancestors between <code>p</code> and <code>q</code>. And the <code>LCA_index</code> element has the <code>lowest</code> ancestor common between p and q.</p>
</blockquote>
<p></p><center>
<p>!?!../Documents/236_LCA_Binary_Tree_2.json:770,460!?!</p>
<p></p></center>
<p>The animation above shows how a stack is used to traverse the binary tree and keep track of the common ancestors between nodes <code>p</code> and <code>q</code>.</p>
<iframe src="https://leetcode.com/playground/sFHRnjM7/shared" frameborder="0" width="100%" height="500" name="sFHRnjM7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity : <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree. The advantage of this approach is that we can prune backtracking. We simply return once both the nodes are found.</p>
</li>
<li>
<p>Space Complexity : <script type="math/tex; mode=display">O(N)</script>. In the worst case the space utilized by stack would be <script type="math/tex; mode=display">N</script> since the height of a skewed binary tree could be <script type="math/tex; mode=display">N</script>.</p>
</li>
</ul>
<p><br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>. Approach 2  inspired by <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution">@dietpepsi</a>.</p>
          </div>
        
      </div>