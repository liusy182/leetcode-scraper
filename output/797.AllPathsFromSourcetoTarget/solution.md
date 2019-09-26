<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Since the graph is a directed, acyclic graph, any path from <code>A</code> to <code>B</code> is going to be composed of <code>A</code> plus a path from any neighbor of <code>A</code> to <code>B</code>.  We can use a recursion to return the answer.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>N</code> be the number of nodes in the graph.  If we are at node <code>N-1</code>, the answer is just the path <code>{N-1}</code>.  Otherwise, if we are at node <code>node</code>, the answer is <code>{node} + {path from nei to N-1}</code> for each neighbor <code>nei</code> of <code>node</code>.  This is a natural setting to use a recursion to form the answer.</p>
<iframe src="https://leetcode.com/playground/KUaNbvp4/shared" frameborder="0" width="100%" height="463" name="KUaNbvp4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^N N^2)</script>.  We can have exponentially many paths, and for each such path, our prepending operation <code>path.add(0, node)</code> will be <script type="math/tex; mode=display">O(N^2)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(2^N N)</script>, the size of the output dominating the final space complexity.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>