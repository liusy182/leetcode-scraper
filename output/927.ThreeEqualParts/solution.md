<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-equal-ones">Approach 1: Equal Ones</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-equal-ones">Approach 1: Equal Ones</h4>
<p><strong>Intuition</strong></p>
<p>Each part has to have the same number of ones in their representation.  The algorithm given below is the natural continuation of this idea.</p>
<p><strong>Algorithm</strong></p>
<p>Say <code>S</code> is the number of ones in <code>A</code>.  Since every part has the same number of ones, they all should have <code>T = S / 3</code> ones.</p>
<p>If <code>S</code> isn't divisible by 3, the task is impossible.</p>
<p>We can find the position of the 1st, T-th, T+1-th, 2T-th, 2T+1-th, and 3T-th one.  The positions of these ones form 3 intervals: <code>[i1, j1], [i2, j2], [i3, j3]</code>.  (If there are only 3 ones, then the intervals are each length 1.)</p>
<p>Between them, there may be some number of zeros.  The zeros after <code>j3</code> must be included in each part: say there are <code>z</code> of them <code>(z = S.length - j3)</code>.</p>
<p>So the first part, <code>[i1, j1]</code>, is now <code>[i1, j1+z]</code>.  Similarly, the second part, <code>[i2, j2]</code>, is now <code>[i2, j2+z]</code>.</p>
<p>If all this is actually possible, then the final answer is <code>[j1+z, j2+z+1]</code>.</p>
<iframe src="https://leetcode.com/playground/svqa2QF7/shared" frameborder="0" width="100%" height="500" name="svqa2QF7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
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