<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>For each possible triangle, check it's area and keep the area of the largest.</p>
<p><strong>Algorithm</strong></p>
<p>We will have 3 for loops to cycle through each choice of 3 points in the array.</p>
<p>After, we'll need a function to calculate the area given 3 points.  Here we have some options:</p>
<ul>
<li>
<p>We can use the Shoelace formula directly, which tells us the area given the 3 points;</p>
</li>
<li>
<p>We can use Heron's formula, which requires the 3 side lengths which we can get by taking the distance of two points;</p>
</li>
<li>
<p>We can use the formula <code>area = 0.5 * a * b * sin(C)</code> and calculate the angle <code>C</code> with trigonometry.</p>
</li>
</ul>
<p>Our implementation illustrates the use of the shoelace formula.</p>
<p>If we did not know the shoelace formula, we could derive it for triangles with the following approach: starting with points <code>(px, py), (qx, qy), (rx, ry)</code>, the area of this triangle is the same under a translation by <code>(-rx, -ry)</code>, so that the points become <code>(px-rx, py-ry), (qx-rx, qy-ry), (0, 0)</code>.</p>
<p>From there, we could draw a square around the triangle with sides touching the coordinate axes, and calculate the area of the square minus the area of the right triangles surrounding the inner triangle.</p>
<p>For more on this approach, see the <a href="https://en.wikipedia.org/wiki/Shoelace_formula">Wikipedia entry for the Shoelace formula</a>.</p>
<iframe src="https://leetcode.com/playground/n9XwHjZg/shared" frameborder="0" width="100%" height="327" name="n9XwHjZg"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>points</code>.  We use three for-loops of length <script type="math/tex; mode=display">O(N)</script>, and our work calculating the area of a single triangle is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>