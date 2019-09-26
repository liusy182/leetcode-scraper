<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-loop-iteration">Approach 1: Loop Iteration</a></li>
<li><a href="#approach-2-base-conversion">Approach 2: Base Conversion</a></li>
<li><a href="#approach-3-mathematics">Approach 3: Mathematics</a></li>
<li><a href="#approach-4-integer-limitations">Approach 4: Integer Limitations</a></li>
</ul>
</li>
<li><a href="#performance-measurements">Performance Measurements</a></li>
<li><a href="#conclusion">Conclusion</a></li>
<li><a href="#references">References</a></li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>In this article we will look into ways of speeding up simple computations and why that is useful in practice.
<br>
<br></p>
<hr>
<h4 id="approach-1-loop-iteration">Approach 1: Loop Iteration</h4>
<p>One simple way of finding out if a number <code>n</code> is a power of a number <code>b</code> is to keep dividing <code>n</code> by <code>b</code> as long as the remainder is <strong>0</strong>. This is because we can write</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
n &= b^x \\
n &= b \times b \times \ldots \times b
\end{aligned}
</script>
</p>
<p>Hence it should be possible to divide <code>n</code> by <code>b</code> <code>x</code> times, every time with a remainder of <strong>0</strong> and the end result to be <strong>1</strong>.</p>
<iframe src="https://leetcode.com/playground/ojoAnJXy/shared" frameborder="0" width="100%" height="276" name="ojoAnJXy"></iframe>

<p>Notice that we need a guard to check that <code>n != 0</code>, otherwise the while loop will never finish. For negative numbers, the algorithm does not make sense, so we will include this guard as well.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log_b(n))</script>. In our case that is <script type="math/tex; mode=display">O(\log_3n)</script>. The number of divisions is given by that logarithm.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. We are not using any additional memory.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-base-conversion">Approach 2: Base Conversion</h4>
<p>In Base 10, all powers of 10 start with the digit <strong>1</strong> and then are followed only by <strong>0</strong> (e.g. 10, 100, 1000). This is true for other bases and their respective powers. For instance in <em>base 2</em>, the representations of <script type="math/tex; mode=display">10_2</script>, <script type="math/tex; mode=display">100_2</script> and <script type="math/tex; mode=display">1000_2</script> are <script type="math/tex; mode=display">2_{10}</script>, <script type="math/tex; mode=display">4_{10}</script> and <script type="math/tex; mode=display">8_{10}</script> respectively. Therefore if we convert our number to base 3 and the representation is of the form 100...0, then the number is a power of 3.</p>
<p><strong>Proof</strong></p>
<p>Given the base 3 representation of a number as the array <code>s</code>, with the least significant digit on index 0, the formula for converting from base <strong>3</strong> to base <strong>10</strong> is:</p>
<p>
<script type="math/tex; mode=display">
\sum_{i=0}^{len(s) - 1} s[i] * 3^{i}
</script>
</p>
<p>Therefore, having just one digit of <strong>1</strong> and everything else <strong>0</strong> means the number is a power of 3.</p>
<p><strong>Implementation</strong></p>
<p>All we need to do is convert <sup id="fnref:note-4"><a class="footnote-ref" href="#fn:note-4" rel="footnote">4</a></sup> the number to <em>base 3</em> and check if it is written as a leading <strong>1</strong> followed by all <strong>0</strong>.</p>
<p>A couple of built-in Java functions will help us along the way.</p>
<iframe src="https://leetcode.com/playground/mswCj3De/shared" frameborder="0" width="100%" height="72" name="mswCj3De"></iframe>

<p>The code above converts <code>number</code> into base <code>base</code> and returns the result as a <code>String</code>. For example, <code>Integer.toString(5, 2) == "101"</code> and <code>Integer.toString(5, 3) == "12"</code>.</p>
<iframe src="https://leetcode.com/playground/T6CmNK28/shared" frameborder="0" width="100%" height="72" name="T6CmNK28"></iframe>

<p>The code above checks if a certain <strong>Regular Expression</strong> <sup id="fnref:note-2"><a class="footnote-ref" href="#fn:note-2" rel="footnote">2</a></sup> pattern exists inside a string. For instance the above will return true if the substring "123" exists inside the string <code>myString</code>.</p>
<iframe src="https://leetcode.com/playground/mujLkBaw/shared" frameborder="0" width="100%" height="72" name="mujLkBaw"></iframe>

