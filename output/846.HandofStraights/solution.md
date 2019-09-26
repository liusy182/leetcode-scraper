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
<p>We will repeatedly try to form a group (of size W) starting with the lowest card.  This works because the lowest card still in our hand must be the bottom end of a size <code>W</code> straight.</p>
<p><strong>Algorithm</strong></p>
<p>Let's keep a count <code>{card: number of copies of card}</code> as a <code>TreeMap</code> (or <code>dict</code>).</p>
<p>Then, repeatedly we will do the following steps: find the lowest value card that has 1 or more copies (say with value <code>x</code>), and try to remove <code>x, x+1, x+2, ..., x+W-1</code> from our count.  If we can't, then the task is impossible.</p>
<iframe src="https://leetcode.com/playground/VyDASsga/shared" frameborder="0" width="100%" height="446" name="VyDASsga"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N * (N/W))</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>hand</code>.  The <script type="math/tex; mode=display">(N / W)</script> factor comes from <code>min(count)</code>.  In Java, the <script type="math/tex; mode=display">(N / W)</script> factor becomes <script type="math/tex; mode=display">\log N</script> due to the complexity of <code>TreeMap</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>