<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>If <script type="math/tex; mode=display">x^i > \text{bound}</script>, the sum <script type="math/tex; mode=display">x^i + y^j</script> can't be less than or equal to the bound.  Similarly for <script type="math/tex; mode=display">y^j</script>.</p>
<p>Thus, we only have to check for <script type="math/tex; mode=display">0 \leq i, j \leq \log_x(\text{bound}) < 18</script>.</p>
<p>We can use a <code>HashSet</code> to store all the different values.</p>
<iframe src="https://leetcode.com/playground/tmg2tZvM/shared" frameborder="0" width="100%" height="276" name="tmg2tZvM"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log^2{\text{bound}})</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log^2{\text{bound}})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>