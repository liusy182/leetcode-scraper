<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-queues-push-o1-pop-on">Approach #1 (Two Queues, push - O(1), pop O(n) )</a></li>
<li><a href="#approach-2-two-queues-push-on-pop-o1">Approach #2 (Two Queues, push - O(n), pop O(1) )</a></li>
<li><a href="#approach-3-one-queue-push-on-pop-o1">Approach #3 (One Queue, push - O(n), pop O(1) )</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for beginners. It introduces the following ideas:
Stack, Queue.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-queues-push-o1-pop-on">Approach #1 (Two Queues, push - <script type="math/tex; mode=display">O(1)</script>, pop <script type="math/tex; mode=display">O(n)</script> )</h4>
<p><strong>Intuition</strong></p>
<p>Stack is <strong>LIFO</strong> (last in - first out) data structure, in which elements are added and removed from the same end, called <code>top</code>.
In general stack is implemented using array or linked list, but in the current article we will review a different approach for implementing stack using queues. In contrast queue is <strong>FIFO</strong> (first in - first out) data structure, in which elements are added only from the one side - <code>rear</code> and removed from the other - <code>front</code>. In order to implement stack using queues, we need to maintain two queues <code>q1</code> and <code>q2</code>. Also we will keep top stack element in a constant memory.</p>
<p><strong>Algorithm</strong></p>
<p><strong>Push</strong></p>
<p>The new element is always added to the rear of queue <code>q1</code> and it is kept as <code>top</code> stack element</p>
<p align="center"><img alt="Push an element in stack" src="https://leetcode.com/media/original_images/225_stack_using_queues_pushA.png" width="539px"></p>
<p align="center"><em>Figure 1. Push an element in stack</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="n">Queue</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">q1</span> <span class="o">=</span> <span class="k">new</span> <span class="n">LinkedList</span><span class="o">&lt;&gt;();</span>
<span class="kd">private</span> <span class="n">Queue</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">q2</span> <span class="o">=</span> <span class="k">new</span> <span class="n">LinkedList</span><span class="o">&lt;&gt;();</span>
<span class="kd">private</span> <span class="kt">int</span> <span class="n">top</span><span class="o">;</span>

<span class="c1">// Push element x onto stack.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">push</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">q1</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">x</span><span class="o">);</span>
    <span class="n">top</span> <span class="o">=</span> <span class="n">x</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>. Queue is implemented as linked list and <code>add</code> operation has <script type="math/tex; mode=display">O(1)</script> time complexity.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>
</p>
</li>
</ul>
<p><strong>Pop</strong></p>
<p>We need to remove the element from the top of the stack. This is the last inserted element in <code>q1</code>.
Because queue is FIFO (first in - first out) data structure, the last inserted element could be removed only after all elements, except it, have been removed. For this reason we need to maintain additional queue <code>q2</code>, which will serve as a temporary storage to enqueue the removed elements from q1. The last inserted element in <code>q2</code> is kept as top. Then the algorithm removes the last element in <code>q1</code>. We swap <code>q1</code> with <code>q2</code> to avoid copying all elements from <code>q2</code> to <code>q1</code>.</p>
<p align="center"><img alt="Pop an element from stack" src="https://leetcode.com/media/original_images/225_stack_using_queues_popA.png" width="539px"></p>
<p align="center"><em>Figure 2. Pop an element from stack</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="c1">// Removes the element on top of the stack.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">pop</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">while</span> <span class="o">(</span><span class="n">q1</span><span class="o">.</span><span class="na">size</span><span class="o">()</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">top</span> <span class="o">=</span> <span class="n">q1</span><span class="o">.</span><span class="na">remove</span><span class="o">();</span>
        <span class="n">q2</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">top</span><span class="o">);</span>
    <span class="o">}</span>
    <span class="n">q1</span><span class="o">.</span><span class="na">remove</span><span class="o">();</span>
    <span class="n">Queue</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">temp</span> <span class="o">=</span> <span class="n">q1</span><span class="o">;</span>
    <span class="n">q1</span> <span class="o">=</span> <span class="n">q2</span><span class="o">;</span>
    <span class="n">q2</span> <span class="o">=</span> <span class="n">temp</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The algorithm  dequeues n elements from <code>q1</code> and enqueues <script type="math/tex; mode=display">n - 1</script> elements to <code>q2</code>, where <script type="math/tex; mode=display">n</script> is the stack size. This gives <script type="math/tex; mode=display">2n - 1</script> operations.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<hr>
