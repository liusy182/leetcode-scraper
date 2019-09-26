<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each index <code>i</code> in the given string, let's remove that character, then check if the resulting string is a palindrome.  If it is, (or if the original string was a palindrome), then we'll return <code>true</code></p>
<iframe src="https://leetcode.com/playground/F8rXiMNb/shared" frameborder="0" name="F8rXiMNb" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script> where <script type="math/tex; mode=display">N</script> is the length of the string.  We do the following <script type="math/tex; mode=display">N</script> times: create a string of length <script type="math/tex; mode=display">N</script> and iterate over it.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by our candidate answer.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If the beginning and end characters of a string are the same (ie. <code>s[0] == s[s.length - 1]</code>), then whether the inner characters are a palindrome (<code>s[1], s[2], ..., s[s.length - 2]</code>) uniquely determines whether the entire string is a palindrome.</p>
<p><strong>Algorithm</strong></p>
<p>Suppose we want to know whether <code>s[i], s[i+1], ..., s[j]</code> form a palindrome.  If <code>i &gt;= j</code> then we are done.  If <code>s[i] == s[j]</code> then we may take <code>i++; j--</code>.  Otherwise, the palindrome must be either <code>s[i+1], s[i+2],  ..., s[j]</code> or <code>s[i], s[i+1], ..., s[j-1]</code>, and we should check both cases.</p>
<iframe src="https://leetcode.com/playground/46SiEhrv/shared" frameborder="0" name="46SiEhrv" width="100%" height="360"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the length of the string.  Each of two checks of whether some substring is a palindrome is <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script> additional complexity.  Only pointers were stored in memory.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>