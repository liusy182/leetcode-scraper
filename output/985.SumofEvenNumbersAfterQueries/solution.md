<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-maintain-array-sum">Approach 1: Maintain Array Sum</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-maintain-array-sum">Approach 1: Maintain Array Sum</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's try to maintain <code>S</code>, the sum of the array throughout one query operation.</p>
<p>When acting on an array element <code>A[index]</code>, the rest of the values of <code>A</code> remain the same.  Let's remove <code>A[index]</code> from <code>S</code> if it is even, then add <code>A[index] + val</code> back (if it is even.)</p>
<p>Here are some examples:</p>
<ul>
<li>
<p>If we have <code>A = [2,2,2,2,2]</code>, <code>S = 10</code>, and we do <code>A[0] += 4</code>: we will update <code>S -= 2</code>, then <code>S += 6</code>.  At the end, we will have <code>A = [6,2,2,2,2]</code> and <code>S = 14</code>.</p>
</li>
<li>
<p>If we have <code>A = [1,2,2,2,2]</code>, <code>S = 8</code>, and we do <code>A[0] += 3</code>: we will skip updating <code>S</code> (since <code>A[0]</code> is odd), then <code>S += 4</code>.  At the end, we will have <code>A = [4,2,2,2,2]</code> and <code>S = 12</code>.</p>
</li>
<li>
<p>If we have <code>A = [2,2,2,2,2]</code>, <code>S = 10</code> and we do <code>A[0] += 1</code>: we will update <code>S -= 2</code>, then skip updating <code>S</code> (since <code>A[0] + 1</code> is odd.)  At the end, we will have <code>A = [3,2,2,2,2]</code> and <code>S = 8</code>.</p>
</li>
<li>
<p>If we have <code>A = [1,2,2,2,2]</code>, <code>S = 8</code> and we do <code>A[0] += 2</code>: we will skip updating <code>S</code> (since <code>A[0]</code> is odd), then skip updating <code>S</code> again (since <code>A[0] + 2</code> is odd.)  At the end, we will have <code>A = [3,2,2,2,2]</code> and <code>S = 8</code>.</p>
</li>
</ul>
<p>These examples help illustrate that our algorithm actually maintains the value of <code>S</code> throughout each query operation.</p>
<iframe src="https://leetcode.com/playground/cYwLoifs/shared" frameborder="0" width="100%" height="395" name="cYwLoifs"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N+Q)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code> and <script type="math/tex; mode=display">Q</script> is the number of <code>queries</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(Q)</script>, though we only allocate <script type="math/tex; mode=display">O(1)</script> additional space.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>