<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-boundary-count-accepted">Approach #1: Boundary Count [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-boundary-count-accepted">Approach #1: Boundary Count [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>When booking a new event <code>[start, end)</code>, count <code>delta[start]++</code> and <code>delta[end]--</code>.  When processing the values of <code>delta</code> in sorted order of their keys, the largest such value is the answer.</p>
<p>In Python, we sort the set each time instead, as there is no analog to <em>TreeMap</em> available.</p>
<iframe src="https://leetcode.com/playground/yJnnXvTf/shared" frameborder="0" width="100%" height="378" name="yJnnXvTf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of events booked.  For each new event, we traverse <code>delta</code> in <script type="math/tex; mode=display">O(N)</script> time.  In Python, this is <script type="math/tex; mode=display">O(N^2 \log N)</script> owing to the extra sort step.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>delta</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Solution in Approach #2 inspired by <a href="https://discuss.leetcode.com/topic/111276/simplified-winner-s-solution">@cchao</a>.</p>
          </div>
        
      </div>