<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-greedy">Approach 1: Greedy</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-greedy">Approach 1: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>We have to push the items in order, so when do we pop them?</p>
<p>If the stack has say, <code>2</code> at the top, then if we have to pop that value next, we must do it now.  That's because any subsequent push will make the top of the stack different from <code>2</code>, and we will never be able to pop again.</p>
<p><strong>Algorithm</strong></p>
<p>For each value, push it to the stack.</p>
<p>Then, greedily pop values from the stack if they are the next values to pop.</p>
<p>At the end, we check if we have popped all the values successfully.</p>
<iframe src="https://leetcode.com/playground/3SkVeyqy/shared" frameborder="0" width="100%" height="344" name="3SkVeyqy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>pushed</code> and <code>popped</code>.</p>
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