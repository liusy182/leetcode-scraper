<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-using-binary-search">Approach 2: Using Binary Search</a></li>
<li><a href="#approach-3-ternary-search">Approach 3: Ternary Search</a></li>
</ul>
</li>
<li><a href="#follow-up">Follow up</a><ul>
<li><a href="#comparisons-between-binary-search-and-ternary-search">Comparisons between Binary Search and Ternary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>We check every number from 1 to n-1 and pass it to the <script type="math/tex; mode=display">guess</script> function. The number
for which a 0 is returned is the required answer.</p>
<iframe src="https://leetcode.com/playground/fbFHDKsc/shared" frameborder="0" width="100%" height="276" name="fbFHDKsc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We scan all the numbers from 1 to n.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-using-binary-search">Approach 2: Using Binary Search</h4>
<p><strong>Algorithm</strong></p>
<p>We can apply Binary Search to find the given number. We start with the mid
number. We pass that number to the <script type="math/tex; mode=display">guess</script> function. If it returns a -1, it implies that the guessed number is larger than the required one. Thus, we use Binary Search for numbers lower than itself. Similarly, if it returns a 1, we use Binary Search
 for numbers higher than itself.</p>
<iframe src="https://leetcode.com/playground/84NfKnsE/shared" frameborder="0" width="100%" height="429" name="84NfKnsE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O\big(\log_2 n\big)</script>. Binary Search is used.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-3-ternary-search">Approach 3: Ternary Search</h4>
<p><strong>Algorithm</strong></p>
<p>In Binary Search, we choose the middle element as the pivot in splitting. In Ternary Search, we choose two pivots (say <script type="math/tex; mode=display">m1</script> and <script type="math/tex; mode=display">m2</script>) such that the given range is divided into three equal parts. If the required number <script type="math/tex; mode=display">num</script> is less than <script type="math/tex; mode=display">m1</script> then we apply ternary search on the left segment of <script type="math/tex; mode=display">m1</script>. If <script type="math/tex; mode=display">num</script> lies between <script type="math/tex; mode=display">m1</script> and <script type="math/tex; mode=display">m2</script>, we apply ternary search between <script type="math/tex; mode=display">m1</script> and <script type="math/tex; mode=display">m2</script>. Otherwise we will search in the segment right to <script type="math/tex; mode=display">m2</script>.</p>
<iframe src="https://leetcode.com/playground/ZVkdvE5j/shared" frameborder="0" width="100%" height="500" name="ZVkdvE5j"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O\big(\log_3 n \big)</script>. Ternary Search is used.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.
<br>
<br></li>
</ul>
<hr>
<h2 id="follow-up">Follow up</h2>
<p>It seems that ternary search is able to terminate earlier compared to binary search. But why is binary search more widely used?</p>
<h4 id="comparisons-between-binary-search-and-ternary-search">Comparisons between Binary Search and Ternary Search</h4>
<p>Ternary Search is worse than Binary Search. The following outlines the recursive formula to count comparisons of Binary Search in the worst case.</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
T(n) &= T\bigg(\frac{n}{2} \ \bigg) + 2, \quad T(1) = 1 \\
T\bigg(\frac{n}{2} \ \bigg) &= T\bigg(\frac{n}{2^2} \ \bigg) + 2 \\
\\
\therefore{} \quad T(n) &= T\bigg(\frac{n}{2^2} \ \bigg) + 2 \times 2 \\
&= T\bigg(\frac{n}{2^3} \ \bigg) + 3 \times 2 \\
&= \ldots \\
&= T\bigg(\frac{n}{2^{\log_2 n}} \ \bigg) + 2 \log_2 n \\
&= T(1) + 2 \log_2 n \\
&= 1 + 2 \log_2 n
\end{aligned}
</script>
</p>
<p>The following outlines the recursive formula to count comparisons of Ternary Search in the worst case.</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
T(n) &= T\bigg(\frac{n}{3} \ \bigg) + 4, \quad T(1) = 1 \\
T\bigg(\frac{n}{3} \ \bigg) &= T\bigg(\frac{n}{3^2} \ \bigg) + 4 \\
\\
\therefore{} \quad T(n) &= T\bigg(\frac{n}{3^2} \ \bigg) + 2 \times 4 \\
&= T\bigg(\frac{n}{3^3} \ \bigg) + 3 \times 4 \\
&= \ldots \\
&= T\bigg(\frac{n}{3^{\log_3 n}} \ \bigg) + 4 \log_3 n \\
&= T(1) + 4 \log_3 n \\
&= 1 + 4 \log_3 n
\end{aligned}
</script>
</p>
<p>As shown above, the total comparisons in the worst case for ternary and binary search are <script type="math/tex; mode=display">1 + 4 \log_3 n</script> and <script type="math/tex; mode=display">1 + 2 \log_2 n</script> comparisons respectively. To determine which is larger, we can just look at the expression <script type="math/tex; mode=display">2 \log_3 n</script> and <script type="math/tex; mode=display">\log_2 n</script> . The expression <script type="math/tex; mode=display">2 \log_3 n</script> can be written as <script type="math/tex; mode=display">\frac{2}{\log_2 3} \times \log_2 n</script> . Since the value of <script type="math/tex; mode=display">\frac{2}{\log_2 3}</script> is greater than one, Ternary Search does more comparisons than Binary Search in the worst case.</p>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>