<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-breadth-first-search">Approach 1: Breadth-First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-breadth-first-search">Approach 1: Breadth-First Search</h4>
<p><strong>Intuition</strong></p>
<p>As we are looking for a shortest path, a breadth-first search is ideal.  The main difficulty is to handle enumerating all possible moves from each square.</p>
<p><strong>Algorithm</strong></p>
<p>Suppose we are on a square with number <code>s</code>.  We would like to know all final destinations with number <code>s2</code> after making one move.</p>
<p>This requires knowing the coordinates <code>get(s2)</code> of square <code>s2</code>.  This is a small puzzle in itself: we know that the row changes every <code>N</code> squares, and so is only based on <code>quot = (s2-1) / N</code>; also the column is only based on <code>rem = (s2-1) % N</code> and what row we are on (forwards or backwards.)</p>
<p>From there, we perform a breadth first search, where the nodes are the square numbers <code>s</code>.</p>
<iframe src="https://leetcode.com/playground/RZ7eqY32/shared" frameborder="0" width="100%" height="500" name="RZ7eqY32"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of the <code>board</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>