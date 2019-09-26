<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion-with-memoization">Approach 1: Recursion with Memoization</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
<li><a href="#approach-3-constant-space-dynamic-programming">Approach 3: Constant Space Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion-with-memoization">Approach 1: Recursion with Memoization</h4>
<p><strong>Algorithm</strong></p>
<p>In order to find the solution to the given problem, we need to consider every case possible(for the arrangement of the input digits/characters)
 and what value needs to be considered for each case. Let's look at each of the possibilites one by one.</p>
<p>Firstly, let's assume, we have a function <code>ways(s,i)</code> which returns the number of ways to decode the input string <script type="math/tex; mode=display">s</script>, if only the characters upto the 
<script type="math/tex; mode=display">i^{th}</script> index in this string are considered. We start off by calling the function <code>ways(s, s.length()-1)</code> i.e. by considering the full length of this string <script type="math/tex; mode=display">s</script>.</p>
<p>We started by using the last index of the string <script type="math/tex; mode=display">s</script>. Suppose, currently, we called the function as <code>ways(s,i)</code>. Let's look at how we proceed. At every step, we need 
to look at the current character at the last index (<script type="math/tex; mode=display">i</script>) and we need to determine the number of ways of decoding that using this <script type="math/tex; mode=display">i^{th}</script> character could 
add to the total value. There are the following possiblities for the <script type="math/tex; mode=display">i^{th}</script> character.</p>
<p>The <script type="math/tex; mode=display">i^{th}</script> character could be  a <code>*</code>. In this case, firstly, we can see that this <code>*</code> could be decoded into any of the digits from <code>1-9</code>. Thus, for every decoding possible 
upto the index <script type="math/tex; mode=display">i-1</script>, this <code>*</code> could be replaced by any of these digits(<code>1-9</code>). Thus, the total number of decodings is 9 times the number of decodings possible 
for the same string upto the index <script type="math/tex; mode=display">i-1</script>. Thus, this <code>*</code> initially adds a factor of <code>9*ways(s,i-1)</code> to the total value. </p>
<p align="center"><img alt="Decode_Ways" src="../Figures/639/639_Decode_Ways2.png"></p>
<p>Apart from this, this <code>*</code> at the <script type="math/tex; mode=display">i^{th}</script> index could also contribute further to the total number of ways depending upon the character/digit at its preceding
 index. If the preceding character happens to be a <code>1</code>, by combining this <code>1</code> with the current <code>*</code>, we could obtain any of the digits from <code>11-19</code> which could be decoded
 into any of the characters from <code>K-S</code>. We need to note that these decodings are in addition to the ones already obtained above by considering only a single current 
 <code>*</code>(<code>1-9</code> decoding to <code>A-J</code>). Thus, this <code>1*</code> pair could be replaced by any of the numbers from <code>11-19</code> irrespective of the decodings done for the previous 
 indices(before <script type="math/tex; mode=display">i-1</script>). Thus, this <code>1*</code> pair leads to 8 times the number of decodings possible with the string <script type="math/tex; mode=display">s</script> upto the index <script type="math/tex; mode=display">i-2</script>. Thus, this adds
 a factor of <code>9 * ways(s, i - 2)</code> to the total number of decodings. </p>
<p>Similarly, a <code>2*</code> pair obtained by a <code>2</code> at the index <script type="math/tex; mode=display">i-1</script> could be considered of the numbers from <code>21-26</code>(decoding into <code>U-Z</code>), adding a total of 6 times the 
 number of decodings possible upto the index <script type="math/tex; mode=display">i-2</script>. </p>
<p align="center"><img alt="Decode_Ways" src="../Figures/639/639_Decode_Ways3.PNG"></p>
<p>On the same basis, if the character at the index <script type="math/tex; mode=display">i-1</script> happens to be another <code>*</code>, this <code>**</code> pairing could be considered as 
 any of the numbers from <code>11-19</code>(9) and <code>21-26</code>(6). Thus, the total number of decodings will be 15(9+6) times  the number of decodings possible upto the index <script type="math/tex; mode=display">i-2</script>.</p>
<p>Now, if the <script type="math/tex; mode=display">i^{th}</script> character could be a digit from <code>1-9</code> as well. In this case, the number of decodings that considering this single digit can 
 contribute to the total number is equal to the number of decodings that can be contributed by the digits upto the index <script type="math/tex; mode=display">i-1</script>. But, if the <script type="math/tex; mode=display">i^{th}</script> character is<br>
 a <code>0</code>, this <code>0</code> alone can't contribute anything to the total number of decodings(but it can only contribute if the digit preceding it is a <code>1</code> or <code>2</code>. We'll consider this case below).</p>
