<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-solve-it-mathematically-accepted">Approach #2 Solve it mathematically [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>Do as directed in question.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>:</li>
<li>Convert <script type="math/tex; mode=display">i</script> to string and count <script type="math/tex; mode=display">\text{'1'}</script> in each integer string</li>
<li>Add count of <script type="math/tex; mode=display">\text{'1'}</script> in each string to the sum, say <script type="math/tex; mode=display">countr</script>
</li>
</ul>
<iframe src="https://leetcode.com/playground/VwAzPgne/shared" frameborder="0" name="VwAzPgne" width="100%" height="207"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n*log_{10}(n))</script>.</li>
<li>We iterate from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>
</li>
<li>
<p>In each iteration, we convert integer to string and count '1' in string which takes linear time in number of digits in <script type="math/tex; mode=display">i</script>, which is <script type="math/tex; mode=display">log_{10}(n)</script>.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(log_{10}(n))</script> Extra space for the countr and the converted string <script type="math/tex; mode=display">\text{str}</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-solve-it-mathematically-accepted">Approach #2 Solve it mathematically [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>In Approach #1, we manually calculated the number of all the <script type="math/tex; mode=display">'1'</script>s in the digits, but this is very slow. Hence, we need a way to find a pattern in the way <script type="math/tex; mode=display">'1'</script>s (or for that matter any digit) appears in the numbers. We could then use the pattern to formulate the answer.</p>
<p>Consider the <script type="math/tex; mode=display">1</script>s in <script type="math/tex; mode=display">\text{ones}</script> place , <script type="math/tex; mode=display">\text{tens}</script> place, <script type="math/tex; mode=display">\text{hundreds}</script> place and so on... An analysis
has been performed in the following figure.</p>
<p align="center"><img alt="Number of digit one" src="../Figures/233/number_of_digit_one.png" width="800px"></p>
<p>From the figure, we can see that from digit '1' at <script type="math/tex; mode=display">\text{ones}</script> place repeat in group of 1 after interval of <script type="math/tex; mode=display">10</script>. Similarly, '1' at <script type="math/tex; mode=display">\text{tens}</script> place repeat in group of 10 after interval of <script type="math/tex; mode=display">100</script>.
This can be formulated as <script type="math/tex; mode=display">(n/(i*10))*i</script>.</p>
<p>Also, notice that if the digit at <script type="math/tex; mode=display">\text{tens}</script> place is <script type="math/tex; mode=display">\text{'1'}</script>, then the number of terms with <script type="math/tex; mode=display">\text{'1's}</script>  is increased by <script type="math/tex; mode=display">x+1</script>, if the number is say <script type="math/tex; mode=display">\text{"ab1x"}</script>. As if digits at <script type="math/tex; mode=display">\text{tens}</script> place is greater than <script type="math/tex; mode=display">1</script>, then all the <script type="math/tex; mode=display">10</script> occurances of numbers with <script type="math/tex; mode=display">'1'</script> at <script type="math/tex; mode=display">\text{tens}</script> place have taken place, hence, we add <script type="math/tex; mode=display">10</script>.
This is formluated as <script type="math/tex; mode=display">{\min(\max((\text{n mod (i*10)} )-i+1,0),i)}</script>.</p>
<p>Lets take an example, say <script type="math/tex; mode=display">n= 1234</script>.</p>
<p>No of <script type="math/tex; mode=display">\text{'1'}</script> in <script type="math/tex; mode=display">\text{ones}</script> place = <script type="math/tex; mode=display">1234/10</script>(corresponding to 1,11,21,...1221) + <script type="math/tex; mode=display">\min(4,1)</script>(corresponding to 1231) =<script type="math/tex; mode=display">124</script>
</p>
<p>No of <script type="math/tex; mode=display">\text{'1'}</script> in <script type="math/tex; mode=display">\text{tens}</script> place = <script type="math/tex; mode=display">(1234/100)*10</script>(corresponding to 10,11,12,...,110,111,...1919) +<script type="math/tex; mode=display">\min(21,10)</script>(corresponding to 1210,1211,...1219)=<script type="math/tex; mode=display">130</script>
</p>
<p>No of <script type="math/tex; mode=display">\text{'1'}</script> in <script type="math/tex; mode=display">\text{hundreds}</script> place = <script type="math/tex; mode=display">(1234/1000)*100</script>(corresponding to 100,101,12,...,199) +<script type="math/tex; mode=display">\min(135,100)</script>(corresponding to 1100,1101...1199)=<script type="math/tex; mode=display">200</script>
</p>
<p>No of <script type="math/tex; mode=display">\text{'1'}</script> in <script type="math/tex; mode=display">\text{thousands}</script> place = <script type="math/tex; mode=display">(1234/10000)*10000</script> +<script type="math/tex; mode=display">\min(235,1000)</script>(corresponding to 1000,1001,...1234)=<script type="math/tex; mode=display">235</script>
</p>
<p>Therefore, Total = <script type="math/tex; mode=display">124+130+200+235 = 689</script>.</p>
<p>Herein, one formula has been devised, but many other formulae can be devised for faster implementations, but the essence and complexity remains the same. The users are encouraged to try to divise their own version of solution using the mathematical concepts.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script> incrementing by <script type="math/tex; mode=display">10</script> each time:</li>
<li>Add  <script type="math/tex; mode=display">(n/(i*10))*i</script> to <script type="math/tex; mode=display">\text{countr}</script> representing the repetition of groups of $$i$ sizes after each <script type="math/tex; mode=display">(i*10)</script> interval.</li>
<li>Add <script type="math/tex; mode=display">{\min(\max((\text{n mod (i*10)} )-i+1,0),i)}</script> to <script type="math/tex; mode=display">\text{countr}</script> representing the additional digits dependant on the digit in <script type="math/tex; mode=display">i</script>th place as described in intuition.</li>
</ul>
<iframe src="https://leetcode.com/playground/QVzpgtNB/shared" frameborder="0" name="QVzpgtNB" width="100%" height="207"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(log_{10}(n))</script>.</li>
<li>
<p>No of iterations equal to the number of digits in n which is <script type="math/tex; mode=display">log_{10}(n)</script>
</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script> space required.</p>
</li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/abhinavbansal0">@abhinavbansal0</a>.</p>
          </div>
        
      </div>