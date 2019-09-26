<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-simulation">Approach 1: Simulation</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-simulation">Approach 1: Simulation</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Simulate the revealing process with a deck set to <code>[0, 1, 2, ...]</code>.  If for example this deck is revealed in the order <code>[0, 2, 4, ...]</code> then we know we need to put the smallest card in index <code>0</code>, the second smallest card in index <code>2</code>, the third smallest card in index <code>4</code>, etc.</p>
<iframe src="https://leetcode.com/playground/mzU2amGq/shared" frameborder="0" width="100%" height="361" name="mzU2amGq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>deck</code>.</p>
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