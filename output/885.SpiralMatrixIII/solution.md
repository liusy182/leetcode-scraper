<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-walk-in-a-spiral">Approach 1: Walk in a Spiral</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-walk-in-a-spiral">Approach 1: Walk in a Spiral</h4>
<p><strong>Intuition</strong></p>
<p>We can walk in a spiral shape from the starting square, ignoring whether we stay in the grid or not.  Eventually, we must have reached every square in the grid.</p>
<p><strong>Algorithm</strong></p>
<p>Examining the lengths of our walk in each direction, we find the following pattern: <code>1, 1, 2, 2, 3, 3, 4, 4, ...</code>  That is, we walk 1 unit east, then 1 unit south, then 2 units west, then 2 units north, then 3 units east, etc.  Because our walk is self-similar, this pattern repeats in the way we expect.</p>
<p>After, the algorithm is straightforward: perform the walk and record positions of the grid in the order we visit them.  Please read the inline comments for more details.</p>
<iframe src="https://leetcode.com/playground/XTsQ5Bi8/shared" frameborder="0" width="100%" height="500" name="XTsQ5Bi8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O((\max(R, C))^2)</script>.  Potentially, our walk needs to spiral until we move <script type="math/tex; mode=display">R</script> in one direction, and <script type="math/tex; mode=display">C</script> in another direction, so as to reach every cell of the grid.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(R * C)</script>, the space used by the answer.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>