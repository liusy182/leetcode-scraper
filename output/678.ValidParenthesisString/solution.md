<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-3-greedy-accepted">Approach #3: Greedy [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each asterisk, let's try both possibilities.</p>
<iframe src="https://leetcode.com/playground/HHVFGh2C/shared" frameborder="0" name="HHVFGh2C" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N * 3^{N})</script>, where <script type="math/tex; mode=display">N</script> is the length of the string.  For each asterisk we try 3 different values.  Thus, we could be checking the validity of up to <script type="math/tex; mode=display">3^N</script> strings.  Then, each check of validity is <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by our character array.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-accepted">Approach #2: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <code>dp[i][j]</code> be <code>true</code> if and only if the interval <code>s[i], s[i+1], ..., s[j]</code> can be made valid.  Then <code>dp[i][j]</code> is true only if:</p>
<ul>
<li>
<p><code>s[i]</code> is <code>'*'</code>, and the interval <code>s[i+1], s[i+2], ..., s[j]</code> can be made valid;</p>
</li>
<li>
<p>or, <code>s[i]</code> can be made to be <code>'('</code>, and there is some <code>k</code> in <code>[i+1, j]</code> such that <code>s[k]</code> can be made to be <code>')'</code>, plus the two intervals cut by <code>s[k]</code> (<code>s[i+1: k]</code> and <code>s[k+1: j+1]</code>) can be made valid;</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/c2qhBzko/shared" frameborder="0" name="c2qhBzko" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the length of the string.  There are <script type="math/tex; mode=display">O(N^2)</script> states corresponding to entries of <code>dp</code>, and we do an average of <script type="math/tex; mode=display">O(N)</script> work on each state.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, the space used to store intermediate results in <code>dp</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-greedy-accepted">Approach #3: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>When checking whether the string is valid, we only cared about the "<code>balance</code>": the number of extra, open left brackets as we parsed through the string.  For example, when checking whether '(()())' is valid, we had a balance of <code>1, 2, 1, 2, 1, 0</code> as we parse through the string: <code>'('</code> has 1 left bracket, <code>'(('</code> has 2, <code>'(()'</code> has 1, and so on.  This means that after parsing the first <code>i</code> symbols, (which may include asterisks,) we only need to keep track of what the <code>balance</code> could be.</p>
<p>For example, if we have string <code>'(***)'</code>, then as we parse each symbol, the set of possible values for the <code>balance</code> is <code>[1]</code> for <code>'('</code>; <code>[0, 1, 2]</code> for <code>'(*'</code>; <code>[0, 1, 2, 3]</code> for <code>'(**'</code>; <code>[0, 1, 2, 3, 4]</code> for <code>'(***'</code>, and <code>[0, 1, 2, 3]</code> for <code>'(***)'</code>.</p>
<p>Furthermore, we can prove these states always form a contiguous interval.  Thus, we only need to know the left and right bounds of this interval.  That is, we would keep those intermediate states described above as <code>[lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4], [0, 3]</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>lo, hi</code> respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.</p>
<p>If we encounter a left bracket (<code>c == '('</code>), then <code>lo++</code>, otherwise we could write a right bracket, so <code>lo--</code>.  If we encounter what can be a left bracket (<code>c != ')'</code>), then <code>hi++</code>, otherwise we must write a right bracket, so <code>hi--</code>.  If <code>hi &lt; 0</code>, then the current prefix can't be made valid no matter what our choices are.  Also, we can never have less than <code>0</code> open left brackets.  At the end, we should check that we can have exactly 0 open left brackets.</p>
<iframe src="https://leetcode.com/playground/AP7MmhXJ/shared" frameborder="0" name="AP7MmhXJ" width="100%" height="258"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of the string.  We iterate through the string once.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>, the space used by our <code>lo</code> and <code>hi</code> pointers.  However, creating a new character array will take <script type="math/tex; mode=display">O(N)</script> space.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>