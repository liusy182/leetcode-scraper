<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-stacks-push-on-per-operation-pop-o1-per-operation">Approach #1 (Two Stacks) Push - O(n) per operation, Pop - O(1) per operation.</a></li>
<li><a href="#approach-2-two-stacks-push-o1-per-operation-pop-amortized-o1-per-operation">Approach #2 (Two Stacks) Push - O(1) per operation, Pop - Amortized O(1) per operation.</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for beginners. It introduces the following ideas:
Queue, Stack.</p>
<h2 id="solution">Solution</h2>
<p>Queue is <strong>FIFO</strong> (first in - first out) data structure, in which the elements are inserted from one side - <code>rear</code> and removed from the other - <code>front</code>.
The most intuitive way to implement it is with linked lists, but this article will introduce another approach  using stacks.
Stack is <strong>LIFO</strong> (last in - first out) data structure, in which elements are added and removed from the same end, called <code>top</code>.
To satisfy <strong>FIFO</strong> property of a queue we need to keep two stacks. They serve to reverse arrival order of the  elements and one of them store the queue elements in their final order.</p>
<hr>
<h4 id="approach-1-two-stacks-push-on-per-operation-pop-o1-per-operation">Approach #1 (Two Stacks) Push - <script type="math/tex; mode=display">O(n)</script> per operation, Pop - <script type="math/tex; mode=display">O(1)</script> per operation.</h4>
<p><strong>Algorithm</strong></p>
<p><strong>Push</strong></p>
<p>A queue is FIFO (first-in-first-out) but a stack is LIFO (last-in-first-out). This means the newest element must be pushed to the bottom of the stack. To do so we first transfer all <code>s1</code> elements to auxiliary stack <code>s2</code>. Then the newly arrived element is pushed on top of <code>s2</code> and all its elements are popped and pushed to <code>s1</code>.</p>
<p align="center"><img alt="Push an element in queue" src="https://leetcode.com/media/original_images/232_queue_using_stacksBPush.png" width="539px"></p>
<p align="center"><em>Figure 1. Push an element in queue</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="kt">int</span> <span class="n">front</span><span class="o">;</span>

