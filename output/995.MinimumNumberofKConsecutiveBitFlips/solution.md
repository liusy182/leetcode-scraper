<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-greedy-events">Approach 1: Greedy + Events</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-greedy-events">Approach 1: Greedy + Events</h4>
<p><strong>Intuition</strong></p>
<p>If the leftmost element is a 0, we must flip the subarray starting at index 0.  Similarly, if the leftmost element is a 1, we should not flip the subarray starting at index 0.  This proves we can proceed in a greedy manner: after finding out whether we have to flip the first subarray (positions 0 to K-1) or not, we can consider the array with the first element (value 1) removed, and repeat this process.</p>
<p>We can do better.  Every time we flip a subarray <code>A[i], A[i+1], ..., A[i+K-1]</code>, we can consider this as two "events", one 'opening event' at position <code>i</code> that marks the start of the subarray, and one 'closing event' at position <code>i+K</code> that marks the end of the subarray.  Using these events, we always know how many overlapping flipped subarrays there are: its simply the number of opening events minus the number of closing events.</p>
<p><strong>Algorithm</strong></p>
<p>When we flip a subarray, let's call the set of indices we flipped an interval.  We'll keep track of <code>flip</code>, the number of overlapping intervals in our current position.  We only care about the value of <code>flip</code> modulo 2.</p>
<p>When we flip an interval starting at <code>i</code>, we create a hint for a closing event at <code>i+K</code> telling us to flip our writing state back.</p>
<p>Please see the inline comments for more details.</p>
<iframe src="https://leetcode.com/playground/C4RkaMHp/shared" frameborder="0" width="100%" height="429" name="C4RkaMHp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is length of <code>A</code>.</p>
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