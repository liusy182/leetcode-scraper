<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-divide-and-conquer">Approach 1: Divide and Conquer</a></li>
<li><a href="#approach-2-stack">Approach 2: Stack</a></li>
<li><a href="#approach-3-count-cores">Approach 3: Count Cores</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-divide-and-conquer">Approach 1: Divide and Conquer</h4>
<p><strong>Intuition</strong></p>
<p>Split the string into <code>S = A + B</code> where <code>A</code> and <code>B</code> are balanced parentheses strings, and <code>A</code> is the smallest possible non-empty prefix of <code>S</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Call a balanced string <em>primitive</em> if it cannot be partitioned into two non-empty balanced strings.</p>
<p>By keeping track of <code>balance</code> (the number of <code>(</code> parentheses minus the number of <code>)</code> parentheses), we can partition <code>S</code> into primitive substrings <code>S = P_1 + P_2 + ... + P_n</code>.  Then, <code>score(S) = score(P_1) + score(P_2) + ... + score(P_n)</code>, by definition.</p>
<p>For each primitive substring <code>(S[i], S[i+1], ..., S[k])</code>, if the string is length 2, then the score of this string is 1.  Otherwise, it's twice the score of the substring <code>(S[i+1], S[i+2], ..., S[k-1])</code>.</p>
<iframe src="https://leetcode.com/playground/9n8zxSrk/shared" frameborder="0" width="100%" height="446" name="9n8zxSrk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.  An example worst case is <code>(((((((....)))))))</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the size of the implied call stack.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-stack">Approach 2: Stack</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Every position in the string has a <em>depth</em> - some number of matching parentheses surrounding it.  For example, the dot in <code>(()(.()))</code> has depth 2, because of these parentheses: <code>(__(.__))</code></p>
<p>Our goal is to maintain the score at the current depth we are on.  When we see an opening bracket, we increase our depth, and our score at the new depth is 0.  When we see a closing bracket, we add twice the score of the previous deeper part - except when counting <code>()</code>, which has a score of 1.</p>
<p>For example, when counting <code>(()(()))</code>, our stack will look like this:</p>
<ul>
<li><code>[0, 0]</code> after parsing <code>(</code></li>
<li><code>[0, 0, 0]</code> after <code>(</code></li>
<li><code>[0, 1]</code> after <code>)</code></li>
<li><code>[0, 1, 0]</code> after <code>(</code></li>
<li><code>[0, 1, 0, 0]</code> after <code>(</code></li>
<li><code>[0, 1, 1]</code> after <code>)</code></li>
<li><code>[0, 3]</code> after <code>)</code></li>
<li><code>[6]</code> after <code>)</code></li>
</ul>
<iframe src="https://leetcode.com/playground/C2ky8oiW/shared" frameborder="0" width="100%" height="327" name="C2ky8oiW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the size of the stack.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-count-cores">Approach 3: Count Cores</h4>
<p><strong>Intuition</strong></p>
<p>The final sum will be a sum of powers of 2, as every <em>core</em> (a substring <code>()</code>, with score 1) will have it's score multiplied by 2 for each exterior set of parentheses that contains that core.</p>
<p><strong>Algorithm</strong></p>
<p>Keep track of the <code>balance</code> of the string, as defined in <em>Approach #1</em>.  For every <code>)</code> that immediately follows a <code>(</code>, the answer is <code>1 &lt;&lt; balance</code>, as <code>balance</code> is the number of exterior set of parentheses that contains this core.</p>
<iframe src="https://leetcode.com/playground/EUsmNAS5/shared" frameborder="0" width="100%" height="344" name="EUsmNAS5"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
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