<span class="kd">public</span> <span class="kt">void</span> <span class="nf">push</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">s1</span><span class="o">.</span><span class="na">empty</span><span class="o">())</span>
        <span class="n">front</span> <span class="o">=</span> <span class="n">x</span><span class="o">;</span>
    <span class="k">while</span> <span class="o">(!</span><span class="n">s1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span>
        <span class="n">s2</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">s1</span><span class="o">.</span><span class="na">pop</span><span class="o">());</span>
    <span class="n">s2</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">x</span><span class="o">);</span>
    <span class="k">while</span> <span class="o">(!</span><span class="n">s2</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span>
        <span class="n">s1</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">s2</span><span class="o">.</span><span class="na">pop</span><span class="o">());</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n)</script>.</li>
</ul>
<p>Each element, with the exception of the newly arrived, is pushed and popped twice. The last inserted element is popped and pushed once. Therefore this gives  <script type="math/tex; mode=display">4 n + 2</script>  operations where <script type="math/tex; mode=display">n</script> is the queue size. The  <code>push</code> and <code>pop</code> operations have <script type="math/tex; mode=display">O(1)</script> time complexity.</p>
<ul>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
We need additional memory to store the queue elements</li>
</ul>
<p><strong>Pop</strong></p>
<p>The algorithm pops an element from  the stack <code>s1</code>, because <code>s1</code> stores always on its top the first inserted element in the queue.
The front element of the queue is kept as <code>front</code>.</p>
<p align="center"><img alt="Pop an element from queue" src="https://leetcode.com/media/original_images/232_queue_using_stacksBPop.png" width="539px"></p>
<p align="center"><em>Figure 2. Pop an element from queue</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="c1">// Removes the element from the front of queue.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">pop</span><span class="o">()</span> <span class="o">{</span>
    <span class="n">s1</span><span class="o">.</span><span class="na">pop</span><span class="o">();</span>
    <span class="k">if</span> <span class="o">(!</span><span class="n">s1</span><span class="o">.</span><span class="na">empty</span><span class="o">())</span>
        <span class="n">front</span> <span class="o">=</span> <span class="n">s1</span><span class="o">.</span><span class="na">peek</span><span class="o">();</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<p><strong>Empty</strong></p>
<p>Stack <code>s1</code> contains all stack elements, so the algorithm checks <code>s1</code> size to return if the queue is empty.</p>
<div class="codehilite"><pre><span></span><span class="c1">// Return whether the queue is empty.</span>
<span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">empty</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">s1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">();</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p><strong>Peek</strong></p>
<p>The <code>front</code> element is kept in constant memory and is modified when we push or pop an element.</p>
<div class="codehilite"><pre><span></span><span class="c1">// Get the front element.</span>
<span class="kd">public</span> <span class="kt">int</span> <span class="nf">peek</span><span class="o">()</span> <span class="o">{</span>
  <span class="k">return</span> <span class="n">front</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.
The <code>front</code> element has been calculated in advance and only returned in <code>peek</code> operation.</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<hr>
<h4 id="approach-2-two-stacks-push-o1-per-operation-pop-amortized-o1-per-operation">Approach #2 (Two Stacks) Push - <script type="math/tex; mode=display">O(1)</script> per operation, Pop - Amortized <script type="math/tex; mode=display">O(1)</script> per operation.</h4>
<p><strong>Algorithm</strong></p>
<p><strong>Push</strong></p>
<p>The newly arrived element is always added on top of stack <code>s1</code> and the first element is kept as <code>front</code> queue element</p>
<p align="center"><img alt="Push an element in queue" src="https://leetcode.com/media/original_images/232_queue_using_stacksAPush.png" width="539px"></p>
<p align="center"><em>Figure 3. Push an element in queue</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="n">Stack</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">s1</span> <span class="o">=</span> <span class="k">new</span> <span class="n">Stack</span><span class="o">&lt;&gt;();</span>
<span class="kd">private</span> <span class="n">Stack</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">s2</span> <span class="o">=</span> <span class="k">new</span> <span class="n">Stack</span><span class="o">&lt;&gt;();</span>

<span class="c1">// Push element x to the back of queue.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">push</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">s1</span><span class="o">.</span><span class="na">empty</span><span class="o">())</span>
        <span class="n">front</span> <span class="o">=</span> <span class="n">x</span><span class="o">;</span>
    <span class="n">s1</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">x</span><span class="o">);</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<p>Аppending an element to a stack is an O(1) operation.</p>
<ul>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
We need additional memory to store the queue elements</li>
</ul>
<p><strong>Pop</strong></p>
<p>We have to remove element in front of the queue. This is the first inserted element in the stack <code>s1</code> and it is positioned at the bottom of the stack because of stack's <code>LIFO (last in - first out)</code> policy. To remove the bottom element  from  <code>s1</code>, we have to pop all elements from <code>s1</code> and to push them on to an additional stack <code>s2</code>, which helps us to store the elements of <code>s1</code> in reversed order. This way  the bottom element of <code>s1</code> will be positioned on top of <code>s2</code> and we can simply pop it from stack <code>s2</code>. Once <code>s2</code> is empty, the algorithm transfer data from <code>s1</code> to <code>s2</code> again.</p>
<p align="center"><img alt="Pop an element from stack" src="https://leetcode.com/media/original_images/232_queue_using_stacksAPop.png" width="539px"></p>
<p align="center"><em>Figure 4. Pop an element from stack</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="c1">// Removes the element from in front of queue.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">pop</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">s2</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span> <span class="o">{</span>
        <span class="k">while</span> <span class="o">(!</span><span class="n">s1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span>
            <span class="n">s2</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">s1</span><span class="o">.</span><span class="na">pop</span><span class="o">());</span>
    <span class="o">}</span>
    <span class="n">s2</span><span class="o">.</span><span class="na">pop</span><span class="o">();</span>    
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity: Amortized <script type="math/tex; mode=display">O(1)</script>, Worst-case <script type="math/tex; mode=display">O(n)</script>.</li>
</ul>
<p>In the worst case scenario when stack <code>s2</code> is empty, the algorithm pops <script type="math/tex; mode=display">n</script> elements from stack s1 and pushes <script type="math/tex; mode=display">n</script> elements to <code>s2</code>, where <script type="math/tex; mode=display">n</script> is the queue size. This gives <script type="math/tex; mode=display">2n</script> operations, which is <script type="math/tex; mode=display">O(n)</script>. But when stack <code>s2</code> is not empty the algorithm has <script type="math/tex; mode=display">O(1)</script> time complexity. So what does it mean by Amortized <script type="math/tex; mode=display">O(1)</script>? Please see the next section on Amortized Analysis for more information.</p>
<ul>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<p><strong>Amortized Analysis</strong></p>
<p>Amortized analysis gives the average performance (over time) of each operation in the worst case. The basic idea is that a worst case operation can alter the state in such a way that the worst case cannot occur again for a long time, thus amortizing its cost.</p>
<p>Consider this example where we start with an empty queue with the following sequence of operations applied:</p>
<p>
<script type="math/tex; mode=display">
push_1, push_2, \ldots, push_n, pop_1,pop_2 \ldots, pop_n
</script>
</p>
<p>The worst case time complexity of a single pop operation is <script type="math/tex; mode=display">O(n)</script>. Since we have <script type="math/tex; mode=display">n</script> pop operations, using the worst-case per operation analysis gives us a total of <script type="math/tex; mode=display">O(n^2)</script> time.</p>
<p>However, in a sequence of operations the worst case does not occur often in each operation - some operations may be cheap, some may be expensive. Therefore, a traditional worst-case per operation analysis can give overly pessimistic bound. For example, in a dynamic array only some inserts take a linear time, though others - a constant time.</p>
<p>In the example above, the number of times pop operation can be called is limited by the number of push operations before it. Although a single pop operation could be expensive, it is expensive only once per <code>n</code> times (queue size), when <code>s2</code> is empty and there is a need for data transfer between <code>s1</code> and <code>s2</code>. Hence the total time complexity of the sequence is : <code>n</code> (for push operations) + <code>2*n</code> (for first pop operation) + <code>n - 1</code> ( for pop operations) which is <script type="math/tex; mode=display">O(2*n)</script>.This gives <script type="math/tex; mode=display">O(2n/2n)</script> = <script type="math/tex; mode=display">O(1)</script> average time per operation.</p>
<p><strong>Empty</strong></p>
<p>Both stacks <code>s1</code> and <code>s2</code> contain all stack elements, so the algorithm checks <code>s1</code> and <code>s2</code> size to return if the queue is empty.</p>
<div class="codehilite"><pre><span></span><span class="c1">// Return whether the queue is empty.</span>
<span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">empty</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">s1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">()</span> <span class="o">&amp;&amp;</span> <span class="n">s2</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">();</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p><strong>Peek</strong></p>
<p>The <code>front</code> element is kept in constant memory and is modified when we push an element. When <code>s2</code> is not empty, front element is positioned on the top of <code>s2</code></p>
<div class="codehilite"><pre><span></span><span class="c1">// Get the front element.</span>
<span class="kd">public</span> <span class="kt">int</span> <span class="nf">peek</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(!</span><span class="n">s2</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span> <span class="o">{</span>
            <span class="k">return</span> <span class="n">s2</span><span class="o">.</span><span class="na">peek</span><span class="o">();</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="n">front</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>The <code>front</code> element was either previously calculated or returned as a top element of stack <code>s2</code>. Therefore complexity is <script type="math/tex; mode=display">O(1)</script>
</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>Analysis written by: @elmirap.</p>
          </div>
        
      </div>