<p>We will use the regular expression above for checking if the string starts with <strong>1</strong> <code>^1</code>, is followed by zero or more <strong>0</strong>s <code>0*</code> and contains nothing else <code>＄</code>.</p>
<iframe src="https://leetcode.com/playground/Vg5V7RYp/shared" frameborder="0" width="100%" height="140" name="Vg5V7RYp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log_3n)</script>.</p>
<p>Assumptions:</p>
<ul>
<li><code>Integer.toString()</code> - Base conversion is generally implemented as a repeated division. The complexity of  should be similar to our Approach 1: <script type="math/tex; mode=display">O(\log_3n)</script>.</li>
<li><code>String.matches()</code> - Method iterates over the entire string. The number of digits in the base 3 representation of <code>n</code> is <script type="math/tex; mode=display">O(\log_3n)</script>.</li>
</ul>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log_3n)</script>.</p>
<p>We are using two additional variables,</p>
<ul>
<li>The string of the base 3 representation of the number (size <script type="math/tex; mode=display">\log_3n</script>)</li>
<li>The string of the regular expression (constant size)
<br>
<br></li>
</ul>
</li>
</ul>
<hr>
<h4 id="approach-3-mathematics">Approach 3: Mathematics</h4>
<p>We can use mathematics as follows</p>
<p>
<script type="math/tex; mode=display">
n = 3^i \\
i = \log_3(n) \\
i = \frac{\log_b(n)}{\log_b(3)}
</script>
</p>
<p><code>n</code> is a power of three if and only if <code>i</code> is an integer. In Java, we check if a number is an integer by taking the decimal part (using <code>% 1</code>) and checking if it is 0.</p>
<iframe src="https://leetcode.com/playground/rGU5MG2p/shared" frameborder="0" width="100%" height="140" name="rGU5MG2p"></iframe>

<p><strong>Common pitfalls</strong></p>
<p>This solution is problematic because we start using <code>double</code>s, which means we are subject to precision errors. This means, we should never use <code>==</code> when comparing <code>double</code>s. That is because the result of <code>Math.log10(n) / Math.log10(3)</code> could be <code>5.0000001</code> or <code>4.9999999</code>. This effect can be observed by using the function <code>Math.log()</code> instead of <code>Math.log10()</code>.</p>
<p>In order to fix that, we need to compare the result against an <code>epsilon</code>.</p>
<iframe src="https://leetcode.com/playground/eVP3xfwb/shared" frameborder="0" width="100%" height="72" name="eVP3xfwb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">Unknown</script> The expensive operation here is <code>Math.log</code>, which upper bounds the time complexity of our algorithm. The implementation is dependent on the language we are using and the compiler <sup id="fnref:note-3"><a class="footnote-ref" href="#fn:note-3" rel="footnote">3</a></sup></p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. We are not using any additional memory. The <code>epsilon</code> variable can be inlined.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-integer-limitations">Approach 4: Integer Limitations</h4>
<p>An important piece of information can be deduced from the function signature</p>
<iframe src="https://leetcode.com/playground/2s2CCD3x/shared" frameborder="0" width="100%" height="0" name="2s2CCD3x"></iframe>

<p>In particular, <code>n</code> is of type <code>int</code>. In Java, this means it is a 4 byte, signed integer [ref]. The maximum value of this data type is <strong>2147483647</strong>. Three ways of calculating this value are</p>
<ul>
<li><a href="https://stackoverflow.com/questions/15004944/max-value-of-integer">Google</a></li>
<li><code>System.out.println(Integer.MAX_VALUE);</code></li>
<li>MaxInt = <script type="math/tex; mode=display">\frac{ 2^{32} }{2} - 1</script> since we use 32 bits to represent the number, half of the range is used for negative numbers and 0 is part of the positive numbers</li>
</ul>
<p>Knowing the limitation of <code>n</code>, we can now deduce that the maximum value of <code>n</code> that is also a power of three is <strong>1162261467</strong>. We calculate this as:</p>
<p>
<script type="math/tex; mode=display">
3^{\lfloor{}\log_3{MaxInt}\rfloor{}} = 3^{\lfloor{}19.56\rfloor{}} = 3^{19} = 1162261467
</script>
</p>
<p>Therefore, the possible values of <code>n</code> where we should return <code>true</code> are <script type="math/tex; mode=display">3^0</script>, <script type="math/tex; mode=display">3^1</script> ... <script type="math/tex; mode=display">3^{19}</script>. Since 3 is a prime number, the only divisors of <script type="math/tex; mode=display">3^{19}</script> are <script type="math/tex; mode=display">3^0</script>, <script type="math/tex; mode=display">3^1</script> ... <script type="math/tex; mode=display">3^{19}</script>, therefore all we need to do is divide <script type="math/tex; mode=display">3^{19}</script> by <code>n</code>. A remainder of <strong>0</strong> means <code>n</code> is a divisor of <script type="math/tex; mode=display">3^{19}</script> and therefore a power of three.</p>
<iframe src="https://leetcode.com/playground/P5BpBmpB/shared" frameborder="0" width="100%" height="140" name="P5BpBmpB"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>. We are only doing one operation.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. We are not using any additional memory.
<br>
<br></p>
</li>
</ul>
<hr>
<h2 id="performance-measurements">Performance Measurements</h2>
<p>Single runs of the function make it is hard to accurately measure the difference of the two solutions. On LeetCode, on the <em>Accepted Solutions Runtime Distribution</em> page, all solutions being between <code>15 ms</code> and <code>20 ms</code>. For completeness, we have proposed the following benchmark to see how the two solutions differ.</p>
<p><strong>Java Benchmark Code</strong></p>
<iframe src="https://leetcode.com/playground/7bpZrVLY/shared" frameborder="0" width="100%" height="174" name="7bpZrVLY"></iframe>

