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
<p>If we have a decoded string like <code>appleappleappleappleappleapple</code> and an index like <code>K = 24</code>, the answer is the same if <code>K = 4</code>.</p>
<p>In general, when a decoded string is equal to some word with <code>size</code> length repeated some number of times (such as <code>apple</code> with <code>size = 5</code> repeated 6 times), the answer is the same for the index <code>K</code> as it is for the index <code>K % size</code>.</p>
<p>We can use this insight by working backwards, keeping track of the size of the decoded string.  Whenever the decoded string would equal some <code>word</code> repeated <code>d</code> times, we can reduce <code>K</code> to <code>K % (word.length)</code>.</p>
<p><strong>Algorithm</strong></p>
<p>First, find the length of the decoded string.  After, we'll work backwards, keeping track of <code>size</code>: the length of the decoded string after parsing symbols <code>S[0], S[1], ..., S[i]</code>.</p>
<p>If we see a digit <code>S[i]</code>, it means the size of the decoded string after parsing <code>S[0], S[1], ..., S[i-1]</code> will be <code>size / Integer(S[i])</code>.  Otherwise, it will be <code>size - 1</code>.</p>
<iframe src="https://leetcode.com/playground/HGcLTehJ/shared" frameborder="0" width="100%" height="500" name="HGcLTehJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
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