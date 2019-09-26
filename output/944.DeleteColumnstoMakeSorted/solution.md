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
<p>If a column isn't sorted, it can't be part of the final answer.</p>
<p><strong>Algorithm</strong></p>
<p>For each column, check if its sorted.  If it isn't, it must be deleted, so we add 1 to the final answer.</p>
<iframe src="https://leetcode.com/playground/FdPeGK2P/shared" frameborder="0" width="100%" height="276" name="FdPeGK2P"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\mathcal{A})</script>, where <script type="math/tex; mode=display">\mathcal{A}</script> is the total <em>content</em> of <code>A</code>.</p>
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