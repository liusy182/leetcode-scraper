<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-balance">Approach 1: Balance</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-balance">Approach 1: Balance</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Keep track of the <em>balance</em> of the string: the number of <code>'('</code>'s minus the number of <code>')'</code>'s.  A string is valid if its balance is 0, plus every prefix has non-negative balance.</p>
<p>The above idea is common with matching brackets problems, but could be difficult to find if you haven't seen it before.</p>
<p>Now, consider the balance of every prefix of <code>S</code>.  If it is ever negative (say, -1), we must add a '(' bracket.  Also, if the balance of <code>S</code> is positive (say, <code>+B</code>), we must add <code>B</code> ')' brackets at the end.</p>
<iframe src="https://leetcode.com/playground/mbE7BCSV/shared" frameborder="0" width="100%" height="310" name="mbE7BCSV"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
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