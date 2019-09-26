<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-hashmap-binary-search">Approach 1: HashMap + Binary Search</a></li>
<li><a href="#approach-2-treemap">Approach 2: TreeMap</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-hashmap-binary-search">Approach 1: HashMap + Binary Search</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each <code>key</code> we get or set, we only care about the timestamps and values for that key.  We can store this information in a <code>HashMap</code>.</p>
<p>Now, for each <code>key</code>, we can binary search the sorted list of timestamps to find the relevant <code>value</code> for that <code>key</code>.</p>
<iframe src="https://leetcode.com/playground/jS7yH954/shared" frameborder="0" width="100%" height="500" name="jS7yH954"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(1)</script> for each <code>set</code> operation, and <script type="math/tex; mode=display">O(\log N)</script> for each <code>get</code> operation, where <script type="math/tex; mode=display">N</script> is the number of entries in the <code>TimeMap</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-treemap">Approach 2: TreeMap</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>In <code>Java</code>, we can use <code>TreeMap.floorKey(timestamp)</code> to find the largest timestamp smaller than the given <code>timestamp</code>.</p>
<p>We build our solution in the same way as <em>Approach 1</em>, swapping in this functionality.</p>
<iframe src="https://leetcode.com/playground/pH7WK8ph/shared" frameborder="0" width="100%" height="429" name="pH7WK8ph"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(1)</script> for each <code>set</code> operation, and <script type="math/tex; mode=display">O(\log N)</script> for each <code>get</code> operation, where <script type="math/tex; mode=display">N</script> is the number of entries in the <code>TimeMap</code>.</p>
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