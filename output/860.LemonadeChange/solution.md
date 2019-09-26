<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-simulation">Approach 1: Simulation</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-simulation">Approach 1: Simulation</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's try to simulate giving change to each customer buying lemonade.  Initially, we start with no <code>five</code> dollar bills, and no <code>ten</code> dollar bills.</p>
<ul>
<li>
<p>If a customer brings a $5 bill, then we take it.</p>
</li>
<li>
<p>If a customer brings a $10 bill, we must return a five dollar bill.  If we don't have a five dollar bill, the answer is <code>False</code>, since we can't make correct change.</p>
</li>
<li>
<p>If a customer brings a $20 bill, we must return $15.</p>
<ul>
<li>
<p>If we have a $10 and a $5, then we always prefer giving change in that, because it is strictly worse for making change than three $5 bills.</p>
</li>
<li>
<p>Otherwise, if we have three $5 bills, then we'll give that.</p>
</li>
<li>
<p>Otherwise, we won't be able to give $15 in change, and the answer is <code>False</code>.</p>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/aZ5ofLyL/shared" frameborder="0" width="100%" height="480" name="aZ5ofLyL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>bills</code>.</p>
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