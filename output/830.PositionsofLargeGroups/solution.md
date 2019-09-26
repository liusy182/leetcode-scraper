<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-two-pointer-accepted">Approach #1: Two Pointer [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-two-pointer-accepted">Approach #1: Two Pointer [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We scan through the string to identify the start and end of each group.  If the size of the group is at least 3, we add it to the answer.</p>
<p><strong>Algorithm</strong></p>
<p>Maintain pointers <code>i, j</code> with <code>i &lt;= j</code>.  The <code>i</code> pointer will represent the start of the current group, and we will increment <code>j</code> forward until it reaches the end of the group.</p>
<p>We know that we have reached the end of the group when <code>j</code> is at the end of the string, or <code>S[j] != S[j+1]</code>.  At this point, we have some group <code>[i, j]</code>; and after, we will update <code>i = j+1</code>, the start of the next group.</p>
<iframe src="https://leetcode.com/playground/m9hgNCUd/shared" frameborder="0" width="100%" height="327" name="m9hgNCUd"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by the answer.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>