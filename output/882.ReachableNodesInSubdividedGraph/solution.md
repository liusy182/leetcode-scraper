<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dijkstras">Approach 1: Dijkstra's</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dijkstras">Approach 1: Dijkstra's</h4>
<p><strong>Intuition</strong></p>
<p>Treating the original graph as a weighted, undirected graph, we can use Dijkstra's algorithm to find all reachable nodes in the original graph.  However, this won't be enough to solve examples where subdivided edges are only used partially.</p>
<p>When we travel along an edge (in either direction), we can keep track of how much we use it.  At the end, we want to know every node we reached in the original graph, plus the sum of the utilization of each edge.</p>
<p><strong>Algorithm</strong></p>
<p>We use <em>Dijkstra's algorithm</em> to find the shortest distance from our source to all targets.  This is a textbook algorithm, refer to <a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">this link</a> for more details.</p>
<p>Additionally, for each (directed) edge <code>(node, nei)</code>, we'll keep track of how many "new" nodes (new from subdivision of the original edge) were <code>used</code>.  At the end, we'll sum up the utilization of each edge.</p>
<p>Please see the inline comments for more details.</p>
<iframe src="https://leetcode.com/playground/obqv6gh4/shared" frameborder="0" width="100%" height="500" name="obqv6gh4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(E \log N)</script>, where <script type="math/tex; mode=display">E</script> is the length of <code>edges</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>