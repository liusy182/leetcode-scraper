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
<p>Instead of multiplying by 2 or subtracting 1 from <code>X</code>, we could divide by 2 (when <code>Y</code> is even) or add 1 to <code>Y</code>.</p>
<p>The motivation for this is that it turns out we always greedily divide by 2:</p>
<ul>
<li>
<p>If say <code>Y</code> is even, then if we perform 2 additions and one division, we could instead perform one division and one addition for less operations [<code>(Y+2) / 2</code> vs <code>Y/2 + 1</code>].</p>
</li>
<li>
<p>If say <code>Y</code> is odd, then if we perform 3 additions and one division, we could instead perform 1 addition, 1 division, and 1 addition for less operations [<code>(Y+3) / 2</code> vs <code>(Y+1) / 2 + 1</code>].</p>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>While <code>Y</code> is larger than <code>X</code>, add 1 if it is odd, else divide by 2.  After, we need to do <code>X - Y</code> additions to reach <code>X</code>.</p>
<iframe src="https://leetcode.com/playground/xhbtbZzk/shared" frameborder="0" width="100%" height="293" name="xhbtbZzk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log Y)</script>.</p>
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