<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-breadth-first-search-accepted">Approach #1: Breadth First Search [Accepted]</a></li>
<li><a href="#approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-breadth-first-search-accepted">Approach #1: Breadth First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>A path 'state' can be represented as the subset of nodes visited, plus the current 'head' node.  Then, the problem reduces to a shortest path problem among these states, which can be solved with a breadth-first search.</p>
<p><strong>Algorithm</strong></p>
<p>Let's call the set of nodes visited by a path so far the <em>cover</em>, and the current node as the <em>head</em>.  We'll store the <code>cover</code> states using set bits: <code>k</code> is in the cover if the <code>k</code>th bit of <code>cover</code> is 1.</p>
<p>For states <code>state = (cover, head)</code>, we can perform a breadth-first search on these states.  The neighbors are <code>(cover | (1 &lt;&lt; child), child)</code> for each <code>child in graph[head]</code>.</p>
<p>If at any point we find a state with all set bits in it's cover, because it is a breadth-first search, we know this must represent the shortest path length.</p>
<iframe src="https://leetcode.com/playground/RSKL3uRn/shared" frameborder="0" width="100%" height="500" name="RSKL3uRn"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^N * N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(2^N * N)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>A path 'state' can be represented as the subset of nodes visited, plus the current 'head' node.  As in Approach #1, we have a recurrence in states: <code>answer(cover, head)</code> is <code>min(1 + answer(cover | (1&lt;&lt;child), child) for child in graph[head])</code>.  Because these states form a DAG (a directed graph with no cycles), we can do dynamic programming.</p>
<p><strong>Algorithm</strong></p>
<p>Let's call the set of nodes visited by a path so far the <em>cover</em>, and the current node as the <em>head</em>.  We'll store <code>dist[cover][head]</code> as the length of the shortest path with that cover and head.  We'll store the <code>cover</code> states using set bits, and maintain the loop invariant (on <code>cover</code>), that <code>dist[k][...]</code> is correct for <code>k &lt; cover</code>.</p>
<p>For every state <code>(cover, head)</code>, the possible <code>next</code> (neighbor) nodes in the path are found in <code>graph[head]</code>.  The new <code>cover2</code> is the old cover plus <code>next</code>.</p>
<p>For each of these, we perform a "relaxation step" (for those familiar with the Bellman-Ford algorithm), where if the new candidate distance for <code>dist[cover2][next]</code> is larger than <code>dist[cover][head] + 1</code>, we'll update it to <code>dist[cover][head] + 1</code>.</p>
<p>Care must be taken to perform the relaxation step multiple times on the same cover if <code>cover = cover2</code>.  This is because a minimum state for <code>dist[cover][head]</code> might only be achieved through multiple steps through some path.</p>
<p>Finally, it should be noted that we are using implicitly the fact that when iterating <code>cover = 0 .. (1&lt;&lt;N) - 1</code>, that each new cover <code>cover2 = cover | 1 &lt;&lt; x</code> is such that <code>cover2 &gt;= cover</code>.  This implies a topological ordering, which means that the recurrence on these states form a DAG.</p>
<iframe src="https://leetcode.com/playground/f8jJAcDL/shared" frameborder="0" width="100%" height="500" name="f8jJAcDL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^N * N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(2^N * N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>