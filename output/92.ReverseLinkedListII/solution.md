<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-iterative-link-reversal">Approach 2: Iterative Link Reversal.</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>The idea for linked list reversal using recursion springs from a similar idea that we use for reversing an array. If we want to reverse an array, the huge advantage that we have is the availability of indexes. So, what we can do there is to simply have two pointers, one at the beginning of the array and one at the end. We repeatedly swap elements pointed to by these two pointers and we move both the pointers towards the center of the array. Let's quickly look at this simple algorithm on a sample array before we move on to linked lists.</p>
<p></p><center>
<img src="../Figures/92/d1.png">
</center>
<p>The first approach for reversing a portion of the given linked list is based on the similar idea expressed above. Essentially, we want two different pointers, one at the <script type="math/tex; mode=display">m^{th}</script> node from the beginning and another one from the <script type="math/tex; mode=display">n^{th}</script> node from the beginning. Once we have such pointers in place, we can repeatedly swap the data between the nodes and progress these pointers towards each other like we saw in the case of an array.</p>
<blockquote>
<p>However, we don't have any backward pointers in our linked list and neither do we have any indexes. So, we rely on recursion to simulate the backward pointer. Essentially, the backtracking process in a recursion will help us in simulating the backward movement of the pointer from the <script type="math/tex; mode=display">n^{th}</script> node in the linked list towards the center.</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<ol>
<li>We define a recursion function that will do the job of reversing a portion of the linked list.</li>
<li>Let's call this function <code>recurse</code>. The function takes in 3 parameters: <code>m</code> being the starting point of the reversal, <code>n</code> being the ending point for the reversal, and a pointer <code>right</code> which will start at the <script type="math/tex; mode=display">n^{th}</script> node in the linked list and move backwards with the backtracking of the recursion. If this is not clear at the moment, the diagrams that follow will help.</li>
<li>Additionally, we have a pointer called <code>left</code> which starts from the <script type="math/tex; mode=display">m^{th}</script> node in the linked list and moves forward. In Python, we have to take a global variable for this which get's changed with recursion. In other languages, where changes made in function calls persist, we can consider this pointer as an additional variable for the function <code>recurse</code>.</li>
<li>In a recursion call, given <code>m</code>, <code>n</code>, and <code>right</code>, we check if <code>n == 1</code>. If this is the case, we don't need to go any further.</li>
<li>Until we reach <code>n = 1</code>, we keep moving the <code>right</code> pointer one step forward and after doing that, we make a recursive call with the value of <code>n</code> decreased by 1. At the same time, we keep on moving the <code>left</code> pointer forward until <code>m == 1</code>. When we refer to a pointer being moved forward, it essentially means <code>pointer.next</code>.</li>
<li>So we <em>backtrack</em> as soon as <code>n</code> reaches 1. At that point of time, the <code>right</code> pointer is at the last node of the sublist we want to reverse and the <code>left</code> has already reached the first node of this sublist. So, we swap out the data and move the left pointer one step forward using <code>left = left.next</code>. We need this change to persist across the backtracking process.</li>
<li>From there on, every time we backtrack, the <code>right</code> pointer moves one step backwards. This is the simulation we've been mentioning all along. The backward movement is simulated by backtracking.</li>
<li>We stop the swaps when either <code>right == left</code>, which happens if the sublist size is odd, or, <code>right.next == left</code> which happens when during the backtracking process for an even sized sublist, the <code>right</code> pointer crosses <code>left</code>. We use a global boolean flag for stopping the swaps once these conditions are met.</li>
</ol>
<p>Let's look at a series of diagrams explaining the process on a sample linked list. Hopefully, things would be clearer after this.</p>
<p></p><center>
<img src="../Figures/92/recursion-1.png">
</center>
<p>This is the first step in the recursion process. We have a list given to us and the <code>left</code> and the <code>right</code> pointers start off from the <code>head</code> of the linked list. The first step makes a recursive call with updated values of <code>m</code> and <code>n</code> i.e. their values each reduced by 1. Also, the <code>left</code> and the <code>right</code> pointers move one step forward in the linked list.</p>
<p></p><center>
<img src="../Figures/92/recursion-2.png">
</center>
<p>The next two steps show the movement of the <code>left</code> and the <code>right</code> pointers in the list. Notice that after the second step, the <code>left</code> pointer reaches it's designated spot. So, we don't move it any further. Only the <code>right</code> pointer progresses from here on out until it reaches node <code>6</code>.</p>
<p></p><center>
<img src="../Figures/92/recursion-3.png">
</center>
<p>As we can see, after the step 5, both the pointers are in their designated spots in the list and we can start the backtracking process. We don't recurse further. The operation performed during the backtracking is swapping of data between the <code>left</code> and <code>right</code> nodes.</p>
<p></p><center>
<img src="../Figures/92/recursion-4.png">
</center>
<p>The <code>right</code> pointer <em>crosses</em> the <code>left</code> pointer after step 3 (backtracking) as can be seen above and by that point, we have already reversed the required portion of the linked list. We needed the output list to be <code>[7 → 9 → 8 → 1 → 10 → 2 → 6]</code> and that's what we have. So, we don't perform any more swaps and in the code, we can use a global boolean flag to stop the swapping after a point. We can't really <em>break out of recursion per say</em>.</p>
<iframe src="https://leetcode.com/playground/XNyieviy/shared" frameborder="0" width="100%" height="500" name="XNyieviy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N)</script> since we process all the nodes at-most twice. Once during the normal recursion process and once during the backtracking process. During the backtracking process we only just swap half of the list if you think about it, but the overall complexity is <script type="math/tex; mode=display">O(N)</script>.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(N)</script> in the worst case when we have to reverse the entire list. This is the space occupied by the recursion stack.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-iterative-link-reversal">Approach 2: Iterative Link Reversal.</h4>
<p><strong>Intuition</strong></p>
<p>In the previous approach, we looked at an algorithm for reversing a portion of the given linked list such that the underlying structure doesn't change. We only modified the values of the nodes for achieving the reversal. However, it may so happen that you cannot change the data available in the nodes. In that scenario, we have to modify the links themselves to achieve the reversal.</p>
<p>Essentially, starting from the node at position <code>m</code> and all the way up to <code>n</code>, we reverse the <code>next</code> pointers for all the nodes in between. Let's look at the algorithm for achieving this.</p>
<p><strong>Algorithm</strong></p>
<p>Before looking at the algorithm, it's important to understand how the link reversal will work and what set of pointers will be required for the same. Let's say we have a linked list consisting of three different nodes, <code>A → B → C</code> and we want to reverse the links between the nodes and obtain <code>A ← B ← C</code>.</p>
<p>Suppose we have at our disposal, two pointers. One of them points to the node <code>A</code> and the other one points to the node <code>B</code>. Let's call these pointers <code>prev</code> and <code>cur</code> respectively. We can simply use these two pointers to reverse the link between <code>A and B</code>.</p>
<pre>
cur.next = prev
</pre>

