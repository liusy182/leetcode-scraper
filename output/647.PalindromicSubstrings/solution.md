<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-expand-around-center-accepted">Approach #1: Expand Around Center [Accepted]</a></li>
<li><a href="#approach-2-manachers-algorithm-accepted">Approach #2: Manacher's Algorithm [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-expand-around-center-accepted">Approach #1: Expand Around Center [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>N</code> be the length of the string.  The middle of the palindrome could be in one of <code>2N - 1</code> positions: either at letter or between two letters.</p>
<p>For each center, let's count all the palindromes that have this center.  Notice that if <code>[a, b]</code> is a palindromic interval (meaning <code>S[a], S[a+1], ..., S[b]</code> is a palindrome), then <code>[a+1, b-1]</code> is one too.</p>
<p><strong>Algorithm</strong></p>
<p>For each possible palindrome center, let's expand our candidate palindrome on the interval <code>[left, right]</code> as long as we can.  The condition for expanding is <code>left &gt;= 0 and right &lt; N and S[left] == S[right]</code>.  That means we want to count a new palindrome <code>S[left], S[left+1], ..., S[right]</code>.</p>
<iframe src="https://leetcode.com/playground/BoR2UhKv/shared" frameborder="0" width="100%" height="310" name="BoR2UhKv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.  Each expansion might do <script type="math/tex; mode=display">O(N)</script> work.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-manachers-algorithm-accepted">Approach #2: Manacher's Algorithm [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Manacher's algorithm is a textbook algorithm that finds in linear time, the maximum size palindrome for any possible palindrome center.  If we had such an algorithm, finding the answer is straightforward.</p>
<p>What follows is a discussion of why this algorithm works.</p>
<p><strong>Algorithm</strong></p>
<p>Our loop invariants will be that <code>center, right</code> is our knowledge of the palindrome with the largest right-most boundary with <code>center &lt; i</code>, centered at <code>center</code> with right-boundary <code>right</code>.  Also, <code>i &gt; center</code>, and we've already computed all <code>Z[j]</code>'s for <code>j &lt; i</code>.</p>
<p>When <code>i &lt; right</code>, we reflect <code>i</code> about <code>center</code> to be at some coordinate <code>j = 2 * center - i</code>.  Then, limited to the interval with radius <code>right - i</code> and center <code>i</code>, the situation for <code>Z[i]</code> is the same as for <code>Z[j]</code>.</p>
<p>For example, if at some time <code>center = 7, right = 13, i = 10</code>, then for a string like <code>A = '@#A#B#A#A#B#A#＄'</code>, the <code>center</code> is at the <code>'#'</code> between the two middle <code>'A'</code>'s, the right boundary is at the last <code>'#'</code>, <code>i</code> is at the last <code>'B'</code>, and <code>j</code> is at the first <code>'B'</code>.</p>
<p>Notice that limited to the interval <code>[center - (right - center), right]</code> (the interval with center <code>center</code> and right-boundary <code>right</code>), the situation for <code>i</code> and <code>j</code> is a reflection of something we have already computed.  Since we already know <code>Z[j] = 3</code>, we can quickly find <code>Z[i] = min(right - i, Z[j]) = 3</code>.</p>
<p>Now, why is this algorithm linear?  The while loop only checks the condition more than once when <code>Z[i] = right - i</code>.  In that case, for each time <code>Z[i] += 1</code>, it increments <code>right</code>, and <code>right</code> can only be incremented up to <code>2*N+2</code> times.</p>
<p>Finally, we sum up <code>(v+1) / 2</code> for each <code>v in Z</code>.  Say the longest palindrome with some given center C has radius R.  Then, the substring with center C and radius R-1, R-2, R-3, ..., 0 are also palindromes.  Example:  <code>abcdedcba</code> is a palindrome with center <code>e</code>, radius 4:  but <code>e</code>, <code>ded</code>, <code>cdedc</code>, <code>bcdedcb</code>, and <code>abcdedcba</code> are all palindromes.</p>
<p>We are dividing by 2 because we were using half-lengths instead of lengths.  For example we actually had the palindrome <code>a#b#c#d#e#d#c#b#a</code>, so our length is twice as big.</p>
<iframe src="https://leetcode.com/playground/dMCfKFBQ/shared" frameborder="0" width="100%" height="500" name="dMCfKFBQ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.  As discussed above, the complexity is linear.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>A</code> and <code>Z</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>