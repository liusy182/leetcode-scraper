<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursive-approach">Approach 1: Recursive Approach</a></li>
<li><a href="#approach-2-iterating-method-using-stack">Approach 2: Iterating method using Stack</a></li>
<li><a href="#approach-3-morris-traversal">Approach 3: Morris Traversal</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursive-approach">Approach 1: Recursive Approach</h4>
<p>The first method to solve this problem is using recursion.
This is the classical method and is straightforward. We can define a helper function to implement recursion.</p>
<iframe src="https://leetcode.com/playground/stzQZusR/shared" frameborder="0" width="100%" height="378" name="stzQZusR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The time complexity is <script type="math/tex; mode=display">O(n)</script> because the recursive function is <script type="math/tex; mode=display">T(n) = 2 \cdot T(n/2)+1</script>.</p>
</li>
<li>
<p>Space complexity : The worst case space required is <script type="math/tex; mode=display">O(n)</script>, and in the average case it's <script type="math/tex; mode=display">O(\log n)</script> where <script type="math/tex; mode=display"> n</script> is number of nodes.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-iterating-method-using-stack">Approach 2: Iterating method using Stack</h4>
<p>The strategy is very similiar to the first method, the different is using stack.</p>
<p>Here is an illustration:</p>
<p>!?!../Documents/94_Binary.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/C9344qJ6/shared" frameborder="0" width="100%" height="344" name="C9344qJ6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-morris-traversal">Approach 3: Morris Traversal</h4>
<p>In this method, we have to use a new data structure-Threaded Binary Tree, and the strategy is as follows:</p>
<blockquote>
<p>Step 1: Initialize current as root</p>
<p>Step 2: While current is not NULL,</p>
<div class="codehilite"><pre><span></span>If current does not have left child

    a. Add current’s value

    b. Go to the right, i.e., current = current.right

Else

    a. In current's left subtree, make current the right child of the rightmost node

    b. Go to this left child, i.e., current = current.left
</pre></div>


</blockquote>
<p>For example:</p>
<div class="codehilite"><pre><span></span>          1
        /   \
       2     3
      / \   /
     4   5 6
</pre></div>


<p>First, 1 is the root, so initialize 1 as current, 1 has left child which is 2, the current's left subtree is</p>
<div class="codehilite"><pre><span></span>         2
        / \
       4   5
</pre></div>


<p>So in this subtree, the rightmost node is 5, then make the current(1) as the right child of 5. Set current = cuurent.left (current = 2).
The tree now looks like:</p>
<div class="codehilite"><pre><span></span>         2
        / \
       4   5
            \
             1
              \
               3
              /
             6
</pre></div>


<p>For current 2, which has left child 4, we can continue with thesame process as we did above</p>
<div class="codehilite"><pre><span></span>        4
         \
          2
           \
            5
             \
              1
               \
                3
               /
              6
</pre></div>


<p>then add 4 because it has no left child, then add 2, 5, 1, 3 one by one, for node 3 which has left child 6, do the same as above.
Finally, the inorder taversal is [4,2,5,1,6,3].</p>
<p>For more details, please check
<a href="https://en.wikipedia.org/wiki/Threaded_binary_tree">Threaded binary tree</a> and
<a href="https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion">Explaination of Morris Method</a></p>
<iframe src="https://leetcode.com/playground/osLqwuNN/shared" frameborder="0" width="100%" height="446" name="osLqwuNN"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. To prove that the time complexity is <script type="math/tex; mode=display">O(n)</script>,
the biggest problem lies in finding the time complexity of finding the predecessor nodes of all the nodes in the binary tree.
Intuitively, the complexity is <script type="math/tex; mode=display">O(n\log n)</script>, because to find the predecessor node for a single node related to the height of the tree.
But in fact, finding the predecessor nodes for all nodes only needs <script type="math/tex; mode=display">O(n)</script> time. Because a binary Tree with <script type="math/tex; mode=display">n</script> nodes has <script type="math/tex; mode=display">n-1</script> edges, the whole processing for each edges up to 2 times, one is to locate a node, and the other is to find the predecessor node.
So the complexity is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Arraylist of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
          </div>
        
      </div>