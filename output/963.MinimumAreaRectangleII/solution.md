<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-iterate-triangles">Approach 1: Iterate Triangles</a></li>
<li><a href="#approach-2-iterate-centers">Approach 2: Iterate Centers</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-iterate-triangles">Approach 1: Iterate Triangles</h4>
<p><strong>Intuition</strong></p>
<p>For each triangle, let's try to find the 4th point and whether it is a rectangle.</p>
<p><strong>Algorithm</strong></p>
<p>Say the first 3 points are <code>p1, p2, p3</code>, and that  <code>p2</code> and <code>p3</code> are opposite corners of the final rectangle.  The 4th point must be <code>p4 = p2 + p3 - p1</code> (using vector notation) because <code>p1, p2, p4, p3</code> must form a parallelogram, and <code>p1 + (p2 - p1) + (p3 - p1) = p4</code>.</p>
<p>If this point exists in our collection (we can use a <code>HashSet</code> to check), then we should check that the angles of this parallelogram are 90 degrees.  The easiest way is to check the dot product of the two vectors <code>(p2 - p1)</code> and <code>(p3 - p1)</code>.  (Another way is we could normalize the vectors to length 1, and check that one equals the other rotated by 90 degrees.)</p>
<iframe src="https://leetcode.com/playground/4L9BqZN7/shared" frameborder="0" width="100%" height="500" name="4L9BqZN7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>points</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-iterate-centers">Approach 2: Iterate Centers</h4>
<p><strong>Intuition</strong></p>
<p>Consider opposite points <code>AC</code> and <code>BD</code> of a rectangle <code>ABCD</code>.  They both have the same center <code>O</code>, which is the midpoint of <code>AC</code> and the midpoint of <code>AB</code>; and they both have the same radius <code>dist(O, A) == dist(O, B) == dist(O, C) == dist(O, D)</code>.  Notice that a necessary and sufficient condition to form a rectangle with two opposite pairs of points is that the points must have the same center and radius.</p>
<p>Motivated by that result, let's classify each pair of points <code>PQ</code> by their center <code>C</code> = the midpoint of <code>PQ</code>, and the radius <code>r = dist(P, C)</code>.  Our strategy is to brute force on pairs of points with the same classification.</p>
<p><strong>Algorithm</strong></p>
<p>For each pair of points, classify them by <code>center</code> and <code>radius</code>.  We only need to record one of the points <code>P</code>, since the other point is <code>P' = 2 * center - P</code> (using vector notation).</p>
<p>For each <code>center</code> and <code>radius</code>, look at every possible rectangle (two pairs of points <code>P, P', Q, Q'</code>).  The area of this rectangle <code>dist(P, Q) * dist(P, Q')</code> is a candidate answer.</p>
<iframe src="https://leetcode.com/playground/2wzCpbAU/shared" frameborder="0" width="100%" height="500" name="2wzCpbAU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2 \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>points</code>.  It can be shown that the number of pairs of points with the same classification is bounded by <script type="math/tex; mode=display">\log N</script> - <a href="https://en.wikipedia.org/wiki/Sum_of_squares_function#Particular_cases">see this link for more.</a></p>
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