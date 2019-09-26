<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-framework">Approach Framework</a></li>
<li><a href="#approach-1-dijkstras-accepted">Approach #1: Dijkstra's [Accepted]</a></li>
<li><a href="#approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-framework">Approach Framework</h4>
<p><strong>Explanation</strong></p>
<p>Let <script type="math/tex; mode=display">A^k</script> denote the command <script type="math/tex; mode=display">A A A \cdots A</script> (k times).</p>
<p>Starting with an <code>"R"</code> command doesn't help, and as the final sequence does not end on an <code>"R"</code>, so we have some sequence like <script type="math/tex; mode=display">R A^{k_1} R A^{k_2} \cdots R A^{k_n}</script> which could be instead <script type="math/tex; mode=display">A^{k_2} R A^{k_3} R \cdots A^{k_n} R R A^{k_1}</script> for the same final position of the car.  (Here, <script type="math/tex; mode=display">k_i \geq 0</script>, where <script type="math/tex; mode=display">A^0</script> means no command.)</p>
<p>So let's suppose our command is always of the form <script type="math/tex; mode=display">A^{k_1} R A^{k_2} R \cdots A^{k_n}</script>.  Note that under such a command, the car will move to final position <script type="math/tex; mode=display">(2^{k_1} - 1) - (2^{k_2} - 1) + (2^{k_3} - 1) - \cdots </script>.</p>
<p>Without loss of generality, we can say that (<script type="math/tex; mode=display">k_i</script>, <script type="math/tex; mode=display">i</script> odd) is monotone decreasing, and (<script type="math/tex; mode=display">k_i</script>, <script type="math/tex; mode=display">i</script> even) is also monotone decreasing.</p>
<p>Also because terms will cancel out, we can also ignore the possibility that <script type="math/tex; mode=display">k_i = k_j</script> (for <script type="math/tex; mode=display">i, j</script> with different parity).</p>
<p>A key claim is that <script type="math/tex; mode=display">k_i</script> is bounded by <script type="math/tex; mode=display">a+1</script>, where <script type="math/tex; mode=display">a</script> is the smallest integer such that <script type="math/tex; mode=display">2^a \geq \text{target}</script> - basically, if you drive past the target, you don't need to keep driving.  This is because it adds another power of two (as <script type="math/tex; mode=display">2^{k_i} - 1 = \sum_{j < k_i} 2^j</script>) to the position that must get erased by one or more negative terms later (in whole or in part), as it is not part of the target.</p>
<hr>
<h4 id="approach-1-dijkstras-accepted">Approach #1: Dijkstra's [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>With some <code>target</code>, we have different moves we can perform (such as <script type="math/tex; mode=display">k_1 = 0, 1, 2, \cdots</script>, using the notation from our <em>Approach Framework</em>), with different costs.</p>
<p>This is an ideal setup for Dijkstra's algorithm, which can help us find the shortest cost path in a weighted graph.  </p>
<p><strong>Algorithm</strong></p>
<p>Dijkstra's algorithm uses a priority queue to continually searches the path with the lowest cost to destination, so that when we reach the target, we know it must have been through the lowest cost path.  Refer to <a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">this link</a> for more detail.</p>
<p>Back to the problem, as described above, we have some <code>barrier</code> where we are guaranteed to never cross.  We will also handle negative targets; in total we will have <code>2 * barrier + 1</code> nodes.</p>
<p>After, we could move <code>walk = 2**k - 1</code> steps for a cost of <code>k + 1</code> (the <code>1</code> is to reverse).  If we reach our destination exactly, we don't need the <code>R</code>, so it is just <code>k</code> steps.</p>
<iframe src="https://leetcode.com/playground/qNruc33Y/shared" frameborder="0" width="100%" height="500" name="qNruc33Y"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(T \log T)</script>.  There are <script type="math/tex; mode=display">O(T)</script> nodes, we process each one using <script type="math/tex; mode=display">O(\log T)</script> work (both popping from the heap and adding the edges).</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(T)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in our <em>Approach Framework</em>, we've framed the problem as a series of moves <script type="math/tex; mode=display">k_i</script>.</p>
<p>Now say we have some target <code>2**(k-1) &lt;= t &lt; 2**k</code> and we want to know the cost to go there, if we know all the other costs <code>dp[u]</code> (for <code>u &lt; t</code>).</p>
<p>If <code>t == 2**k - 1</code>, the cost is just <code>k</code>: we use the command <script type="math/tex; mode=display">A^k</script>, and clearly we can't do better.</p>
<p>Otherwise, we might drive without crossing the target for a position change of <script type="math/tex; mode=display">2^{k-1} - 2**j</script>, by the command <script type="math/tex; mode=display">A^{k-1} R A^{j} R</script>, for a total cost of <script type="math/tex; mode=display">k - 1 + j + 2</script>.</p>
<p>Finally, we might drive <script type="math/tex; mode=display">2^k - 1</script> which crosses the target, by the command <script type="math/tex; mode=display">A^k R</script>, for a total cost of <script type="math/tex; mode=display">k + 1</script>.</p>
<p>We can use dynamic programming together with the above recurrence to implement the code below.</p>
<iframe src="https://leetcode.com/playground/ZF65uxfa/shared" frameborder="0" width="100%" height="412" name="ZF65uxfa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(T \log T)</script>.  Each node <code>i</code> does <script type="math/tex; mode=display">\log i</script> work.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(T)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>