<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth First Search</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We traverse the tree using a depth first search.  If <code>node.val</code> falls outside the range <code>[L, R]</code>, (for example <code>node.val &lt; L</code>), then we know that only the right branch could have nodes with value inside <code>[L, R]</code>.</p>
<p>We showcase two implementations - one using a recursive algorithm, and one using an iterative one.</p>
<p><strong>Recursive Implementation</strong></p>
<iframe src="https://leetcode.com/playground/zwwcTGCT/shared" frameborder="0" width="100%" height="378" name="zwwcTGCT"></iframe>

<p><strong>Iterative Implementation</strong></p>
<iframe src="https://leetcode.com/playground/LyVV4ZSy/shared" frameborder="0" width="100%" height="378" name="LyVV4ZSy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(H)</script>, where <script type="math/tex; mode=display">H</script> is the height of the tree.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>