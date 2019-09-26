<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-simulation-accepted">Approach #1: Simulation [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-simulation-accepted">Approach #1: Simulation [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Instead of keeping track of how much champagne should end up in a glass, keep track of the total amount of champagne that flows through a glass.  For example, if <code>poured = 10</code> cups are poured at the top, then the total flow-through of the top glass is <code>10</code>; the total flow-through of each glass in the second row is <code>4.5</code>, and so on.</p>
<p><strong>Algorithm</strong></p>
<p>In general, if a glass has flow-through <code>X</code>, then <code>Q = (X - 1.0) / 2.0</code> quantity of champagne will equally flow left and right.  We can simulate the entire pour for 100 rows of glasses.  A glass at <code>(r, c)</code> will have excess champagne flow towards <code>(r+1, c)</code> and <code>(r+1, c+1)</code>.</p>
<iframe src="https://leetcode.com/playground/GbytuGmq/shared" frameborder="0" width="100%" height="344" name="GbytuGmq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(R^2)</script>, where <script type="math/tex; mode=display">R</script> is the number of rows.  As this is fixed, we can consider this complexity to be <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(R^2)</script>, or <script type="math/tex; mode=display">O(1)</script> by the reasoning above.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>