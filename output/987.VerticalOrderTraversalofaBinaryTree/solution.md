<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-store-locations">Approach 1: Store Locations</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-store-locations">Approach 1: Store Locations</h4>
<p><strong>Intuition</strong></p>
<p>It's evident that there are two steps in a straightforward solution: first, find the location of every node, then report their locations.</p>
<p><strong>Algorithm</strong></p>
<p>To find the location of every node, we can use a depth-first search.  During the search, we will maintain the location <code>(x, y)</code> of the node.  As we move from parent to child, the location changes to <code>(x-1, y+1)</code> or <code>(x+1, y+1)</code> depending on if it is a left child or right child.  [We use <code>y+1</code> to make our sorting by decreasing <code>y</code> easier.]</p>
<p>To report the locations, we sort them by <code>x</code> coordinate, then <code>y</code> coordinate, so that they are in the correct order to be added to our answer.</p>
<p>Please see the inline comments for more details.</p>
<iframe src="https://leetcode.com/playground/vohQWX2P/shared" frameborder="0" width="100%" height="500" name="vohQWX2P"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
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