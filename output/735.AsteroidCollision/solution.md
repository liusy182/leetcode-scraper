<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-stack-accepted">Approach #1: Stack [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-stack-accepted">Approach #1: Stack [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>A row of asteroids is stable if no further collisions will occur.  After adding a new asteroid to the right, some more collisions may happen before it becomes stable again, and all of those collisions (if they happen) must occur right to left.  This is the perfect situation for using a <em>stack</em>.</p>
<p><strong>Algorithm</strong></p>
<p>Say we have our answer as a stack with rightmost asteroid <code>top</code>, and a <code>new</code> asteroid comes in.  If <code>new</code> is moving right (<code>new &gt; 0</code>), or if <code>top</code> is moving left (<code>top &lt; 0</code>), no collision occurs.</p>
<p>Otherwise, if <code>abs(new) &lt; abs(top)</code>, then the <code>new</code> asteroid will blow up; if <code>abs(new) == abs(top)</code> then both asteroids will blow up; and if <code>abs(new) &gt; abs(top)</code>, then the <code>top</code> asteroid will blow up (and possibly more asteroids will, so we should continue checking.)</p>
<iframe src="https://leetcode.com/playground/CyN24YU5/shared" frameborder="0" width="100%" height="480" name="CyN24YU5"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of asteroids.  Our stack pushes and pops each asteroid at most once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>ans</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>