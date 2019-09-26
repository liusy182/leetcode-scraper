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
<p>If we play a token face up, we might as well play the one with the smallest value.  Similarly, if we play a token face down, we might as well play the one with the largest value.</p>
<p><strong>Algorithm</strong></p>
<p>We don't need to play anything until absolutely necessary.  Let's play tokens face up until we can't, then play a token face down and continue.</p>
<p>We must be careful, as it is easy for our implementation to be incorrect if we do not handle corner cases correctly.  We should always play tokens face up until exhaustion, then play one token face down and continue.</p>
<p>Our loop must be constructed with the right termination condition: we can either play a token face up or face down.</p>
<p>Our final answer could be any of the intermediate answers we got after playing tokens face up (but before playing them face down.)</p>
<iframe src="https://leetcode.com/playground/FarrjFkE/shared" frameborder="0" width="100%" height="412" name="FarrjFkE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>tokens</code>.</p>
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