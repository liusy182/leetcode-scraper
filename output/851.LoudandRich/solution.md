<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-cached-depth-first-search-accepted">Approach #1: Cached Depth-First Search [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-cached-depth-first-search-accepted">Approach #1: Cached Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Consider the directed graph with edge <code>x -&gt; y</code> if <code>y</code> is richer than <code>x</code>.</p>
<p>For each person <code>x</code>, we want the quietest person in the subtree at <code>x</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Construct the graph described above, and say <code>dfs(person)</code> is the quietest person in the subtree at <code>person</code>.   Notice because the statements are logically consistent, the graph must be a DAG - a directed graph with no cycles.</p>
<p>Now <code>dfs(person)</code> is either <code>person</code>, or <code>min(dfs(child) for child in person)</code>.  That is to say, the quietest person in the subtree is either the <code>person</code> itself, or the quietest person in some subtree of a child of <code>person</code>.</p>
<p>We can cache values of <code>dfs(person)</code> as <code>answer[person]</code>, when performing our <em>post-order traversal</em> of the graph.  That way, we don't repeat work.  This technique reduces a quadratic time algorithm down to linear time.</p>
<iframe src="https://leetcode.com/playground/uMRUYCdD/shared" frameborder="0" width="100%" height="500" name="uMRUYCdD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of people.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by the <code>answer</code>, and the implicit call stack of <code>dfs</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>