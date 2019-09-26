<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
<li><a href="#approach-2-divide-and-conquer">Approach 2: Divide and Conquer</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>When writing the permutation <code>P = P_0, P_1, ..., P_N</code> from left to right, we only care about the relative rank of the last element placed.  For example, if <code>N = 5</code> (so that we have elements <code>{0, 1, 2, 3, 4, 5}</code>), and our permutation starts <code>2, 3, 4</code>, then it is similar to a situation where we have placed <code>?, ?, 2</code> and the remaining elements are <code>{0, 1, 3}</code>, in terms of how many possibilities there are to place the remaining elements in a valid way.</p>
<p>To this end, let <code>dp(i, j)</code> be the number of ways to place every number up to and inlcuding <code>P_i</code>, such that <code>P_i</code> when placed had relative rank <code>j</code>.  (Namely, there are <code>j</code> remaining numbers less than <code>P_i</code>.)</p>
<p><strong>Algorithm</strong></p>
<p>When placing <code>P_i</code> following a decreasing instruction <code>S[i-1] == 'D'</code>, we want <code>P_{i-1}</code> to have a higher value.  When placing <code>P_i</code> following an increasing instruction, we want <code>P_{i-1}</code> to have a lower value.  It is relatively easy to deduce the recursion from this fact.</p>
<iframe src="https://leetcode.com/playground/ymMfbxds/shared" frameborder="0" width="100%" height="500" name="ymMfbxds"></iframe>

<p><strong>Optimization</strong></p>
<p>Actually, we can do better than this.  For any given <code>i</code>, let's look at how the sum of <code>D_k = dp(i-1, k)</code> is queried.  Assuming <code>S[i-1] == 'I'</code>, we query <code>D_0, D_0 + D_1, D_0 + D_1 + D_2, ...</code> etc.  The case for <code>S[i-1] == 'D'</code> is similar.</p>
<p>Thus, we don't need to query the sum every time.  Instead, we could use (for <code>S[i-1] == 'I'</code>) the fact that <code>dp(i, j) = dp(i, j-1) + dp(i-1, j-1)</code>.  For <code>S[i-1] == 'D'</code>, we have the similar fact that <code>dp(i, j) = dp(i, j+1) + dp(i-1, j)</code>.  </p>
<p>These two facts make the work done for each state of <code>dp</code> have <script type="math/tex; mode=display">O(1)</script> (amortized) complexity, leading to a total time complexity of <script type="math/tex; mode=display">O(N^2)</script> for this solution.</p>
<iframe src="https://leetcode.com/playground/yKpXsoX7/shared" frameborder="0" width="100%" height="395" name="yKpXsoX7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>, or <script type="math/tex; mode=display">O(N^2)</script> with the optimized version.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-divide-and-conquer">Approach 2: Divide and Conquer</h4>
<p><strong>Intuition</strong></p>
<p>Let's place the zero of the permutation first.  It either goes between a <code>'DI'</code> part of the sequence, or it could go on the ends (the left end if it starts with <code>'I'</code>, and the right end if it ends in <code>'D'</code>.)  Afterwards, this splits the problem into two disjoint subproblems that we can solve with similar logic.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>dp(i, j)</code> be the number of valid permutations (of <code>n = j-i+2</code> total integers from <code>0</code> to <code>n-1</code>) corresponding to the DI sequence <code>S[i], S[i+1], ..., S[j]</code>.  If we can successfully place a zero between <code>S[k-1]</code> and <code>S[k]</code>, then there are two disjoint problems <code>S[i], ..., S[k-2]</code> and <code>S[k+1], ..., S[j]</code>.</p>
<p>To count the number of valid permutations in this case, we should choose <code>k-i</code> elements from <code>n-1</code> (<code>n</code> total integers, minus the zero) to put in the left group; then the answer is this, times the number of ways to arrange the left group [<code>dp(i, k-2)</code>], times the number of ways to arrange the right group [<code>dp(k+1, j)</code>].</p>
<iframe src="https://leetcode.com/playground/KreEbZYZ/shared" frameborder="0" width="100%" height="500" name="KreEbZYZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>