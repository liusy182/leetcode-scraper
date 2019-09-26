<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-prefix-sum-accepted">Approach #1: Prefix Sum [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-prefix-sum-accepted">Approach #1: Prefix Sum [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's ask how many times the <code>i</code>th character is shifted.</p>
<p><strong>Algorithm</strong></p>
<p>The <code>i</code>th character is shifted <code>shifts[i] + shifts[i+1] + ... + shifts[shifts.length - 1]</code> times.  That's because only operations at the <code>i</code>th operation and after, affect the <code>i</code>th character.</p>
<p>Let <code>X</code> be the number of times the current <code>i</code>th character is shifted.  Then the next character <code>i+1</code> is shifted <code>X - shifts[i]</code> times.</p>
<p>For example, if <code>S.length = 4</code> and <code>S[0]</code> is shifted <code>X = shifts[0] + shifts[1] + shifts[2] + shifts[3]</code> times, then <code>S[1]</code> is shifted <code>shifts[1] + shifts[2] + shifts[3]</code> times, <code>S[2]</code> is shifted <code>shifts[2] + shifts[3]</code> times, and so on.</p>
<p>In general, we need to do <code>X -= shifts[i]</code> to maintain the correct value of <code>X</code> as we increment <code>i</code>.</p>
<iframe src="https://leetcode.com/playground/eh9zG8Q2/shared" frameborder="0" width="100%" height="327" name="eh9zG8Q2"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code> (and <code>shifts</code>).</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space needed to output the answer.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>