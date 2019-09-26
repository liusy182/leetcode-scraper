<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-scan-through-blocks">Approach 1: Scan Through Blocks</a></li>
<li><a href="#approach-2-sliding-window">Approach 2: Sliding Window</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-scan-through-blocks">Approach 1: Scan Through Blocks</h4>
<p><strong>Intuition</strong></p>
<p>Equivalently, we want the longest subarray with at most two "types" (values of <code>tree[i]</code>).</p>
<p>Instead of considering each element individually, we can consider blocks of adjacent elements of the same type.</p>
<p>For example, instead of <code>tree = [1, 1, 1, 1, 2, 2, 3, 3, 3]</code>, we can say this is <code>blocks = [(1, weight = 4), (2, weight = 2), (3, weight = 3)]</code>.</p>
<p>Now say we brute forced, scanning from left to right.  We'll have something like <code>blocks = [1, _2_, 1, 2, 1, 2, _1_, 3, ...]</code> (with various weights).</p>
<p>The key insight is that when we encounter a <code>3</code>, we do not need to start from the second element <code>2</code> (marked <code>_2_</code> for convenience); we can start from the first element (<code>_1_</code>) before the <code>3</code>.  This is because if we started two or more elements before, the sequence must have types <code>1</code> and <code>2</code>, and that sequence is going to end at the <code>3</code>, and thus be shorter than anything we've already considered.</p>
<p>Since every starting point (that is the left-most index of a block) was considered, this solution is correct.</p>
<p><strong>Algorithm</strong></p>
<p>As the notation and strategy around implementing this differs between Python and Java, please see the inline comments for more details.</p>
<iframe src="https://leetcode.com/playground/pvsyyXLb/shared" frameborder="0" width="100%" height="500" name="pvsyyXLb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>tree</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-sliding-window">Approach 2: Sliding Window</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach 1</em>, we want the longest subarray with at most two different "types" (values of <code>tree[i]</code>).  Call these subarrays <em>valid</em>.</p>
<p>Say we consider all valid subarrays that end at index <code>j</code>.  There must be one with the smallest possible starting index <code>i</code>: lets say <code>opt(j) = i</code>.</p>
<p>Now the key idea is that <code>opt(j)</code> is a monotone increasing function.  This is because any subarray of a valid subarray is valid.</p>
<p><strong>Algorithm</strong></p>
<p>Let's perform a sliding window, keeping the loop invariant that <code>i</code> will be the smallest index for which <code>[i, j]</code> is a valid subarray.</p>
<p>We'll maintain <code>count</code>, the count of all the elements in the subarray.  This allows us to quickly query whether there are 3 types in the subarray or not.</p>
<iframe src="https://leetcode.com/playground/tZWTV9pU/shared" frameborder="0" width="100%" height="500" name="tZWTV9pU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>tree</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>