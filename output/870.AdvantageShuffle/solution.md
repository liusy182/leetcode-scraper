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
<p>If the smallest card <code>a</code> in <code>A</code> beats the smallest card <code>b</code> in <code>B</code>, we should pair them.  Otherwise, <code>a</code> is useless for our score, as it can't beat any cards.</p>
<p>Why should we pair <code>a</code> and <code>b</code> if <code>a &gt; b</code>?  Because every card in <code>A</code> is larger than <code>b</code>, any card we place in front of <code>b</code> will score a point.  We might as well use the weakest card to pair with <code>b</code> as it makes the rest of the cards in <code>A</code> strictly larger, and thus have more potential to score points.</p>
<p><strong>Algorithm</strong></p>
<p>We can use the above intuition to create a greedy approach.  The current smallest card to beat in <code>B</code> will always be <code>b = sortedB[j]</code>.  For each card <code>a</code> in <code>sortedA</code>, we will either have <code>a</code> beat that card <code>b</code> (put <code>a</code> into <code>assigned[b]</code>), or throw <code>a</code> out (put <code>a</code> into <code>remaining</code>).</p>
<p>Afterwards, we can use our annotations <code>assigned</code> and <code>remaining</code> to reconstruct the answer.  Please see the comments for more details.</p>
<iframe src="https://leetcode.com/playground/GJdLmnhx/shared" frameborder="0" width="100%" height="500" name="GJdLmnhx"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code> and <code>B</code>.</p>
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