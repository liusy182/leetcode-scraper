<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Because all numbers are positive, if we "take" a number (use it to score points), we might as well take all copies of it, since we've already erased all its neighbors.  We could keep a count of each number so we know how many points taking a number is worth total.</p>
<p>Now let's investigate what happens when we add a new number <code>X</code> (plus copies) that is larger than all previous numbers.  Naively, our answer would be the previous answer, plus the value of <code>X</code> - which can be solved with dynamic programming.  However, this fails if our previous answer had a number taken that was adjacent to <code>X</code>.</p>
<p>Luckily, we can remedy this.  Let's say we knew <code>using</code>, the value of our previous answer, and <code>avoid</code>, the value of our previous answer that doesn't use the previously largest value <code>prev</code>.  Then we could compute new values of <code>using</code> and <code>avoid</code> appropriately.</p>
<p><strong>Algorithm</strong></p>
<p>For each unique value <code>k</code> of <code>nums</code> in increasing order, let's maintain the correct values of <code>avoid</code> and <code>using</code>, which represent the answer if we don't take or take <code>k</code> respectively.</p>
<p>If the new value <code>k</code> is adjacent to the previously largest value <code>prev</code>, then the answer if we must take <code>k</code> is <code>(the point value of k) + avoid</code>, while the answer if we must not take <code>k</code> is <code>max(avoid, using)</code>.  Similarly, if <code>k</code> is not adjacent to <code>prev</code>, the answer if we must take <code>k</code> is <code>(the point value of k) + max(avoid, using)</code>, and the answer if we must not take <code>k</code> is <code>max(avoid, using)</code>.</p>
<p>At the end, the best answer may or may not use the largest value in <code>nums</code>, so we return <code>max(avoid, using)</code>.</p>
<p>Our demonstrated solutions showcase two different kinds of sorts: a library one, and a radix sort.  For each language, the other kind of solution can be done without much difficulty, by using an array (Python) or HashMap (Java) respectively.</p>
<iframe src="https://leetcode.com/playground/TBKVkiLD/shared" frameborder="0" width="100%" height="395" name="TBKVkiLD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity (Python): <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  We make a single pass through the sorted keys of <script type="math/tex; mode=display">N</script>, and the complexity is dominated by the sorting step.</p>
</li>
<li>
<p>Space Complexity (Python): <script type="math/tex; mode=display">O(N)</script>, the size of our <code>count</code>.</p>
</li>
<li>
<p>Time Complexity (Java): We performed a radix sort instead, so our complexity is <script type="math/tex; mode=display">O(N+W)</script> where <script type="math/tex; mode=display">W</script> is the range of allowable values for <code>nums[i]</code>.</p>
</li>
<li>
<p>Space Complexity (Java): <script type="math/tex; mode=display">O(W)</script>, the size of our <code>count</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>