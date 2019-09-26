<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-reverse-edges-accepted">Approach #1: Reverse Edges [Accepted]</a></li>
<li><a href="#approach-2-depth-first-search-accepted">Approach #2: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-reverse-edges-accepted">Approach #1: Reverse Edges [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The crux of the problem is whether you can reach a cycle from the node you start in.  If you can, then there is a way to avoid stopping indefinitely; and if you can't, then after some finite number of steps you'll stop.</p>
<p>Thinking about this property more, a node is eventually safe if all it's outgoing edges are to nodes that are eventually safe.</p>
<p>This gives us the following idea: we start with nodes that have no outgoing edges - those are eventually safe.  Now, we can update any nodes which only point to eventually safe nodes - those are also eventually safe.  Then, we can update again, and so on.</p>
<p>However, we'll need a good algorithm to make sure our updates are efficient.</p>
<p><strong>Algorithm</strong></p>
<p>We'll keep track of <code>graph</code>, a way to know for some node <code>i</code>, what the outgoing edges <code>(i, j)</code> are.  We'll also keep track of <code>rgraph</code>, a way to know for some node <code>j</code>, what the incoming edges <code>(i, j)</code> are.</p>
<p>Now for every node <code>j</code> which was declared eventually safe, we'll process them in a queue.  We'll look at all parents <code>i = rgraph[j]</code> and remove the edge <code>(i, j)</code> from the graph (from <code>graph</code>).  If this causes the <code>graph</code> to have no outgoing edges <code>graph[i]</code>, then we'll declare it eventually safe and add it to our queue.</p>
<p>Also, we'll keep track of everything we ever added to the queue, so we can read off the answer in sorted order later.</p>
<iframe src="https://leetcode.com/playground/x49F98kC/shared" frameborder="0" width="100%" height="500" name="x49F98kC"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + E)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given graph, and <script type="math/tex; mode=display">E</script> is the total number of edges.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script> in additional space complexity.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-depth-first-search-accepted">Approach #2: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, the crux of the problem is whether you reach a cycle or not.</p>
<p>Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually.  This is a classic "white-gray-black" DFS algorithm that would be part of any textbook on DFS.  We mark a node gray on entry, and black on exit.  If we see a gray node during our DFS, it must be part of a cycle.  In a naive view, we'll clear the colors between each search.</p>
<p><strong>Algorithm</strong></p>
<p>We can improve this approach, by noticing that we don't need to clear the colors between each search.</p>
<p>When we visit a node, the only possibilities are that we've marked the entire subtree black (which must be eventually safe), or it has a cycle and we have only marked the members of that cycle gray.  So indeed, the invariant that gray nodes are always part of a cycle, and black nodes are always eventually safe is maintained.</p>
<p>In order to exit our search quickly when we find a cycle (and not paint other nodes erroneously), we'll say the result of visiting a node is <code>true</code> if it is eventually safe, otherwise <code>false</code>.  This allows information that we've reached a cycle to propagate up the call stack so that we can terminate our search early.</p>
<iframe src="https://leetcode.com/playground/VxkXPWTw/shared" frameborder="0" width="100%" height="500" name="VxkXPWTw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + E)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given graph, and <script type="math/tex; mode=display">E</script> is the total number of edges.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script> in additional space complexity.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>