<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
<li><a href="#approach-2-dijkstras-algorithm-accepted">Approach #2: Dijkstra's Algorithm [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's record the time <code>dist[node]</code> when the signal reaches the node.  If some signal arrived earlier, we don't need to broadcast it anymore.  Otherwise, we should broadcast the signal.</p>
<p><strong>Algorithm</strong></p>
<p>We'll maintain <code>dist[node]</code>, the earliest that we arrived at each <code>node</code>.  When visiting a <code>node</code> while <code>elapsed</code> time has elapsed, if this is the currently-fastest signal at this node, let's broadcast signals from this node.</p>
<p>To speed things up, at each visited node we'll consider signals exiting the node that are faster first, by sorting the edges.</p>
<iframe src="https://leetcode.com/playground/YadsYraY/shared" frameborder="0" width="100%" height="500" name="YadsYraY"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^N + E \log E)</script> where <script type="math/tex; mode=display">E</script> is the length of <code>times</code>.  We can only fully visit each node up to <script type="math/tex; mode=display">N-1</script> times, one per each other node.  Plus, we have to explore every edge and sort them.  Sorting each small bucket of outgoing edges is bounded by sorting all of them, because of repeated use of the inequality <script type="math/tex; mode=display">x \log x + y \log y \leq (x+y) \log (x+y)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N + E)</script>, the size of the graph (<script type="math/tex; mode=display">O(E)</script>), plus the size of the implicit call stack in our DFS (<script type="math/tex; mode=display">O(N)</script>).</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dijkstras-algorithm-accepted">Approach #2: Dijkstra's Algorithm [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We use <em>Dijkstra's algorithm</em> to find the shortest path from our source to all targets.  This is a textbook algorithm, refer to <a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">this link</a> for more details.</p>
<p>Dijkstra's algorithm is based on repeatedly making the candidate move that has the least distance travelled.</p>
<p>In our implementations below, we showcase both <script type="math/tex; mode=display">O(N^2)</script> (basic) and <script type="math/tex; mode=display">O(N \log N)</script> (heap) approaches.</p>
<p><em>Basic Implementation</em>
<iframe src="https://leetcode.com/playground/HxrhmhUo/shared" frameborder="0" width="100%" height="500" name="HxrhmhUo"></iframe></p>
<p><em>Heap Implementation</em></p>
<iframe src="https://leetcode.com/playground/FAHPcmsE/shared" frameborder="0" width="100%" height="500" name="FAHPcmsE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2 + E)</script>m where <script type="math/tex; mode=display">E</script> is the length of <code>times</code> in the basic implementation, and <script type="math/tex; mode=display">O(E \log E)</script> in the heap implementation, as potentially every edge gets added to the heap.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N + E)</script>, the size of the graph (<script type="math/tex; mode=display">O(E)</script>), plus the size of the other objects used (<script type="math/tex; mode=display">O(N)</script>).</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>