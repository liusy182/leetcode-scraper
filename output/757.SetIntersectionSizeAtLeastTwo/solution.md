<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to solve a simpler problem: what is the answer when the set intersection size is at least <em>one</em>?</p>
<p>Sort the points.  Take the last interval <code>[s, e]</code>, which point on this interval will be in <code>S</code>?  Since every other interval has start point <code>&lt;= s</code>, it is strictly better to choose <code>s</code> as the start.  So we can repeatedly take <code>s</code> in our set <code>S</code> and remove all intervals containing <code>s</code>.</p>
<p>We will try to extend this solution to the case when we want an intersection of size two.</p>
<p><strong>Algorithm</strong></p>
<p>For each interval, we will perform the algorithm described above, storing a <code>todo</code> <em>multiplicity</em> which starts at <code>2</code>.  As we identify points in <code>S</code>, we will subtract from these multiplicities as appropriate.</p>
<p>One case that is important to handle is the following:
<code>[[1, 2], [2, 3], [2, 4], [4, 5]]</code>.  If we put <code>4, 5</code> in <code>S</code>, then we put <code>2</code> in <code>S</code>, when handling <code>[2, 3]</code> we need to put <code>3</code> in <code>S</code>, not <code>2</code> which was already put.</p>
<p>We can handle this case succinctly by sorting intervals <code>[s, e]</code> by <code>s</code> ascending, then <code>e</code> descending.  This makes it so that any interval encountered with the same <code>s</code> has the lowest possible <code>e</code>, and so it has the highest <em>multiplicity</em>.  When at interval <code>[s, e]</code> and choosing points to be included into <code>S</code>, it will always be the case that the start of the interval (either <code>s</code> or <code>s, s+1</code>) will be unused.</p>
<iframe src="https://leetcode.com/playground/w4QM4e3U/shared" frameborder="0" width="100%" height="412" name="w4QM4e3U"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>intervals</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>