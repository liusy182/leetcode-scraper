<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-min-array-accepted">Approach #1: Min Array [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-min-array-accepted">Approach #1: Min Array [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>For each index <code>S[i]</code>, let's try to find the distance to the next character <code>C</code> going left, and going right.  The answer is the minimum of these two values.</p>
<p><strong>Algorithm</strong></p>
<p>When going left to right, we'll remember the index <code>prev</code> of the last character <code>C</code> we've seen.  Then the answer is <code>i - prev</code>.</p>
<p>When going right to left, we'll remember the index <code>prev</code> of the last character <code>C</code> we've seen.  Then the answer is <code>prev - i</code>.</p>
<p>We take the minimum of these two answers to create our final answer.</p>
<iframe src="https://leetcode.com/playground/oPmtNjJL/shared" frameborder="0" width="100%" height="395" name="oPmtNjJL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.  We scan through the string twice.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>ans</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>