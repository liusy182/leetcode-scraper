<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort">Approach 1: Sort</a></li>
<li><a href="#approach-2-divide-and-conquer">Approach 2: Divide and Conquer</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort">Approach 1: Sort</h4>
<p><strong>Intuition</strong></p>
<p>Sort the points by distance, then take the closest K points.</p>
<p><strong>Algorithm</strong></p>
<p>There are two variants.</p>
<p>In Java, we find the K-th distance by creating an array of distances and then sorting them.  After, we select all the points with distance less than or equal to this K-th distance.</p>
<p>In Python, we sort by a custom key function - namely, the distance to the origin.  Afterwards, we return the first K elements of the list.</p>
<iframe src="https://leetcode.com/playground/qsCBvg6X/shared" frameborder="0" width="100%" height="429" name="qsCBvg6X"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>points</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-divide-and-conquer">Approach 2: Divide and Conquer</h4>
<p><strong>Intuition</strong></p>
<p>We want an algorithm faster than <script type="math/tex; mode=display">N \log N</script>.  Clearly, the only way to do this is to use the fact that the K elements returned can be in any order -- otherwise we would be sorting which is at least <script type="math/tex; mode=display">N \log N</script>.</p>
<p>Say we choose some random element <code>x = A[i]</code> and split the array into two buckets: one bucket of all the elements less than <code>x</code>, and another bucket of all the elements greater than or equal to <code>x</code>.  This is known as "quickselecting by a pivot <code>x</code>".</p>
<p>The idea is that if we quickselect by some pivot, on average in linear time we'll reduce the problem to a problem of half the size.</p>
<p><strong>Algorithm</strong></p>
<p>Let's do the <code>work(i, j, K)</code> of partially sorting the subarray <code>(points[i], points[i+1], ..., points[j])</code> so that the smallest <code>K</code> elements of this subarray occur in the first <code>K</code> positions <code>(i, i+1, ..., i+K-1)</code>.</p>
<p>First, we quickselect by a random pivot element from the subarray.  To do this in place, we have two pointers <code>i</code> and <code>j</code>, and move these pointers to the elements that are in the wrong bucket -- then, we swap these elements.</p>
<p>After, we have two buckets <code>[oi, i]</code> and <code>[i+1, oj]</code>, where <code>(oi, oj)</code> are the original <code>(i, j)</code> values when calling <code>work(i, j, K)</code>.  Say the first bucket has <code>10</code> items and the second bucket has <code>15</code> items.  If we were trying to partially sort say, <code>K = 5</code> items, then we only need to partially sort the first bucket: <code>work(oi, i, 5)</code>.  Otherwise, if we were trying to partially sort say, <code>K = 17</code> items, then the first <code>10</code> items are already partially sorted, and we only need to partially sort the next 7 items: <code>work(i+1, oj, 7)</code>.</p>
<iframe src="https://leetcode.com/playground/9yZ96Kwf/shared" frameborder="0" width="100%" height="500" name="9yZ96Kwf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script> in <em>average case</em> complexity, where <script type="math/tex; mode=display">N</script> is the length of <code>points</code>.</p>
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