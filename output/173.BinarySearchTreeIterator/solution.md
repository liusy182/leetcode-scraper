<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-flattening-the-bst">Approach 1: Flattening the BST</a></li>
<li><a href="#approach-2-controlled-recursion">Approach 2: Controlled Recursion</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>Before looking at the solutions for this problem, let's try and boil down what the problem statement essentially asks us to do. So, we need to implement an iterator class with two functions namely <code>next()</code> and <code>hasNext()</code>. The <code>hasNext()</code> function returns a boolean value indicating whether there are any more elements left in the binary search tree or not. The <code>next()</code> function returns the next smallest element in the BST. Therefore, the first time we call the <code>next()</code> function, it should return the smallest element in the BST and likewise, when we call <code>next()</code> for the very last time, it should return the largest element in the BST. </p>
<p>You might be wondering as to what could be the use case for an iterator. Essentially, an iterator can be used to <em>iterate over</em> any container object. For our purpose, the container object is a binary search tree. If such an iterator is defined, then the traversal logic can be abstracted out and we can simply make use of the iterator to process the elements in a certain order.</p>
<div class="codehilite"><pre><span></span><span class="mf">1.</span> <span class="n">new_iterator</span> <span class="o">=</span> <span class="n">BSTIterator</span><span class="p">(</span><span class="n">root</span><span class="p">);</span>
<span class="mf">2.</span> <span class="k">while</span> <span class="p">(</span><span class="n">new_iterator</span><span class="o">.</span><span class="n">hasNext</span><span class="p">())</span>
<span class="mf">3.</span>     <span class="n">process</span><span class="p">(</span><span class="n">new_iterator</span><span class="o">.</span><span class="n">next</span><span class="p">());</span>
</pre></div>


<p>Now that we know the motivation behind designing a good iterator class for a data structure, let's take a look at another interesting aspect about the iterator that we have to build for this problem. Usually, an iterator simply goes over each of the elements of the container one by one. For the BST, we want the iterator to return elements in an ascending order.</p>
<blockquote>
<p>An important property of the binary search tree is that the inorder traversal of a BST gives us the elements in a sorted order. Thus, the inorder traversal will be the core of the solutions that we will look ahead.</p>
</blockquote>
<p>!?!../Documents/173_anim.json:770,405!?!</p>
<hr>
<h4 id="approach-1-flattening-the-bst">Approach 1: Flattening the BST</h4>
<p><strong>Intuition</strong></p>
<p>In computer programming, an iterator is an object that enables a programmer to traverse a container, particularly lists. This is the Wikipedia definition of an iterator. Naturally, the easiest way to implement an iterator would be on an array like container interface. So, if we had an array, all we would need is a pointer or an index and we could easily implement the two required functions <code>next()</code> and <code>hasNext()</code>.</p>
<p>Hence, the first approach that we will look at is based on this idea. We will be using additional memory and we will flatten the binary search tree into an array. Since we need the elements to be in a sorted order, we will do an inorder traversal over the tree and store the elements in a new array and then build the iterator functions using this new array.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize an empty array that will contain the nodes of the binary search tree in the sorted order. </li>
<li>We traverse the binary search tree in the inorder fashion and for each node that we process, we add it to our array <code>nodes</code>. Note that before processing a node, its left subtree has to be processed (or recursed upon) and after processing a node, its right subtree has to be recursed upon.</li>
<li>Once we have all the nodes in an array, we simply need a pointer or an index in that array to implement the two functions <code>next</code> and <code>hasNext</code>. Whenever there's a call to <code>hasNext</code>, we simply check if the index has reached the end of the array or not. For the call to <code>next</code> function, we simply return the element pointed by the index. Also, after a the <code>next</code> function call is made, we have to move the index one step forward to simulate the progress of our iterator. </li>
</ol>
<p></p><center>
<img src="../Figures/173/appr_1.png"></center>
<iframe src="https://leetcode.com/playground/wjgc9wdu/shared" frameborder="0" width="100%" height="500" name="wjgc9wdu"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(N)</script> is the time taken by the constructor for the iterator. The problem statement only asks us to analyze the complexity of the two functions, however, when implementing a class, it's important to also note the time it takes to initialize a new object of the class and in this case it would be linear in terms of the number of nodes in the BST. In addition to the space occupied by the new array we initialized, the recursion stack for the inorder traversal also occupies space but that is limited to <script type="math/tex; mode=display">O(h)</script> where <script type="math/tex; mode=display">h</script> is the height of the tree.<ul>
<li><code>next()</code> would take <script type="math/tex; mode=display">O(1)</script>
</li>
<li><code>hasNext()</code> would take <script type="math/tex; mode=display">O(1)</script>
</li>
</ul>
</li>
<li>Space complexity : <script type="math/tex; mode=display">O(N)</script> since we create a new array to contain all the nodes of the BST. This doesn't comply with the requirement specified in the problem statement that the maximum space complexity of either of the functions should be <script type="math/tex; mode=display">O(h)</script> where <script type="math/tex; mode=display">h</script> is the height of the tree and for a well balanced BST, the height is usually <script type="math/tex; mode=display">logN</script>. So, we get great time complexities but we had to compromise on the space. Note that the new array is used for both the function calls and hence the space complexity for both the calls is <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-controlled-recursion">Approach 2: Controlled Recursion</h4>
<p><strong>Intuition</strong></p>
<p>The approach we saw earlier uses space which is linear in the number of nodes in the binary search tree. However, the reason we had to resort to such an approach was because we can control the iteration over the array. We can't really <em>pause</em> a recursion in between and then start it off sometime later. </p>
<blockquote>
<p>However, if we could simulate a controlled recursion for an inorder traversal, we wouldn't really need to use any additional space other than the space used by the stack for our recursion simulation. </p>
</blockquote>
<p>So, this approach essentially uses a custom stack to simulate the inorder traversal i.e. we will be taking an iterative approach to inorder traversal rather than going with the recursive approach and in doing so, we will be able to easily implement the two function calls without any other additional space. </p>
<p>Things however, do get a bit complicated as far as the time complexity of the two operations is concerned and that is where we will spend a little bit of time to understand if this approach complies with all the asymptotic complexity requirements of the question. Let's move on to the algorithm for now to look at this idea more concretely.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize an empty stack <code>S</code> which will be used to simulate the inorder traversal for our binary search tree. Note that we will be following the same approach for inorder traversal as before except that now we will be using our own stack rather than the system stack. Since we are using a custom data structure, we can <em>pause</em> and <em>resume</em> the recursion at will.</li>
<li>
<p>Let's also consider a helper function that we will be calling again and again in the implementation. This function, called <code>_inorder_left</code> will essentially add all the nodes in the leftmost branch of the tree rooted at the given node <code>root</code> to the stack and it will keep on doing so until there is no <code>left</code> child of the <code>root</code> node. Something like the following code:</p>
<p></p><pre>def inorder_left(root):
  while (root):
    S.append(root)
    root = root.left</pre>
