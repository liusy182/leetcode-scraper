<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-pass">Approach 1: Two Pass</a></li>
<li><a href="#approach-2-read-write-heads">Approach 2: Read / Write Heads</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-pass">Approach 1: Two Pass</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Read all the even integers and put them into places <code>ans[0]</code>, <code>ans[2]</code>, <code>ans[4]</code>, and so on.</p>
<p>Then, read all the odd integers and put them into places <code>ans[1]</code>, <code>ans[3]</code>, <code>ans[5]</code>, etc.</p>
<iframe src="https://leetcode.com/playground/sV3wKPcR/shared" frameborder="0" width="100%" height="429" name="sV3wKPcR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-read-write-heads">Approach 2: Read / Write Heads</h4>
<p><strong>Intuition</strong></p>
<p>We are motivated (perhaps by the interviewer) to pursue a solution where we modify the original array <code>A</code> in place.</p>
<p>First, it is enough to put all even elements in the correct place, since all odd elements will be in the correct place too.  So let's only focus on <code>A[0], A[2], A[4], ...</code></p>
<p>Ideally, we would like to have some partition where everything to the left is already correct, and everything to the right is undecided.</p>
<p>Indeed, this idea works if we separate it into two slices <code>even = A[0], A[2], A[4], ...</code> and <code>odd = A[1], A[3], A[5], ...</code>.  Our invariant will be that everything less than <code>i</code> in the even slice is correct, and everything less than <code>j</code> in the odd slice is correct.</p>
<p><strong>Algorithm</strong></p>
<p>For each even <code>i</code>, let's make <code>A[i]</code> even.  To do it, we will draft an element from the odd slice.  We pass <code>j</code> through the odd slice until we find an even element, then swap.  Our invariant is maintained, so the algorithm is correct.</p>
<iframe src="https://leetcode.com/playground/aWm3c7PK/shared" frameborder="0" width="100%" height="344" name="aWm3c7PK"></iframe>

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