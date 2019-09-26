<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-work-backwards">Approach 1: Work Backwards</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-work-backwards">Approach 1: Work Backwards</h4>
<p><strong>Intuition</strong></p>
<p>Imagine we stamped the sequence with moves <script type="math/tex; mode=display">m_1, m_2, \cdots</script>.  Now, from the final position <code>target</code>, we will make those moves in reverse order.  </p>
<p>Let's call the <code>i</code>th <em>window</em>, a subarray of <code>target</code> of length <code>stamp.length</code> that starts at <code>i</code>.  Each move at position <code>i</code> is possible if the <code>i</code>th window matches the stamp.  After, every character in the window becomes a wildcard that can match any character in the stamp.</p>
<p>For example, say we have <code>stamp = "abca"</code> and <code>target = "aabcaca"</code>.  Working backwards, we will reverse stamp at window <code>1</code> to get <code>"a????ca"</code>, then reverse stamp at window <code>3</code> to get <code>"a??????"</code>, and finally reverse stamp at position <code>0</code> to get <code>"???????"</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's keep track of every window.  We want to know how many cells initially match the stamp (our "<code>made</code>" list), and which ones don't (our <code>"todo"</code> list).  Any windows that are ready (ie. have no todo list), get enqueued.</p>
<p>Specifically, we enqueue the positions of each character.  (To save time, we enqueue by character, not by window.)  This represents that the character is ready to turn into a <code>"?"</code> in our working <code>target</code> string.</p>
<p>Now, how to process characters in our queue?  For each character, let's look at all the windows that intersect it, and update their todo lists.  If any todo lists become empty in this manner <code>(window.todo is empty)</code>, then we enqueue the characters in <code>window.made</code> that we haven't processed yet.</p>
<iframe src="https://leetcode.com/playground/fePTAdQw/shared" frameborder="0" width="100%" height="500" name="fePTAdQw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N(N-M))</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>stamp</code>, <code>target</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N(N-M))</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>