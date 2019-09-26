<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-greedy">Approach 1: Greedy</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-greedy">Approach 1: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>If <code>x</code> is currently the array element with the least absolute value, it must pair with <code>2*x</code>, as there does not exist any other <code>x/2</code> to pair with it.</p>
<p><strong>Algorithm</strong></p>
<p>Let's try to (virtually) "write" the final reordered array.</p>
<p>Let's check elements in order of absolute value.  When we check an element <code>x</code> and it isn't used, it must pair with <code>2*x</code>.  We will attempt to write <code>x, 2x</code> - if we can't, then the answer is <code>false</code>.  If we write everything, the answer is <code>true</code>.</p>
<p>To keep track of what we have not yet written, we will store it in a <code>count</code>.</p>
<iframe src="https://leetcode.com/playground/2njGcRUM/shared" frameborder="0" width="100%" height="500" name="2njGcRUM"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
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