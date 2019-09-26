<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-mathematical-naive-time-limit-exceeded">Approach #2: Mathematical (Naive) [Time Limit Exceeded]</a></li>
<li><a href="#approach-3-mathematical-fast-accepted">Approach #3: Mathematical (Fast) [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each starting number, we scan forward until we meet or exceed the target <code>N</code>.  If we meet it, then it represents one way to write <code>N</code> as a sum of consecutive numbers.</p>
<p>For example, if <code>N = 6</code>, and we scan forward from <code>1</code>, we'll get <code>1 + 2 + 3 = 6</code> which contributes to the answer.  If we scan forward from <code>2</code>, we'll get <code>2 + 3 + 4</code> (the first time that the sum is <code>&gt;= N</code>) which is too big.</p>
<iframe src="https://leetcode.com/playground/W5wabBJ4/shared" frameborder="0" width="100%" height="259" name="W5wabBJ4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-mathematical-naive-time-limit-exceeded">Approach #2: Mathematical (Naive) [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can model the situation by the equation <script type="math/tex; mode=display">N = (x+1) + (x+2) + \cdots + (x+k)</script>.  Here, <script type="math/tex; mode=display">x \geq 0, k \geq 1</script>.  Using the identity <script type="math/tex; mode=display">1 + 2 + \cdots + k = \frac{k(k+1)}{2}</script>, we can simplify this equation to <script type="math/tex; mode=display">2*N = k(2*x + k + 1)</script>.</p>
<p>From here, clearly <script type="math/tex; mode=display">1 \leq k \leq 2*N</script>.  We can try every such <script type="math/tex; mode=display">k</script>.  We need <script type="math/tex; mode=display">x = \frac{\frac{2*N}{k} - k - 1}{2}</script> to be a non-negative integer for a solution to exist for the <script type="math/tex; mode=display">k</script> we are trying.</p>
<iframe src="https://leetcode.com/playground/y3LRDRHT/shared" frameborder="0" width="100%" height="276" name="y3LRDRHT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-mathematical-fast-accepted">Approach #3: Mathematical (Fast) [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in <em>Approach #2</em>, <script type="math/tex; mode=display">2*N = k(2*x + k + 1)</script> with <script type="math/tex; mode=display">x \geq 0, k \geq 1</script>.  Call <script type="math/tex; mode=display">k</script> the first factor, and <script type="math/tex; mode=display">2*x + k + 1</script> the second factor.  We are looking for ways to solve this equation without trying all <script type="math/tex; mode=display">2*N</script> possibilities.</p>
<p>Now notice that the parity of <script type="math/tex; mode=display">k</script> and <script type="math/tex; mode=display">(2*x + k + 1)</script> are different.  That is, if <script type="math/tex; mode=display">k</script> is even then the other quantity is odd, and vice versa.  Also, <script type="math/tex; mode=display">2*x + k + 1 \geq k + 1 > k</script>, so the second factor must be bigger.</p>
<p>Now write <script type="math/tex; mode=display">2N = 2^\alpha * M</script> where <script type="math/tex; mode=display">M</script> is odd.  If we factor <script type="math/tex; mode=display">M = a * b</script>, then two candidate solutions are <script type="math/tex; mode=display">k = a, 2x+k+1 = b * 2^\alpha</script>, or <script type="math/tex; mode=display">k = a * 2^\alpha, 2x+k+1 = b</script>.  However, only one of these solutions will have the second factor larger than the first.  (Because <script type="math/tex; mode=display">\alpha \geq 1</script>, we are guaranteed that one factor is strictly larger.)</p>
<p>Thus, the answer is the number of ways to factor the odd part of <script type="math/tex; mode=display">N</script>.</p>
<iframe src="https://leetcode.com/playground/RNh28dQE/shared" frameborder="0" width="100%" height="378" name="RNh28dQE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\sqrt(N))</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>