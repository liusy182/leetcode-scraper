<div class="article-body">
        
          <div class="block-markdown">
            <h4 id="approach-1-stack-accepted">Approach #1: Stack [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's maintain the value of each valid round on a stack as we process the data.  A stack is ideal since we only deal with operations involving the last or second-last valid round.</p>
<iframe src="https://leetcode.com/playground/FRAbgcgJ/shared" frameborder="0" name="FRAbgcgJ" width="100%" height="462"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>ops</code>.  We parse through every element in the given array once, and do <script type="math/tex; mode=display">O(1)</script> work for each element.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used to store our <code>stack</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>