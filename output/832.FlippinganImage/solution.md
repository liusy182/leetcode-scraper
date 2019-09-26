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
<p>We can do this in place.  In each row, the <code>i</code>th value from the left is equal to the inverse of the <code>i</code>th value from the right.</p>
<p>We use <code>(C+1) / 2</code> (with floor division) to iterate over all indexes <code>i</code> in the first half of the row, including the center.</p>
<iframe src="https://leetcode.com/playground/rePZz3yF/shared" frameborder="0" width="100%" height="276" name="rePZz3yF"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <code>N</code> is the total number of elements in <code>A</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script> in <em>additional</em> space complexity.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>