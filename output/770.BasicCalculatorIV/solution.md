<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-polynomial-class-accepted">Approach #1: Polynomial Class [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-polynomial-class-accepted">Approach #1: Polynomial Class [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Keep a class <code>Poly</code> that knows a map from a list of free variables to a coefficient, and support operations on this class.</p>
<p><strong>Algorithm</strong></p>
<p>Each function is straightforward individually.  Let's list the functions we use:</p>
<ul>
<li><code>Poly:add(this, that)</code> returns the result of <code>this + that</code>.</li>
<li><code>Poly:sub(this, that)</code> returns the result of <code>this - that</code>.</li>
<li><code>Poly:mul(this, that)</code> returns the result of <code>this * that</code>.</li>
<li><code>Poly:evaluate(this, evalmap)</code> returns the polynomial after replacing all free variables with constants as specified by <code>evalmap</code>.</li>
<li>
<p><code>Poly:toList(this)</code> returns the polynomial in the correct output format.</p>
</li>
<li>
<p><code>Solution::combine(left, right, symbol)</code> returns the result of applying the binary operator represented by <code>symbol</code> to <code>left</code> and <code>right</code>.</p>
</li>
<li><code>Solution::make(expr)</code> makes a new <code>Poly</code> represented by either the constant or free variable specified by <code>expr</code>.</li>
<li><code>Solution::parse(expr)</code> parses an expression into a new <code>Poly</code>.</li>
</ul>
<iframe src="https://leetcode.com/playground/9KquDr4P/shared" frameborder="0" width="100%" height="500" name="9KquDr4P"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  Let <script type="math/tex; mode=display">N</script> is the length of <code>expression</code> and <script type="math/tex; mode=display">M</script> is the length of <code>evalvars</code> and <code>evalints</code>.  With an expression like <code>(a + b) * (c + d) * (e + f) * ...</code> the complexity is <script type="math/tex; mode=display">O(2^N + M)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N + M)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>