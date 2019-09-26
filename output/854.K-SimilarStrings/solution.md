<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-framework">Approach Framework</a></li>
<li><a href="#approach-1-brute-force-with-dynamic-programming">Approach 1: Brute Force with Dynamic Programming</a></li>
<li><a href="#approach-2-pruned-breadth-first-search">Approach 2: Pruned Breadth First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-framework">Approach Framework</h4>
<p><strong>Explanation</strong></p>
<p>We'll call the <em>underlying graph</em> of the problem, the graph with 6 nodes <code>'a', 'b', ..., 'f'</code> and the edges <code>A[i] -&gt; B[i]</code>.  Our goal is for this graph to have only self-edges (edges of the form <code>a -&gt; a</code>.)  Let's make some deductions about how swaps between <code>A[i]</code> and <code>A[j]</code> affect this graph, and the nature of optimal swap schedules.</p>
<p>If <code>A = 'ca...'</code> and <code>B = 'ab...'</code>, then the first two edges of the underlying graph are <code>c -&gt; a</code> and <code>a -&gt; b</code>; and a swap between <code>A[1]</code> and <code>A[0]</code> changes these two edges to the single edge <code>c -&gt; b</code>.  Let's call this type of operation <em>'cutting corners'</em>.  Intuitively, our optimal swap schedule always increases the number of matches (<code>A[i] == B[i]</code>s) for each swap, so cutting corners is the only type of operation we need to consider.  (This is essentially the <em>happy swap assumption</em>, proved in <a href="https://leetcode.com/articles/couples-holding-hands/">765 - Couples Holding Hands</a>)</p>
<p>Now consider any cycle decomposition of the underlying graph.  [This decomposition (or the number of cycles), is not necessarily unique.]  Through operations of cutting corners, we'll delete all the (non-self) edges.  Each cycle of length <code>k</code> requires <code>k-1</code> operations to delete.  Thus, the answer is just the minimum possible value of <script type="math/tex; mode=display">\sum (C_k - 1)</script>, where <script type="math/tex; mode=display">C_1, \cdots C_k</script> are the lengths of the cycles in some cycle decomposition of the underlying graph.  This can be re-written as <script type="math/tex; mode=display">\text{(Number of non-self edges)} - \text{(Number of cycles)}</script>.  Hence, we want to maximize the number of cycles in a cycle decomposition of the underlying graph.
<br>
<br></p>
<hr>
<h4 id="approach-1-brute-force-with-dynamic-programming">Approach 1: Brute Force with Dynamic Programming</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <script type="math/tex; mode=display">P_1, P_2, \cdots</script> be possible cycles of the underlying graph <script type="math/tex; mode=display">G</script>.  Let's attempt to write <script type="math/tex; mode=display">G = \sum k_i P_i</script> for some constants <script type="math/tex; mode=display">k_i</script>.  Then, the number of cycles is <script type="math/tex; mode=display">\sum k_i</script>.</p>
<p>We can represent <script type="math/tex; mode=display">G</script> and <script type="math/tex; mode=display">P_i</script> as the number of directed edges from node <script type="math/tex; mode=display">X</script> to <script type="math/tex; mode=display">Y</script>.  For example, if <script type="math/tex; mode=display">P_1</script> is the cycle <code>a -&gt; b -&gt; d -&gt; e -&gt; a</code>, then <script type="math/tex; mode=display">P_1</script> is <code>a -&gt; b</code> plus <code>b -&gt; d</code> plus <code>d -&gt; e</code> plus <code>e -&gt; a</code>.  This can be represented as a column vector <code>possibles[0]</code> of 1s and 0s, with four 1s, (each <code>possibles[0][i] == 1</code> represents the <code>i</code>th directed edge being there [and having quantity 1]).  Similarly, the graph <script type="math/tex; mode=display">G</script> can also be represented as a column vector.</p>
<p>This sets the stage for dynamic programming.  For each graph <script type="math/tex; mode=display">G</script>, represented as a column vector, say we want to find <code>numCycles(G)</code>.  We can take all possible cycles <script type="math/tex; mode=display">C</script>, and check if <script type="math/tex; mode=display">G</script> contains <script type="math/tex; mode=display">C</script>.  If it does, then a candidate answer is <code>1 + numCycles(G - C)</code>.</p>
<p>It should also be noted that maximizing the number of cycles cannot be done in a greedy way, ie. by always removing the lowest size cycle.  For example, consider the graph with edges <code>a -&gt; b -&gt; c -&gt; a</code>, <code>b -&gt; d -&gt; e -&gt; b</code>, and <code>c -&gt; e -&gt; f -&gt; c</code>.  Those form cycles, and there is a fourth 3-cycle <code>b -&gt; c -&gt; e -&gt; b</code>.  If we remove that cycle first, then we would have only two cycles; but if we remove the first 3 cycles, then we would have three cycles.</p>
<iframe src="https://leetcode.com/playground/FcbDkuSz/shared" frameborder="0" width="100%" height="500" name="FcbDkuSz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^{N+W})</script>, where <script type="math/tex; mode=display">N</script> is the length of the string, and <script type="math/tex; mode=display">W</script> is the length of the alphabet.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(2^{N+W})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-pruned-breadth-first-search">Approach 2: Pruned Breadth First Search</h4>
<p><strong>Intuition</strong></p>
<p>Based on the <em>underlying graph</em> interpretation of the problem, we can prove that an optimal solution swaps the left-most unmatched character <code>A[i]</code> with an appropriate match <code>A[j] == B[i] (j &gt; i)</code>.</p>
<p>This reduces the number of "neighbors" of a node (string state) from <script type="math/tex; mode=display">O(N^2)</script> to <script type="math/tex; mode=display">O(N)</script>, but it also focuses our search greatly.  Each node searched with <code>k</code> matches, will have at most <script type="math/tex; mode=display">2^k</script> swaps on the unmatched characters.  This leads to <script type="math/tex; mode=display">\sum_k \binom{N}{k} 2^k = 3^N</script> checked states.  Furthermore, some characters are the same, so we must divide the number of states by approximate factors of <script type="math/tex; mode=display">\prod (N_i)!</script> [where <script type="math/tex; mode=display">N_i</script> is the number of occurrences of the <script type="math/tex; mode=display">i</script>th character in <code>A</code>.]  With <script type="math/tex; mode=display">N \leq 20</script>, this means the number of states will be small.</p>
<p><strong>Algorithm</strong></p>
<p>We'll perform a regular breadth-first search.  The neighbors to each node string <code>S</code> are all the strings reachable with 1 swap, that match the first unmatched character in <code>S</code>.</p>
<iframe src="https://leetcode.com/playground/nNLRdQYX/shared" frameborder="0" width="100%" height="500" name="nNLRdQYX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\sum_{k=0}^n \binom{N}{k} \frac{\min(2^k, (N-k)!)}{W * (\frac{N-k}{W})!})</script>, where <script type="math/tex; mode=display">N</script> is the length of the string, and <script type="math/tex; mode=display">W</script> is the length of the alphabet.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N * t)</script>, where <script type="math/tex; mode=display">t</script> is the time complexity given above.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>