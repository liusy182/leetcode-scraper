<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-binary-search">Approach 1: Binary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-binary-search">Approach 1: Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>If Koko can finish eating all the bananas (within <code>H</code> hours) with an eating speed of <code>K</code>, she can finish with a larger speed too.</p>
<p>If we let <code>possible(K)</code> be <code>true</code> if and only if Koko can finish with an eating speed of <code>K</code>, then there is some <code>X</code> such that <code>possible(K) = True</code> if and only if <code>K &gt;= X</code>.</p>
<p>For example, with <code>piles = [3, 6, 7, 11]</code> and <code>H = 8</code>, there is some <code>X = 4</code> so that <code>possible(1) = possible(2) = possible(3) = False</code>, and <code>possible(4) = possible(5) = ... = True</code>.</p>
<p><strong>Algorithm</strong></p>
<p>We can binary search on the values of <code>possible(K)</code> to find the first <code>X</code> such that <code>possible(X)</code> is <code>True</code>: that will be our answer.  Our loop invariant will be that <code>possible(hi)</code> is always <code>True</code>, and <code>lo</code> is always less than or equal to the answer.  For more information on binary search, please visit <a href="https://leetcode.com/explore/learn/card/binary-search/">[LeetCode Explore - Binary Search]</a>.</p>
<p>To find the value of <code>possible(K)</code>, (ie. whether <code>Koko</code> with an eating speed of <code>K</code> can eat all bananas in <code>H</code> hours), we simulate it.  For each pile of size <code>p &gt; 0</code>, we can deduce that Koko finishes it in <code>Math.ceil(p / K) = ((p-1) // K) + 1</code> hours, and we add these times across all piles and compare it to <code>H</code>.</p>
<iframe src="https://leetcode.com/playground/r7NHTXn2/shared" frameborder="0" width="100%" height="446" name="r7NHTXn2"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log W)</script>, where <script type="math/tex; mode=display">N</script> is the number of piles, and <script type="math/tex; mode=display">W</script> is the maximum size of a pile.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>