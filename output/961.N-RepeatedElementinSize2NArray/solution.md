<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-count">Approach 1: Count</a></li>
<li><a href="#approach-2-compare">Approach 2: Compare</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-count">Approach 1: Count</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's count the number of elements.  We can use a <code>HashMap</code> or an array - here, we use a <code>HashMap</code>.</p>
<p>After, the element with a count larger than 1 must be the answer.</p>
<iframe src="https://leetcode.com/playground/Xu4ee6QT/shared" frameborder="0" width="100%" height="293" name="Xu4ee6QT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-compare">Approach 2: Compare</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>If we ever find a repeated element, it must be the answer.  Let's call this answer the <em>major element</em>.</p>
<p>Consider all subarrays of length 4.  There must be a major element in at least one such subarray.</p>
<p>This is because either:</p>
<ul>
<li>There is a major element in a length 2 subarray, or;</li>
<li>Every length 2 subarray has exactly 1 major element, which means that a length 4 subarray that begins at a major element will have 2 major elements.</li>
</ul>
<p>Thus, we only have to compare elements with their neighbors that are distance 1, 2, or 3 away.</p>
<iframe src="https://leetcode.com/playground/9URvAsjC/shared" frameborder="0" width="100%" height="225" name="9URvAsjC"></iframe>

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