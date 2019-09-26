<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-2-matrix-exponentiation-accepted">Approach #2: Matrix Exponentiation [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <code>f[r][c][steps]</code> be the probability of being on square <code>(r, c)</code> after <code>steps</code> steps.  Based on how a knight moves, we have the following recursion:</p>
<p>
<script type="math/tex; mode=display">f[r][c][steps] = \sum_{dr, dc} f[r+dr][c+dc][steps-1] / 8.0</script>
</p>
<p>where the sum is taken over the eight <script type="math/tex; mode=display">(dr, dc)</script> pairs <script type="math/tex; mode=display">(2, 1),</script>
<script type="math/tex; mode=display">(2, -1),</script>
<script type="math/tex; mode=display">(-2, 1),</script>
<script type="math/tex; mode=display">(-2, -1),</script>
<script type="math/tex; mode=display">(1, 2),</script>
<script type="math/tex; mode=display">(1, -2),</script>
<script type="math/tex; mode=display">(-1, 2),</script>
<script type="math/tex; mode=display">(-1, -2)</script>.</p>
<p>Instead of using a three-dimensional array <code>f</code>, we will use two two-dimensional ones <code>dp</code> and <code>dp2</code>, storing the result of the two most recent layers we are working on.  <code>dp2</code> will represent <code>f[][][steps]</code>, and <code>dp</code> will represent <code>f[][][steps-1]</code>.</p>
<iframe src="https://leetcode.com/playground/VTNPLt6H/shared" frameborder="0" name="VTNPLt6H" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2 K)</script> where <script type="math/tex; mode=display">N, K</script> are defined as in the problem.  We do <script type="math/tex; mode=display">O(1)</script> work on each layer <code>dp</code> of <script type="math/tex; mode=display">N^2</script> elements, and there are <script type="math/tex; mode=display">K</script> layers considered.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the size of <code>dp</code> and <code>dp2</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-matrix-exponentiation-accepted">Approach #2: Matrix Exponentiation [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The recurrence expressed in <em>Approach #1</em> expressed states that transitioned to a linear combination of other states.  Any time this happens, we can represent the entire transition as a matrix of those linear combinations.  Then, the <script type="math/tex; mode=display">n</script>-th power of this matrix represents the transition of <script type="math/tex; mode=display">n</script> moves, and thus we can reduce the problem to a problem of matrix exponentiation.</p>
<p><strong>Algorithm</strong></p>
<p>First, there is a lot of symmetry on the board that we can exploit.  Naively, there are <script type="math/tex; mode=display">N^2</script> possible states the knight can be in (assuming it is on the board).  Because of symmetry through the horizontal, vertical, and diagonal axes, we can assume that the knight is in the top-left quadrant of the board, and that the column number is equal to or larger than the row number.  For any square, the square that is found by reflecting about these axes to satisfy these conditions will be the <em>canonical index</em> of that square.</p>
<p>This will reduce the number of states from <script type="math/tex; mode=display">N^2</script> to approximately <script type="math/tex; mode=display">\frac{N^2}{8}</script>, which makes the following (cubic) matrix exponentiation on this <script type="math/tex; mode=display">O(\frac{N^2}{8}) \times O(\frac{N^2}{8})</script> matrix approximately <script type="math/tex; mode=display">8^3</script> times faster.</p>
<p>Now, if we know that every state becomes some linear combination of states after one move, then let's write a transition matrix <script type="math/tex; mode=display">\mathcal{T}</script> of them, where the <script type="math/tex; mode=display">i</script>-th row of <script type="math/tex; mode=display">\mathcal{T}</script> represents the linear combination of states that the <script type="math/tex; mode=display">i</script>-th state goes to.  Then, <script type="math/tex; mode=display">\mathcal{T}^n</script> represents a transition of <script type="math/tex; mode=display">n</script> moves, for which we want the sum of the <script type="math/tex; mode=display">i</script>-th row, where <script type="math/tex; mode=display">i</script> is the index of the starting square.</p>
<iframe src="https://leetcode.com/playground/ARu5yUUd/shared" frameborder="0" name="ARu5yUUd" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^6 \log(K))</script> where <script type="math/tex; mode=display">N, K</script> are defined as in the problem.  There are approximately <script type="math/tex; mode=display">\frac{N^2}{8}</script> canonical states, which makes our matrix multiplication <script type="math/tex; mode=display">O(N^6)</script>.  To find the <script type="math/tex; mode=display">K</script>-th power of this matrix, we make <script type="math/tex; mode=display">O(\log(K))</script> matrix multiplications.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^4)</script>.  The matrix has approximately <script type="math/tex; mode=display">\frac{N^4}{64}</script> elements.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>