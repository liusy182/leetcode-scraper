<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-copy-directly">Approach 1: Copy Directly</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-copy-directly">Approach 1: Copy Directly</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>The transpose of a matrix <code>A</code> with dimensions <code>R x C</code> is a matrix <code>ans</code> with dimensions <code>C x R</code> for which <code>ans[c][r] = A[r][c]</code>.</p>
<p>Let's initialize a new matrix <code>ans</code> representing the answer.  Then, we'll copy each entry of the matrix as appropriate.</p>
<iframe src="https://leetcode.com/playground/npb7vRxu/shared" frameborder="0" width="100%" height="242" name="npb7vRxu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(R * C)</script>, where <script type="math/tex; mode=display">R</script> and <script type="math/tex; mode=display">C</script> are the number of rows and columns in the given matrix <code>A</code>.</p>
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