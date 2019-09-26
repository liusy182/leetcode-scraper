<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-convert-to-string-accepted">Approach #1: Convert to String [Accepted]</a></li>
<li><a href="#approach-2-divide-by-two-accepted">Approach #2: Divide By Two [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-convert-to-string-accepted">Approach #1: Convert to String [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's convert the given number into a string of binary digits.  Then, we should simply check that no two adjacent digits are the same.</p>
<iframe src="https://leetcode.com/playground/79o5Wvyy/shared" frameborder="0" name="79o5Wvyy" width="100%" height="241"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(1)</script>.  For arbitrary inputs, we do <script type="math/tex; mode=display">O(w)</script> work, where <script type="math/tex; mode=display">w</script> is the number of bits in <code>n</code>.  However, <script type="math/tex; mode=display">w \leq 32</script>.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script>, or alternatively <script type="math/tex; mode=display">O(w)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-divide-by-two-accepted">Approach #2: Divide By Two [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can get the last bit and the rest of the bits via <code>n % 2</code> and <code>n // 2</code> operations.  Let's remember <code>cur</code>, the last bit of <code>n</code>.  If the last bit ever equals the last bit of the remaining, then two adjacent bits have the same value, and the answer is <code>False</code>.  Otherwise, the answer is <code>True</code>.</p>
<p>Also note that instead of <code>n % 2</code> and <code>n // 2</code>, we could have used operators <code>n &amp; 1</code> and <code>n &gt;&gt;= 1</code> instead.</p>
<iframe src="https://leetcode.com/playground/oFAELrSA/shared" frameborder="0" name="oFAELrSA" width="100%" height="258"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(1)</script>.  For arbitrary inputs, we do <script type="math/tex; mode=display">O(w)</script> work, where <script type="math/tex; mode=display">w</script> is the number of bits in <code>n</code>.  However, <script type="math/tex; mode=display">w \leq 32</script>.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>