<p>The only problem with this is, we don't have a way of progressing further i.e. once we do this, we can't reach the node <code>C</code>. That's why we need a third pointer that will help us continue the link reversal process. So, we do the following instead.</p>
<pre>
third = cur.next
cur.next = prev
prev = cur
cur = third
</pre>

<p>We do the above <em>iteratively</em> and we will achieve what the question asks us to do. Let's look at the steps for the algorithm now.</p>
<ol>
<li>We need two pointers, <code>prev</code> and <code>cur</code> as explained above.</li>
<li>The <code>prev</code> pointer should be initialized to <code>None</code> initially while <code>cur</code> is initialized to the <code>head</code> of the linked list.</li>
<li>We progress the <code>cur</code> pointer one step at a time and the <code>prev</code> pointer follows it.</li>
<li>We keep progressing the two pointers in this way until the <code>cur</code> pointer reaches the <script type="math/tex; mode=display">m^{th}</script> node from the beginning of the list. This is the point from where we start reversing our linked list.</li>
<li>
<p>An important thing to note here is the usage of two additional pointers which we will call as <code>tail</code> and <code>con</code>. The <code>tail</code> pointer points to the <script type="math/tex; mode=display">m^{th}</script> node from the beginning of the linked list and we call it a <em>tail</em> pointer since this node becomes the tail of the reverse sublist. The <code>con</code> points to the node one before <script type="math/tex; mode=display">m^{th}</script> node and this connects to the new head of the reversed sublist. Let's take a look at a figure to understand these two pointers better.</p>
<p></p><center>
<img src="../Figures/92/tail_and_con.png">
</center>
</li>
<li>
<p>The <code>tail</code> and the <code>con</code> pointers are set once initially and then used in the end to finish the linked list reversal.</p>
</li>
<li>Once we reach the <script type="math/tex; mode=display">m^{th}</script> node, we iteratively reverse the links as explained before using the two pointers. We keep on doing this until we are done reversing the link (next pointer) for the <script type="math/tex; mode=display">n^{th}</script> node. At that point, the <code>prev</code> pointer would point to the <script type="math/tex; mode=display">n^{th}</script> node.</li>
<li>We use the <code>con</code> pointer to attach to the <code>prev</code> pointer since the node now pointed to by the <code>prev</code> pointer (the <script type="math/tex; mode=display">n^{th}</script> node from the beginning) will come in place of the <script type="math/tex; mode=display">m^{th}</script> node due after the reversal. Similarly, we will make use of the <code>tail</code> pointer to connect to the node next to the <code>prev</code> node i.e. <script type="math/tex; mode=display">(n+1)^{th}</script> node from the beginning.</li>
</ol>
<p>Let's have a look at the algorithm execute on a sample linked list to make the use case for all these pointers clearer. We are given a linked list initially with elements <code>7 → 9 → 2 → 10 → 1 → 8 → 6</code> and we need to reverse the list from node 3 through 6.</p>
<p></p><center>
<img src="../Figures/92/iterative-1.png">
</center>
<p>We can see the first few steps of our iterative solution above. The first step shows the initialization of the two pointers and the third step shows us the starting point for the list reversal process.</p>
<p></p><center>
<img src="../Figures/92/iterative-2.png">
</center>
<p>This shows us in detail how the links are reversed and how we move forward after reversing the links between two nodes. This step is done multiple times as shown in the following images.</p>
<p></p><center>
<img src="../Figures/92/iterative-3.png">
</center>
<p></p><center>
<img src="../Figures/92/iterative-4.png">
</center>
<p>As we can see from the above images, now the two pointers have reached their final positions. We are done reversing the sublist that we were required to do i.e. nodes 3 through 6. However, we still have to fix some connections. The next image explains how we use the <code>tail</code> and <code>con</code> pointers to make the final connections.</p>
<p></p><center>
<img src="../Figures/92/iterative-5.png">
</center>
<iframe src="https://leetcode.com/playground/EUGQLPwW/shared" frameborder="0" width="100%" height="500" name="EUGQLPwW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N)</script> considering the list consists of <script type="math/tex; mode=display">N</script> nodes. We process each of the nodes at most once (we don't process the nodes after the <script type="math/tex; mode=display">n^{th}</script> node from the beginning.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(1)</script> since we simply adjust some pointers in the original linked list and only use <script type="math/tex; mode=display">O(1)</script> additional memory for achieving the final result.
<br></li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>