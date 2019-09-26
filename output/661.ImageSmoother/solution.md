<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-iterate-through-grid">Approach #1: Iterate Through Grid</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-iterate-through-grid">Approach #1: Iterate Through Grid</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each cell in the grid, look at the immediate neighbors - up to 9 of them, including the original cell.</p>
<p>Then, we will add the sum of the neighbors into <code>ans[r][c]</code> while recording <code>count</code>, the number of such neighbors.  The final answer is the sum divided by the count.</p>
<iframe src="https://leetcode.com/playground/i8A5ppzu/shared" frameborder="0" width="100%" height="395" name="i8A5ppzu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of pixels in our image.  We iterate over every pixel.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of our answer.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>