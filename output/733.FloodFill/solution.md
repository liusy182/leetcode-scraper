<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We perform the algorithm explained in the problem description: paint the starting pixels, plus adjacent pixels of the same color, and so on.</p>
<p><strong>Algorithm</strong></p>
<p>Say <code>color</code> is the color of the starting pixel.  Let's floodfill the starting pixel: we change the color of that pixel to the new color, then check the 4 neighboring pixels to make sure they are valid pixels of the same <code>color</code>, and of the valid ones, we floodfill those, and so on.</p>
<p>We can use a function <code>dfs</code> to perform a floodfill on a target pixel.</p>
<iframe src="https://leetcode.com/playground/iMoEAq7k/shared" frameborder="0" width="100%" height="327" name="iMoEAq7k"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of pixels in the image.  We might process every pixel.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of the implicit call stack when calling <code>dfs</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>