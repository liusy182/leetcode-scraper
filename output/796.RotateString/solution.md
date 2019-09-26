<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
<li><a href="#approach-2-simple-check-accepted">Approach #2: Simple Check [Accepted]</a></li>
<li><a href="#approach-3-rolling-hash-accepted">Approach #3: Rolling Hash [Accepted]</a></li>
<li><a href="#approach-4-kmp-knuth-morris-pratt-accepted">Approach #4: KMP (Knuth-Morris-Pratt) [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>For each rotation of <code>A</code>, let's check if it equals <code>B</code>.</p>
<p><strong>Algorithm</strong></p>
<p>More specifically, say we rotate <code>A</code> by <code>s</code>.  Then, instead of <code>A[0], A[1], A[2], ...</code>, we have <code>A[s], A[s+1], A[s+2], ...</code>; and we should check that <code>A[s] == B[0]</code>, <code>A[s+1] == B[1]</code>, <code>A[s+2] == B[2]</code>, etc.</p>
<iframe src="https://leetcode.com/playground/Q9S39BXZ/shared" frameborder="0" width="100%" height="361" name="Q9S39BXZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.  For each rotation <code>s</code>, we check up to <script type="math/tex; mode=display">N</script> elements in <code>A</code> and <code>B</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.  We only use pointers to elements of <code>A</code> and <code>B</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-simple-check-accepted">Approach #2: Simple Check [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>All rotations of <code>A</code> are contained in <code>A+A</code>.  Thus, we can simply check whether <code>B</code> is a substring of <code>A+A</code>.  We also need to check <code>A.length == B.length</code>, otherwise we will fail cases like <code>A = "a", B = "aa"</code>.</p>
<iframe src="https://leetcode.com/playground/ETPY9FAY/shared" frameborder="0" width="100%" height="140" name="ETPY9FAY"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used building <code>A+A</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-rolling-hash-accepted">Approach #3: Rolling Hash [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Our approach comes down to quickly checking whether want to check whether <code>B</code> is a substring of <code>A2 = A+A</code>.  Specifically, (if <code>N = A.length</code>) we should check whether <code>B = A2[0:N], or B = A2[1:N+1], or B = A2[2:N+2]</code> and so on.  To check this, we can use a rolling hash.</p>
<p><strong>Algorithm</strong></p>
<p>For a string <code>S</code>, say <code>hash(S) = (S[0] * P**0 + S[1] * P**1 + S[2] * P**2 + ...) % MOD</code>, where <code>X**Y</code> represents exponentiation, and <code>S[i]</code> is the ASCII character code of the string at that index.</p>
<p>The idea is that <code>hash(S)</code> has output that is approximately uniformly distributed between <code>[0, 1, 2, ..., MOD-1]</code>, and so if <code>hash(S) == hash(T)</code> it is very likely that <code>S == T</code>.</p>
<p>Now say we have a hash <code>hash(A)</code>, and we want the hash of <code>A[1], A[2], ..., A[N-1], A[0]</code>.  We can subtract <code>A[0]</code> from the hash, divide by <code>P</code>, and add <code>A[0] * P**(N-1)</code>.  (Our division is under the finite field <script type="math/tex; mode=display">\mathbb{F}_\text{MOD}</script> - done by multiplying by the modular inverse <code>Pinv = pow(P, MOD-2, MOD)</code>.)</p>
<iframe src="https://leetcode.com/playground/v8qW4q9q/shared" frameborder="0" width="100%" height="500" name="v8qW4q9q"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, to perform the final check <code>A_rotation == B</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-kmp-knuth-morris-pratt-accepted">Approach #4: KMP (Knuth-Morris-Pratt) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As before, we want to find whether <code>B</code> exists in <code>A+A</code>.  The KMP algorithm is a textbook algorithm that does string matching in linear time, which is faster than brute force.</p>
<p><strong>Algorithm</strong></p>
<p>The algorithm is broken up into two steps, building the shifts table (or <em>failure table</em>), and using it to find whether a match exists.</p>
<p>The shift table tells us about the largest prefix of <code>B</code> that ends here.  More specifically, <code>B[:shifts[i+1]] == B[i - shifts[i+1] : i]</code> is the largest possible prefix of <code>B</code> ending before <code>B[i]</code>.</p>
<p>To build the shift table, we use a dynamic programming approach, where all previously calculated values of <code>shifts</code> are correct.  Then, <code>left</code> will be the end of the candidate prefix of <code>B</code>, and <code>right</code> will be the end of the candidate section that should match the prefix <code>B[0], B[1], ..., B[left]</code>.  Call positions <code>(left, right)</code> "matching" if the prefix ending at <code>B[left]</code> matches the same length string ending at <code>B[right]</code>.  The invariant in our loop will be that <code>(left - 1, right - 1)</code> is matching by the end of each for-block.</p>
<p>In a new for-block, if <code>(left, right)</code> is matching (ie. <code>(left - 1, right - 1)</code> is matching from before, plus <code>B[left] == B[right]</code>), then we know the shift (<code>right - left</code>) is the same number as before.  Otherwise, when <code>(left, right)</code> is not matching, we need to find a shorter prefix.</p>
<p>Our strategy is to find a matching of <code>(left2, right)</code> where <code>left2 &lt; left</code>, by finding matchings <code>(left2 - 1, right - 1)</code> plus checking <code>B[left2] == B[right]</code>.  Since <code>(left - 1, right - 1)</code> is a matching, by transitivity we want to find matchings <code>(left2 - 1, left - 1)</code>.  The largest such <code>left2</code> is <code>left2 = left - shifts[left]</code>.  We repeatedly check these <code>left2</code>'s in greedy order from largest to smallest.</p>
<p>To find a match of <code>B</code> in <code>A+A</code> with such a shift table ready, we employ a similar strategy.  We maintain a matching <code>(match_len - 1, i - 1)</code>, where these positions correspond to strings of length <code>match_len</code> that end at <code>B[match_len - 1]</code> and <code>(A+A)[i-1]</code> respectively.</p>
<p>Now when trying to find the largest length matching for <code>(A+A)</code> at position <code>i</code>, it must be at most <code>(match_len - 1) + 1</code>, where the quantity in brackets is the largest length matching to position <code>i-1</code>.</p>
<p>Again, our strategy is to find a matching <code>(match_len2 - 1, i - 1)</code> plus check that <code>B[match_len2] == (A+A)[i]</code>.  Similar to before, if <code>B[match_len] != (A+A)[i]</code>, then because <code>(match_len - 1, i - 1)</code> was a matching, by transitivity <code>(match_len2 - 1, match_len - 1)</code> must be a matching, of which the largest is found by <code>match_len2 = match_len - shifts[match_len]</code>.  We also repeatedly check these <code>match_len</code>'s in order from largest to smallest.</p>
<p>If at any point in this algorithm our match length is <code>N</code>, we've found <code>B</code> in <code>A+A</code> successfully.</p>
<iframe src="https://leetcode.com/playground/PBHA9iPW/shared" frameborder="0" width="100%" height="500" name="PBHA9iPW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, to create the shift table <code>shifts</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>