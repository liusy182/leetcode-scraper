<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-prefix-sums-and-counting">Approach 1: Prefix Sums and Counting</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-prefix-sums-and-counting">Approach 1: Prefix Sums and Counting</h4>
<p><strong>Intuition</strong></p>
<p>As is typical with problems involving subarrays, we use prefix sums to add each subarray.  Let <code>P[i+1] = A[0] + A[1] + ... + A[i]</code>.  Then, each subarray can be written as <code>P[j] - P[i]</code> (for <code>j &gt; i</code>).  Thus, we have <code>P[j] - P[i]</code> equal to <code>0</code> modulo <code>K</code>, or equivalently <code>P[i]</code> and <code>P[j]</code> are the same value modulo <code>K</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Count all the <code>P[i]</code>'s modulo <code>K</code>.  Let's say there are <script type="math/tex; mode=display">C_x</script> values <script type="math/tex; mode=display">P[i] \equiv x \pmod{K}</script>.  Then, there are <script type="math/tex; mode=display">\sum_x \binom{C_x}{2}</script> possible subarrays.</p>
<p>For example, take <code>A = [4,5,0,-2,-3,1]</code> and <code>K = 5</code>.  Then <code>P = [0,4,9,9,7,4,5]</code>, and <script type="math/tex; mode=display">C_0 = 2, C_2 = 1, C_4 = 4</script>:</p>
<ul>
<li>With <script type="math/tex; mode=display">C_0 = 2</script> (at <script type="math/tex; mode=display">P[0]</script>, <script type="math/tex; mode=display">P[6]</script>), it indicates <script type="math/tex; mode=display">\binom{2}{2} = 1</script> subarray with sum divisible by <script type="math/tex; mode=display">K</script>, namely <script type="math/tex; mode=display">A[0:6] = [4, 5, 0, -2, -3, 1]</script>.</li>
<li>With <script type="math/tex; mode=display">C_4 = 4</script> (at <script type="math/tex; mode=display">P[1]</script>, <script type="math/tex; mode=display">P[2]</script>, <script type="math/tex; mode=display">P[3]</script>, <script type="math/tex; mode=display">P[5]</script>), it indicates <script type="math/tex; mode=display">\binom{4}{2} = 6</script> subarrays with sum divisible by <script type="math/tex; mode=display">K</script>, namely <script type="math/tex; mode=display">A[1:2]</script>, <script type="math/tex; mode=display">A[1:3]</script>, <script type="math/tex; mode=display">A[1:5]</script>, <script type="math/tex; mode=display">A[2:3]</script>, <script type="math/tex; mode=display">A[2:5]</script>, <script type="math/tex; mode=display">A[3:5]</script>.</li>
</ul>
<iframe src="https://leetcode.com/playground/oRReLTA2/shared" frameborder="0" width="100%" height="344" name="oRReLTA2"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.  (However, the solution can be modified to use <script type="math/tex; mode=display">O(K)</script> space by storing only <code>count</code>.)
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>