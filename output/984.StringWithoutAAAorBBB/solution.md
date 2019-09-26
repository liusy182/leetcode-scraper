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
<p>Intuitively, we should write the most common letter first.  For example, if we have <code>A = 6, B = 2</code>, we want to write <code>'aabaabaa'</code>.  The only time we don't write the most common letter is if the last two letters we have written are also the most common letter</p>
<p><strong>Algorithm</strong></p>
<p>Let's maintain <code>A, B</code>: the number of <code>'a'</code> and <code>'b'</code>'s left to write.</p>
<p>If we have already written the most common letter twice, we'll write the other letter.  Otherwise, we'll write the most common letter.</p>
<iframe src="https://leetcode.com/playground/Ps9koK2t/shared" frameborder="0" width="100%" height="500" name="Ps9koK2t"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(A+B)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(A+B)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>