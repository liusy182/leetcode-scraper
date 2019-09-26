<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
<li><a href="#approach-2-ad-hoc-accepted">Approach #2: Ad-Hoc [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Traverse the tree with a depth-first search, and record every unique value in the tree using a Set structure <code>uniques</code>.</p>
<p>Then, we'll look through the recorded values for the second minimum.  The first minimum must be <script type="math/tex; mode=display">\text{root.val}</script>.</p>
<iframe src="https://leetcode.com/playground/rVYM4qCQ/shared" frameborder="0" name="rVYM4qCQ" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the total number of nodes in the given tree.  We visit each node exactly once, and scan through the <script type="math/tex; mode=display">O(N)</script> values in <code>unique</code> once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the information stored in <code>uniques</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-ad-hoc-accepted">Approach #2: Ad-Hoc [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <script type="math/tex; mode=display">\text{min1 = root.val}</script>.  When traversing the tree at some node, <script type="math/tex; mode=display">\text{node}</script>, if <script type="math/tex; mode=display">\text{node.val > min1}</script>, we know all values in the subtree at <script type="math/tex; mode=display">\text{node}</script> are at least <script type="math/tex; mode=display">\text{node.val}</script>, so there cannot be a better candidate for the second minimum in this subtree.  Thus, we do not need to search this subtree.</p>
<p>Also, as we only care about the second minimum <script type="math/tex; mode=display">\text{ans}</script>, we do not need to record any values that are larger than our current candidate for the second minimum, so unlike Approach #1 we can skip maintaining a Set of values(<code>uniques</code>) entirely.</p>
<iframe src="https://leetcode.com/playground/btTLPkjK/shared" frameborder="0" name="btTLPkjK" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the total number of nodes in the given tree.  We visit each node at most once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.  The information stored in <script type="math/tex; mode=display">\text{ans}</script> and <script type="math/tex; mode=display">\text{min1}</script> is <script type="math/tex; mode=display">O(1)</script>, but our depth-first search may store up to <script type="math/tex; mode=display">O(h) = O(N)</script> information in the call stack, where <script type="math/tex; mode=display">h</script> is the height of the tree.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>