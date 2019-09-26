<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-breadth-first-search-accepted">Approach #1: Breadth First Search [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-breadth-first-search-accepted">Approach #1: Breadth First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Instead of thinking of the stops as nodes (of a graph), think of the buses as nodes.  We want to take the least number of buses, which is a shortest path problem, conducive to using a breadth-first search.</p>
<p><strong>Algorithm</strong></p>
<p>We perform a breadth first search on bus numbers.  When we start at <code>S</code>, originally we might be able to board many buses, and if we end at <code>T</code> we may have many <code>targets</code> for our goal state.</p>
<p>One difficulty is to efficiently decide whether two buses are connected by an edge.  They are connected if they share at least one bus stop.  Whether two lists share a common value can be done by set intersection (HashSet), or by sorting each list and using a two pointer approach.</p>
<p>To make our search easy, we will annotate the depth of each node: <code>info[0] = node, info[1] = depth</code>.</p>
<iframe src="https://leetcode.com/playground/fji6uJ5m/shared" frameborder="0" width="100%" height="500" name="fji6uJ5m"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  Let <script type="math/tex; mode=display">N</script> denote the number of buses, and <script type="math/tex; mode=display">b_i</script> be the number of stops on the <script type="math/tex; mode=display">i</script>th bus.</p>
<ul>
<li>
<p>To create the graph, in Python we do <script type="math/tex; mode=display">O(\sum (N - i) b_i)</script> work (we can improve this by checking for which of <code>r1, r2</code> is smaller), while in Java we did a <script type="math/tex; mode=display">O(\sum b_i \log b_i)</script> sorting step, plus our searches are <script type="math/tex; mode=display">O(N \sum b_i)</script> work.</p>
</li>
<li>
<p>Our (breadth-first) search is on <script type="math/tex; mode=display">N</script> nodes, and each node could have <script type="math/tex; mode=display">N</script> edges, so it is <script type="math/tex; mode=display">O(N^2)</script>.</p>
</li>
</ul>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2 + \sum b_i)</script> additional space complexity, the size of <code>graph</code> and <code>routes</code>.  In Java, our space complexity is <script type="math/tex; mode=display">O(N^2)</script> because we do not have an equivalent of <code>routes</code>.  Dual-pivot quicksort (as used in <code>Arrays.sort(int[])</code>) is an in-place algorithm, so in Java we did not increase our space complexity by sorting.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>