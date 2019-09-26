<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-backtracking-accepted">Approach #1: Backtracking [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-backtracking-accepted">Approach #1: Backtracking [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>There are only 4 cards and only 4 operations that can be performed.  Even when all operations do not commute, that gives us an upper bound of <script type="math/tex; mode=display">12 * 6 * 2 * 4 * 4 * 4 = 9216</script> possibilities, which makes it feasible to just try them all.  Specifically, we choose two numbers (with order) in 12 ways and perform one of 4 operations (12 * 4). Then, with 3 remaining numbers, we choose 2 of them and perform one of 4 operations (6 * 4).  Finally we have two numbers left and make a final choice of 2 * 4 possibilities.</p>
<p>We will perform 3 binary operations (<code>+, -, *, /</code> are the operations) on either our numbers or resulting numbers.  Because <code>-</code> and <code>/</code> do not commute, we must be careful to consider both <code>a / b</code> and <code>b / a</code>.</p>
<p>For every way to remove two numbers <code>a, b</code> in our list, and for each possible result they can make, like <code>a+b</code>, <code>a/b</code>, etc., we will recursively solve the problem on this smaller list of numbers.</p>
<iframe src="https://leetcode.com/playground/vSR6aMjS/shared" frameborder="0" name="vSR6aMjS" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(1)</script>.  There is a hard limit of 9216 possibilities, and we do <script type="math/tex; mode=display">O(1)</script> work for each of them.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.  Our intermediate arrays are at most 4 elements, and the number made is bounded by an <script type="math/tex; mode=display">O(1)</script> factor.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>