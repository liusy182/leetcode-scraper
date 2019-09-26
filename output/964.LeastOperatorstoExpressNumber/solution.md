<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>First, we notice that we can consider blocks of multiplication and division separately.  Each block is a power of <code>x</code>: either <code>x / x</code>, <code>x</code>, <code>x * x</code>, <code>x * x * x</code>, <code>x * x * x * x</code> and so on.  (There is no point to write expressions like <code>x * x / x</code> because it uses strictly more operators.)</p>
<p>Let's think of the cost of a block as all the operators needed to express it, including the addition or subtraction operator in front of it.  For example, we can think of <code>x * x + x + x / x</code> as <code>(+ x * x) (+ x) (+ x / x)</code> for a cost of <code>2 + 1 + 2</code>, minus 1 for the leading <code>+</code> (so the total cost is <code>4</code>).</p>
<p>We can write the cost of writing a block that has value <script type="math/tex; mode=display">x^e</script>: it is <script type="math/tex; mode=display">e</script>, except when <script type="math/tex; mode=display">e = 0</script> it is 2.  We want the sum of the costs of all blocks minus 1.</p>
<p>Now, we have the reduced problem: we have the costs of writing all <script type="math/tex; mode=display">x^e</script> or <script type="math/tex; mode=display">-x^e</script>, and we want to find the least cost to express the target.</p>
<p>Notice that modulo <script type="math/tex; mode=display">x</script>, the only blocks that change the expression are <script type="math/tex; mode=display">x^0</script>.  Let <script type="math/tex; mode=display">r_1 = \text{target} \pmod x</script>.  So we must either subtract <script type="math/tex; mode=display">r_1</script>
<script type="math/tex; mode=display">x^0</script>'s, or add <script type="math/tex; mode=display">x-r_1</script>
<script type="math/tex; mode=display">x^0</script>'s.  This will form a new "remaining" target, <script type="math/tex; mode=display">\text{target}_2</script>, that is divisible by <script type="math/tex; mode=display">x</script>.</p>
<p>Then, modulo <script type="math/tex; mode=display">x^2</script>, the only blocks that change the expression are <script type="math/tex; mode=display">x^1</script> and <script type="math/tex; mode=display">x^0</script>.  However, since the new target is divisible by <script type="math/tex; mode=display">x</script>, there is no point to use <script type="math/tex; mode=display">x^0</script>, as we would have to use at least <script type="math/tex; mode=display">x</script> of them to do the same work as one use of <script type="math/tex; mode=display">x^1</script>, which is a strictly higher cost.</p>
<p>Again, in a similar way, we have <script type="math/tex; mode=display">r_2 = \text{target}_2 \pmod {x^2}</script>, and we must either subtract <script type="math/tex; mode=display">r_2 / x</script>
<script type="math/tex; mode=display">x^1</script>'s, or add <script type="math/tex; mode=display">x - r_2 / x</script>
<script type="math/tex; mode=display">x^1</script>'s.  This will form a new remaining target <script type="math/tex; mode=display">\text{target}_3</script>, and so on.</p>
<p>As a concrete example, say <code>x = 5, target = 123</code>.  We either add <code>2</code> or subtract <code>3</code>.  This leaves us with a target of <code>120</code> or <code>125</code>.  If the target is <code>120</code>, we can either add <code>5</code> or subtract <code>20</code>, leaving us with a target of <code>100</code> or <code>125</code>.  If the target is <code>100</code>, we can either add <code>25</code> or subtract <code>100</code>, leaving us with a target of <code>125</code> or <code>0</code>.  If the target is <code>125</code>, we subtract <code>125</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's calculate <code>dp(i, target)</code> using a top down <code>dp</code>.  Here, <code>i</code> will be the exponent of the block <script type="math/tex; mode=display">x^i</script> being considered, and <code>target</code> will be the remaining target, already divided by <script type="math/tex; mode=display">x^i</script>.</p>
<p>From here, the recursion is straightforward: <script type="math/tex; mode=display">r = \text{target} \pmod x</script>, and we either subtract <script type="math/tex; mode=display">r</script> blocks or add <script type="math/tex; mode=display">(x-r)</script> of them.  The base cases are easily deduced - see the code for more details.</p>
<iframe src="https://leetcode.com/playground/zS62KWLG/shared" frameborder="0" width="100%" height="500" name="zS62KWLG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log_{x} \text{target})</script>.  We can prove that we only visit up to two states for each base-x digit of <script type="math/tex; mode=display">\text{target}</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log \text{target})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>