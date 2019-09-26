<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-interval-stabbing-accepted">Approach #1: Interval Stabbing [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-interval-stabbing-accepted">Approach #1: Interval Stabbing [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Say <code>N = 10</code> and <code>A[2] = 5</code>.  Then there are 5 rotations that are bad for this number: rotation indexes <code>0, 1, 2, 8, 9</code> - these rotations will cause this number to not get 1 point later.</p>
<p>In general, for each number in the array, we can map out what rotation indexes will be bad for this number.  It will always be a region of one interval, possibly two if the interval wraps around (eg. <code>8, 9, 0, 1, 2</code> wraps around, to become <code>[8, 9]</code> and <code>[0, 1, 2]</code>.)</p>
<p>At the end of plotting these intervals, we need to know which rotation index has the least intervals overlapping it - this one is the answer.</p>
<p><strong>Algorithm</strong></p>
<p>First, an element like <code>A[2] = 5</code> will not get score in (up to) 5 posiitons: when the 5 is at final index 0, 1, 2, 3, or 4.  When we shift by 2, we'll get final index 0.  If we shift <code>5-1 = 4</code> before this, this element will end up at final index 4.  In general (modulo N), a shift of <code>i - A[i] + 1</code> to <code>i</code> will be the rotation indexes that will make <code>A[i]</code> not score a point.</p>
<p>If we are trying to plot an interval like <code>[2, 3, 4]</code>, then instead of doing <code>bad[2]--; bad[3]--; bad[4]--;</code>, what we will do instead is keep track of the cumulative total: <code>bad[2]--; bad[5]++</code>.  For "wrap-around" intervals like <code>[8, 9, 0, 1, 2]</code>, we will keep track of this as two separate intervals: <code>bad[8]--, bad[10]++, bad[0]--, bad[3]++</code>.  (Actually, because of our implementation, we don't need to remember the <code>bad[10]++</code> part.)</p>
<p>At the end, we want to find a rotation index with the least intervals overlapping.  We'll maintain a cumulative total <code>cur</code> representing how many intervals are currently overlapping our current rotation index, then update it as we step through each rotation index.</p>
<iframe src="https://leetcode.com/playground/wYbwGZmT/shared" frameborder="0" width="100%" height="480" name="wYbwGZmT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>