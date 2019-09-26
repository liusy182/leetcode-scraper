<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-recursive-accepted">Approach #1: Depth-First Search (Recursive) [Accepted]</a></li>
<li><a href="#approach-2-depth-first-search-iterative-accepted">Approach #2: Depth-First Search (Iterative) [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-depth-first-search-recursive-accepted">Approach #1: Depth-First Search (Recursive) [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We want to know the area of each connected shape in the grid, then take the maximum of these.</p>
<p>If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected to those squares, and so on), then the total number of squares explored will be the area of that connected shape.</p>
<p>To ensure we don't count squares in a shape more than once, let's use <code>seen</code> to keep track of squares we haven't visited before.  It will also prevent us from counting the same shape more than once.</p>
<iframe src="https://leetcode.com/playground/CQGNqDhr/shared" frameborder="0" name="CQGNqDhr" width="100%" height="479"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(R*C)</script>, where <script type="math/tex; mode=display">R</script> is the number of rows in the given <code>grid</code>, and <script type="math/tex; mode=display">C</script> is the number of columns.  We visit every square once.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(R*C)</script>, the space used by <code>seen</code> to keep track of visited squares, and the space used by the call stack during our recursion.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-depth-first-search-iterative-accepted">Approach #2: Depth-First Search (Iterative) [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can try the same approach using a stack based, (or "iterative") depth-first search.</p>
<p>Here, <code>seen</code> will represent squares that have either been visited or are added to our list of squares to visit (<code>stack</code>).  For every starting land square that hasn't been visited, we will explore 4-directionally around it, adding land squares that haven't been added to <code>seen</code> to our <code>stack</code>.</p>
<p>On the side, we'll keep a count <code>shape</code> of the total number of squares seen during the exploration of this shape.  We'll want the running max of these counts.</p>
<iframe src="https://leetcode.com/playground/khZHhSir/shared" frameborder="0" name="khZHhSir" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(R*C)</script>, where <script type="math/tex; mode=display">R</script> is the number of rows in the given <code>grid</code>, and <script type="math/tex; mode=display">C</script> is the number of columns.  We visit every square once.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(R*C)</script>, the space used by <code>seen</code> to keep track of visited squares, and the space used by <code>stack</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>