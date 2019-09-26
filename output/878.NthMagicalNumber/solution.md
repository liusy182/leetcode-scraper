<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-mathematical">Approach 1: Mathematical</a></li>
<li><a href="#approach-2-binary-search">Approach 2: Binary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-mathematical">Approach 1: Mathematical</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's try to count to the <script type="math/tex; mode=display">N</script>-th magical number mathematically.</p>
<p>First, the pattern of magical numbers repeats.  Let <script type="math/tex; mode=display">L</script> be the least common multiple of <script type="math/tex; mode=display">A</script> and <script type="math/tex; mode=display">B</script>.  If <script type="math/tex; mode=display">X \leq L</script> is magical, then <script type="math/tex; mode=display">X + L</script> is magical, because (for example) <script type="math/tex; mode=display">A \| X</script> and <script type="math/tex; mode=display">A \| L</script> implies <script type="math/tex; mode=display">A \| (X + L)</script>, and similarly if <script type="math/tex; mode=display">B</script> were the divisor.</p>
<p>There are <script type="math/tex; mode=display">M = \frac{L}{A} + \frac{L}{B} - 1</script> magical numbers less than or equal to <script type="math/tex; mode=display">L</script>: <script type="math/tex; mode=display">\frac{L}{A}</script> of them are divisible by <script type="math/tex; mode=display">A</script>, <script type="math/tex; mode=display">\frac{L}{B}</script> of them are divisible by <script type="math/tex; mode=display">B</script>, and <script type="math/tex; mode=display">1</script> of them is divisible by both.  So instead of counting one at a time, we can count by <script type="math/tex; mode=display">M</script> at a time.</p>
<p>Now, suppose <script type="math/tex; mode=display">N = M*q + r</script> (with <script type="math/tex; mode=display">r < M</script>).  The first <script type="math/tex; mode=display">L*q</script> numbers contain <script type="math/tex; mode=display">M*q</script> magical numbers, and within the next numbers <script type="math/tex; mode=display">(L*q + 1, L*q + 2, \cdots)</script> we want to find <script type="math/tex; mode=display">r</script> more magical ones.</p>
<p>For this task, we can use brute force.  The next magical number (less <script type="math/tex; mode=display">L*q</script>) will either be <script type="math/tex; mode=display">A</script> or <script type="math/tex; mode=display">B</script>.  If for example it is <script type="math/tex; mode=display">A</script>, then the next number will either be <script type="math/tex; mode=display">2*A</script> or <script type="math/tex; mode=display">B</script>, and so on.</p>
<p>If the <script type="math/tex; mode=display">r</script>-th such magical number is <script type="math/tex; mode=display">Y</script>, then the final answer is <script type="math/tex; mode=display">L*q + Y</script>.  Care must also be taken in the case that <script type="math/tex; mode=display">r</script> is <script type="math/tex; mode=display">0</script>.</p>
<iframe src="https://leetcode.com/playground/noAa9JNU/shared" frameborder="0" width="100%" height="500" name="noAa9JNU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(A+B)</script>, assuming a model where integer math operations are <script type="math/tex; mode=display">O(1)</script>.  The calculation of <code>q * L</code> is <script type="math/tex; mode=display">O(1)</script>.  The calculation of the <script type="math/tex; mode=display">r</script>-th magical number after <script type="math/tex; mode=display">q*M</script> is <script type="math/tex; mode=display">O(M)</script> which is <script type="math/tex; mode=display">O(A+B)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-binary-search">Approach 2: Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>The number of magical numbers less than or equal to <script type="math/tex; mode=display">x</script> is a monotone increasing function in <script type="math/tex; mode=display">x</script>, so we can binary search for the answer.</p>
<p><strong>Algorithm</strong></p>
<p>Say <script type="math/tex; mode=display">L = \text{lcm}(A, B)</script>, the <em>least common multiple</em> of <script type="math/tex; mode=display">A</script> and <script type="math/tex; mode=display">B</script>; and let <script type="math/tex; mode=display">f(x)</script> be the number of magical numbers less than or equal to <script type="math/tex; mode=display">x</script>.  A well known result says that <script type="math/tex; mode=display">L = \frac{A * B}{\text{gcd}(A, B)}</script>, and that we can calculate the function <script type="math/tex; mode=display">\gcd</script>.  For more information on least common multiples and greatest common divisors, please visit <a href="https://en.wikipedia.org/wiki/Least_common_multiple">Wikipedia - Lowest Common Multiple</a>.</p>
<p>Then <script type="math/tex; mode=display">f(x) = \lfloor \frac{x}{A} \rfloor + \lfloor \frac{x}{B} \rfloor - \lfloor \frac{x}{L} \rfloor</script>.  Why?  There are <script type="math/tex; mode=display">\lfloor \frac{x}{A} \rfloor</script> numbers <script type="math/tex; mode=display">A,  2A,  3A,  \cdots</script> that are divisible by <script type="math/tex; mode=display">A</script>, there are <script type="math/tex; mode=display">\lfloor \frac{x}{B} \rfloor</script> numbers divisible by <script type="math/tex; mode=display">B</script>, and we need to subtract the <script type="math/tex; mode=display">\lfloor \frac{x}{L} \rfloor</script> numbers divisible by <script type="math/tex; mode=display">A</script> and <script type="math/tex; mode=display">B</script> that we double counted.</p>
<p>Finally, the answer must be between <script type="math/tex; mode=display">0</script> and <script type="math/tex; mode=display">N * \max(A, B)</script>.  Without loss of generality, suppose <script type="math/tex; mode=display">A \geq B</script>, so that it remains to show</p>
<p>
<script type="math/tex; mode=display">
\lfloor \frac{N * \max(A, B)}{A} \rfloor + \lfloor \frac{N * \max(A, B)}{B} \rfloor - \lfloor \frac{N * \max(A, B)}{\text{lcm}(A, B)} \rfloor \geq N
</script>
</p>
<p>
<script type="math/tex; mode=display">
\Leftrightarrow \lfloor \frac{N*A}{A} \rfloor + \lfloor \frac{N*A}{B} \rfloor - \lfloor \frac{N*A*\gcd(A, B)}{A*B} \rfloor \geq N
</script>
</p>
<p>
<script type="math/tex; mode=display">
\Leftrightarrow \lfloor \frac{N*A}{B} \rfloor \geq \lfloor \frac{N*\gcd(A, B)}{B} \rfloor
</script>
</p>
<p>
<script type="math/tex; mode=display">
\Leftrightarrow A \geq \gcd(A, B)
</script>
</p>
<p>as desired.</p>
<p>Afterwards, the binary search on <script type="math/tex; mode=display">f</script> is straightforward.  For more information on binary search, please visit <a href="https://leetcode.com/explore/learn/card/binary-search/">[LeetCode Explore - Binary Search]</a>.</p>
<iframe src="https://leetcode.com/playground/3erxMBCQ/shared" frameborder="0" width="100%" height="480" name="3erxMBCQ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log (N * \max(A, B)))</script>.</p>
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