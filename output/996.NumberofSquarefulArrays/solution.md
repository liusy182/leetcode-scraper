<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-backtracking">Approach 1: Backtracking</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-backtracking">Approach 1: Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>Construct a graph where an edge from <script type="math/tex; mode=display">i</script> to <script type="math/tex; mode=display">j</script> exists if <script type="math/tex; mode=display">A[i] + A[j]</script> is a perfect square.  Our goal is to investigate Hamiltonian paths of this graph: paths that visit all the nodes exactly once.</p>
<p><strong>Algorithm</strong></p>
<p>Let's keep a current <code>count</code> of what values of nodes are left to visit, and a count <code>todo</code> of how many nodes left to visit.</p>
<p>From each node, we can explore all neighboring nodes (by value, which reduces the complexity blowup).</p>
<p>Please see the inline comments for more details.</p>
<iframe src="https://leetcode.com/playground/bQrNAHHo/shared" frameborder="0" width="100%" height="500" name="bQrNAHHo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^N)</script>, where <script type="math/tex; mode=display">N</script> is length of <code>A</code>.  A tighter bound is outside the scope of this article.  However, it can be shown that the underlying graph is triangle free, as well as other properties that would dramatically shrink this complexity.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach 1</em>, construct an underlying graph.  Since the number of nodes is small, we can use dynamic programming with a 'visited' mask.</p>
<p><strong>Algorithm</strong></p>
<p>We construct the graph in the same method as in <em>Approach 1</em>.</p>
<p>Now, let <code>dfs(node, visited)</code> be the number of ways from <code>node</code> to visit the remaining unvisited nodes.  Here, <code>visited</code> is a mask: <code>(visited &gt;&gt; i) &amp; 1</code> is true if and only if the <code>i</code>th node has been visited.</p>
<p>Afterwards, we may have overcounted if there are repeated values in <code>A</code>.  To account for this, for every <code>x</code> in <code>A</code>, if <code>A</code> contains <code>x</code> a total of <code>k</code> times, we divide the answer by <code>k!</code>.</p>
<iframe src="https://leetcode.com/playground/odBEReYN/shared" frameborder="0" width="100%" height="500" name="odBEReYN"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N 2^N)</script>, where <script type="math/tex; mode=display">N</script> is length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N 2^N)</script>.
<br>
<br></p>
</li>
</ul>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>