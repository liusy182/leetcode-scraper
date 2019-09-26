<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Any path can be written as two <em>arrows</em> (in different directions) from some node, where an arrow is a path that starts at some node and only travels down to child nodes.</p>
<p>If we knew the maximum length arrows <code>L, R</code> for each child, then the best path touches <code>L + R + 1</code> nodes.</p>
<p><strong>Algorithm</strong></p>
<p>Let's calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1. While we do, a path "through" this node uses 1 + (depth of node.left) + (depth of node.right) nodes. Let's search each node and remember the highest number of nodes used in some path. The desired length is 1 minus this number.</p>
<iframe src="https://leetcode.com/playground/6ahaRHCG/shared" frameborder="0" width="100%" height="310" name="6ahaRHCG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>.  We visit every node once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of our implicit call stack during our depth-first search.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>