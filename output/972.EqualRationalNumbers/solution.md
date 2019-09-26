<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-fraction-class">Approach 1: Fraction Class</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-fraction-class">Approach 1: Fraction Class</h4>
<p><strong>Intuition</strong></p>
<p>As both numbers represent a fraction, we need a fraction class to handle fractions.  It should help us add two fractions together, keeping the answer in lowest terms.</p>
<p><strong>Algorithm</strong></p>
<p>We need to make sense of the fraction we are given.  The hard part is the repeating part.</p>
<p>Say we have a string like <code>S = "0.(12)"</code>.  It represents (for <script type="math/tex; mode=display">r = \frac{1}{100}</script>):</p>
<p>
<script type="math/tex; mode=display">
S = \frac{12}{100} + \frac{12}{10000} + \frac{12}{10^6} + \frac{12}{10^8} + \frac{12}{10^{10}} + \cdots
</script>
</p>
<p>
<script type="math/tex; mode=display">
S = 12 * (r + r^2 + r^3 + \cdots)
</script>
</p>
<p>
<script type="math/tex; mode=display">
S = 12 * \frac{r}{1-r}
</script>
</p>
<p>as the sum <script type="math/tex; mode=display">(r + r^2 + r^3 + \cdots)</script> is a geometric sum.</p>
<p>In general, for a repeating part <script type="math/tex; mode=display">x</script> with length <script type="math/tex; mode=display">k</script>, we have <script type="math/tex; mode=display">r = 10^{-k}</script> and the contribution is <script type="math/tex; mode=display">\frac{xr}{1-r}</script>.</p>
<p>The other two parts are easier, as it is just a literal interpretation of the value.</p>
<iframe src="https://leetcode.com/playground/hvAK7yRs/shared" frameborder="0" width="100%" height="500" name="hvAK7yRs"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(1)</script>, if we take the length of <script type="math/tex; mode=display">S, T</script> as <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>