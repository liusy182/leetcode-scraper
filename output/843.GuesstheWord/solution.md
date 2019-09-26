<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-minimax-with-heuristic-accepted">Approach #1: Minimax with Heuristic [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-minimax-with-heuristic-accepted">Approach #1: Minimax with Heuristic [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can guess that having less words in the word list is generally better.  If the data is random, we can reason this is often the case.</p>
<p>Now let's use the strategy of making the guess that minimizes the maximum possible size of the resulting word list.  If we started with <script type="math/tex; mode=display">N</script> words in our word list, we can iterate through all possibilities for what the secret could be.</p>
<p><strong>Algorithm</strong></p>
<p>Store <code>H[i][j]</code> as the number of matches of <code>wordlist[i]</code> and <code>wordlist[j]</code>.  For each guess that hasn't been guessed before, do a minimax as described above, taking the guess that gives us the smallest group that might occur.</p>
<iframe src="https://leetcode.com/playground/XyZRWsin/shared" frameborder="0" width="100%" height="500" name="XyZRWsin"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2 \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of words, and assuming their length is <script type="math/tex; mode=display">O(1)</script>.  Each call to <code>solve</code> is <script type="math/tex; mode=display">O(N^2)</script>, and the number of calls is bounded by <script type="math/tex; mode=display">O(\log N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>