<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-find-and-grow">Approach 1: Find and Grow</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-find-and-grow">Approach 1: Find and Grow</h4>
<p><strong>Intuition</strong></p>
<p>Conceptually, our method is very straightforward: find both islands, then for one of the islands, keep "growing" it by 1 until we touch the second island.</p>
<p>We can use a depth-first search to find the islands, and a breadth-first search to "grow" one of them.  This leads to a verbose but correct solution.</p>
<p><strong>Algorithm</strong></p>
<p>To find both islands, look for a square with a <code>1</code> we haven't visited, and dfs to get the component of that region.  Do this twice.  After, we have two components <code>source</code> and <code>target</code>.</p>
<p>To find the shortest bridge, do a BFS from the nodes <code>source</code>.  When we reach any node in <code>target</code>, we will have found the shortest distance.</p>
<p>Please see the code for more implementation details.</p>
<iframe src="https://leetcode.com/playground/wfdtey9G/shared" frameborder="0" width="100%" height="500" name="wfdtey9G"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\mathcal{A})</script>, where <script type="math/tex; mode=display">\mathcal{A}</script> is the content of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\mathcal{A})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>