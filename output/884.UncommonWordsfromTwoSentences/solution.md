<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-counting">Approach 1: Counting</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-counting">Approach 1: Counting</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Every uncommon word occurs exactly once in total.  We can count the number of occurrences of every word, then return ones that occur exactly once.</p>
<iframe src="https://leetcode.com/playground/YwdvfZv6/shared" frameborder="0" width="100%" height="327" name="YwdvfZv6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(M + N)</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>A</code> and <code>B</code> respectively.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(M + N)</script>, the space used by <code>count</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>