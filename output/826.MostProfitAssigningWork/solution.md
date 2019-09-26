<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-sorting-events-accepted">Approach #1: Sorting Events [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-sorting-events-accepted">Approach #1: Sorting Events [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can consider the workers in any order, so let's process them in order of skill.</p>
<p>If we processed all jobs with lower skill first, then the profit is just the most profitable job we have seen so far.</p>
<p><strong>Algorithm</strong></p>
<p>We can use a "two pointer" approach to process jobs in order.  We will keep track of <code>best</code>, the maximum profit seen.</p>
<p>For each worker with a certain <code>skill</code>, after processing all jobs with lower or equal difficulty, we add <code>best</code> to our answer.</p>
<iframe src="https://leetcode.com/playground/52pUn6By/shared" frameborder="0" width="100%" height="412" name="52pUn6By"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N + Q \log Q)</script>, where <script type="math/tex; mode=display">N</script> is the number of jobs, and <script type="math/tex; mode=display">Q</script> is the number of people.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the additional space used by <code>jobs</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>