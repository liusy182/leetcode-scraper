<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-using-dynamic-programming">Approach 2: Using Dynamic Programming</a></li>
<li><a href="#approach-3-using-stack">Approach 3: Using Stack</a></li>
<li><a href="#approach-4-without-extra-space">Approach 4: Without extra space</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>We need to determine the length of the largest valid substring of parentheses from a given string.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>In this approach, we consider every possible non-empty even length substring from the given string and check whether it's
a valid string of parentheses or not. In order to check the validity, we use the Stack's Method.</p>
<p>Every time we
encounter a <script type="math/tex; mode=display">\text{‘(’}</script>, we push it onto the stack. For every <script type="math/tex; mode=display">\text{‘)’}</script> encountered, we pop a <script type="math/tex; mode=display">\text{‘(’}</script> from the stack. If <script type="math/tex; mode=display">\text{‘(’}</script> isn't
 available on the stack for popping at anytime or if stack contains some elements after processing complete substring, the substring of parentheses is invalid. In this way, we repeat the
 process for every possible substring and we keep on
  storing the length of the longest valid string found so far.</p>
<div class="codehilite"><pre><span></span>Example:
"((())"

(( --&gt; invalid
(( --&gt; invalid
() --&gt; valid, length=2
)) --&gt; invalid
((()--&gt; invalid
(())--&gt; valid, length=4
maxlength=4
</pre></div>


<iframe src="https://leetcode.com/playground/smDecW2X/shared" frameborder="0" width="100%" height="497" name="smDecW2X"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>. Generating every possible substring from a string of length <script type="math/tex; mode=display">n</script> requires <script type="math/tex; mode=display">O(n^2)</script>. Checking validity of a string of length <script type="math/tex; mode=display">n</script> requires <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. A stack of depth <script type="math/tex; mode=display">n</script> will be required for the longest substring.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-dynamic-programming">Approach 2: Using Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>This problem can be solved by using Dynamic Programming. We make use of a <script type="math/tex; mode=display">\text{dp}</script> array where <script type="math/tex; mode=display">i</script>th element of <script type="math/tex; mode=display">\text{dp}</script> represents the length of the longest valid substring ending at <script type="math/tex; mode=display">i</script>th index. We initialize the complete <script type="math/tex; mode=display">\text{dp}</script> array with 0's. Now, it's obvious that the valid substrings must end with <script type="math/tex; mode=display">\text{‘)’}</script>. This further leads to the conclusion that the substrings ending with <script type="math/tex; mode=display">\text{‘(’}</script> will always contain '0' at their corresponding <script type="math/tex; mode=display">\text{dp}</script> indices. Thus, we update the <script type="math/tex; mode=display">\text{dp}</script> array only when <script type="math/tex; mode=display">\text{‘)’}</script> is encountered.</p>
<p>To fill <script type="math/tex; mode=display">\text{dp}</script> array we will check every two consecutive characters of the string and if</p>
<ol>
<li>
<p>
<script type="math/tex; mode=display">\text{s}[i] = \text{‘)’}</script> and <script type="math/tex; mode=display">\text{s}[i - 1] = \text{‘(’}</script>, i.e. string looks like <script type="math/tex; mode=display">``.......()" \Rightarrow</script>
</p>
<p>
<script type="math/tex; mode=display">
\text{dp}[i]=\text{dp}[i-2]+2
</script>
</p>
<p>We do so because the ending "()" portion is a valid substring anyhow and leads to an increment of 2 in the length of the just previous valid substring's length.</p>
</li>
<li>
<p>
<script type="math/tex; mode=display">\text{s}[i] = \text{‘)’}</script> and <script type="math/tex; mode=display">\text{s}[i - 1] = \text{‘)’}</script>, i.e. string looks like <script type="math/tex; mode=display">``.......))" \Rightarrow</script>
</p>
<p>if <script type="math/tex; mode=display">\text{s}[i - \text{dp}[i - 1] - 1] = \text{‘(’}</script> then</p>
<p>
<script type="math/tex; mode=display">
\text{dp}[i]=\text{dp}[i-1]+\text{dp}[i-\text{dp}[i-1]-2]+2
</script>
</p>
</li>
</ol>
<p>The reason behind this is that if the 2nd last <script type="math/tex; mode=display">\text{‘)’}</script> was a part of a valid substring (say <script type="math/tex; mode=display">sub_s</script>), for the last <script type="math/tex; mode=display">\text{‘)’}</script> to be a part of a larger substring, there must be a corresponding starting <script type="math/tex; mode=display">\text{‘(’}</script> which lies before the valid substring of which the 2nd last <script type="math/tex; mode=display">\text{‘)’}</script> is a part (i.e. before <script type="math/tex; mode=display">sub_s</script>). Thus, if the character before <script type="math/tex; mode=display">sub_s</script> happens to be <script type="math/tex; mode=display">\text{‘(’}</script>, we update the <script type="math/tex; mode=display">\text{dp}[i]</script> as an addition of <script type="math/tex; mode=display">2</script> in the length of <script type="math/tex; mode=display">sub_s</script> which is <script type="math/tex; mode=display">\text{dp}[i-1]</script>. To this, we also add the length of the valid substring just before the term "(,sub_s,)" , i.e. <script type="math/tex; mode=display">\text{dp}[i-\text{dp}[i-1]-2]</script>.</p>
<p>For better understanding of this method, see this example:</p>
<!--![Longest_Valid_Parenthesis](../Figures/32_LongestValidParenthesisDP.gif)-->

<p>!?!../Documents/32_Longest_Valid2.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/YGuAh4tp/shared" frameborder="0" width="100%" height="344" name="YGuAh4tp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single traversal of string to fill dp array is done.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. dp array of size <script type="math/tex; mode=display">n</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-stack">Approach 3: Using Stack</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of finding every possible string and checking its validity, we can make use of stack while scanning
the given string to check if the string scanned so far is valid, and also the length of the longest valid string. In order to do so, we start by pushing <script type="math/tex; mode=display">-1</script> onto the stack.</p>
<p>For every <script type="math/tex; mode=display">\text{‘(’}</script> encountered, we push its index onto the stack.</p>
<p>For every <script type="math/tex; mode=display">\text{‘)’}</script> encountered, we pop the topmost element and subtract the current element's index from the top element of the stack, which gives the length of the currently encountered valid string of parentheses. If while popping the element, the stack becomes empty, we push the current element's index onto the stack. In this way, we keep on calculating the lengths of the valid substrings, and return the length of the longest valid string at the end.</p>
<p>See this example for better understanding.</p>
<!--![Longest_Valid_Parenthesis](../Figures/32_LongestValidParenthesisSTACK.gif)-->

<p>!?!../Documents/32_Longest_Valid_stack_new.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/A2oPe4yE/shared" frameborder="0" width="100%" height="412" name="A2oPe4yE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">n</script> is the length of the given string..</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The size of stack can go up to <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-without-extra-space">Approach 4: Without extra space</h4>
<p><strong>Algorithm</strong></p>
<p>In this approach, we make use of two counters <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script>. First, we start traversing the string from the left towards the right and for every <script type="math/tex; mode=display">\text{‘(’}</script> encountered, we increment the <script type="math/tex; mode=display">left</script> counter and for every <script type="math/tex; mode=display">\text{‘)’}</script> encountered, we increment the <script type="math/tex; mode=display">right</script> counter. Whenever <script type="math/tex; mode=display">left</script> becomes equal to <script type="math/tex; mode=display">right</script>, we calculate the length of the current valid string and keep track of maximum length substring found so far. If <script type="math/tex; mode=display">right</script> becomes greater than <script type="math/tex; mode=display">left</script> we reset <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> to <script type="math/tex; mode=display">0</script>.</p>
<p>Next, we start traversing the string from right to left and similar procedure is applied.</p>
<p>Example of this approach:</p>
<!--![Longest_Valid_Parenthesis](../Figures/32_LongestValidParenthesisLR.gif)-->

<p>!?!../Documents/32_Longest_Validlr.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/RsBpRHK7/shared" frameborder="0" width="100%" height="500" name="RsBpRHK7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Two traversals of the string.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Only two extra variables <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> are needed.</p>
</li>
</ul>
          </div>
        
      </div>