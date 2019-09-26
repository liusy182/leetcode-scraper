<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-queue">Approach 1: Queue</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-queue">Approach 1: Queue</h4>
<p><strong>Intuition</strong></p>
<p>We only care about the most recent calls in the last 3000 ms, so let's use a data structure that keeps only those.</p>
<p><strong>Algorithm</strong></p>
<p>Keep a queue of the most recent calls in increasing order of <code>t</code>.  When we see a new call with time <code>t</code>, remove all calls that occurred before <code>t - 3000</code>.</p>
<iframe src="https://leetcode.com/playground/qZ2BJSqK/shared" frameborder="0" width="100%" height="276" name="qZ2BJSqK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(Q)</script>, where <script type="math/tex; mode=display">Q</script> is the number of queries made.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(W)</script>, where <script type="math/tex; mode=display">W = 3000</script> is the size of the window we should scan for recent calls.  In this problem, the complexity can be considered <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>