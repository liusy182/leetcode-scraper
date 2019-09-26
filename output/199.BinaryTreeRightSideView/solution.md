<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#initial-thoughts">Initial Thoughts</a></li>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1 Depth-First Search [Accepted]</a></li>
<li><a href="#approach-2-breadth-first-search-accepted">Approach #2 Breadth-First Search [Accepted]</a></li>
</ul>
</div>
<h4 id="initial-thoughts">Initial Thoughts</h4>
<p>Because the tree topography is unknown ahead of time, it is not possible to
design an algorithm that visits asymptotically fewer than <script type="math/tex; mode=display">n</script> nodes.
Therefore, we should try to aim for a linear time solution. With that in
mind, let's consider a few equally-efficient solutions.</p>
<h4 id="approach-1-depth-first-search-accepted">Approach #1 Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can efficiently obtain the right-hand view of the binary tree if we visit
each node in the proper order.</p>
<p><strong>Algorithm</strong></p>
<p>One of the aforementioned orderings is defined by a depth-first search in
which we always visit the right subtree first. This guarantees that the first
time we visit a particular depth of the tree, the node that we are visiting
is the rightmost node at that depth. Therefore, we can store the value of the
first node that we visit at each depth, ultimately generating a final array
of values once we know exactly how many layers are in the tree.</p>
<p align="center"><img alt="Depth-First Search" src="../Figures/199/199_depth_first.png"></p>
<p>The figure above illustrates one instance of the problem. The red nodes
compose the solution from top to bottom, and the edges are labelled in order
of visitation.</p>
<iframe src="https://leetcode.com/playground/U8377M7P/shared" frameborder="0" width="100%" height="500" name="U8377M7P"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
<p>Because a binary tree with only child pointers is <em>directed acyclic graph</em>
with only one source node, a traversal of the tree from the root will visit
each node exactly once (plus a sublinear amount of leaves, represented as
<code>None</code>). Each visitation requires only <script type="math/tex; mode=display">O(1)</script> work, so the while loop
runs in linear time. Finally, building the array of rightmost values is
<script type="math/tex; mode=display">O(</script>height of the tree<script type="math/tex; mode=display">) = O(n)</script> because it is not possible for a
right-hand view of the tree to contain more nodes than the tree itself.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
<p>At worst, our stack will contain a number of nodes close to the height of
the tree. Because we are exploring the tree in a depth-first order, there
are never two nodes from different subtrees of the same parent node on the
stack at once. Said another way, the entire right subtree of a node will be
visited before any nodes of the left subtree are pushed onto the stack. If
this logic is applied recursively down the tree, it follows that the stack
will be largest when we have reached the end of the tree's longest path
(the height of the tree). However, because we know nothing about the tree's
topography, the height of the tree may be equivalent to <script type="math/tex; mode=display">n</script>, causing the
space complexity to degrade to <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-breadth-first-search-accepted">Approach #2 Breadth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Much like depth-first search can guarantee that we visit a depth's rightmost
node first, breadth-first search can guarantee that we visit it <em>last</em>.</p>
<p><strong>Algorithm</strong></p>
<p>By performing a breadth-first search that enqueues the left child before the
right child, we visit each node in each layer from left to right. Therefore,
by retaining only the most recently visited node per depth, we will have
the rightmost node for each depth once we finish the tree traversal. The
algorithm is unchanged, other than swapping out the stack for a
<code>deque</code><sup id="fnref:1"><a class="footnote-ref" href="#fn:1" rel="footnote">1</a></sup> and removing the containment check before assigning into
<code>rightmost_value_at_depth</code>.</p>
<p align="center"><img alt="Breadth-first Search Example" src="../Figures/199/199_breadth_first.png"></p>
<p>The figure above illustrates the same instance as before, but solved via
breadth-first search. The red nodes compose the solution from top to bottom,
and the edges are labelled in order of visitation.</p>
<iframe src="https://leetcode.com/playground/9Aia2BUi/shared" frameborder="0" width="100%" height="500" name="9Aia2BUi"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
<p>The differences itemized in the <strong>Algorithm</strong> section do not admit
differences in the time complexity analysis between the bread-first and
depth-first search approaches.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
<p>Because breadth-first search visits the tree layer-by-layer, the queue
will be at its largest immediately before visiting the largest layer. The
size of this layer is <script type="math/tex; mode=display">0.5n = O(n)</script> in the worst case (a complete binary
tree).</p>
</li>
</ul>
<hr>
<p><strong>Footnotes</strong></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/emptyset">@emptyset</a></p>
<div class="footnote">
<hr>
<ol>
<li id="fn:1">
<p>The
<a href="https://docs.python.org/3/library/collections.html#collections.deque"><code>deque</code></a>
datatype from the
<a href="https://docs.python.org/3/library/collections.html"><code>collections</code></a> module
supports constant time append/pop from both the head and the tail. If we were
to use a Python <code>list</code>, it would cost us <script type="math/tex; mode=display">O(n)</script> time to remove its head via
<code>list.pop(0)</code>. <a class="footnote-backref" href="#fnref:1" rev="footnote" title="Jump back to footnote 1 in the text">↩</a></p>
</li>
</ol>
</div>
          </div>
        
      </div>