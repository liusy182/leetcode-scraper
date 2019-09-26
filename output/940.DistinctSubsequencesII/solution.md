<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Even though the final code for this problem is very short, it is not very intuitive to find the answer.  In the solution below, we'll focus on finding all subsequences (including empty ones), and subtract the empty subsequence at the end.</p>
<p>Let's try for a dynamic programming solution.  In order to not repeat work, our goal is to phrase the current problem in terms of the answer to previous problems.  A typical idea will be to try to count the number of states <code>dp[k]</code> (distinct subsequences) that use letters <code>S[0], S[1], ..., S[k]</code>.</p>
<p>Naively, for say, <code>S = "abcx"</code>, we have <code>dp[k] = dp[k-1] * 2</code>.  This is because for <code>dp[2]</code> which counts <code>("", "a", "b", "c", "ab", "ac", "bc", "abc")</code>, <code>dp[3]</code> counts all of those, plus all of those with the <code>x</code> ending, like <code>("x", "ax", "bx", "cx", "abx", "acx", "bcx", "abcx")</code>.</p>
<p>However, for something like <code>S = "abab"</code>, let's play around with it.  We have:</p>
<ul>
<li><code>dp[0] = 2</code>, as it counts <code>("", "a")</code></li>
<li><code>dp[1] = 4</code>, as it counts <code>("", "a", "b", "ab")</code>;</li>
<li><code>dp[2] = 7</code> as it counts <code>("", "a", "b", "aa", "ab", "ba", "aba")</code>;</li>
<li><code>dp[3] = 12</code>, as it counts <code>("", "a", "b", "aa", "ab", "ba", "bb", "aab", "aba", "abb", "bab", "abab")</code>.</li>
</ul>
<p>We have that dp[3]<code>counts</code>dp[2]<code>, plus</code>("b", "aa", "ab", "ba", "aba")<code>with</code>"b"<code>added to it.  Notice that</code>("", "a")<code>are missing from this list, as they get double counted.  In general, the sequences that resulted from putting</code>"b"<code>the last time (ie.</code>"b", "ab"`) will get double counted.</p>
<p>This insight leads to the recurrence:</p>
<p><code>dp[k] = 2 * dp[k-1] - dp[last[S[k]] - 1]</code></p>
<p>The number of distinct subsequences ending at <code>S[k]</code>, is twice the distinct subsequences counted by <code>dp[k-1]</code> (all of them, plus all of them with S[k] appended), minus the amount we double counted, which is <code>dp[last[S[k]] - 1]</code>.</p>
<iframe src="https://leetcode.com/playground/XejQAwZ4/shared" frameborder="0" width="100%" height="463" name="XejQAwZ4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.  It is possible to adapt this solution to take <script type="math/tex; mode=display">O(1)</script> space.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>