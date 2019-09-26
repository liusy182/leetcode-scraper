<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-two-pointer-accepted">Approach #1: Two Pointer [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-two-pointer-accepted">Approach #1: Two Pointer [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Without loss of generality, a mountain can only start after the previous one ends.</p>
<p>This is because if it starts before the peak, it will be smaller than a mountain starting previous; and it is impossible to start after the peak.</p>
<p><strong>Algorithm</strong></p>
<p>For a starting index <code>base</code>, let's calculate the length of the longest mountain <code>A[base], A[base+1], ..., A[end]</code>.</p>
<p>If such a mountain existed, the next possible mountain will start at <code>base = end</code>; if it didn't, then either we reached the end, or we have <code>A[base] &gt; A[base+1]</code> and we can start at <code>base + 1</code>.</p>
<p><strong>Example</strong></p>
<p>Here is a worked example on the array <code>A = [1, 2, 3, 2, 1, 0, 2, 3, 1]</code>:</p>
<p></p><center>
    <img src="../Figures/845/diagram1.png" alt="Worked example of A = [1,2,3,2,1,0,2,3,1]" style="height: 150px">
</center>
<p><br></p>
<p><code>base</code> starts at <code>0</code>, and <code>end</code> travels using the first while loop to <code>end = 2</code> (<code>A[end] = 3</code>), the potential peak of this mountain.  After, it travels to <code>end = 5</code> (<code>A[end] = 0</code>) during the second while loop, and a candidate answer of 6 <code>(base = 0, end = 5)</code> is recorded.</p>
<p>Afterwards, base is set to <code>5</code> and the process starts over again, with <code>end = 7</code> the peak of the mountain, and <code>end = 8</code> the right boundary, and the candidate answer of 4 <code>(base = 5, end = 8)</code> being recorded.</p>
<iframe src="https://leetcode.com/playground/7cVQKFLP/shared" frameborder="0" width="100%" height="500" name="7cVQKFLP"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>