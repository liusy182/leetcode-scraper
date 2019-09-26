<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</a></li>
<li><a href="#approach-2-truncate-after-cliff-accepted">Approach #2: Truncate After Cliff [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's construct the answer digit by digit.</p>
<p>If the current answer is say, <code>123</code>, and the next digit is <code>5</code>, then the answer must be at least <code>123555...5</code>, since the digits in the answer must be monotonically increasing.  If this is larger than <code>N</code>, then it's impossible.</p>
<p><strong>Algorithm</strong></p>
<p>For each digit of <code>N</code>, let's build the next digit of our answer <code>ans</code>.  We'll find the smallest possible digit <code>d</code> such that <code>ans + (d repeating) &gt; N</code> when comparing by string; that means <code>d-1</code> must have satisfied <code>ans + (d-1 repeating) &lt;= N</code>, and so we'll add <code>d-1</code> to our answer.  If we don't find such a digit, we can add a <code>9</code> instead.</p>
<iframe src="https://leetcode.com/playground/FBLCwPuk/shared" frameborder="0" width="100%" height="429" name="FBLCwPuk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(D^2)</script>, where <script type="math/tex; mode=display">D \approx \log N</script> is the number of digits in <script type="math/tex; mode=display">N</script>.  We do <script type="math/tex; mode=display">O(D)</script> work building and comparing each candidate, and we do this <script type="math/tex; mode=display">O(D)</script> times.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(D)</script>, the size of the answer and the temporary string we are comparing.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-truncate-after-cliff-accepted">Approach #2: Truncate After Cliff [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>One initial thought that comes to mind is we can always have a candidate answer of <code>d999...9</code> (a digit <code>0 &lt;= d &lt;= 9</code> followed by some number of nines.)  For example if <code>N = 432543654</code>, we could always have an answer of at least <code>399999999</code>.</p>
<p>We can do better.  For example, when the number is <code>123454321</code>, we could have a candidate of <code>123449999</code>.  It seems like a decent strategy is to take a monotone increasing prefix of <code>N</code>, then decrease the number before the "cliff" (the index where adjacent digits decrease for the first time) if it exists, and replace the rest of the characters with <code>9</code>s.</p>
<p>When does that strategy fail?  If <code>N = 333222</code>, then our strategy would give us the candidate answer of <code>332999</code> - but this isn't monotone increasing.  However, since we are looking at all indexes before the original first occurrence of a cliff, the only place where a cliff could exist, is next to where we just decremented a digit.</p>
<p>Thus, we can repair our strategy, by successfully morphing our answer <code>332999 -&gt; 329999 -&gt; 299999</code> with a linear scan.</p>
<p><strong>Algorithm</strong></p>
<p>We'll find the first cliff <code>S[i-1] &gt; S[i]</code>.  Then, while the cliff exists, we'll decrement the appropriate digit and move <code>i</code> back.  Finally, we'll make the rest of the digits <code>9</code>s and return our work.</p>
<p>We can prove our algorithm is correct because every time we encounter a cliff, the digit we decrement has to decrease by at least 1.  Then, the largest possible selection for the rest of the digits is all nines, which is always going to be monotone increasing with respect to the other digits occurring earlier in the number.</p>
<iframe src="https://leetcode.com/playground/yeDAMaRm/shared" frameborder="0" width="100%" height="242" name="yeDAMaRm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(D)</script>, where <script type="math/tex; mode=display">D \approx \log N</script> is the number of digits in <script type="math/tex; mode=display">N</script>.  Each step in the algorithm is a linear scan of the digits.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(D)</script>, the size of the answer.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>