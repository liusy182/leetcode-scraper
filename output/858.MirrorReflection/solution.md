<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-simulation">Approach 1: Simulation</a></li>
<li><a href="#approach-2-mathematical">Approach 2: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-simulation">Approach 1: Simulation</h4>
<p><strong>Intuition</strong></p>
<p>The initial ray can be described as going from an origin <code>(x, y) = (0, 0)</code> in the direction <code>(rx, ry) = (p, q)</code>.  From this, we can figure out which wall it will meet and where, and what the appropriate new ray will be (based on reflection.)  We keep simulating the ray until it finds it's destination.</p>
<p><strong>Algorithm</strong></p>
<p>The parameterized position of the laser after time <code>t</code> will be <code>(x + rx * t, y + ry * t)</code>.  From there, we know when it will meet the east wall (if <code>x + rx * t == p</code>), and so on.  For a positive (and nonnegligible) time <code>t</code>, it meets the next wall.</p>
<p>We can then calculate how the ray reflects.  If it hits an east or west wall, then <code>rx *= -1</code>, else <code>ry *= -1</code>.</p>
<p>In Java, care must be taken with floating point operations.</p>
<iframe src="https://leetcode.com/playground/Ds4FZeYo/shared" frameborder="0" width="100%" height="500" name="Ds4FZeYo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(p)</script>.  We can prove (using <em>Approach #2</em>) that the number of bounces is bounded by this.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-mathematical">Approach 2: Mathematical</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Instead of modelling the ray as a bouncing line, model it as a straight line through reflections of the room.</p>
<p>For example, if <code>p = 2, q = 1</code>, then we can reflect the room horizontally, and draw a straight line from <code>(0, 0)</code> to <code>(4, 2)</code>.  The ray meets the receptor <code>2</code>, which was reflected from <code>(0, 2)</code> to <code>(4, 2)</code>.</p>
<p>In general, the ray goes to the first integer point <code>(kp, kq)</code> where <code>k</code> is an integer, and <code>kp</code> and <code>kq</code> are multiples of <code>p</code>.  Thus, the goal is just to find the smallest <code>k</code> for which <code>kq</code> is a multiple of <code>p</code>.</p>
<p>The mathematical answer is <code>k = p / gcd(p, q)</code>.</p>
<iframe src="https://leetcode.com/playground/srjkydcW/shared" frameborder="0" width="100%" height="327" name="srjkydcW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log P)</script>, the complexity of the <code>gcd</code> operation.</p>
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