<p>For a given node <code>root</code>, the next smallest element will <em>always</em> be the leftmost element in its tree. So, for a given root node, we keep on following the leftmost branch until we reach a node which doesn't have a left child and that will be the next smallest element. For the root of our BST, this leftmost node would be the smallest node in the tree. Rest of the nodes are added to the stack because they are pending processing. Try and relate this with a dry run of a simple recursive inorder traversal and things will make a bit more sense. </p>
</li>
<li>
<p>The first time <code>next()</code> function call is made, the smallest element of the BST has to be returned and then our simulated recursion has to move one step forward i.e. move onto the next smallest element in the BST. The invariant that will be maintained in this algorithm is that the stack top always contains the element to be returned for the <code>next()</code> function call. However, there is additional work that needs to be done to maintain that invariant. It's very easy to implement the <code>hasNext()</code> function since all we need to check is if the stack is empty or not. So, we will only focus on the <code>next()</code> call from now. </p>
</li>
<li>
<p>Initially, given the root node of the BST, we call the function <code>_inorder_left</code> and that ensures our invariant holds. Let's see this first step with an example.</p>
<p></p><center>
<img src="../Figures/173/approach_2-1.png" width="700"></center>
</li>
<li>
<p>Suppose we get a call to the <code>next()</code> function. The node which we have to return i.e. the next smallest element in the binary search tree iterator is the one sitting at the top of our stack. So, for the example above, that node would be <code>2</code> which is the correct value. Now, there are two possibilities that we have to deal with:</p>
<ul>
<li>One is where the node at the top of the stack is actually a leaf node. This is the best case and here we don't have to do anything. Simply pop the node off the stack and return its value. So, this would be a constant time operation.</li>
<li>
<p>Second is where the node has a <code>right</code> child. We don't need to check for the left child because of the way we have added nodes onto the stack. The topmost node either won't have a <code>left</code> child or would already have the <code>left</code> subtree processed. If it has a <code>right</code> child, then we call our helper function on the node's right child. This would comparatively be a costly operation depending upon the structure of the tree.</p>
<p></p><center>
<img src="../Figures/173/approach_2-2.png" width="700"></center>
</li>
</ul>
</li>
<li>
<p>We keep on maintaining the invariant this way in the function call for <code>next</code> and this way we will always be able to return the next smallest element in the BST from the top of the stack. Again, it's important to understand that obtaining the next smallest element doesn't take much time. However, some time is spent in maintaining the invariant that the stack top will <em>always</em> have the node we are looking for.       </p>
</li>
</ol>
<iframe src="https://leetcode.com/playground/Mu4q3jYZ/shared" frameborder="0" width="100%" height="500" name="Mu4q3jYZ"></iframe>

<p><strong>Complexity analysis</strong>        </p>
<ul>
<li>
<p>Time complexity : The time complexity for this approach is very interesting to analyze. Let's look at the complexities for both the functions in the class:</p>
<ul>
<li><code>hasNext</code> is the easier of the lot since all we do in this is to return true if there are any elements left in the stack. Otherwise, we return false. So clearly, this is an <script type="math/tex; mode=display">O(1)</script> operation every time. Let's look at the more complicated function now to see if we satisfy all the requirements in the problem statement</li>
<li>
<p><code>next</code> involves two major operations. One is where we pop an element from the stack which becomes the next smallest element to return. This is a <script type="math/tex; mode=display">O(1)</script> operation. However, we then make a  call to our helper function <code>_inorder_left</code> which iterates over a bunch of nodes. This is clearly a linear time operation i.e. <script type="math/tex; mode=display">O(N)</script> in the worst case. This is true. </p>
<blockquote>
<p>However, the important thing to note here is that we only make such a call for nodes which have a right child. Otherwise, we simply return. Also, even if we end up calling the helper function, it won't always process N nodes. They will be much lesser. Only if we have a skewed tree would there be N nodes for the root. But that is the only node for which we would call the helper function. </p>
</blockquote>
<p>Thus, the amortized (average) time complexity for this function would still be <script type="math/tex; mode=display">O(1)</script> which is what the question asks for. We don't need to have a solution which gives constant time operations for <em>every</em> call. We need that complexity on average and that is what we get. </p>
</li>
</ul>
</li>
<li>
<p>Space complexity: The space complexity is <script type="math/tex; mode=display">O(h)</script> which is occupied by our custom stack for simulating the inorder traversal. Again, we satisfy the space requirements as well as specified in the problem statement.
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>