<p>In the table below, the values are in seconds.</p>
<table>
<thead>
<tr>
<th align="center">Iterations</th>
<th align="center">
<script type="math/tex; mode=display">10^6</script>
</th>
<th align="center">
<script type="math/tex; mode=display">10^7</script>
</th>
<th align="center">
<script type="math/tex; mode=display">10^8</script>
</th>
<th align="center">
<script type="math/tex; mode=display">10^9</script>
</th>
<th align="center">
<script type="math/tex; mode=display">Maxint</script>
</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Java Approach 1: (Naive)</td>
<td align="center">0.04</td>
<td align="center">0.07</td>
<td align="center">0.30</td>
<td align="center">2.47</td>
<td align="center">5.26</td>
</tr>
<tr>
<td align="center">Java Approach 2: (Strings)</td>
<td align="center">0.68</td>
<td align="center">4.02</td>
<td align="center">38.90</td>
<td align="center">409.16</td>
<td align="center">893.89</td>
</tr>
<tr>
<td align="center">Java Approach 3: (Logarithms)</td>
<td align="center">0.09</td>
<td align="center">0.50</td>
<td align="center">4.59</td>
<td align="center">45.53</td>
<td align="center">97.50</td>
</tr>
<tr>
<td align="center">Java Approach 4: (Fast)</td>
<td align="center">0.04</td>
<td align="center">0.06</td>
<td align="center">0.08</td>
<td align="center">0.41</td>
<td align="center">0.78</td>
</tr>
</tbody>
</table>
<p>As we can see, for small values of N, the difference is not noticeable, but as we do more iterations and the values of <code>n</code> passed to <code>isPowerOfThree()</code> grow, we see significant boosts in performance for Approach 4.
<br>
<br></p>
<hr>
<h2 id="conclusion">Conclusion</h2>
<p>Simple optimizations like this might seem negligible, but historically, when computation power was an issue, it allowed certain computer programs (such as Quake 3 <sup id="fnref:note-1"><a class="footnote-ref" href="#fn:note-1" rel="footnote">1</a></sup>) possible.
<br>
<br></p>
<hr>
<h2 id="references">References</h2>
<p>Analysis written by: <a href="http://andrei.cioara.me">@aicioara</a></p>
<div class="footnote">
<hr>
<ol>
<li id="fn:note-1">
<p><a href="https://en.wikipedia.org/wiki/Fast_inverse_square_root">https://en.wikipedia.org/wiki/Fast_inverse_square_root</a> <a class="footnote-backref" href="#fnref:note-1" rev="footnote" title="Jump back to footnote 1 in the text">↩</a></p>
</li>
<li id="fn:note-2">
<p><a href="https://en.wikipedia.org/wiki/Regular_expression">https://en.wikipedia.org/wiki/Regular_expression</a> <a class="footnote-backref" href="#fnref:note-2" rev="footnote" title="Jump back to footnote 2 in the text">↩</a></p>
</li>
<li id="fn:note-3">
<p><a href="http://developer.classpath.org/doc/java/lang/StrictMath-source.html">http://developer.classpath.org/doc/java/lang/StrictMath-source.html</a> <a class="footnote-backref" href="#fnref:note-3" rev="footnote" title="Jump back to footnote 3 in the text">↩</a></p>
</li>
<li id="fn:note-4">
<p><a href="https://www.cut-the-knot.org/recurrence/conversion.shtml">http://www.cut-the-knot.org/recurrence/conversion.shtml</a> <a class="footnote-backref" href="#fnref:note-4" rev="footnote" title="Jump back to footnote 4 in the text">↩</a></p>
</li>
</ol>
</div>
          </div>
        
      </div>