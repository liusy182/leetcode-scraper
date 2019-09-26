<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-one-pass">Approach 1: One Pass</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-one-pass">Approach 1: One Pass</h4>
<p><strong>Intuition</strong></p>
<p>If we walk along the mountain from left to right, we have to move strictly up, then strictly down.</p>
<p><strong>Algorithm</strong></p>
<p>Let's walk up from left to right until we can't: that has to be the peak.  We should ensure the peak is not the first or last element.  Then, we walk down.  If we reach the end, the array is valid, otherwise its not.</p>
<iframe src="https://leetcode.com/playground/yszb4GTC/shared" frameborder="0" width="100%" height="395" name="yszb4GTC"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
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