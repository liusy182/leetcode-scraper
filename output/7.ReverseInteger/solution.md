<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-pop-and-push-digits-check-before-overflow">Approach 1: Pop and Push Digits &amp; Check before Overflow</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-pop-and-push-digits-check-before-overflow">Approach 1: Pop and Push Digits &amp; Check before Overflow</h4>
<p><strong>Intuition</strong></p>
<p>We can build up the reverse integer one digit at a time.
While doing so, we can check beforehand whether or not appending another digit would cause overflow.</p>
<p><strong>Algorithm</strong></p>
<p>Reversing an integer can be done similarly to reversing a string.</p>
<p>We want to repeatedly "pop" the last digit off of <script type="math/tex; mode=display">x</script> and "push" it to the back of the <script type="math/tex; mode=display">\text{rev}</script>. In the end, <script type="math/tex; mode=display">\text{rev}</script> will be the reverse of the <script type="math/tex; mode=display">x</script>.</p>
<p>To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.</p>
<div class="codehilite"><pre><span></span><span class="c1">//pop operation:</span>
<span class="n">pop</span> <span class="o">=</span> <span class="n">x</span> <span class="o">%</span> <span class="mi">10</span><span class="p">;</span>
<span class="n">x</span> <span class="o">/=</span> <span class="mi">10</span><span class="p">;</span>

<span class="c1">//push operation:</span>
<span class="n">temp</span> <span class="o">=</span> <span class="n">rev</span> <span class="o">*</span> <span class="mi">10</span> <span class="o">+</span> <span class="n">pop</span><span class="p">;</span>
<span class="n">rev</span> <span class="o">=</span> <span class="n">temp</span><span class="p">;</span>
</pre></div>


<p>However, this approach is dangerous, because the statement <script type="math/tex; mode=display">\text{temp} = \text{rev} \cdot 10 + \text{pop}</script> can cause overflow.</p>
<p>Luckily, it is easy to check beforehand whether or this statement would cause an overflow.</p>
<p>To explain, lets assume that <script type="math/tex; mode=display">\text{rev}</script> is positive.</p>
<ol>
<li>If <script type="math/tex; mode=display">temp = \text{rev} \cdot 10 + \text{pop}</script> causes overflow, then it must be that <script type="math/tex; mode=display">\text{rev} \geq \frac{INTMAX}{10}</script>
</li>
<li>If <script type="math/tex; mode=display">\text{rev} > \frac{INTMAX}{10}</script>, then <script type="math/tex; mode=display">temp = \text{rev} \cdot 10 + \text{pop}</script> is guaranteed to overflow.</li>
<li>If <script type="math/tex; mode=display">\text{rev} == \frac{INTMAX}{10}</script>, then <script type="math/tex; mode=display">temp = \text{rev} \cdot 10 + \text{pop}</script> will overflow if and only if <script type="math/tex; mode=display">\text{pop} > 7</script>
</li>
</ol>
<p>Similar logic can be applied when <script type="math/tex; mode=display">\text{rev}</script> is negative.</p>
<iframe src="https://leetcode.com/playground/Ufhk9yCy/shared" frameborder="0" width="100%" height="293" name="Ufhk9yCy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(\log(x))</script>. There are roughly <script type="math/tex; mode=display">\log_{10}(x)</script> digits in <script type="math/tex; mode=display">x</script>.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
          </div>
        
      </div>