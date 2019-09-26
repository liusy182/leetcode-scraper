<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-recursion-conversion-to-array">Approach 2: Recursion + Conversion to Array</a></li>
<li><a href="#approach-3-inorder-simulation">Approach 3: Inorder Simulation</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>The important condition that we have to adhere to in this problem is that we have to create a <code>height balanced</code> binary search tree using the set of nodes given to us in the form of a linked list. The good thing is that the nodes in the linked list are sorted in ascending order.</p>
<p>As we know, a binary search tree is essentially a rooted binary tree with a very special property or relationship amongst its nodes. For a given node of the binary search tree, it's value must be <script type="math/tex; mode=display">\ge</script> the value of <code>all</code> the nodes in the left subtree and <script type="math/tex; mode=display">\le</script> the value of <code>all</code> the nodes in the right subtree. Since a binary tree has a recursive substructure, so does a BST i.e. all the subtrees are binary search trees in themselves.</p>
<p>The main idea in this approach and the next is that:</p>
<blockquote>
<p>the middle element of the given list would form the root of the binary search tree. All the elements to the left of the middle element would form the left subtree recursively. Similarly, all the elements to the right of the middle element will form the right subtree of the binary search tree. This would ensure the height balance required in the resulting binary search tree.</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<ol>
<li>Since we are given a linked list and not an array, we don't really have access to the elements of the list using indexes. We want to know the middle element of the linked list.</li>
<li>We can use the two pointer approach for finding out the middle element of a linked list. Essentially, we have two pointers called <code>slow_ptr</code> and <code>fast_ptr</code>. The <code>slow_ptr</code> moves one node at a time whereas the <code>fast_ptr</code> moves two nodes at a time. By the time the <code>fast_ptr</code> reaches the end of the linked list, the <code>slow_ptr</code> would have reached the middle element of the linked list. For an even sized list, any of the two middle elements can act as the root of the BST.</li>
<li>Once we have the middle element of the linked list, we disconnect the portion of the list to the left of the middle element. The way we do this is by keeping a <code>prev_ptr</code> as well which points to one node before the <code>slow_ptr</code> i.e. <code>prev_ptr.next</code> = <code>slow_ptr</code>. For disconnecting the left portion we simply do <code>prev_ptr.next = None</code></li>
<li>We only need to pass the head of the linked list to the function that converts it to a height balances BST. So, we recurse on the left half of the linked list by passing the original head of the list and on the right half by passing <code>slow_ptr.next</code> as the head.</li>
</ol>
<p>Let's look at this algorithm in action on a sample linked list.</p>
<div>
<center>
<video width="100%" poster="../Figures/109/A1.png" controls>
<source src="../Figures/109/Animation2.mp4" type="video/mp4">
</source></video>
</center>
</div>

