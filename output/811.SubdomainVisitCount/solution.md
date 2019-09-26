<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-hash-map-accepted">Approach #1: Hash Map [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-hash-map-accepted">Approach #1: Hash Map [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>The algorithm is straightforward: we just do what the problem statement tells us to do.</p>
<p>For an address like <code>a.b.c</code>, we will count <code>a.b.c</code>, <code>b.c</code>, and <code>c</code>.  For an address like <code>x.y</code>, we will count <code>x.y</code> and <code>y</code>.</p>
<p>To count these strings, we will use a hash map.  To split the strings into the required pieces, we will use library <code>split</code> functions.</p>
<iframe src="https://leetcode.com/playground/tMRWeTNX/shared" frameborder="0" width="100%" height="395" name="tMRWeTNX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>cpdomains</code>, and assuming the length of <code>cpdomains[i]</code> is fixed.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used in our count.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>