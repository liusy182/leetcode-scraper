<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
<li><a href="#approach-2-unique-identifier-accepted">Approach #2: Unique Identifier [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can serialize each subtree.  For example, the tree</p>
<div class="codehilite"><pre><span></span>   <span class="mi">1</span>
  <span class="o">/</span> \
 <span class="mi">2</span>   <span class="mi">3</span>
    <span class="o">/</span> \
   <span class="mi">4</span>   <span class="mi">5</span>
</pre></div>


<p>can be represented as the serialization <code>1,2,#,#,3,4,#,#,5,#,#</code>, which is a unique representation of the tree.</p>
<p><strong>Algorithm</strong></p>
<p>Perform a depth-first search, where the recursive function returns the serialization of the tree.  At each node, record the result in a map, and analyze the map after to determine duplicate subtrees.</p>
<iframe src="https://leetcode.com/playground/4UyWd7Zu/shared" frameborder="0" width="100%" height="378" name="4UyWd7Zu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.  We visit each node once, but each creation of <code>serial</code> may take <script type="math/tex; mode=display">O(N)</script> work.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the size of <code>count</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-unique-identifier-accepted">Approach #2: Unique Identifier [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Suppose we have a unique identifier for subtrees: two subtrees are the same if and only if they have the same id.</p>
<p>Then, for a node with left child id of <code>x</code> and right child id of <code>y</code>, <code>(node.val, x, y)</code> uniquely determines the tree.</p>
<p><strong>Algorithm</strong></p>
<p>If we have seen the triple <code>(node.val, x, y)</code> before, we can use the identifier we've remembered.  Otherwise, we'll create a new one.</p>
<iframe src="https://leetcode.com/playground/sgdon7Zu/shared" frameborder="0" width="100%" height="480" name="sgdon7Zu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.  We visit each node once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.  Every structure we use is using <script type="math/tex; mode=display">O(1)</script> storage per node.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approach #2 inspired by <a href="https://discuss.leetcode.com/topic/97625/o-n-time-and-space-lots-of-analysis">@StefanPochmann</a>.</p>
          </div>
        
      </div>