<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-counting-accepted">Approach #1: Counting [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-counting-accepted">Approach #1: Counting [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Instead of processing all <code>20000</code> people, we can process pairs of <code>(age, count)</code> representing how many people are that age.  Since there are only 120 possible ages, this is a much faster loop.</p>
<p><strong>Algorithm</strong></p>
<p>For each pair <code>(ageA, countA)</code>, <code>(ageB, countB)</code>, if the conditions are satisfied with respect to age, then <code>countA * countB</code> pairs of people made friend requests.</p>
<p>If <code>ageA == ageB</code>, then we overcounted: we should have <code>countA * (countA - 1)</code> pairs of people making friend requests instead, as you cannot friend request yourself.</p>
<iframe src="https://leetcode.com/playground/hhWFMLmx/shared" frameborder="0" width="100%" height="412" name="hhWFMLmx"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\mathcal{A}^2 + N)</script>, where <script type="math/tex; mode=display">N</script> is the number of people, and <script type="math/tex; mode=display">\mathcal{A}</script> is the number of ages.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(\mathcal{A})</script>, the space used to store <code>count</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>