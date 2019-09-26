<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-connected-components">Approach 1: Connected Components</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-connected-components">Approach 1: Connected Components</h4>
<p><strong>Intuition</strong></p>
<p>All variables that are equal to each other form connected components.  For example, if <code>a=b, b=c, c=d</code> then <code>a, b, c, d</code> are in the same connected component as they all must be equal to each other.</p>
<p><strong>Algorithm</strong></p>
<p>First, we use a depth first search to color each variable by connected component based on these equality equations.</p>
<p>After coloring these components, we can parse statements of the form <code>a != b</code>.  If two components have the same color, then they must be equal, so if we say they can't be equal then it is impossible to satisfy the equations.</p>
<p>Otherwise, our coloring demonstrates a way to satisfy the equations, and thus the result is true.</p>
<iframe src="https://leetcode.com/playground/w97VUNhP/shared" frameborder="0" width="100%" height="500" name="w97VUNhP"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>equations</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>, assuming the size of the alphabet is <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>