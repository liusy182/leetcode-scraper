<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-direct-accepted">Approach #1: Direct [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-direct-accepted">Approach #1: Direct [Accepted]</h4>
<p><strong>Intuition and Approach</strong></p>
<p>For each number from <code>L</code> to <code>R</code>, let's find out how many set bits it has.  If that number is <code>2, 3, 5, 7, 11, 13, 17</code>, or <code>19</code>, then we add one to our count.  We only need primes up to 19 because <script type="math/tex; mode=display">R \leq 10^6 < 2^{20}</script>.</p>
<iframe src="https://leetcode.com/playground/GCVcZ6pE/shared" frameborder="0" width="100%" height="276" name="GCVcZ6pE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(D)</script>, where <script type="math/tex; mode=display">D = R-L</script> is the number of integers considered.  In a bit complexity model, this would be <script type="math/tex; mode=display">O(D\log D)</script> as we have to count the bits in <script type="math/tex; mode=display">O(\log D)</script> time.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>