<p><br></p>
<iframe src="https://leetcode.com/playground/xhGFXBfU/shared" frameborder="0" width="100%" height="500" name="xhGFXBfU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N\log N)</script>. Suppose our linked list consists of <script type="math/tex; mode=display">N</script> elements. For every list we pass to our recursive function, we have to calculate the middle element for that list. For a list of size <script type="math/tex; mode=display">N</script>, it takes <script type="math/tex; mode=display">N / 2</script> steps to find the middle element i.e. <script type="math/tex; mode=display">O(N)</script> to find the mid. We do this for <strong>every</strong> half of the original linked list. From the looks of it, this seems to be an <script type="math/tex; mode=display">O(N^2)</script> algorithm. However, on closer analysis, it turns out to be a bit more efficient than <script type="math/tex; mode=display">O(N^2)</script>.</p>
<p>Let's look at the number of operations that we have to perform on each of the halves of the linked list. As we mentioned earlier, it takes <script type="math/tex; mode=display">N/2</script> steps to find the middle of a linked list with <script type="math/tex; mode=display">N</script> elements. After finding the middle element, we are left with two halves of size <script type="math/tex; mode=display">N / 2</script> each. Then, we find the middle element for <code>both</code> of these halves and it would take a total of <script type="math/tex; mode=display">2 \times N / 4</script> steps for that. And similarly for the smaller sublists that keep forming recursively. This would give us the following series of operations for a list of size <script type="math/tex; mode=display">N</script>.</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
\frac{N}{2} + 2 \cdot \frac{N}{4} + 4 \cdot \frac{N}{8} + 8 \cdot \frac{N}{16} \; \ldots
\end{aligned}
</script>
</p>
<p>Essentially, this is done <script type="math/tex; mode=display">\log N</script> times since we split the linked list in half every time. Hence, the above equation becomes:</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
&\sum_{i = 1}^{\log N} 2^{i - 1} \cdot \frac{N}{2^i} \\
= \; &\sum_{i = 1}^{\log N}\frac{N}{2} \\
= \; &\frac{N}{2} \; \log N \\
= \; &O(N\log N)
\end{aligned}
</script>
</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(\log N)</script>. Since we are resorting to recursion, there is always the added space complexity of the recursion stack that comes into picture. This could have been <script type="math/tex; mode=display">O(N)</script> for a skewed tree, but the question clearly states that we need to maintain the height balanced property. This ensures the height of the tree to be bounded by <script type="math/tex; mode=display">O(\log N)</script>. Hence, the space complexity is <script type="math/tex; mode=display">O(\log N)</script>.</p>
</li>
</ul>
<p>The main problem with the above solution seems to be the middle element computation. That takes up a lot of unnecessary time and this is due to the nature of the linked list data structure. Let's look at the next solution which tries to overcome this.
<br>
<br></p>
<hr>
<h4 id="approach-2-recursion-conversion-to-array">Approach 2: Recursion + Conversion to Array</h4>
<p>This approach is a classic example of the time-space tradeoff.</p>
<blockquote>
<p>You can get the time complexity down by using more space.</p>
</blockquote>
<p>That's exactly what we're going to do in this approach. Essentially, we will convert the given linked list into an array and then use that array to form our binary search tree. In an array fetching the middle element is a <script type="math/tex; mode=display">O(1)</script> operation and this will bring down the overall time complexity.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Convert the given linked list into an array. Let's call the beginning and the end of the array as <code>left</code> and <code>right</code></li>
<li>Find the middle element as <code>(left + right) / 2</code>. Let's call this element as <code>mid</code>. This is a <script type="math/tex; mode=display">O(1)</script> time operation and is the only major improvement over the previous algorithm.</li>
<li>The middle element forms the root of the BST.</li>
<li>Recursively form binary search trees on the two halves of the array represented by <code>(left, mid - 1)</code> and <code>(mid + 1, right)</code> respectively.</li>
</ol>
<p>Let's look at the implementation for this algorithm and then we will get to the complexity analysis.</p>
<iframe src="https://leetcode.com/playground/c8hTLmwD/shared" frameborder="0" width="100%" height="500" name="c8hTLmwD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: The time complexity comes down to just <script type="math/tex; mode=display">O(N)</script> now since we convert the linked list to an array initially and then we convert the array into a BST. Accessing the middle element now takes <script type="math/tex; mode=display">O(1)</script> time and hence the time complexity comes down.</li>
<li>Space Complexity: Since we used extra space to bring down the time complexity, the space complexity now goes up to <script type="math/tex; mode=display">O(N)</script> as opposed to just <script type="math/tex; mode=display">O(\log N)</script> in the previous solution. This is due to the array we construct initially.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-3-inorder-simulation">Approach 3: Inorder Simulation</h4>
<p><strong>Intuition</strong></p>
<p>As we know, there are three different types of traversals for a binary tree:</p>
<ul>
<li>Inorder</li>
<li>Preorder and</li>
<li>Postorder traversals.</li>
</ul>
<p>The inorder traversal on a binary search tree leads to a very interesting outcome.</p>
<blockquote>
<p>Elements processed in the inorder fashion on a binary search tree turn out to be sorted in ascending order.</p>
</blockquote>
<p>The approach listed here make use of this idea to formulate the construction of a binary search tree. The reason we are able to use this idea in this problem is because we are given a <code>sorted</code> linked list initially.</p>
<p>Before looking at the algorithm, let us look at how the inorder traversal actually leads to a sorted order of nodes' values.</p>
<div>
<center>
<video width="100%" poster="../Figures/109/Inorder_Traversal_1.png" controls>
<source src="../Figures/109/Animation1.mp4" type="video/mp4">
</source></video>
</center>
</div>

<p>The critical idea based on the inorder traversal that we will exploit to solve this problem, is:</p>
<blockquote>
<p>We know that the leftmost element in the inorder traversal has to be the head of our given linked list. Similarly, the next element in the inorder traversal will be the second element in the linked list and so on. This is made possible because the initial list given to us is sorted in ascending order.</p>
</blockquote>
<p>Now that we have an idea about the relationship between the inorder traversal of a binary search tree and the numbers being sorted in ascending order, let's get to the algorithm.</p>
<p><strong>Algorithm</strong></p>
<p>Let's quickly look at a pseudo-code to make the algorithm simple to understand.</p>
<pre>
➔ function formBst(start, end)
➔      mid = (start + end) / 2
➔      formBst(start, mid - 1)
➔
➔      TreeNode(head.val)
➔      head = head.next
➔       
➔      formBst(mid + 1, end)
➔
</pre>

<ol>
<li>Iterate over the linked list to find out it's length. We will make use of two different pointer variables here to mark the beginning and the end of the list. Let's call them <code>start</code> and <code>end</code> with their initial values being <code>0</code> and <code>length - 1</code> respectively.</li>
<li>Remember, we have to simulate the inorder traversal here. We can find out the middle element by using <code>(start + end) / 2</code>. Note that we don't really find out the middle node of the linked list. We just have a variable telling us the index of the middle element. We simply need this to make recursive calls on the two halves.</li>
<li>Recurse on the left half by using <code>start, mid - 1</code> as the starting and ending points.</li>
<li>The invariance that we maintain in this algorithm is that whenever we are done building the left half of the BST, the head pointer in the linked list will point to the root node or the middle node (which becomes the root). So, we simply use the current value pointed to by <code>head</code> as the root node and progress the head node by once i.e. <code>head = head.next</code></li>
<li>We recurse on the right hand side using <code>mid + 1, end</code> as the starting and ending points.</li>
</ol>
<p>Let's look at an animation to make things even clearer.</p>
<div>
<center>
<video width="100%" poster="../Figures/109/B1.png" controls>
<source src="../Figures/109/Animation3.mp4" type="video/mp4">
</source></video>
</center>
</div>

<p><br></p>
<iframe src="https://leetcode.com/playground/V2CBnnrM/shared" frameborder="0" width="100%" height="500" name="V2CBnnrM"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: The time complexity is still <script type="math/tex; mode=display">O(N)</script> since we still have to process each of the nodes in the linked list once and form corresponding BST nodes.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(\log N)</script> since now the only extra space is used by the recursion stack and since we are building a height balanced BST, the height is bounded by <script type="math/tex; mode=display">\log N</script>.</li>
</ul>
<p><br><br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>