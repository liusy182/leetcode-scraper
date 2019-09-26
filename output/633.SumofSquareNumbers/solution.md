<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-better-brute-force">Approach 2: Better Brute Force</a></li>
<li><a href="#approach-3-using-sqrt-function">Approach 3: Using Sqrt Function</a></li>
<li><a href="#approach-4-binary-search">Approach 4: Binary Search</a></li>
<li><a href="#approach-5-fermat-theorem">Approach 5: Fermat Theorem</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>The simplest solution would be to consider every possible combination of integers <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> and check if the sum of their squares equals <script type="math/tex; mode=display">c</script>. Now, both <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> can lie within the range <script type="math/tex; mode=display">(0,\sqrt{c})</script>. Thus, we need to check for the values of <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> in this range only.</p>
<iframe src="https://leetcode.com/playground/jHjno8MG/shared" frameborder="0" width="100%" height="242" name="jHjno8MG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(c)</script>. Two loops upto <script type="math/tex; mode=display">\sqrt{c}</script>. Here, <script type="math/tex; mode=display">c</script> refers to the given integer(sum of squares).</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force">Approach 2: Better Brute Force</h4>
<p>We can improve the last solution, if we make the following observation. For any particular <script type="math/tex; mode=display">a</script> chosen, the value of <script type="math/tex; mode=display">b</script> required to satisfy the equation <script type="math/tex; mode=display">a^2 + b^2 = c</script> will be such that <script type="math/tex; mode=display">b^2 = c - a^2</script>. Thus, we need to traverse over the range <script type="math/tex; mode=display">(0, \sqrt{c})</script> only for considering the various values of <script type="math/tex; mode=display">a</script>. For every current value of <script type="math/tex; mode=display">a</script> chosen, we can determine the corresponding <script type="math/tex; mode=display">b^2</script> value and check if it is a perfect square or not. If it happens to be a perfect square, <script type="math/tex; mode=display">c</script> is a sum of squares of two integers, otherwise not.</p>
<p>Now, to determine, if the number <script type="math/tex; mode=display">c - a^2</script> is a perfect square or not, we can make use of the following theorem:</p>
<blockquote>
<p>The square of <script type="math/tex; mode=display">n^{th}</script> positive integer can be represented as a sum of first <script type="math/tex; mode=display">n</script> odd positive integers.</p>
</blockquote>
<p>Or in mathematical terms:</p>
<p>
<script type="math/tex; mode=display">
n^2 = 1 + 3 + 5 + ... + (2 \cdot n-1) = \sum_{i=1}^{n} (2 \cdot i - 1)
</script>
</p>
<p>To look at the proof of this statement, look at the L.H.S. of the above statement.</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
&1 + 3 + 5 + \ldots + (2 \cdot n-1) \\
= \; &(2 \cdot 1-1) + (2 \cdot 2-1) + (2 \cdot 3-1) + \ldots + (2 \cdot n-1) \\
= \; &2 \cdot (1+2+3+....+n) - (\underbrace{1+1+ \ldots +1}_{n\text{ times}}) \\
= \; &2 \cdot \frac{n\;(n+1)}{2} - n \\
= \; &n\;(n+1) - n \\
= \; &n^2 + n - n \\
= \; &n^2
\end{aligned}
</script>
</p>
<p>This completes the proof of the above statement.</p>
<iframe src="https://leetcode.com/playground/U2tJwtas/shared" frameborder="0" width="100%" height="310" name="U2tJwtas"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(c)</script>. The total number of times the <script type="math/tex; mode=display">sum</script> is updated is: <script type="math/tex; mode=display">1 + 2 + 3 + \ldots + \sqrt{c} = \frac{\sqrt{c}\;(\sqrt{c}+1)}{2} = O(c)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-sqrt-function">Approach 3: Using Sqrt Function</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of finding if <script type="math/tex; mode=display">c - a^2</script> is a perfect square using sum of odd numbers, as done in the last approach, we can make use of the inbuilt <script type="math/tex; mode=display">sqrt</script> function and check if <script type="math/tex; mode=display">\sqrt{c - a^2}</script> turns out to be an integer. If it happens for any value of <script type="math/tex; mode=display">a</script> in the range <script type="math/tex; mode=display">[0, \sqrt{c}]</script>, we can return a True value immediately.</p>
<iframe src="https://leetcode.com/playground/XxfAG3pm/shared" frameborder="0" width="100%" height="225" name="XxfAG3pm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(\sqrt{c}\log c\big)</script>. We iterate over <script type="math/tex; mode=display">\sqrt{c}</script> values for choosing <script type="math/tex; mode=display">a</script>. For every <script type="math/tex; mode=display">a</script> chosen, finding square root of <script type="math/tex; mode=display">c - a^2</script> takes <script type="math/tex; mode=display">O\big(\log c\big)</script> time in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-binary-search">Approach 4: Binary Search</h4>
<p><strong>Algorithm</strong></p>
<p>Another method to check if <script type="math/tex; mode=display">c - a^2</script> is a perfect square, is by making use of Binary Search. The method remains same as that of a typical Binary Search to find a number.
The only difference lies in that we need to find an integer, <script type="math/tex; mode=display">mid</script> in the range <script type="math/tex; mode=display">[0, c - a^2]</script>, such that this number is the square root of <script type="math/tex; mode=display">c - a^2</script>.
Or in other words, we need to find an integer, <script type="math/tex; mode=display">mid</script>, in the range <script type="math/tex; mode=display">[0, c - a^2]</script>, such that <script type="math/tex; mode=display">mid \times mid = c - a^2</script>.</p>
<p>The following animation illustrates the search process for a particular value of <script type="math/tex; mode=display">c - a^2 = 36</script>.</p>
<p>!?!../Documents/633_Sum_of_Squares.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/rjrUuXxS/shared" frameborder="0" width="100%" height="395" name="rjrUuXxS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(\sqrt{c}\log c\big)</script>. Binary search taking <script type="math/tex; mode=display">O\big(\log c\big)</script> in the worst case is done for <script type="math/tex; mode=display">\sqrt{c}</script> values of <script type="math/tex; mode=display">a</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log c)</script>. Binary Search will take <script type="math/tex; mode=display">O(\log c)</script> space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-fermat-theorem">Approach 5: Fermat Theorem</h4>
<p><strong>Algorithm</strong></p>
<p>This approach is based on the following statement, which is based on Fermat's Theorem:</p>
<blockquote>
<p>Any positive number <script type="math/tex; mode=display">n</script> is expressible as a sum of two squares if and only if the prime factorization of <script type="math/tex; mode=display">n</script>, every prime of the form <script type="math/tex; mode=display">(4k+3)</script> occurs an even number of times.</p>
</blockquote>
<p>By making use of the above theorem, we can directly find out if the given number <script type="math/tex; mode=display">c</script> can be expressed as a sum of two squares.</p>
<p>To do so we simply find all the prime factors of the given number <script type="math/tex; mode=display">c</script>, which could range from <script type="math/tex; mode=display">[2,\sqrt{c}]</script> along with the count of those factors, by repeated division. 
If at any step, we find out that the number of occurences of any prime factor of the form <script type="math/tex; mode=display">(4k+3)</script> occurs an odd number of times, we can return a False value.</p>
<p>In case, <script type="math/tex; mode=display">c</script> itself is a prime number, it won't be divisible by any of the primes in the <script type="math/tex; mode=display">[2,\sqrt{c}]</script>. Thus, we need to check if <script type="math/tex; mode=display">c</script> can be expressed in the form of
<script type="math/tex; mode=display">4k+3</script>. If so, we need to return a False value, indicating that this prime occurs an odd number(1) of times. </p>
<p>Otherwise, we can return a True value.</p>
<p>The proof of this theorem includes the knowledge of advanced mathematics and is beyond the scope of this article. However, interested reader can refer to <a href="http://wstein.org/edu/124/lectures/lecture21/lecture21/node2.html">this</a> documentation.</p>
<iframe src="https://leetcode.com/playground/fRuxZSWf/shared" frameborder="0" width="100%" height="327" name="fRuxZSWf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(\sqrt{c}\log c\big)</script>. We find the factors of <script type="math/tex; mode=display">c</script> and their count using repeated division. We check for the factors in the range <script type="math/tex; mode=display">[0, \sqrt{c}]</script>.
The maximum number of times a factor can occur(repeated division can be done) is <script type="math/tex; mode=display">\log n</script>(considering 2 as the only factor, <script type="math/tex; mode=display">c=2^x</script>. Thus, <script type="math/tex; mode=display">x=\log c</script>).</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>