<p>Apart from the value obtained(just above) for the digit at the <script type="math/tex; mode=display">i^{th}</script> index being anyone from <code>0-9</code>, this digit could also pair with the digit at the 
 preceding index, contributing a value dependent on the previous digit. If the previous digit happens to be a <code>1</code>, this <code>1</code> can combine with any of the current 
digits forming a valid number in the range <code>10-19</code>. Thus, in this case, we can consider a pair formed by the current and the preceding digit, and, the number of 
decodings possible by considering the decoded character to be a one formed using this pair, is equal to the total number of decodings possible by using the digits 
upto the index <script type="math/tex; mode=display">i-2</script> only. </p>
<p>But, if the previous digit is a <code>2</code>, a valid number for decoding could only be a one from the range <code>20-26</code>. Thus, if the current digit is lesser than 7, again
this pairing could add decodings with count equal to the ones possible by using the digits upto the <script type="math/tex; mode=display">(i-2)^{th}</script> index only.</p>
<p>Further, if the previous digit happens to be a <code>*</code>, the additional number of decodings depend on the current digit again i.e. If the current digit is greater than 
<code>6</code>, this <code>*</code> could lead to pairings only in the range <code>17-19</code>(<code>*</code> can't be replaced by <code>2</code> leading to <code>27-29</code>). Thus, additional decodings with count equal to the
decodings possible upto the index <script type="math/tex; mode=display">i-2</script>. </p>
<p>On the other hand, if the current digit is lesser than 7, this <code>*</code> could be replaced by either a <code>1</code> or a <code>2</code> leading to the 
decodings <code>10-16</code> and <code>20-26</code> respectively. Thus, the total number of decodings possible by considering this pair is equal to twice the number of decodings possible upto the 
index <script type="math/tex; mode=display">i-2</script>(since <code>*</code> can now be replaced by two values).</p>
<p>This way, by considering every possible case, we can obtain the required number of decodings by making use of the recursive function <code>ways</code> as and where necessary.</p>
<p>By making use of memoization, we can reduce the time complexity owing to duplicate function calls.</p>
<iframe src="https://leetcode.com/playground/ris2YoV8/shared" frameborder="0" width="100%" height="500" name="ris2YoV8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Size of recursion tree can go upto <script type="math/tex; mode=display">n</script>, since <script type="math/tex; mode=display">memo</script> array is filled exactly once. Here, <script type="math/tex; mode=display">n</script> refers to the length of the input 
string.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of recursion tree can go upto <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>From the solutions discussed above, we can observe that the number of decodings possible upto any index, <script type="math/tex; mode=display">i</script>, is dependent only on the characters upto the 
index <script type="math/tex; mode=display">i</script> and not on any of the characters following it. This leads us to the idea that this problem can be solved by making use of Dynamic Programming.</p>
<p>We can also easily observe from the recursive solution that, the number of decodings possible upto the index <script type="math/tex; mode=display">i</script> can be determined easily if we know 
the number of decodings possible upto the index <script type="math/tex; mode=display">i-1</script> and <script type="math/tex; mode=display">i-2</script>. Thus, we fill in the <script type="math/tex; mode=display">dp</script> array in a forward manner. <script type="math/tex; mode=display">dp[i]</script> is used to store the 
number of decodings possible by considering the characters in the given string <script type="math/tex; mode=display">s</script> upto the <script type="math/tex; mode=display">(i-1)^{th}</script> index only(including it).</p>
<p>The equations for filling this <script type="math/tex; mode=display">dp</script> at any step again depend on the current character and the just preceding character. These equations are similar 
to the ones used in the recursive solution.</p>
<p>The following animation illustrates the process of filling the <script type="math/tex; mode=display">dp</script> for a simple example.</p>
<p>!?!../Documents/639_Decode_Ways_II.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/XQA3ciCB/shared" frameborder="0" width="100%" height="500" name="XQA3ciCB"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n+1</script> is filled once only. Here, <script type="math/tex; mode=display">n</script> refers to the length of the input string.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n+1</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-constant-space-dynamic-programming">Approach 3: Constant Space Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we can observe that only the last two values <script type="math/tex; mode=display">dp[i-2]</script> and <script type="math/tex; mode=display">dp[i-1]</script> are used to fill the entry at <script type="math/tex; mode=display">dp[i-1]</script>. We can save some 
space in the last approach, if instead of maintaining a whole <script type="math/tex; mode=display">dp</script> array of length <script type="math/tex; mode=display">n</script>, we keep a track of only the required last two values. The rest of the 
process remains the same as in the last approach.</p>
<iframe src="https://leetcode.com/playground/Xsv3bxSj/shared" frameborder="0" width="100%" height="500" name="Xsv3bxSj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single loop upto <script type="math/tex; mode=display">n</script> is required to find the required result. Here, <script type="math/tex; mode=display">n</script> refers to the length of the input string <script type="math/tex; mode=display">s</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>