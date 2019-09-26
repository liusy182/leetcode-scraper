<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-mathematical">Approach 1: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-mathematical">Approach 1: Mathematical</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>From the top, the shadow made by the shape will be 1 square for each non-zero value.</p>
<p>From the side, the shadow made by the shape will be the largest value for each row in the grid.</p>
<p>From the front, the shadow made by the shape will be the largest value for each column in the grid.</p>
<p><strong>Example</strong></p>
<p>With the example <code>[[1,2],[3,4]]</code>:</p>
<ul>
<li>
<p>The shadow from the top will be 4, since there are four non-zero values in the grid;</p>
</li>
<li>
<p>The shadow from the side will be <code>2 + 4</code>, since the maximum value of the first row is <code>2</code>, and the maximum value of the second row is <code>4</code>;</p>
</li>
<li>
<p>The shadow from the front will be <code>3 + 4</code>, since the maximum value of the first column is <code>3</code>, and the maximum value of the second column is <code>4</code>.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/unjtgTJT/shared" frameborder="0" width="100%" height="429" name="unjtgTJT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>grid</code>.</p>
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