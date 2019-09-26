<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-simulation">Approach 1: Simulation</a></li>
<li><a href="#approach-2-layer-by-layer">Approach 2: Layer-by-Layer</a></li>
</ul>
</div>
<h4 id="approach-1-simulation">Approach 1: Simulation</h4>
<p><strong>Intuition</strong></p>
<p>Draw the path that the spiral makes.  We know that the path should turn clockwise whenever it would go out of bounds or into a cell that was previously visited.</p>
<p><strong>Algorithm</strong></p>
<p>Let the array have <script type="math/tex; mode=display">\text{R}</script> rows and <script type="math/tex; mode=display">\text{C}</script> columns.  <script type="math/tex; mode=display">\text{seen[r][c]}</script> denotes that the cell on the<script type="math/tex; mode=display">\text{r}</script>-th row and <script type="math/tex; mode=display">\text{c}</script>-th column was previously visited.  Our current position is <script type="math/tex; mode=display">\text{(r, c)}</script>, facing direction <script type="math/tex; mode=display">\text{di}</script>, and we want to visit <script type="math/tex; mode=display">\text{R}</script> x <script type="math/tex; mode=display">\text{C}</script> total cells.</p>
<p>As we move through the matrix, our candidate next position is <script type="math/tex; mode=display">\text{(cr, cc)}</script>.  If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise turn.</p>
<iframe src="https://leetcode.com/playground/62u9UXjz/shared" frameborder="0" width="100%" height="497" name="62u9UXjz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the total number of elements in the input matrix.  We add every element in the matrix to our final answer.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the information stored in <code>seen</code> and in <code>ans</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-layer-by-layer">Approach 2: Layer-by-Layer</h4>
<p><strong>Intuition</strong></p>
<p>The answer will be all the elements in clockwise order from the first-outer layer, followed by the elements from the second-outer layer, and so on.</p>
<p><strong>Algorithm</strong></p>
<p>We define the <script type="math/tex; mode=display">\text{k}</script>-th outer layer of a matrix as all elements that have minimum distance to some border equal to <script type="math/tex; mode=display">\text{k}</script>.  For example, the following matrix has all elements in the first-outer layer equal to 1, all elements in the second-outer layer equal to 2, and all elements in the third-outer layer equal to 3.</p>
<div class="codehilite"><pre><span></span>[[1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 2, 3, 3, 3, 2, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 1, 1, 1, 1, 1, 1]]
</pre></div>


<p>For each outer layer, we want to iterate through its elements in clockwise order starting from the top left corner.  Suppose the current outer layer has top-left coordinates <script type="math/tex; mode=display">\text{(r1, c1)}</script> and bottom-right coordinates <script type="math/tex; mode=display">\text{(r2, c2)}</script>.</p>
<p>Then, the top row is the set of elements <script type="math/tex; mode=display">\text{(r1, c)}</script> for <script type="math/tex; mode=display">\text{c = c1,...,c2}</script>, in that order.  The rest of the right side is the set of elements <script type="math/tex; mode=display">\text{(r, c2)}</script> for <script type="math/tex; mode=display">\text{r = r1+1,...,r2}</script>, in that order.  Then, if there are four sides to this layer (ie., <script type="math/tex; mode=display">\text{r1 < r2}</script> and <script type="math/tex; mode=display">\text{c1 < c2}</script>), we iterate through the bottom side and left side as shown in the solutions below.</p>
<p><img alt="SpiralMatrix" src="../Figures/54_spiralmatrix.png"></p>
<iframe src="https://leetcode.com/playground/hWE2c3x4/shared" frameborder="0" width="100%" height="446" name="hWE2c3x4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the total number of elements in the input matrix.  We add every element in the matrix to our final answer.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the information stored in <code>ans</code>.</p>
</li>
</ul>
          </div>
        
      </div>