<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-check-position-accepted">Approach #1: Check Position [Accepted]</a></li>
<li><a href="#approach-2-check-area-accepted">Approach #2: Check Area [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-check-position-accepted">Approach #1: Check Position [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If the rectangles do not overlap, then <code>rec1</code> must either be higher, lower, to the left, or to the right of <code>rec2</code>.</p>
<p><strong>Algorithm</strong></p>
<p>The answer for whether they <em>don't</em> overlap is <code>LEFT OR RIGHT OR UP OR DOWN</code>, where <code>OR</code> is the logical OR, and <code>LEFT</code> is a boolean that represents whether <code>rec1</code> is to the left of <code>rec2</code>.  The answer for whether they do overlap is the negation of this.</p>
<p>The condition "<code>rec1</code> is to the left of <code>rec2</code>" is <code>rec1[2] &lt;= rec2[0]</code>, that is the right-most x-coordinate of <code>rec1</code> is left of the left-most x-coordinate of <code>rec2</code>.  The other cases are similar.</p>
<iframe src="https://leetcode.com/playground/XsHWyYAa/shared" frameborder="0" width="100%" height="191" name="XsHWyYAa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<hr>
<h4 id="approach-2-check-area-accepted">Approach #2: Check Area [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If the rectangles overlap, they have positive area.  This area must be a rectangle where both dimensions are positive, since the boundaries of the intersection are axis aligned.</p>
<p>Thus, we can reduce the problem to the one-dimensional problem of determining whether two line segments overlap.</p>
<p><strong>Algorithm</strong></p>
<p>Say the area of the intersection is <code>width * height</code>, where <code>width</code> is the intersection of the rectangles projected onto the x-axis, and <code>height</code> is the same for the y-axis.  We want both quantities to be positive.</p>
<p>The <code>width</code> is positive when <code>min(rec1[2], rec2[2]) &gt; max(rec1[0], rec2[0])</code>, that is when the smaller of (the largest x-coordinates) is larger than the larger of (the smallest x-coordinates).  The <code>height</code> is similar.</p>
<iframe src="https://leetcode.com/playground/gthZq8DL/shared" frameborder="0" width="100%" height="157" name="gthZq8DL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>