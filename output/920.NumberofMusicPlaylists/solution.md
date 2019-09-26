<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
<li><a href="#approach-2-partitions-dynamic-programming">Approach 2: Partitions + Dynamic Programming</a></li>
<li><a href="#approach-3-generating-functions">Approach 3: Generating Functions</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>dp[i][j]</code> be the number of playlists of length <code>i</code> that have exactly <code>j</code> unique songs.  We want <code>dp[L][N]</code>, and it seems likely we can develop a recurrence for <code>dp</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Consider <code>dp[i][j]</code>.  Last song, we either played a song for the first time or we didn't.  If we did, then we had <code>dp[i-1][j-1] * (N-j)</code> ways to choose it.  If we didn't, then we repeated a previous song in <code>dp[i-1][j] * max(j-K, 0)</code> ways (<code>j</code> of them, except the last <code>K</code> ones played are banned.)</p>
<iframe src="https://leetcode.com/playground/9tJ8LAAB/shared" frameborder="0" width="100%" height="327" name="9tJ8LAAB"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NL)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(NL)</script>.  (However, we can adapt this algorithm to only store the last row of <code>dp</code> to easily get <script type="math/tex; mode=display">O(L)</script> space complexity.)
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-partitions-dynamic-programming">Approach 2: Partitions + Dynamic Programming</h4>
<p>(<em>Note: This solution is extremely challenging, but is a natural consequence of trying to enumerate the playlists in this manner.</em>)</p>
<p><strong>Intuition</strong></p>
<p>Since we are interested in playing every song at least once, let's keep track of what times <script type="math/tex; mode=display">x = (x_1, x_2, \cdots)</script> a song was played that wasn't yet played before.  For example, if we have 5 songs <code>abcde</code>, and we play <code>abacabdcbaeacbd</code>, then <script type="math/tex; mode=display">x = (1, 2, 4, 7, 11)</script> as these are the first occurrences of a unique song.  For convenience, we'll also put <script type="math/tex; mode=display">x_{N+1} = L+1</script>.  Our strategy is to count the number of playlists <script type="math/tex; mode=display">\#_x</script> that satisfy this <script type="math/tex; mode=display">x</script>, so that our final answer will be <script type="math/tex; mode=display">\sum \#_x</script>.  </p>
<p>Doing a direct count,</p>
<p>
<script type="math/tex; mode=display">
\#_x = N * (N-1) * \cdots * (N-K+1) 1^{x_{K+1} - x_K - 1} * (N-K+2)  2^{x_{K+2} - x_{K+1}} * \cdots
</script>
</p>
<p>
<script type="math/tex; mode=display">
\Rightarrow \#_x = N! \prod_{j=1}^{N-K+1} j^{x_{K+j} - x_{K+j-1} - 1}
</script>
</p>
<p>Now, let <script type="math/tex; mode=display">\delta_i = x_{K+i} - x_{K+i-1} - 1</script>, so that <script type="math/tex; mode=display">\sum \delta_i = L-N</script>.  To recap, the final answer will be (for <script type="math/tex; mode=display">S = L-N, P = N-K+1</script>):</p>
<p>
<script type="math/tex; mode=display">
N! \Big(\sum\limits_{\delta : \sum\limits_{0 \leq i \leq P} \delta_i = S} \prod\limits_{j=1}^P j^{\delta_j} \Big)
</script>
</p>
<p>For convenience, let's denote the stuff in the large brackets as <script type="math/tex; mode=display">\langle S, P\rangle</script>.</p>
<p><strong>Algorithm</strong></p>
<p>We can develop a recurrence for <script type="math/tex; mode=display">\langle S, P\rangle</script> mathematically, by factoring out the <script type="math/tex; mode=display">P^{\delta_P}</script> term.</p>
<p>
<script type="math/tex; mode=display">
\langle S, P\rangle = \sum_{\delta_P = 0}^S P^{\delta_P} \sum_{\sum\limits_{0\leq i < P} \delta_i = S - \delta_P} \prod\limits_{j=1}^{P-1} j^{\delta_j}
</script>
</p>
<p>
<script type="math/tex; mode=display">
\Rightarrow \langle S, P\rangle = \sum_{\delta_P = 0}^S P^{\delta_P} \langle S - \delta_P, P-1\rangle
</script>
</p>
<p>so that it can be shown through algebraic manipulation that:
<script type="math/tex; mode=display">
\langle S, P \rangle = P \langle S-1, P-1 \rangle + \langle S, P-1 \rangle
</script>
</p>
<p>With this recurrence, we can perform dynamic programming similar to Approach 1.  The final answer is <script type="math/tex; mode=display">N! \langle L-N, N-K+1 \rangle</script>.</p>
<iframe src="https://leetcode.com/playground/KdGurUUX/shared" frameborder="0" width="100%" height="395" name="KdGurUUX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NL)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(L)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-generating-functions">Approach 3: Generating Functions</h4>
<p>(<em>Note: This solution is extremely challenging and not recommended for interviews, but is included here for completeness.</em>)</p>
<p><strong>Analysis</strong></p>
<p>Following the terminology of Approach 2, we would like to compute <script type="math/tex; mode=display">\langle S, P \rangle</script> quickly.  We can use generating functions.</p>
<p>For a fixed <script type="math/tex; mode=display">P</script>, consider the function:</p>
<p>
<script type="math/tex; mode=display">
f(x) = (1^0x^0 + 1^1x^1 + 1^2x^2 + 1^3x^3 + \cdots) * (2^0x^0 + 2^1x^1 + 2^2x^2 + 2^3x^3 + \cdots)
</script>
<script type="math/tex; mode=display">
\cdots * (P^0x^0 + P^1x^1 + P^2x^2 + P^3x^3 + \cdots)
</script>
</p>
<p>
<script type="math/tex; mode=display">
\Leftrightarrow f(x) = \prod_{k=1}^{P} (\sum_{j \geq 0} k^j x^j) = \prod_{k=1}^P \frac{1}{1-kx}
</script>
</p>
<p>The coefficient of <script type="math/tex; mode=display">x^S</script> in <script type="math/tex; mode=display">f</script> (denoted <script type="math/tex; mode=display">[x^S]f</script>) is the desired <script type="math/tex; mode=display">\langle S, P \rangle</script>.</p>
<p>By the Chinese Remainder theorem on polynomials, this product can be written as a partial fraction decomposition:</p>
<p>
<script type="math/tex; mode=display">
\prod_{k=1}^P \frac{1}{1-kx} = \sum_{k=1}^P \frac{A_k}{1-kx}
</script>
</p>
<p>for some rational coefficients <script type="math/tex; mode=display">A_k</script>.  We can solve for these coefficients by clearing denominators and setting <script type="math/tex; mode=display">x = 1/m</script> for <script type="math/tex; mode=display">1 \leq m \leq P</script>.  Then for a given <script type="math/tex; mode=display">m</script>, all the terms except the <script type="math/tex; mode=display">m</script>-th vanish, and:</p>
<p>
<script type="math/tex; mode=display">
A_m = \frac{1}{\prod\limits_{\substack{1 \leq j \leq P\\j \neq m}} 1 - j/m} = \prod_{j \neq m} \frac{m}{m-j}
</script>
</p>
<p>Since a geometric series has sum <script type="math/tex; mode=display">\sum_{j \geq 0} (kx)^j = \frac{1}{1-kx}</script>, altogether it implies:</p>
<p>
<script type="math/tex; mode=display">
[x^S]f = \sum_{k=1}^P A_k * k^S
</script>
</p>
<p>so that the final answer is</p>
<p>
<script type="math/tex; mode=display">
\text{answer} = N! \sum_{k=1}^{N-K} k^{L-N} \prod_{\substack{1 \leq j \leq N-K\\j \neq k}} \frac{k}{k-j}
</script>
</p>
<p>
<script type="math/tex; mode=display">
\Rightarrow \text{answer} = N! \sum_k k^{L-K-1} \prod_{j \neq k} \frac{1}{k-j}
</script>
</p>
<p>We only need a quick way to compute <script type="math/tex; mode=display">C_k = \prod\limits_{j \neq k} \frac{1}{k-j}</script>.  Indeed,</p>
<p>
<script type="math/tex; mode=display">
C_{k+1} = C_k * \frac{k - (N-K)}{k}
</script>
</p>
<p>so that we now have everything we need to compute the answer quickly.</p>
<iframe src="https://leetcode.com/playground/ypP5xqYU/shared" frameborder="0" width="100%" height="395" name="ypP5xqYU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log L)</script>.</p>
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