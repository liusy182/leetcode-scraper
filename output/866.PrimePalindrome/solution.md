<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-framework">Approach Framework</a></li>
<li><a href="#approach-1-iterate-palindromes">Approach 1: Iterate Palindromes</a></li>
<li><a href="#approach-2-brute-force-with-mathematical-shortcut">Approach 2: Brute Force with Mathematical Shortcut</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-framework">Approach Framework</h4>
<p><strong>Investigation of Brute Force</strong></p>
<p>Let's investigate and improve on a brute force method.</p>
<p>With basic methods, we can check whether an integer <script type="math/tex; mode=display">N</script> is a palindrome in <script type="math/tex; mode=display">O(\log N)</script> time, and check whether it is prime in <script type="math/tex; mode=display">O(\sqrt{N})</script> time.  So we would probably like to do the palindrome check first.</p>
<p>Now, say we naively check every number <script type="math/tex; mode=display">N, N+1, \cdots, N+K</script>.  How big is <script type="math/tex; mode=display">K</script>?</p>
<p>Well, the palindromes could be approximately <script type="math/tex; mode=display">10^4</script> apart, since for example <code>99988999</code>'s next palindrome is <code>99999999</code>.  </p>
<p>If we assume being a palindrome and being a prime is independent, then based on the density of primes, <script type="math/tex; mode=display">K \approx 10^4 \log N</script>, and we would do a palindrome check on approximately <script type="math/tex; mode=display">10^4 \log^2 N</script> values, and a primality test on <script type="math/tex; mode=display">\log N</script> values of complexity <script type="math/tex; mode=display">\sqrt{N} \log N</script>.  This seems to work.</p>
<p>However, we can't make this assumption of independence: whether a number is a palindrome or prime are <em>negatively correlated</em> events!  For example, <script type="math/tex; mode=display">22, 33, 44, \cdots, 99</script> are clearly not prime.  Actually, all palindromes with an even number of digits are divisible by 11, and are therefore not prime!  (Except for 11.)  For example, an 8 digit palindrome can be written as:</p>
<p>
<script type="math/tex; mode=display">\sum_{i=0}^{3} a_i(10^{7-i} + 10^i) \equiv \sum a_i((-1)^{7-i} + (-1)^i) \equiv \sum a_i(0) \equiv 0 \pmod{11}</script>
</p>
<p>where the second-last equivalence follows as <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">7-i</script> have different parity.</p>
<p><strong>Density of Palindromes</strong></p>
<p>For a palindrome of <script type="math/tex; mode=display">d</script> digits, choosing the first <script type="math/tex; mode=display">k = \lfloor \frac{d+1}{2} \rfloor</script> digits uniquely determines the remaining digits.  Hence, there are <script type="math/tex; mode=display">9 * 10^{k-1}</script> of them (the first digit can't be 0.)  Thus, there are</p>
<p>
<script type="math/tex; mode=display">9(10^0 + 10^0 + 10^1 + 10^1 + 10^2 + 10^2 + 10^3 + 10^3) < 20000</script>
</p>
<p>palindromes of 8 digits or less.  </p>
<p>Actually, we don't need to check the palindromes with an even number of digits, so there are under 10000 palindromes we need to check.  However, we also need to check palindromes until we encounter the first 9 digit prime palindrome, as all 8 digit numbers <script type="math/tex; mode=display">N</script> will have an answer equal to that.  Luckily, it occurs quickly: <code>100030001</code> is the 4th 9-digit value checked.  (We can verify this with brute force.)</p>
<p>For each palindrome, we can test whether it is prime in <script type="math/tex; mode=display">O(\sqrt{N})</script> operations.  So in total, an approach centered around enumerating palindromes seems like it will succeed.
<br>
<br></p>
<hr>
<h4 id="approach-1-iterate-palindromes">Approach 1: Iterate Palindromes</h4>
<p><strong>Intuition</strong></p>
<p>Say we have a palindrome <script type="math/tex; mode=display">X</script>.  What is the next palindrome?</p>
<p>Each palindrome of <script type="math/tex; mode=display">d</script> digits has a <em>palindromic root</em>, it's first <script type="math/tex; mode=display">k = \frac{d+1}{2}</script> digits.  The next palindrome is formed by the next root.</p>
<p>For example, if <script type="math/tex; mode=display">123</script> is a root for the 5 digit palindrome <script type="math/tex; mode=display">12321</script>, then the next palindrome is <script type="math/tex; mode=display">12421</script> with root <script type="math/tex; mode=display">124</script>.</p>
<p>Notice that roots and palindromes are not a bijection, as palindromes <script type="math/tex; mode=display">123321</script> and <script type="math/tex; mode=display">12321</script> have the same root.</p>
<p><strong>Algorithm</strong></p>
<p>For each <em>palindromic root</em>, let's find the two associated palindromes (one with an odd number of digits, and one with an even number.)  For roots with <script type="math/tex; mode=display">k</script> digits, they will generate palindromes of <script type="math/tex; mode=display">2*k - 1</script> and <script type="math/tex; mode=display">2*k</script> digits.</p>
<p>If we didn't know that palindromes with an even number of digits (and greater than 11) are never prime, we're still fine - we can just check both possibilities.  When checking both possibilities, we check the palindromes with <script type="math/tex; mode=display">2k - 1</script> digits first, as they are all smaller than the palindromes with <script type="math/tex; mode=display">2k</script> digits.</p>
<p>We'll use an idea from <a href="https://leetcode.com/problems/reverse-integer">[LeetCode Problem: Reverse an Integer]</a>, in order to check whether an integer is a palindrome.  We could have also converted the integer to a string, and checked the indices directly.</p>
<p>As for testing primes with <code>isPrime(N)</code>, we'll use the standard <script type="math/tex; mode=display">O(\sqrt{N})</script> check: testing whether every number <script type="math/tex; mode=display">\leq \sqrt{N}</script> is a divisor of <script type="math/tex; mode=display">N</script>.</p>
<iframe src="https://leetcode.com/playground/UgnkELMD/shared" frameborder="0" width="100%" height="500" name="UgnkELMD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity:  Based on our analysis above, we performed on the order of <script type="math/tex; mode=display">O(N)</script> operations (not counting log factors from dealing with integers), given we knew the existence of prime palindrome <code>100030001</code>.  </li>
</ul>
<p>Interestingly, the time complexity is an open problem in mathematics, as it is not even known whether there are infinitely many prime palindromes, or whether palindromes behave as random integers for our purposes here - see <a href="https://arxiv.org/pdf/math/0405056.pdf">["Almost All Palindromes are Composite"]</a> for more.</p>
<ul>
<li>Space Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, the space used by <code>s</code> (or <code>sb</code> in Java.)
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-brute-force-with-mathematical-shortcut">Approach 2: Brute Force with Mathematical Shortcut</h4>
<p><strong>Intuition</strong></p>
<p>Our brute force works except when <script type="math/tex; mode=display">N</script> is 8 digits (as explained in <em>Approach Framework</em> when we established that all 8 digit palindromes are not prime), so we can skip all 8 digit numbers.</p>
<p><strong>Algorithm</strong></p>
<p>For each number, check whether it is a palindrome.  If it is, check whether it is a prime.  If the number is 8 digits, skip to the 9 digit numbers.</p>
<iframe src="https://leetcode.com/playground/NSw4owuf/shared" frameborder="0" width="100%" height="500" name="NSw4owuf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, with the caveats explained in <em>Approach #1</em>, and ignoring the <script type="math/tex; mode=display">\log N</script> factor when checking an integer for palindromes.</p>
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