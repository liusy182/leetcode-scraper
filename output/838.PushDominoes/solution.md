<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-adjacent-symbols-accepted">Approach #1: Adjacent Symbols [Accepted]</a></li>
<li><a href="#approach-2-calculate-force-accepted">Approach #2: Calculate Force [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-adjacent-symbols-accepted">Approach #1: Adjacent Symbols [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Between every group of vertical dominoes (<code>'.'</code>), we have up to two non-vertical dominoes bordering this group.  Since additional dominoes outside this group do not affect the outcome, we can analyze these situations individually: there are 9 of them (as the border could be empty). Actually, if we border the dominoes by <code>'L'</code> and <code>'R'</code>, there are only 4 cases.  We'll write new letters between these symbols depending on each case.</p>
<p><strong>Algorithm</strong></p>
<p>Continuing our explanation, we analyze cases:</p>
<ul>
<li>
<p>If we have say <code>"A....B"</code>, where A = B, then we should write <code>"AAAAAA"</code>.</p>
</li>
<li>
<p>If we have <code>"R....L"</code>, then we will write <code>"RRRLLL"</code>, or <code>"RRR.LLL"</code> if we have an odd number of dots.  If the initial symbols are at positions <code>i</code> and <code>j</code>, we can check our distance <code>k-i</code> and <code>j-k</code> to decide at position <code>k</code> whether to write <code>'L'</code>, <code>'R'</code>, or <code>'.'</code>.</p>
</li>
<li>
<p>(If we have <code>"L....R"</code> we don't do anything.  We can skip this case.)</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/X63wt96u/shared" frameborder="0" width="100%" height="500" name="X63wt96u"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>dominoes</code>.</li>
</ul>
<hr>
<h4 id="approach-2-calculate-force-accepted">Approach #2: Calculate Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can calculate the net force applied on every domino.  The forces we care about are how close a domino is to a leftward <code>'R'</code>, and to a rightward <code>'L'</code>: the closer we are, the stronger the force.</p>
<p><strong>Algorithm</strong></p>
<p>Scanning from left to right, our force decays by 1 every iteration, and resets to <code>N</code> if we meet an <code>'R'</code>, so that <code>force[i]</code> is higher (than <code>force[j]</code>) if and only if <code>dominoes[i]</code> is closer (looking leftward) to <code>'R'</code> (than <code>dominoes[j]</code>).</p>
<p>Similarly, scanning from right to left, we can find the force going rightward (closeness to <code>'L'</code>).</p>
<p>For some domino <code>answer[i]</code>, if the forces are equal, then the answer is <code>'.'</code>.  Otherwise, the answer is implied by whichever force is stronger.</p>
<p><strong>Example</strong></p>
<p>Here is a worked example on the string <code>S = 'R.R...L'</code>:  We find the force going from left to right is <code>[7, 6, 7, 6, 5, 4, 0]</code>.  The force going from right to left is <code>[0, 0, 0, -4, -5, -6, -7]</code>.  Combining them (taking their vector addition), the combined force is <code>[7, 6, 7, 2, 0, -2, -7]</code>, for a final answer of <code>RRRR.LL</code>.</p>
<iframe src="https://leetcode.com/playground/xrAD5knD/shared" frameborder="0" width="100%" height="500" name="xrAD5knD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>