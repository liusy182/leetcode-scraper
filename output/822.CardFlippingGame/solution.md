<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-hash-set-accepted">Approach #1: Hash Set [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-hash-set-accepted">Approach #1: Hash Set [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If a card has the same value <code>x</code> on the front and back, it is impossible to win with <code>x</code>.  Otherwise, it has two different values, and if we win with <code>x</code>, we can put <code>x</code> face down on the rest of the cards.</p>
<p><strong>Algorithm</strong></p>
<p>Remember all values <code>same</code> that occur twice on a single card.  Then for every value <code>x</code> on any card that isn't in <code>same</code>, <code>x</code> is a candidate answer.  If we have no candidate answers, the final answer is zero.</p>
<iframe src="https://leetcode.com/playground/DvJ47nbA/shared" frameborder="0" width="100%" height="378" name="DvJ47nbA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>fronts</code> (and <code>backs</code>).  We scan through the arrays.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>