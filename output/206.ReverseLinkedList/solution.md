<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-iterative-accepted">Approach #1 (Iterative) [Accepted]</a></li>
<li><a href="#approach-2-recursive-accepted">Approach #2 (Recursive) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-iterative-accepted">Approach #1 (Iterative) [Accepted]</h4>
<p>Assume that we have linked list <code>1 → 2 → 3 → Ø</code>, we would like to change it to <code>Ø ← 1 ← 2 ← 3</code>.</p>
<p>While you are traversing the list, change the current node's next pointer to point to its previous element. Since a node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!</p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="n">ListNode</span> <span class="nf">reverseList</span><span class="o">(</span><span class="n">ListNode</span> <span class="n">head</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">ListNode</span> <span class="n">prev</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
    <span class="n">ListNode</span> <span class="n">curr</span> <span class="o">=</span> <span class="n">head</span><span class="o">;</span>
    <span class="k">while</span> <span class="o">(</span><span class="n">curr</span> <span class="o">!=</span> <span class="kc">null</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">ListNode</span> <span class="n">nextTemp</span> <span class="o">=</span> <span class="n">curr</span><span class="o">.</span><span class="na">next</span><span class="o">;</span>
        <span class="n">curr</span><span class="o">.</span><span class="na">next</span> <span class="o">=</span> <span class="n">prev</span><span class="o">;</span>
        <span class="n">prev</span> <span class="o">=</span> <span class="n">curr</span><span class="o">;</span>
        <span class="n">curr</span> <span class="o">=</span> <span class="n">nextTemp</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="n">prev</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
Assume that <script type="math/tex; mode=display">n</script> is the list's length, the time complexity is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursive-accepted">Approach #2 (Recursive) [Accepted]</h4>
<p>The recursive version is slightly trickier and the key is to work backwards. Assume that the rest of the list had already been reversed, now how do I reverse the front part? Let's assume the list is: n<sub>1</sub> → … → n<sub>k-1</sub> → n<sub>k</sub> → n<sub>k+1</sub> → … → n<sub>m</sub> → Ø</p>
<p>Assume from node n<sub>k+1</sub> to n<sub>m</sub> had been reversed and you are at node n<sub>k</sub>.</p>
<p>n<sub>1</sub> → … → n<sub>k-1</sub> → <b>n<sub>k</sub></b> → n<sub>k+1</sub> ← … ← n<sub>m</sub></p>
<p>We want n<sub>k+1</sub>’s next node to point to n<sub>k</sub>.</p>
<p>So,</p>
<p>n<sub>k</sub>.next.next = n<sub>k</sub>;</p>
<p>Be very careful that n<sub>1</sub>'s next must point to Ø. If you forget about this, your linked list has a cycle in it. This bug could be caught if you test your code with a linked list of size 2.</p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="n">ListNode</span> <span class="nf">reverseList</span><span class="o">(</span><span class="n">ListNode</span> <span class="n">head</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">head</span> <span class="o">==</span> <span class="kc">null</span> <span class="o">||</span> <span class="n">head</span><span class="o">.</span><span class="na">next</span> <span class="o">==</span> <span class="kc">null</span><span class="o">)</span> <span class="k">return</span> <span class="n">head</span><span class="o">;</span>
    <span class="n">ListNode</span> <span class="n">p</span> <span class="o">=</span> <span class="n">reverseList</span><span class="o">(</span><span class="n">head</span><span class="o">.</span><span class="na">next</span><span class="o">);</span>
    <span class="n">head</span><span class="o">.</span><span class="na">next</span><span class="o">.</span><span class="na">next</span> <span class="o">=</span> <span class="n">head</span><span class="o">;</span>
    <span class="n">head</span><span class="o">.</span><span class="na">next</span> <span class="o">=</span> <span class="kc">null</span><span class="o">;</span>
    <span class="k">return</span> <span class="n">p</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
Assume that <script type="math/tex; mode=display">n</script> is the list's length, the time complexity is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
The extra space comes from implicit stack space due to recursion. The recursion could go up to <script type="math/tex; mode=display">n</script> levels deep.</p>
</li>
</ul>
          </div>
        
      </div>