<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>It is clear that the probability that Alice wins the game is only related to how many points <code>x</code> she starts the next draw with, so we can try to formulate an answer in terms of <code>x</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>f(x)</code> be the answer when we already have <code>x</code> points.  When she has between <code>K</code> and <code>N</code> points, then she stops drawing and wins.  If she has more than <code>N</code> points, then she loses.</p>
<p>The key recursion is <script type="math/tex; mode=display">f(x) = (\frac{1}{W}) * (f(x+1) + f(x+2) + ... + f(x+W))</script>  This is because there is a probability of <script type="math/tex; mode=display">\frac{1}{W}</script> to draw each card from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">W</script>.</p>
<p>With this recursion, we could do a naive dynamic programming solution as follows:</p>
<div class="codehilite"><pre><span></span><span class="c1">#psuedocode</span>
<span class="n">dp</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="mf">1.0</span> <span class="n">when</span> <span class="n">K</span> <span class="o">&lt;=</span> <span class="n">k</span> <span class="o">&lt;=</span> <span class="n">N</span><span class="p">,</span> <span class="k">else</span> <span class="mf">0.0</span>
<span class="c1"># dp[x] = the answer when Alice has x points</span>
<span class="k">for</span> <span class="n">k</span> <span class="kn">from</span> <span class="nn">K</span><span class="o">-</span><span class="mi">1</span> <span class="n">to</span> <span class="mi">0</span><span class="p">:</span>
    <span class="n">dp</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">dp</span><span class="p">[</span><span class="n">k</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="o">...</span> <span class="o">+</span> <span class="n">dp</span><span class="p">[</span><span class="n">k</span><span class="o">+</span><span class="n">W</span><span class="p">])</span> <span class="o">/</span> <span class="n">W</span>
<span class="k">return</span> <span class="n">dp</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>


<p>This leads to a solution with <script type="math/tex; mode=display">O(K*W + (N-K))</script> time complexity, which isn't efficient enough.  Every calculation of <code>dp[k]</code> does <script type="math/tex; mode=display">O(W)</script> work, but the work is quite similar.</p>
<p>Actually, the difference is <script type="math/tex; mode=display">f(x) - f(x-1) = \frac{1}{W} \big( f(x+W) - f(x) \big)</script>.  This allows us to calculate subsequent <script type="math/tex; mode=display">f(k)</script>'s in <script type="math/tex; mode=display">O(1)</script> time, by maintaining the numerator <script type="math/tex; mode=display">S = f(x+1) + f(x+2) + \cdots + f(x+W)</script>.</p>
<p>As we calculate each <code>dp[k] = S / W</code>, we maintain the correct value of this numerator <script type="math/tex; mode=display">S \Rightarrow S + f(k) - f(k+W)</script>.</p>
<iframe src="https://leetcode.com/playground/x4pmytdi/shared" frameborder="0" width="100%" height="327" name="x4pmytdi"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity:  <script type="math/tex; mode=display">O(N + W)</script>.<br>
Note that we can reduce the time complexity to <script type="math/tex; mode=display">O(\max(K, W))</script> and the space complexity to <script type="math/tex; mode=display">O(W)</script> by only keeping track of the last <script type="math/tex; mode=display">W</script> values of <code>dp</code>, but it isn't required.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>