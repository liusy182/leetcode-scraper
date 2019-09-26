<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-prefix-sums">Approach 1: Prefix Sums</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-prefix-sums">Approach 1: Prefix Sums</h4>
<p><strong>Intuition</strong></p>
<p>For say a 5 digit string, the answer is either <code>'00000'</code>, <code>'00001'</code>, <code>'00011'</code>, <code>'00111'</code>, <code>'01111'</code>, or <code>'11111'</code>.  Let's try to calculate the cost of switching to that answer.  The answer has two halves, a left (zero) half, and a right (one) half.</p>
<p>Evidently, it comes down to a question of knowing, for each candidate half: how many ones are in the left half, and how many zeros are in the right half.</p>
<p>We can use prefix sums.  Say <code>P[i+1] = A[0] + A[1] + ... + A[i]</code>, where <code>A[i] = 1</code> if <code>S[i] == '1'</code>, else <code>A[i] = 0</code>.  We can calculate <code>P</code> in linear time.</p>
<p>Then if we want <code>x</code> zeros followed by <code>N-x</code> ones, there are <code>P[x]</code> ones in the start that must be flipped, plus <code>(N-x) - (P[N] - P[x])</code> zeros that must be flipped.  The last calculation comes from the fact that there are <code>P[N] - P[x]</code> ones in the later segment of length <code>N-x</code>, but we want the number of zeros.</p>
<p><strong>Algorithm</strong></p>
<p>For example, with <code>S = "010110"</code>:  we have <code>P = [0, 0, 1, 1, 2, 3, 3]</code>.  Now say we want to evaluate having <code>x=3</code> zeros.</p>
<p>There are <code>P[3] = 1</code> ones in the first 3 characters, and <code>P[6] - P[3] = 2</code> ones in the later <code>N-x = 3</code> characters.</p>
<p>So, there is <code>(N-x) - (P[N] - P[x]) = 1</code> zero in the later <code>N-x</code> characters.</p>
<p>We take the minimum among all candidate answers to arrive at the final answer.</p>
<iframe src="https://leetcode.com/playground/AoUF2isa/shared" frameborder="0" width="100%" height="310" name="AoUF2isa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>