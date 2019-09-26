<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-annotate-parent-and-depth">Approach 1: Annotate Parent and Depth</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-annotate-parent-and-depth">Approach 1: Annotate Parent and Depth</h4>
<p><strong>Intuition</strong></p>
<p>Nodes are cousins if they have the same depth but different parents.  A straightforward approach is to be able to know the parent and depth of each node.</p>
<p><strong>Algorithm</strong></p>
<p>We can use a depth-first search to annotate each node.  For each <code>node</code> with parent <code>par</code> and depth <code>d</code>, we will record results in hashmaps: <code>parent[node.val] = par</code> and <code>depth[node.val] = d</code>.</p>
<iframe src="https://leetcode.com/playground/2M2DeUvF/shared" frameborder="0" width="100%" height="395" name="2M2DeUvF"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.</p>
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