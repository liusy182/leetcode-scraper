<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#initial-thoughts">Initial Thoughts</a></li>
<li><a href="#approach-1-recursion-accepted">Approach #1 Recursion [Accepted]</a></li>
<li><a href="#approach-2-iteration-with-a-stack-accepted">Approach #2 Iteration with a Stack [Accepted]</a></li>
<li><a href="#approach-3-reverse-morris-in-order-traversal-accepted">Approach #3 Reverse Morris In-order Traversal [Accepted]</a></li>
</ul>
</div>
<h4 id="initial-thoughts">Initial Thoughts</h4>
<p>This question asks us to modify an asymptotically linear number of nodes in a
given binary search tree, so a very efficient solution will visit each node
once. The key to such a solution would be a way to visit nodes in descending
order, keeping a sum of all values that we have already visited and adding
that sum to the node's values as we traverse the tree. This method for tree traversal is
known as a
<em>reverse in-order traversal</em>, and allows us to guarantee visitation of each
node in the desired order. The basic idea of such a traversal is that before
visiting any node in the tree, we must first visit all nodes with greater
value. Where are all of these nodes conveniently located? In the right
subtree.</p>
<h4 id="approach-1-recursion-accepted">Approach #1 Recursion [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>One way to perform a reverse in-order traversal is via recursion. By using
the call stack to return to previous nodes, we can easily visit the nodes in
reverse order.</p>
<p><strong>Algorithm</strong></p>
<p>For the recursive approach, we maintain some minor "global" state so each
recursive call can access and modify the current total sum. Essentially, we
ensure that the current node exists, recurse on the right subtree, visit the
current node by updating its value and the total sum, and finally recurse on
the left subtree. If we know that recursing on <code>root.right</code> properly
updates the right subtree and that recursing on <code>root.left</code> properly updates
the left subtree, then we are guaranteed to update all nodes with larger values
before the current node and all nodes with smaller values after.</p>
<iframe src="https://leetcode.com/playground/izz2BZVf/shared" frameborder="0" width="100%" height="276" name="izz2BZVf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>A binary tree has no cycles by definition, so <code>convertBST</code> gets called on
each node no more than once. Other than the recursive calls, <code>convertBST</code>
does a constant amount of work, so a linear number of calls to <code>convertBST</code>
will run in linear time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>Using the prior assertion that <code>convertBST</code> is called a linear number of
times, we can also show that the entire algorithm has linear space
complexity. Consider the worst case, a tree with only right (or only left)
subtrees. The call stack will grow until the end of the longest path is
reached, which in this case includes all <script type="math/tex; mode=display">n</script> nodes.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-iteration-with-a-stack-accepted">Approach #2 Iteration with a Stack [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If we don't want to use recursion, we can also perform a reverse in-order
traversal via iteration and a literal stack to emulate the call stack.</p>
<p><strong>Algorithm</strong></p>
<p>One way to describe the iterative stack method is in terms of the intuitive
recursive solution. First, we initialize an empty stack and set the current
node to the root. Then, so long as there are unvisited nodes in the stack or
<code>node</code> does not point to <code>null</code>, we push all of the nodes along the path to
the rightmost leaf onto the stack. This is equivalent to always processing
the right subtree first in the recursive solution, and is crucial for the
guarantee of visiting nodes in order of decreasing value. Next, we visit the
node on the top of our stack, and consider its left subtree. This is just
like visiting the current node before recursing on the left subtree in the
recursive solution. Eventually, our stack is empty and <code>node</code> points to the
left <code>null</code> child of the tree's minimum value node, so the loop terminates.</p>
<iframe src="https://leetcode.com/playground/U56ntS8W/shared" frameborder="0" width="100%" height="497" name="U56ntS8W"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>The key observation is that each node is pushed onto the stack exactly
once. I will take for granted the assumption that a node will always be
pushed <em>at least</em> once, as the alternative would imply that at least one
node is disconnected from the root. Notice that nodes are only pushed
onto the stack when they are pointed to by <code>node</code> at the beginning of the
outer <code>while</code> loop, or when there is a path to them from such a node by
using only <code>right</code> pointers. Then notice that at the end of each
iteration of the loop, <code>node</code> points to the left child of a node that has
been pushed onto (and subsequently popped from) the stack. Therefore,
because the outer <code>while</code> loop always begins with <code>node</code> pointing to
<code>None</code>, the root (which is not pointed to by any other node), or a left
child of a visited node, we cannot revisit nodes.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>If we assume that the above logic is sound, the assertion that each node is
pushed onto the stack exactly once implies that the stack can contain (at
most) <script type="math/tex; mode=display">n</script> nodes. All other parts of the algorithm use constant space, so
there is overall a linear memory footprint.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-reverse-morris-in-order-traversal-accepted">Approach #3 Reverse Morris In-order Traversal [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>There is a clever way to perform an in-order traversal using only linear time
and constant space, first described by J. H. Morris in his 1979 paper
"Traversing Binary Trees Simply and Cheaply". In general, the recursive and
iterative stack methods sacrifice linear space for the ability to return to a
node after visiting its left subtree. The Morris traversal instead exploits
the unused <code>null</code> pointer(s) of the tree's leaves to create a temporary link
out of the left subtree, allowing the traversal to be performed using only
constant additional memory. To apply it to this problem, we can simply swap
all "left" and "right" references, which will reverse the traversal.</p>
<p><strong>Algorithm</strong></p>
<p>First, we initialize <code>node</code>, which points to the root. Then, until <code>node</code>
points to <code>null</code> (specifically, the left <code>null</code> of the tree's minimum-value
node), we repeat the following. First, consider whether the current node has
a right subtree. If it does not have a right subtree, then there is no
unvisited node with a greater value, so we can visit this node and move into
the left subtree. If it does have a right subtree, then there is at least one
unvisited node with a greater value, and thus we must visit first go to the
right subtree. To do so, we obtain a reference to the in-order successor (the
smallest-value node larger than the current) via our helper function
<code>getSuccessor</code>. This successor node is the node that must be visited
immediately before the current node, so it by definition has a <code>null</code> <code>left</code>
pointer (otherwise it would not be the successor). Therefore, when we first
find a node's successor, we temporarily link it (via its <code>left</code> pointer) to
the node and proceed to the node's right subtree. Then, when we finish
visiting the right subtree, the leftmost <code>left</code> pointer in it will be our
temporary link that we can use to escape the subtree. After following this
link, we have returned to the original node that we previously passed
through, but did not visit. This time, when we find that the successor's
<code>left</code> pointer loops back to the current node, we know that we have visited
the entire right subtree, so we can now erase the temporary link and move
into the left subtree.</p>
<p align="center"><img alt="Reverse Morris Traversal Example" src="../Figures/543/morris.png"></p>
<p>The figure above shows an example of the modified tree during a reverse
Morris traversal. Left pointers are illustrated in blue and right pointers in
red. Dashed edges indicate temporary links generated at some point during the
algorithm (which will be erased before it terminates). Notice that blue edges
can be dashed, as we always exploit the empty <code>left</code> pointer of successor
nodes. Additionally, notice that every node with a right subtree has a link
from its in-order successor.</p>
<iframe src="https://leetcode.com/playground/9fu9CDg3/shared" frameborder="0" width="100%" height="500" name="9fu9CDg3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>Although the Morris traversal does slightly more work than the other
approaches, it is only by a constant factor. To be specific, if we can
show that each edge in the tree is traversed no more than <script type="math/tex; mode=display">k</script> times (for
some constant <script type="math/tex; mode=display">k</script>), then the algorithm is shown to have linear time
complexity. First, note that <code>getSuccessor</code> is called at most twice per
node. On the first invocation, the temporary link back to the node in
question is created, and on the second invocation, the temporary link is
erased. Then, the algorithm steps into the left subtree with no way to
return to the node. Therefore, each edge can only be traversed 3 times:
once when we move the <code>node</code> pointer, and once for each of the two calls
to <code>getSuccessor</code>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>
</p>
<p>Because we only manipulate pointers that already exist, the Morris
traversal uses constant space.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/emptyset/">@emptyset</a>.</p>
          </div>
        
      </div>