<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort">Approach 1: Sort</a></li>
<li><a href="#approach-2-two-pass">Approach 2: Two Pass</a></li>
<li><a href="#approach-2-two-pass_1">Approach 2: Two Pass</a></li>
<li><a href="#approach-3-in-place">Approach 3: In-Place</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort">Approach 1: Sort</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Use a custom comparator when sorting, to sort by parity.</p>
<iframe src="https://leetcode.com/playground/bcMSW6MA/shared" frameborder="0" width="100%" height="412" name="bcMSW6MA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script> for the sort, depending on the built-in implementation of <code>sort</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pass">Approach 2: Two Pass</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Write all the even elements first, then write all the odd elements.</p>
<iframe src="https://leetcode.com/playground/uepE6ksC/shared" frameborder="0" width="100%" height="327" name="uepE6ksC"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script> for the sort, depending on the built-in implementation of <code>sort</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pass_1">Approach 2: Two Pass</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Write all the even elements first, then write all the odd elements.</p>
<iframe src="https://leetcode.com/playground/AjwfiQ8K/shared" frameborder="0" width="100%" height="327" name="AjwfiQ8K"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by the answer.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-in-place">Approach 3: In-Place</h4>
<p><strong>Intuition</strong></p>
<p>If we want to do the sort in-place, we can use quicksort, a standard textbook algorithm.</p>
<p><strong>Algorithm</strong></p>
<p>We'll maintain two pointers <code>i</code> and <code>j</code>.  The loop invariant is everything below <code>i</code> has parity <code>0</code> (ie. <code>A[k] % 2 == 0</code> when <code>k &lt; i</code>), and everything above <code>j</code> has parity <code>1</code>.</p>
<p>Then, there are 4 cases for <code>(A[i] % 2, A[j] % 2)</code>:</p>
<ul>
<li>
<p>If it is <code>(0, 1)</code>, then everything is correct: <code>i++</code> and <code>j--</code>.</p>
</li>
<li>
<p>If it is <code>(1, 0)</code>, we swap them so they are correct, then continue.</p>
</li>
<li>
<p>If it is <code>(0, 0)</code>, only the <code>i</code> place is correct, so we <code>i++</code> and continue.</p>
</li>
<li>
<p>If it is <code>(1, 1)</code>, only the <code>j</code> place is correct, so we <code>j--</code> and continue.</p>
</li>
</ul>
<p>Throughout all 4 cases, the loop invariant is maintained, and <code>j-i</code> is getting smaller.  So eventually we will be done with the array sorted as desired.</p>
<iframe src="https://leetcode.com/playground/SCAvRwWS/shared" frameborder="0" width="100%" height="344" name="SCAvRwWS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.  Each step of the while loop makes <code>j-i</code> decrease by at least one.  (Note that while quicksort is <script type="math/tex; mode=display">O(N \log N)</script> normally, this is <script type="math/tex; mode=display">O(N)</script> because we only need one pass to sort the elements.)</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script> in additional space complexity.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>