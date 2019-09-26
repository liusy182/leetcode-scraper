<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursive-accepted">Approach #1 (Recursive) [Accepted]</a></li>
<li><a href="#approach-2-iterative-accepted">Approach #2 (Iterative) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursive-accepted">Approach #1 (Recursive) [Accepted]</h4>
<p>This is a classic tree problem that is best-suited for a recursive approach.</p>
<p><strong>Algorithm</strong></p>
<p>The inverse of an empty tree is the empty tree. The inverse of a tree with root <script type="math/tex; mode=display">r</script>, and subtrees <script type="math/tex; mode=display">\mbox{right}</script> and <script type="math/tex; mode=display">\mbox{left}</script>, is a tree with root <script type="math/tex; mode=display">r</script>, whose right subtree is the inverse of <script type="math/tex; mode=display">\mbox{left}</script>, and whose left subtree is the inverse of <script type="math/tex; mode=display">\mbox{right}</script>.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="n">TreeNode</span> <span class="nf">invertTree</span><span class="o">(</span><span class="n">TreeNode</span> <span class="n">root</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">root</span> <span class="o">==</span> <span class="kc">null</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">return</span> <span class="kc">null</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="n">TreeNode</span> <span class="n">right</span> <span class="o">=</span> <span class="n">invertTree</span><span class="o">(</span><span class="n">root</span><span class="o">.</span><span class="na">right</span><span class="o">);</span>
    <span class="n">TreeNode</span> <span class="n">left</span> <span class="o">=</span> <span class="n">invertTree</span><span class="o">(</span><span class="n">root</span><span class="o">.</span><span class="na">left</span><span class="o">);</span>
    <span class="n">root</span><span class="o">.</span><span class="na">left</span> <span class="o">=</span> <span class="n">right</span><span class="o">;</span>
    <span class="n">root</span><span class="o">.</span><span class="na">right</span> <span class="o">=</span> <span class="n">left</span><span class="o">;</span>
    <span class="k">return</span> <span class="n">root</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<p>Since each node in the tree is visited only once, the time complexity is <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n</script> is the number of nodes in the tree. We cannot do better than that, since at the very least we have to visit each node to invert it.</p>
<p>Because of recursion, <script type="math/tex; mode=display">O(h)</script> function calls will be placed on the stack in the worst case, where <script type="math/tex; mode=display">h</script> is the height of the tree. Because <script type="math/tex; mode=display">h\in O(n)</script>, the space complexity is <script type="math/tex; mode=display">O(n)</script>.</p>
<hr>
<h4 id="approach-2-iterative-accepted">Approach #2 (Iterative) [Accepted]</h4>
<p>Alternatively, we can solve the problem iteratively, in a manner similar to breadth-first search.</p>
<p><strong>Algorithm</strong></p>
<p>The idea is that we need to swap the left and right child of all nodes in the tree. So we create a queue to store nodes whose left and right child have not been swapped yet. Initially, only the root is in the queue. As long as the queue is not empty, remove the next node from the queue, swap its children, and add the children to the queue. Null nodes are not added to the queue. Eventually, the queue will be empty and all the children swapped, and we return the original root.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="n">TreeNode</span> <span class="nf">invertTree</span><span class="o">(</span><span class="n">TreeNode</span> <span class="n">root</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">root</span> <span class="o">==</span> <span class="kc">null</span><span class="o">)</span> <span class="k">return</span> <span class="kc">null</span><span class="o">;</span>
    <span class="n">Queue</span><span class="o">&lt;</span><span class="n">TreeNode</span><span class="o">&gt;</span> <span class="n">queue</span> <span class="o">=</span> <span class="k">new</span> <span class="n">LinkedList</span><span class="o">&lt;</span><span class="n">TreeNode</span><span class="o">&gt;();</span>
    <span class="n">queue</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">root</span><span class="o">);</span>
    <span class="k">while</span> <span class="o">(!</span><span class="n">queue</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span> <span class="o">{</span>
        <span class="n">TreeNode</span> <span class="n">current</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="na">poll</span><span class="o">();</span>
        <span class="n">TreeNode</span> <span class="n">temp</span> <span class="o">=</span> <span class="n">current</span><span class="o">.</span><span class="na">left</span><span class="o">;</span>
        <span class="n">current</span><span class="o">.</span><span class="na">left</span> <span class="o">=</span> <span class="n">current</span><span class="o">.</span><span class="na">right</span><span class="o">;</span>
        <span class="n">current</span><span class="o">.</span><span class="na">right</span> <span class="o">=</span> <span class="n">temp</span><span class="o">;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">current</span><span class="o">.</span><span class="na">left</span> <span class="o">!=</span> <span class="kc">null</span><span class="o">)</span> <span class="n">queue</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">current</span><span class="o">.</span><span class="na">left</span><span class="o">);</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">current</span><span class="o">.</span><span class="na">right</span> <span class="o">!=</span> <span class="kc">null</span><span class="o">)</span> <span class="n">queue</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">current</span><span class="o">.</span><span class="na">right</span><span class="o">);</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="n">root</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<p>Since each node in the tree is visited / added to the queue only once, the time complexity is <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n</script> is the number of nodes in the tree.</p>
<p>Space complexity is <script type="math/tex; mode=display">O(n)</script>, since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has <script type="math/tex; mode=display">\lceil \frac{n}{2}\rceil=O(n)</script> leaves.</p>
<p>Analysis written by: @noran</p>
          </div>
        
      </div>