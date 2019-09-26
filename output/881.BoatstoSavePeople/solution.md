<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-greedy-two-pointer">Approach 1: Greedy (Two Pointer)</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-greedy-two-pointer">Approach 1: Greedy (Two Pointer)</h4>
<p><strong>Intuition</strong></p>
<p>If the heaviest person can share a boat with the lightest person, then do so.  Otherwise, the heaviest person can't pair with anyone, so they get their own boat.</p>
<p>The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>people[i]</code> to the currently lightest person, and <code>people[j]</code> to the heaviest.</p>
<p>Then, as described above, if the heaviest person can share a boat with the lightest person (if <code>people[j] + people[i] &lt;= limit</code>) then do so; otherwise, the heaviest person sits in their own boat.</p>
<iframe src="https://leetcode.com/playground/Vy4ovfs7/shared" frameborder="0" width="100%" height="344" name="Vy4ovfs7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>people</code>.</p>
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