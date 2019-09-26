<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sliding-window">Approach 1: Sliding Window</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sliding-window">Approach 1: Sliding Window</h4>
<p><strong>Intuition</strong></p>
<p>Evidently, we only care about the comparisons between adjacent elements.  If the comparisons are represented by <code>-1, 0, 1</code> (for <code>&lt;, =, &gt;</code>), then we want the longest sequence of alternating <code>1, -1, 1, -1, ...</code> (starting with either <code>1</code> or <code>-1</code>).</p>
<p>These alternating comparisons form contiguous blocks.  We know when the next block ends: when it is the last two elements being compared, or when the sequence isn't alternating.</p>
<p>For example, take an array like <code>A = [9,4,2,10,7,8,8,1,9]</code>.  The comparisons are <code>[1,1,-1,1,-1,0,-1,1]</code>.  The blocks are <code>[1], [1,-1,1,-1], [0], [-1,1]</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Scan the array from left to right.  If we are at the end of a block (last elements OR it stopped alternating), then we should record the length of that block as our candidate answer, and set the start of the new block as the next element.</p>
<iframe src="https://leetcode.com/playground/9pQoKhee/shared" frameborder="0" width="100%" height="378" name="9pQoKhee"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
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