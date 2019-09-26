<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort-by-column">Approach 1: Sort by Column</a></li>
<li><a href="#approach-2-count-by-diagonal">Approach 2: Count by Diagonal</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort-by-column">Approach 1: Sort by Column</h4>
<p><strong>Intuition</strong></p>
<p>Count each rectangle by right-most edge.</p>
<p><strong>Algorithm</strong></p>
<p>Group the points by <code>x</code> coordinates, so that we have columns of points.  Then, for every pair of points in a column (with coordinates <code>(x,y1)</code> and <code>(x,y2)</code>), check for the smallest rectangle with this pair of points as the rightmost edge.  We can do this by keeping memory of what pairs of points we've seen before.</p>
<iframe src="https://leetcode.com/playground/kTVsWSQg/shared" frameborder="0" width="100%" height="497" name="kTVsWSQg"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>points</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-count-by-diagonal">Approach 2: Count by Diagonal</h4>
<p><strong>Intuition</strong></p>
<p>For each pair of points in the array, consider them to be the long diagonal of a potential rectangle.  We can check if all 4 points are there using a Set.</p>
<p>For example, if the points are <code>(1, 1)</code> and <code>(5, 5)</code>, we check if we also have <code>(1, 5)</code> and <code>(5, 1)</code>.  If we do, we have a candidate rectangle.</p>
<p><strong>Algorithm</strong></p>
<p>Put all the points in a set.  For each pair of points, if the associated rectangle are 4 distinct points all in the set, then take the area of this rectangle as a candidate answer.</p>
<iframe src="https://leetcode.com/playground/x8SzczGY/shared" frameborder="0" width="100%" height="412" name="x8SzczGY"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>points</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">H</script> is the height of the tree.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approach #1 inspired by: <a href="https://leetcode.com/lee215">@lee215</a>.</p>
          </div>
        
      </div>