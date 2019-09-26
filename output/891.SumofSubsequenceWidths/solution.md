<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-mathematical">Approach 1: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-mathematical">Approach 1: Mathematical</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to count the number of subsequences with minimum <code>A[i]</code> and maximum <code>A[j]</code>.</p>
<p><strong>Algorithm</strong></p>
<p>We can sort the array as it doesn't change the answer.  After sorting the array, this allows us to know that the number of subsequences with minimum <code>A[i]</code> and maximum <code>A[j]</code> is <script type="math/tex; mode=display">2^{j-i-1}</script>.  Hence, the desired answer is:</p>
<p>
<script type="math/tex; mode=display">
\sum\limits_{j > i} (2^{j-i-1}) (A_j - A_i)
</script>
</p>
<p>
<script type="math/tex; mode=display">
= \big( \sum\limits_{i = 0}^{n-2} \sum\limits_{j = i+1}^{n-1} (2^{j-i-1}) (A_j) \big) - \big( \sum\limits_{i = 0}^{n-2} \sum\limits_{j = i+1}^{n-1} (2^{j-i-1}) (A_i) \big)
</script>
</p>
<p>
<script type="math/tex; mode=display">
= \big( (2^0 A_1 + 2^1 A_2 + 2^2 A_3 + \cdots) + (2^0 A_2 + 2^1 A_3 + \cdots) + (2^0 A_3 + 2^1 A_4 + \cdots) + \cdots \big)
</script>
<script type="math/tex; mode=display">
 - \big( \sum\limits_{i = 0}^{n-2} (2^0 + 2^1 + \cdots + 2^{N-i-2}) (A_i) \big)
</script>
</p>
<p>
<script type="math/tex; mode=display">
= \big( \sum\limits_{j = 1}^{n-1} (2^j - 1) A_j \big) - \big( \sum\limits_{i = 0}^{n-2} (2^{N-i-1} - 1) A_i \big)
</script>
</p>
<p>
<script type="math/tex; mode=display">
= \sum\limits_{i = 0}^{n-1} \big(((2^i - 1) A_i) - ((2^{N-i-1} - 1) A_i)\big)
</script>
</p>
<p>
<script type="math/tex; mode=display">
= \sum\limits_{i = 0}^{n-1} (2^i - 2^{N-i-1}) A_i
</script>
</p>
<iframe src="https://leetcode.com/playground/DmYZUfzN/shared" frameborder="0" width="100%" height="361" name="DmYZUfzN"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by <code>pow2</code>.  (We can improve this to <script type="math/tex; mode=display">O(1)</script> space by calculating these powers on the fly.)
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>