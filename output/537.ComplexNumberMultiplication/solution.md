<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-simple-solutionaccepted">Approach #1 Simple Solution[Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-simple-solutionaccepted">Approach #1 Simple Solution[Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Multiplication of two complex numbers can be done as:</p>
<p>
<script type="math/tex; mode=display">
(a+ib) \times (x+iy)=ax+i^2by+i(bx+ay)=ax-by+i(bx+ay)
</script>
</p>
<p>We simply split up the real and the imaginary parts of the given complex strings based on the '+' and the 'i' symbols. We store the real parts of the two strings <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> as <script type="math/tex; mode=display">x[0]</script> and <script type="math/tex; mode=display">y[0]</script> respectively and the imaginary parts as <script type="math/tex; mode=display">x[1]</script> and <script type="math/tex; mode=display">y[1]</script> respectively. Then, we multiply the real and the imaginary parts as required after converting the extracted parts into integers. Then, we again form the return string in the required format and return the result.</p>
<iframe src="https://leetcode.com/playground/jgLSUzDc/shared" frameborder="0" name="jgLSUzDc" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>. Here splitting takes constant time as length of the string is very small <script type="math/tex; mode=display">(<20)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>