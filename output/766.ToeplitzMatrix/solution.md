<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-group-by-category-accepted">Approach #1: Group by Category [Accepted]</a></li>
<li><a href="#approach-2-compare-with-top-left-neighbor-accepted">Approach #2: Compare With Top-Left Neighbor [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-group-by-category-accepted">Approach #1: Group by Category [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We ask what feature makes two coordinates <code>(r1, c1)</code> and <code>(r2, c2)</code> belong to the same diagonal?</p>
<p>It turns out two coordinates are on the same diagonal if and only if <code>r1 - c1 == r2 - c2</code>.</p>
<p>This leads to the following idea: remember the value of that diagonal as <code>groups[r-c]</code>.  If we see a mismatch, the matrix is not Toeplitz; otherwise it is.</p>
<iframe src="https://leetcode.com/playground/aPydaE7r/shared" frameborder="0" width="100%" height="293" name="aPydaE7r"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M*N)</script>.  (Recall in the problem statement that <script type="math/tex; mode=display">M, N</script> are the number of rows and columns in <code>matrix</code>.)</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M+N)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-compare-with-top-left-neighbor-accepted">Approach #2: Compare With Top-Left Neighbor [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each diagonal with elements in order <script type="math/tex; mode=display">a_1, a_2, a_3, \dots, a_k</script>, we can check <script type="math/tex; mode=display">a_1 = a_2, a_2 = a_3, \dots, a_{k-1} = a_k</script>.  The matrix is <em>Toeplitz</em> if and only if all of these conditions are true for all (top-left to bottom-right) diagonals.</p>
<p>Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor.  Thus, for the square <code>(r, c)</code>, we only need to check <code>r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c]</code>.</p>
<iframe src="https://leetcode.com/playground/bfeF5wnM/shared" frameborder="0" width="100%" height="208" name="bfeF5wnM"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M*N)</script>, as defined in the problem statement.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>