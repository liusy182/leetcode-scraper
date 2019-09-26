<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-direct-accepted">Approach #1: Direct [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-direct-accepted">Approach #1: Direct [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We will reverse each block of <code>2k</code> characters directly.</p>
<p>Each block starts at a multiple of <code>2k</code>: for example, <code>0, 2k, 4k, 6k, ...</code>.  One thing to be careful about is we may not reverse each block if there aren't enough characters.</p>
<p>To reverse a block of characters from <code>i</code> to <code>j</code>, we can swap characters in positions <code>i++</code> and <code>j--</code>.</p>
<iframe src="https://leetcode.com/playground/2qnQN5xs/shared" frameborder="0" width="100%" height="293" name="2qnQN5xs"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the size of <code>s</code>.  We build a helper array, plus reverse about half the characters in <code>s</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>a</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>