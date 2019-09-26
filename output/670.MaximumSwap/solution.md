<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
<li><a href="#approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The number only has at most 8 digits, so there are only <script type="math/tex; mode=display">{}^{8}\text{C}_{2}</script> = 28 available swaps.  We can easily brute force them all.</p>
<p><strong>Algorithm</strong></p>
<p>We will store the candidates as lists of length <script type="math/tex; mode=display">\text{len(num)}</script>.  For each candidate swap with positions <script type="math/tex; mode=display">\text{(i, j)}</script>, we swap the number and record if the candidate is larger than the current answer, then swap back to restore the original number.</p>
<p>The only detail is possibly to check that we didn't introduce a leading zero.  We don't actually need to check it, because our original number doesn't have one.</p>
<iframe src="https://leetcode.com/playground/9BbnzEUC/shared" frameborder="0" name="9BbnzEUC" width="100%" height="462"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the total number of digits in the input number.  For each pair of digits, we spend up to <script type="math/tex; mode=display">O(N)</script> time to compare the final sequences.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the information stored in <script type="math/tex; mode=display">\text{A}</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>At each digit of the input number in order, if there is a larger digit that occurs later, we know that the best swap must occur with the digit we are currently considering.</p>
<p><strong>Algorithm</strong></p>
<p>We will compute <script type="math/tex; mode=display">\text{last[d] = i}</script>, the index <script type="math/tex; mode=display">\text{i}</script> of the last occurrence of digit <script type="math/tex; mode=display">\text{d}</script> (if it exists).</p>
<p>Afterwards, when scanning the number from left to right, if there is a larger digit in the future, we will swap it with the largest such digit; if there are multiple such digits, we will swap it with the one that occurs the latest.</p>
<iframe src="https://leetcode.com/playground/c2u3L78L/shared" frameborder="0" name="c2u3L78L" width="100%" height="411"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the total number of digits in the input number.  Every digit is considered at most once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.  The additional space used by <script type="math/tex; mode=display">\text{last}</script> only has up to 10 values.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>