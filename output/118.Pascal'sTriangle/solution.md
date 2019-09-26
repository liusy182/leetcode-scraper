<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
</ul>
</div>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>If we have the a row of Pascal's triangle, we can easily compute the next
row by each pair of adjacent values.</p>
<p><strong>Algorithm</strong></p>
<p>Although the algorithm is very simple, the iterative approach to constructing
Pascal's triangle can be classified as dynamic programming because we
construct each row based on the previous row.</p>
<p>First, we generate the overall <code>triangle</code> list, which will store each row as
a sublist. Then, we check for the special case of <script type="math/tex; mode=display">0</script>, as we would otherwise
return <script type="math/tex; mode=display">[1]</script>. If <script type="math/tex; mode=display">numRows > 0</script>, then we initialize <code>triangle</code> with <script type="math/tex; mode=display">[1]</script>
as its first row, and proceed to fill the rows as follows:</p>
<p>!?!../Documents/118_Pascals_Triangle.json:1280,720!?!</p>
<iframe src="https://leetcode.com/playground/idrxbCSN/shared" frameborder="0" width="100%" height="500" name="idrxbCSN"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(numRows^2)</script>
</p>
<p>Although updating each value of <code>triangle</code> happens in constant time, it
is performed <script type="math/tex; mode=display">O(numRows^2)</script> times. To see why, consider how many
overall loop iterations there are. The outer loop obviously runs
<script type="math/tex; mode=display">numRows</script> times, but for each iteration of the outer loop, the inner
loop runs <script type="math/tex; mode=display">rowNum</script> times. Therefore, the overall number of <code>triangle</code> updates
that occur is <script type="math/tex; mode=display">1 + 2 + 3 + \ldots + numRows</script>, which, according to Gauss' formula,
is</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
    \frac{numRows(numRows+1)}{2} &= \frac{numRows^2 + numRows}{2} \\
    &= \frac{numRows^2}{2} + \frac{numRows}{2} \\
    &= O(numRows^2)
\end{aligned}
</script>
</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(numRows^2)</script>
</p>
<p>Because we need to store each number that we update in <code>triangle</code>, the
space requirement is the same as the time complexity.</p>
</li>
</ul>
          </div>
        
      </div>