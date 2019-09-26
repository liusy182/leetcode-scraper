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
<p><strong>Intuition</strong></p>
<p>We simulate the path of the robot step by step.  Since there are at most 90000 steps, this is efficient enough to pass the given input limits.</p>
<p><strong>Algorithm</strong></p>
<p>We store the robot's position and direction.  If we get a turning command, we update the direction; otherwise we walk the specified number of steps in the given direction.</p>
<p>Care must be made to use a <code>Set</code> data structure for the obstacles, so that we can check efficiently if our next step is obstructed.  If we don't, our check <code>is point in obstacles</code> could be ~10,000 times slower.</p>
<p>In some languages, we need to encode the coordinates of each obstacle as a <code>long</code> integer so that it is a hashable key that we can put into a <code>Set</code> data structure.  Alternatively, we could also encode the coordinates as a <code>string</code>.</p>
<iframe src="https://leetcode.com/playground/BzLAA5NV/shared" frameborder="0" width="100%" height="500" name="BzLAA5NV"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + K)</script>, where <script type="math/tex; mode=display">N, K</script> are the lengths of <code>commands</code> and <code>obstacles</code> respectively.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(K)</script>, the space used in storing the <code>obstacleSet</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>