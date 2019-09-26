<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-ad-hoc">Approach 1: Ad-Hoc</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-ad-hoc">Approach 1: Ad-Hoc</h4>
<p><strong>Intuition</strong></p>
<p>If we see say <code>S[0] == 'I'</code>, we can always put <code>0</code> as the first element; similarly, if we see <code>S[0] == 'D'</code>, we can always put <code>N</code> as the first element.</p>
<p>Say we have a match for the rest of the string <code>S[1], S[2], ...</code> using <code>N</code> distinct elements.  Notice it doesn't matter what the elements are, only that they are distinct and totally ordered.  Then, putting <code>0</code> or <code>N</code> at the first character will match, and the rest of the elements (<code>1, 2, ..., N</code> or <code>0, 1, ..., N-1</code>) can use the matching we have.</p>
<p><strong>Algorithm</strong></p>
<p>Keep track of the smallest and largest element we haven't placed.  If we see an <code>'I'</code>, place the small element; otherwise place the large element.</p>
<iframe src="https://leetcode.com/playground/Lornz86n/shared" frameborder="0" width="100%" height="327" name="Lornz86n"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
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