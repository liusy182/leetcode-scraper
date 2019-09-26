<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-ad-hoc-accepted">Approach #1: Ad-Hoc [Accepted]</a></li>
<li><a href="#approach-2-rabin-karp-rolling-hash-accepted">Approach #2: Rabin-Karp (Rolling Hash) [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-ad-hoc-accepted">Approach #1: Ad-Hoc [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The question can be summarized as "What is the smallest <code>k</code> for which <code>B</code> is a substring of <code>A * k</code>?"  We can just try every <code>k</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Imagine we wrote <code>S = A+A+A+...</code>.  If <code>B</code> is to be a substring of <code>S</code>, we only need to check whether some <code>S[0:], S[1:], ..., S[len(A) - 1:]</code> starts with <code>B</code>, as <code>S</code> is long enough to contain <code>B</code>, and <code>S</code> has period at most <code>len(A)</code>.</p>
<p>Now, suppose <code>q</code> is the least number for which <code>len(B) &lt;= len(A * q)</code>.  We only need to check whether <code>B</code> is a substring of <code>A * q</code> or <code>A * (q+1)</code>.  If we try <code>k &lt; q</code>, then <code>B</code> has larger length than <code>A * q</code> and therefore can't be a substring.  When <code>k = q+1</code>, <code>A * k</code> is already big enough to try all positions for <code>B</code>; namely, <code>A[i:i+len(B)] == B</code> for <code>i = 0, 1, ..., len(A) - 1</code>.</p>
<iframe src="https://leetcode.com/playground/gTtmgvev/shared" frameborder="0" name="gTtmgvev" width="100%" height="224"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N*(N+M))</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of strings <code>A, B</code>.  We create two strings <code>A * q</code>, <code>A * (q+1)</code> which have length at most <code>O(M+N)</code>.  When checking whether <code>B</code> is a substring of <code>A</code>, this check takes naively the product of their lengths.</p>
</li>
<li>
<p>Space complexity: As justified above, we created strings that used <script type="math/tex; mode=display">O(M+N)</script> space.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-rabin-karp-rolling-hash-accepted">Approach #2: Rabin-Karp (Rolling Hash) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, we've reduced the problem to deciding whether B is a substring of some <code>A * k</code>.  Using the following technique, we can decide whether <code>B</code> is a substring in <script type="math/tex; mode=display">O(len(A) * k)</script> time.</p>
<p><strong>Algorithm</strong></p>
<p>For strings <script type="math/tex; mode=display">S</script>, consider each <script type="math/tex; mode=display">S[i]</script> as some integer ASCII code.  Then for some prime <script type="math/tex; mode=display">p</script>, consider the following function modulo some prime modulus <script type="math/tex; mode=display">\mathcal{M}</script>:</p>
<p>
<script type="math/tex; mode=display">\text{hash}(S) = \sum_{0 \leq i < len(S)} p^i * S[i]</script>
</p>
<p>Notably, <script type="math/tex; mode=display">\text{hash}(S[1:] + x) = \frac{(\text{hash}(S) - S[0])}{p} + p^{n-1} x</script>.  This shows we can get the hash of every substring of <code>A * q</code> in time complexity linear to it's size.  (We will also use the fact that <script type="math/tex; mode=display">p^{-1} = p^{\mathcal{M}-2} \mod \mathcal{M}</script>.)</p>
<p>However, hashes may collide haphazardly.  To be absolutely sure in theory, we should check the answer in the usual way.  The expected number of checks we make is in the order of <script type="math/tex; mode=display">1 + \frac{s}{\mathcal{M}}</script> where <script type="math/tex; mode=display">s</script> is the number of substrings we computed hashes for (assuming the hashes are equally distributed), which is effectively 1.</p>
<iframe src="https://leetcode.com/playground/DKSFgXSr/shared" frameborder="0" name="DKSFgXSr" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M+N)</script> (at these sizes), where <script type="math/tex; mode=display">M, N</script> are the lengths of strings <code>A, B</code>.  As in <em>Approach #1</em>, we justify that <code>A * (q+1)</code> will be of length <script type="math/tex; mode=display">O(M + N)</script>, and computing the rolling hashes was linear work.  We will also do a linear <script type="math/tex; mode=display">O(N)</script> final check of our answer <script type="math/tex; mode=display">1 + O(M) / \mathcal{M}</script> times.  In total, this is <script type="math/tex; mode=display">O(M+N + N(1 + \frac{M}{\mathcal{M}}))</script> work.  Since <script type="math/tex; mode=display">M \leq 10000 < \mathcal{M} = 10^9 + 7</script>, we can consider this to be linear behavior.</p>
</li>
<li>
<p>Space complexity:  <script type="math/tex; mode=display">O(1)</script>.  Only integers were stored with additional memory.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>