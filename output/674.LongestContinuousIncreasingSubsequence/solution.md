<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-sliding-window-accepted">Approach #1: Sliding Window [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-sliding-window-accepted">Approach #1: Sliding Window [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Every (continuous) increasing subsequence is disjoint, and the boundary of each such subsequence occurs whenever <code>nums[i-1] &gt;= nums[i]</code>.  When it does, it marks the start of a new increasing subsequence at <code>nums[i]</code>, and we store such <code>i</code> in the variable <code>anchor</code>.</p>
<p>For example, if <code>nums = [7, 8, 9, 1, 2, 3]</code>, then <code>anchor</code> starts at <code>0</code> (<code>nums[anchor] = 7</code>) and gets set again to <code>anchor = 3</code> (<code>nums[anchor] = 1</code>).  Regardless of the value of <code>anchor</code>, we record a candidate answer of <code>i - anchor + 1</code>, the length of the subarray <code>nums[anchor], nums[anchor+1], ..., nums[i]</code>; and our answer gets updated appropriately.</p>
<iframe src="https://leetcode.com/playground/AvR7oHwg/shared" frameborder="0" width="100%" height="225" name="AvR7oHwg"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  We perform one loop through <code>nums</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>anchor</code> and <code>ans</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>