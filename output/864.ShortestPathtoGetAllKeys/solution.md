<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-permutations">Approach 1: Brute Force + Permutations</a></li>
<li><a href="#approach-2-points-of-interest-dijkstra">Approach 2: Points of Interest + Dijkstra</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-permutations">Approach 1: Brute Force + Permutations</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We have to pick up the keys <script type="math/tex; mode=display">K</script> in some order, say <script type="math/tex; mode=display">K_{\sigma_i}</script>.</p>
<p>For each ordering, let's do a breadth first search to find the distance to the next key.</p>
<p>For example, if the keys are <code>'abcdef'</code>, then for each ordering such as <code>'bafedc'</code>, we will try to calculate the candidate distance from <code>'@' -&gt; 'b' -&gt; 'a' -&gt; 'f' -&gt; 'e' -&gt; 'd' -&gt; 'c'</code>.</p>
<p>Between each segment of our path (and corresponding breadth-first search), we should remember what keys we've picked up.  Keys that are picked up become part of a mask that helps us identify what locks we are allowed to walk through during the next breadth-first search.</p>
<p>Each part of the algorithm is relatively straightforward, but the implementation in total can be quite challenging.  See the comments for more details.</p>
<iframe src="https://leetcode.com/playground/cJwN3eUy/shared" frameborder="0" width="100%" height="500" name="cJwN3eUy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(R * C * \mathcal{A} * \mathcal{A}!)</script>, where <script type="math/tex; mode=display">R, C</script> are the dimensions of the grid, and <script type="math/tex; mode=display">\mathcal{A}</script> is the maximum number of keys (<script type="math/tex; mode=display">\mathcal{A}</script> because it is the "size of the alphabet".)  Each <code>bfs</code> is performed up to <script type="math/tex; mode=display">\mathcal{A} * \mathcal{A}!</script> times.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(R * C + \mathcal{A}!)</script>, the space for the <code>bfs</code> and to store the candidate key permutations.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-points-of-interest-dijkstra">Approach 2: Points of Interest + Dijkstra</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Clearly, we only really care about walking between points of interest: the keys, locks, and starting position.  We can use this insight to speed up our calculation.</p>
<p>Let's make this intuition more formal: any walk can be decomposed into <em>primitive</em> segments, where each segment (between two points of interest) is primitive if and only if it doesn't touch any other point of interest in between.</p>
<p>Then, we can calculate the distance (of a primitive segment) between any two points of interest, using a breadth first search.</p>
<p>Afterwards, we have some graph (where each node refers to at most <script type="math/tex; mode=display">13</script> places, and at most <script type="math/tex; mode=display">2^6</script> states of keys).  We have a starting node (at <code>'@'</code> with no keys) and ending nodes (at anywhere with all keys.)  We also know all the costs to go from one node to another - each node has outdegree at most 13.  This shortest path problem is now ideal for using Dijkstra's algorithm.</p>
<p>Dijkstra's algorithm uses a priority queue to continually searches the path with the lowest cost to destination, so that when we reach the target, we know it must have been through the lowest cost path.  Refer to <a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">this link</a> for more detail.</p>
<p>Again, each part of the algorithm is relatively straightforward (for those familiar with BFS and Dijkstra's algorithm), but the implementation in total can be quite challenging.</p>
<iframe src="https://leetcode.com/playground/M5ZW2JJm/shared" frameborder="0" width="100%" height="500" name="M5ZW2JJm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(RC(2\mathcal{A} + 1) + \mathcal{E} \log \mathcal{N})</script>, where <script type="math/tex; mode=display">R, C</script> are the dimensions of the grid, and <script type="math/tex; mode=display">\mathcal{A}</script> is the maximum number of keys, <script type="math/tex; mode=display">\mathcal{N} = (2\mathcal{A} + 1) * 2^\mathcal{A}</script> is the number of nodes when we perform Dijkstra's, and <script type="math/tex; mode=display">\mathcal{E} = \mathcal{N} * (2 \mathcal{A} + 1)</script> is the maximum number of edges.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\mathcal{N})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>