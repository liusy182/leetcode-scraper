<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-better-brute-force-time-limit-exceeded">Approach #2 Better Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-3-optimal-solution-accepted">Approach #3 Optimal Solution [Accepted]</a></li>
<li><a href="#approach-4-euclid-euler-theorem-accepted">Approach #4 Euclid-Euler Theorem [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>In brute force approach, we consider every possible number to be a divisor of the given number <script type="math/tex; mode=display">num</script>, by iterating over all the numbers lesser than <script type="math/tex; mode=display">num</script>. Then, we add up all the factors to check if the given number satisfies the Perfect Number property. This approach obviously fails if the number <script type="math/tex; mode=display">num</script> is very large.</p>
<iframe src="https://leetcode.com/playground/6Nzf7w9h/shared" frameborder="0" name="6Nzf7w9h" width="100%" height="343"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We iterate over all the numbers lesser than <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force-time-limit-exceeded">Approach #2 Better Brute Force [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>We can little optimize the brute force by breaking the loop when the value of <script type="math/tex; mode=display">sum</script> increase the value of <script type="math/tex; mode=display">num</script>. In that case, we can directly return <script type="math/tex; mode=display">false</script>.</p>
<iframe src="https://leetcode.com/playground/bGGFxpmt/shared" frameborder="0" name="bGGFxpmt" width="100%" height="377"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. In worst case, we iterate over all the numbers lesser than <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-optimal-solution-accepted">Approach #3 Optimal Solution [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In this method, instead of iterating over all the integers to find the factors of <script type="math/tex; mode=display">num</script>, we only iterate upto the <script type="math/tex; mode=display">\sqrt{n}</script>. The reasoning behind this can be understood as follows.</p>
<p>Consider the given number <script type="math/tex; mode=display">num</script> which can have <script type="math/tex; mode=display">m</script> distinct factors, namely <script type="math/tex; mode=display">n_1, n_2,..., n_m</script>. Now, since the number <script type="math/tex; mode=display">num</script> is divisible by <script type="math/tex; mode=display">n_i</script>, it is also divisible by <script type="math/tex; mode=display">n_j=num/n_1</script> i.e. <script type="math/tex; mode=display">n_i*n_j=num</script>. Also, the largest number in such a pair can only be up to <script type="math/tex; mode=display">\sqrt{num}</script> (because <script type="math/tex; mode=display">\sqrt{num} \times \sqrt{num}=num</script>). Thus, we can get a significant reduction in the run-time by iterating only upto <script type="math/tex; mode=display">\sqrt{num}</script> and considering such <script type="math/tex; mode=display">n_i</script>'s and <script type="math/tex; mode=display">n_j</script>'s in a single pass directly.</p>
<p>Further, if <script type="math/tex; mode=display">\sqrt{num}</script> is also a factor, we have to consider the factor only once while checking for the perfect number property.</p>
<p>We sum up all such factors and check if the given number is a Perfect Number or not. Another point to be observed is that while considering 1 as such a factor, <script type="math/tex; mode=display">num</script> will also be considered as the other factor. Thus, we need to subtract <script type="math/tex; mode=display">num</script> from the <script type="math/tex; mode=display">sum</script>.</p>
<iframe src="https://leetcode.com/playground/ZpHuGfHj/shared" frameborder="0" name="ZpHuGfHj" width="100%" height="377"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(\sqrt{n})</script>. We iterate only over the range <script type="math/tex; mode=display">1 < i &leq; \sqrt{num}</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</li>
</ul>
<hr>
<h4 id="approach-4-euclid-euler-theorem-accepted">Approach #4 Euclid-Euler Theorem [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Euclid proved that <script type="math/tex; mode=display">2^{p−1}(2^p − 1)</script> is an even perfect number whenever <script type="math/tex; mode=display">2^p − 1</script> is prime, where <script type="math/tex; mode=display">p</script> is prime.</p>
<p>For example, the first four perfect numbers are generated by the formula <script type="math/tex; mode=display">2^{p−1}(2^p − 1)</script>, with <script type="math/tex; mode=display">p</script> a prime number, as follows:</p>
<div class="codehilite"><pre><span></span>for p = 2:   21(22 − 1) = 6
for p = 3:   22(23 − 1) = 28
for p = 5:   24(25 − 1) = 496
for p = 7:   26(27 − 1) = 8128.
</pre></div>


<p>Prime numbers of the form <script type="math/tex; mode=display">2^p − 1</script> are known as Mersenne primes. For <script type="math/tex; mode=display">2^p − 1</script> to be prime, it is necessary that <script type="math/tex; mode=display">p</script> itself be prime. However, not all numbers of the form <script type="math/tex; mode=display">2^p − 1</script> with a prime <script type="math/tex; mode=display">p</script> are prime; for example, <script type="math/tex; mode=display">2^{11} − 1 = 2047 = 23 × 89</script> is not a prime number.</p>
<p>You can see that for small value of <script type="math/tex; mode=display">p</script>, its related perfect number goes very high. So, we need to evaluate perfect numbers for some primes <script type="math/tex; mode=display">(2, 3, 5, 7, 13, 17, 19, 31)</script> only, as for bigger prime its perfect number will not fit in 64 bits.</p>
<iframe src="https://leetcode.com/playground/kBfJ6TtU/shared" frameborder="0" name="kBfJ6TtU" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log{n})</script>. Number of primes will be in order <script type="math/tex; mode=display">\log{num}</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log{n})</script>. Space used to store primes.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>