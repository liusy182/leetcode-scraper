<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-list-operation">Approach 1: List operation</a></li>
<li><a href="#approach-2-hash-table">Approach 2: Hash Table</a></li>
<li><a href="#approach-3-math">Approach 3: Math</a></li>
<li><a href="#approach-4-bit-manipulation">Approach 4: Bit Manipulation</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-list-operation">Approach 1: List operation</h4>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate over all the elements in <script type="math/tex; mode=display">\text{nums}</script>
</li>
<li>If some number in <script type="math/tex; mode=display">\text{nums}</script> is new to array, append it</li>
<li>If some number is already in the array, remove it</li>
</ol>
<iframe src="https://leetcode.com/playground/bCj3rwUg/shared" frameborder="0" width="100%" height="276" name="bCj3rwUg"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We iterate through <script type="math/tex; mode=display">\text{nums}</script>, taking <script type="math/tex; mode=display">O(n)</script> time. We search the whole list to find whether there is duplicate number, taking <script type="math/tex; mode=display">O(n)</script> time. Because search is in the <code>for</code> loop, so we have to multiply both time complexities which is <script type="math/tex; mode=display">O(n^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.  We need a list of size <script type="math/tex; mode=display">n</script> to contain elements in <script type="math/tex; mode=display">\text{nums}</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-hash-table">Approach 2: Hash Table</h4>
<p><strong>Algorithm</strong></p>
<p>We use hash table to avoid the <script type="math/tex; mode=display">O(n)</script> time required for searching the elements.</p>
<ol>
<li>Iterate through all elements in <script type="math/tex; mode=display">\text{nums}</script>
</li>
<li>Try if <script type="math/tex; mode=display">hash\_table</script> has the key for <code>pop</code></li>
<li>If not, set up key/value pair</li>
<li>In the end, there is only one element in <script type="math/tex; mode=display">hash\_table</script>, so use <code>popitem</code> to get it</li>
</ol>
<iframe src="https://leetcode.com/playground/ebzkQT6R/shared" frameborder="0" width="100%" height="276" name="ebzkQT6R"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n \cdot 1) = O(n)</script>.  Time complexity of <code>for</code> loop is <script type="math/tex; mode=display">O(n)</script>. Time complexity of hash table(dictionary in python) operation <code>pop</code> is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The space required by <script type="math/tex; mode=display">hash\_table</script> is equal to the number of elements in <script type="math/tex; mode=display">\text{nums}</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-math">Approach 3: Math</h4>
<p><strong>Concept</strong></p>
<p>
<script type="math/tex; mode=display">2 * (a + b + c) - (a + a + b + b + c) = c</script>
</p>
<iframe src="https://leetcode.com/playground/hQwrqahc/shared" frameborder="0" width="100%" height="174" name="hQwrqahc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n + n) = O(n)</script>. <code>sum</code> will call <code>next</code> to iterate through <script type="math/tex; mode=display">\text{nums}</script>.
We can see it as <code>sum(list(i, for i in nums))</code> which means the time complexity is <script type="math/tex; mode=display">O(n)</script> because of the number of elements(<script type="math/tex; mode=display">n</script>) in <script type="math/tex; mode=display">\text{nums}</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n + n) = O(n)</script>. <code>set</code> needs space for the elements in <code>nums</code>
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-bit-manipulation">Approach 4: Bit Manipulation</h4>
<p><strong>Concept</strong></p>
<ul>
<li>If we take XOR of zero and some bit, it will return that bit<ul>
<li>
<script type="math/tex; mode=display">a \oplus 0 = a</script>
</li>
</ul>
</li>
<li>If we take XOR of two same bits, it will return 0<ul>
<li>
<script type="math/tex; mode=display">a \oplus a = 0</script>
</li>
</ul>
</li>
<li>
<script type="math/tex; mode=display">a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b</script>
</li>
</ul>
<p>So we can XOR all bits together to find the unique number.</p>
<iframe src="https://leetcode.com/playground/3TAX3mmj/shared" frameborder="0" width="100%" height="225" name="3TAX3mmj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.  We only iterate through <script type="math/tex; mode=display">\text{nums}</script>, so the time complexity is the number of elements in <script type="math/tex; mode=display">\text{nums}</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>