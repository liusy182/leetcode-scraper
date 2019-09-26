<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-translate-by-delta-accepted">Approach #1: Translate by Delta [Accepted]</a></li>
<li><a href="#approach-2-count-by-delta-accepted">Approach #2: Count by Delta [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-translate-by-delta-accepted">Approach #1: Translate by Delta [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each translation <code>delta</code>, we calculate the candidate answer <code>overlap(delta)</code>, which is the size of the overlap if we shifted the matrix <code>A</code> by delta.</p>
<p>We only need to check <code>delta</code> for which some point in <code>A</code> maps to some point in <code>B</code>, since a candidate overlap must be at least 1.  Using a Set <code>seen</code>, we remember if we've calculated <code>overlap(delta)</code>, so that we don't perform this expensive check more than once per <code>delta</code>.</p>
<p>We use <code>java.awt.Point</code> (or <code>complex</code> in Python) to handle our 2D vectors gracefully.  We could have also mapped a vector <code>delta = (x, y)</code> (which has coordinates between <code>-(N-1)</code> and <code>N-1</code>) to <code>2*N x + y</code> for convenience.  Note that we cannot map it to <code>N*dx, dy</code> as there would be interference: <code>(0, N-1)</code> and <code>(1, -1)</code> would map to the same point.</p>
<iframe src="https://leetcode.com/playground/gnwqTeGt/shared" frameborder="0" width="100%" height="500" name="gnwqTeGt"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^6)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code> or <code>B</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-count-by-delta-accepted">Approach #2: Count by Delta [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can do the reverse of <em>Approach #1</em>: count every possible <code>delta = b - a</code> we see.  If we see say, 5 of the same <code>delta = b - a</code>, then the translation by <code>delta</code> must have overlap 5.</p>
<iframe src="https://leetcode.com/playground/YmA2kxzz/shared" frameborder="0" width="100%" height="378" name="YmA2kxzz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^4)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code> or <code>B</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>