<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-next-array-accepted">Approach #1: Next Array [Accepted]</a></li>
<li><a href="#approach-2-two-pointer-accepted">Approach #2: Two Pointer [Accepted]</a></li>
<li><a href="#approach-3-group-by-zero-accepted">Approach #3: Group by Zero [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-next-array-accepted">Approach #1: Next Array [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>left[i]</code> be the distance from seat <code>i</code> to the closest person sitting to the left of <code>i</code>.  Similarly, let <code>right[i]</code> be the distance to the closest person sitting to the right of <code>i</code>.  This is motivated by the idea that the closest person in seat <code>i</code> sits a distance <code>min(left[i], right[i])</code> away.</p>
<p><strong>Algorithm</strong></p>
<p>To construct <code>left[i]</code>, notice it is either <code>left[i-1] + 1</code> if the seat is empty, or <code>0</code> if it is full.  <code>right[i]</code> is constructed in a similar way.</p>
<iframe src="https://leetcode.com/playground/Mdkek4gh/shared" frameborder="0" width="100%" height="480" name="Mdkek4gh"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>seats</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by <code>left</code> and <code>right</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pointer-accepted">Approach #2: Two Pointer [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As we iterate through seats, we'll update the closest person sitting to our left, and closest person sitting to our right.</p>
<p><strong>Algorithm</strong></p>
<p>Keep track of <code>prev</code>, the filled seat at or to the left of <code>i</code>, and <code>future</code>, the filled seat at or to the right of <code>i</code>.</p>
<p>Then at seat <code>i</code>, the closest person is <code>min(i - prev, future - i)</code>, with one exception.  <code>i - prev</code> should be considered infinite if there is no person to the left of seat <code>i</code>, and similarly <code>future - i</code> is infinite if there is no one to the right of seat <code>i</code>.</p>
<iframe src="https://leetcode.com/playground/VSP6cs27/shared" frameborder="0" width="100%" height="429" name="VSP6cs27"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>seats</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-group-by-zero-accepted">Approach #3: Group by Zero [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>In a group of <code>K</code> adjacent empty seats between two people, the answer is <code>(K+1) / 2</code>.</p>
<p><strong>Algorithm</strong></p>
<p>For each group of <code>K</code> empty seats between two people, we can take into account the candidate answer <code>(K+1) / 2</code>.</p>
<p>For groups of empty seats between the edge of the row and one other person, the answer is <code>K</code>, and we should take into account those answers too.</p>
<iframe src="https://leetcode.com/playground/wKJwsWbr/shared" frameborder="0" width="100%" height="500" name="wKJwsWbr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>seats</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.  (In Python, <code>seats[::-1]</code> uses <script type="math/tex; mode=display">O(N)</script> space, but this can be remedied.)</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>