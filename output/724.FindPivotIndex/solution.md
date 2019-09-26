<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-prefix-sum-accepted">Approach #1: Prefix Sum [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-prefix-sum-accepted">Approach #1: Prefix Sum [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We need to quickly compute the sum of values to the left and the right of every index.</p>
<p>Let's say we knew <code>S</code> as the sum of the numbers, and we are at index <code>i</code>.  If we knew the sum of numbers <code>leftsum</code> that are to the left of index <code>i</code>, then the other sum to the right of the index would just be <code>S - nums[i] - leftsum</code>.  </p>
<p>As such, we only need to know about <code>leftsum</code> to check whether an index is a pivot index in constant time.  Let's do that: as we iterate through candidate indexes <code>i</code>, we will maintain the correct value of <code>leftsum</code>.</p>
<iframe src="https://leetcode.com/playground/332EfbBV/shared" frameborder="0" width="100%" height="242" name="332EfbBV"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>leftsum</code> and <code>S</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>