<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>Try all possible times, and remember the largest one.</p>
<p><strong>Algorithm (Java)</strong></p>
<p>Iterate over all permutations <code>(i, j, k, l)</code> of <code>(0, 1, 2, 3)</code>.  For each permutation, we can try the time <code>A[i]A[j] : A[k]A[l]</code>.</p>
<p>This is a valid time if and only if the number of hours <code>10*A[i] + A[j]</code> is less than <code>24</code>; and the number of minutes <code>10*A[k] + A[l]</code> is less than <code>60</code>.</p>
<p>We will output the largest valid time.</p>
<p><strong>Algorithm (Python)</strong></p>
<p>For each possible ordering of the 4 digits, if it's a legal time and the time is greater than the one we have stored, update the answer.</p>
<iframe src="https://leetcode.com/playground/vzuf8WrS/shared" frameborder="0" width="100%" height="429" name="vzuf8WrS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Java implementation inspired by <a href="https://leetcode.com/problems/largest-time-for-given-digits/discuss/200693/Java-11-liner-O(64)-w-comment-6-ms.">@rock</a>.</p>
          </div>
        
      </div>