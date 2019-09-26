<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-check-adjacent-words">Approach 1: Check Adjacent Words</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-check-adjacent-words">Approach 1: Check Adjacent Words</h4>
<p><strong>Intuition</strong></p>
<p>The words are sorted lexicographically if and only if adjacent words are.  This is because order is transitive: <code>a &lt;= b</code> and <code>b &lt;= c</code> implies <code>a &lt;= c</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's check whether all adjacent words <code>a</code> and <code>b</code> have <code>a &lt;= b</code>.</p>
<p>To check whether <code>a &lt;= b</code> for two adjacent words <code>a</code> and <code>b</code>, we can find their first difference.  For example, <code>"applying"</code> and <code>"apples"</code> have a first difference of <code>y</code> vs <code>e</code>.  After, we compare these characters to the index in <code>order</code>.</p>
<p>Care must be taken to deal with the blank character effectively.  If for example, we are comparing <code>"app"</code> to <code>"apply"</code>, this is a first difference of <code>(null)</code> vs <code>"l"</code>.</p>
<iframe src="https://leetcode.com/playground/8bE6hgJ8/shared" frameborder="0" width="100%" height="500" name="8bE6hgJ8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\mathcal{C})</script>, where <script type="math/tex; mode=display">\mathcal{C}</script> is the total <em>content</em> of <code>words</code>.</p>
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