<h4 id="approach-2-two-queues-push-on-pop-o1">Approach #2 (Two Queues, push - <script type="math/tex; mode=display">O(n)</script>, pop <script type="math/tex; mode=display">O(1)</script> )</h4>
<p><strong>Algorithm</strong></p>
<p><strong>Push</strong></p>
<p>The algorithm inserts each new element to queue <code>q2</code> and keep it as the <code>top</code> element. In case queue <code>q1</code> is not empty (there are elements in the stack), we remove all elements from <code>q1</code> and add them to <code>q2</code>. In this way the new inserted element (<code>top</code> element in the stack) will be always positioned at the front of <code>q2</code>. We swap <code>q1</code> with <code>q2</code> to avoid copying all elements from <code>q2</code> to <code>q1</code>.</p>
<p align="center"><img alt="Push an element in stack" src="https://leetcode.com/media/original_images/225_stack_using_queues_pushB.png" width="539px"></p>
<p align="center"><em>Figure 3. Push an element in stack</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">void</span> <span class="nf">push</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">q2</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">x</span><span class="o">);</span>
    <span class="n">top</span> <span class="o">=</span> <span class="n">x</span><span class="o">;</span>
    <span class="k">while</span> <span class="o">(!</span><span class="n">q1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span> <span class="o">{</span>                
        <span class="n">q2</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">q1</span><span class="o">.</span><span class="na">remove</span><span class="o">());</span>
    <span class="o">}</span>
    <span class="n">Queue</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">temp</span> <span class="o">=</span> <span class="n">q1</span><span class="o">;</span>
    <span class="n">q1</span> <span class="o">=</span> <span class="n">q2</span><span class="o">;</span>
    <span class="n">q2</span> <span class="o">=</span> <span class="n">temp</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The algorithm  removes n elements from <code>q1</code> and inserts <script type="math/tex; mode=display">n + 1</script> elements to <code>q2</code>, where n is the stack size. This gives <script type="math/tex; mode=display">2n + 1</script> operations. The operations <code>add</code> and <code>remove</code> in linked lists has <script type="math/tex; mode=display">O(1)</script> complexity.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<p><strong>Pop</strong></p>
<p>The algorithm dequeues an element from  queue <code>q1</code> and keeps front element of <code>q1</code> as <code>top</code>.</p>
<p align="center"><img alt="Pop an element from stack" src="https://leetcode.com/media/original_images/225_stack_using_queues_popB.png" width="539px"></p>
<p align="center"><em>Figure 4. Pop an element from stack</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="c1">// Removes the element on top of the stack.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">pop</span><span class="o">()</span> <span class="o">{</span>
    <span class="n">q1</span><span class="o">.</span><span class="na">remove</span><span class="o">();</span>
    <span class="k">if</span> <span class="o">(!</span><span class="n">q1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span> <span class="o">{</span>
        <span class="n">top</span> <span class="o">=</span> <span class="n">q1</span><span class="o">.</span><span class="na">peek</span><span class="o">();</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<p>In both approaches <code>empty</code> and <code>top</code> operations have the same implementation.</p>
<p><strong>Empty</strong></p>
<p>Queue <code>q1</code> always contains all stack elements, so the algorithm checks <code>q1</code> size to return if the stack is empty.</p>
<div class="codehilite"><pre><span></span><span class="c1">// Return whether the stack is empty.</span>
<span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">empty</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">q1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">();</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p><strong>Top</strong></p>
<p>The <code>top</code> element is kept in constant memory and is modified each time when we push or pop an element.</p>
<div class="codehilite"><pre><span></span><span class="c1">// Get the top element.</span>
<span class="kd">public</span> <span class="kt">int</span> <span class="nf">top</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">top</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.
 The <code>top</code> element has been calculated in advance and only returned in <code>top</code> operation.</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<hr>
<h4 id="approach-3-one-queue-push-on-pop-o1">Approach #3 (One Queue, push - <script type="math/tex; mode=display">O(n)</script>, pop <script type="math/tex; mode=display">O(1)</script> )</h4>
<p>The mentioned above two approaches have one weakness, they use two queues. This could be optimized as we use only one queue, instead of two.</p>
<p><strong>Algorithm</strong></p>
<p><strong>Push</strong></p>
<p>When we push an element into a queue, it will be stored at back of the queue due to queue's properties.
But we need to implement a stack, where last inserted element should be in the front of the queue, not at the back. To achieve this we can invert the order of queue elements when pushing a new element.</p>
<p align="center"><img alt="Push an element in stack" src="https://leetcode.com/media/original_images/225_stack_using_queues_pushC.png" width="539px"></p>
<p align="center"><em>Figure 5. Push an element in stack</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="n">LinkedList</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">q1</span> <span class="o">=</span> <span class="k">new</span> <span class="n">LinkedList</span><span class="o">&lt;&gt;();</span>

<span class="c1">// Push element x onto stack.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">push</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">q1</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">x</span><span class="o">);</span>
    <span class="kt">int</span> <span class="n">sz</span> <span class="o">=</span> <span class="n">q1</span><span class="o">.</span><span class="na">size</span><span class="o">();</span>
    <span class="k">while</span> <span class="o">(</span><span class="n">sz</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">q1</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">q1</span><span class="o">.</span><span class="na">remove</span><span class="o">());</span>
        <span class="n">sz</span><span class="o">--;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The algorithm  removes n elements and inserts <script type="math/tex; mode=display">n + 1</script> elements to <code>q1</code> , where n is the stack size. This gives <script type="math/tex; mode=display">2n + 1</script> operations. The operations <code>add</code> and <code>remove</code> in linked lists has <script type="math/tex; mode=display">O(1)</script> complexity.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<p><strong>Pop</strong></p>
<p>The last inserted element is always stored at the front of <code>q1</code> and we can pop it for constant time.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="c1">// Removes the element on top of the stack.</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">pop</span><span class="o">()</span> <span class="o">{</span>
    <span class="n">q1</span><span class="o">.</span><span class="na">remove</span><span class="o">();</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<p><strong>Empty</strong></p>
<p>Queue <code>q1</code> contains all stack elements, so the algorithm checks if <code>q1</code> is empty.</p>
<div class="codehilite"><pre><span></span><span class="c1">// Return whether the stack is empty.</span>
<span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">empty</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">q1</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">();</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p><strong>Top</strong></p>
<p>The <code>top</code> element is always positioned at the front of <code>q1</code>. Algorithm return it.</p>
<div class="codehilite"><pre><span></span><span class="c1">// Get the top element.</span>
<span class="kd">public</span> <span class="kt">int</span> <span class="nf">top</span><span class="o">()</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">q1</span><span class="o">.</span><span class="na">peek</span><span class="o">();</span>
<span class="o">}</span>
</pre></div>


<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>Analysis written by: @elmirap.</p>
          </div>
        
      </div>