<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>A palindrome consists of letters with equal partners, plus possibly a unique center (without a partner).  The letter <code>i</code> from the left has its partner <code>i</code> from the right.  For example in <code>'abcba'</code>, <code>'aa'</code> and <code>'bb'</code> are partners, and <code>'c'</code> is a unique center.</p>
<p>Imagine we built our palindrome.  It consists of as many partnered letters as possible, plus a unique center if possible.  This motivates a greedy approach.</p>
<p><strong>Algorithm</strong></p>
<p>For each letter, say it occurs <code>v</code> times.  We know we have <code>v // 2 * 2</code> letters that can be partnered for sure.  For example, if we have <code>'aaaaa'</code>, then we could have <code>'aaaa'</code> partnered, which is <code>5 // 2 * 2 = 4</code> letters partnered.</p>
<p>At the end, if there was any <code>v % 2 == 1</code>, then that letter could have been a unique center.  Otherwise, every letter was partnered.  To perform this check, we will check for <code>v % 2 == 1</code> and <code>ans % 2 == 0</code>, the latter meaning we haven't yet added a unique center to the answer.</p>
<iframe src="https://leetcode.com/playground/ZnPVAdHR/shared" frameborder="0" width="100%" height="310" name="ZnPVAdHR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>s</code>.  We need to count each letter.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space for our count, as the alphabet size of <code>s</code> is fixed.  We should also consider that in a bit complexity model, technically we need <script type="math/tex; mode=display">O(\log N)</script> bits to store the count values.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>