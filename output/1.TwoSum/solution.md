<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-two-pass-hash-table">Approach 2: Two-pass Hash Table</a></li>
<li><a href="#approach-3-one-pass-hash-table">Approach 3: One-pass Hash Table</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>The brute force approach is simple. Loop through each element <script type="math/tex; mode=display">x</script> and find if there is another value that equals to <script type="math/tex; mode=display">target - x</script>.</p>
<iframe src="https://leetcode.com/playground/CLZq9vzU/shared" frameborder="0" width="100%" height="225" name="CLZq9vzU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>.
For each element, we try to find its complement by looping through the rest of array which takes <script type="math/tex; mode=display">O(n)</script> time. Therefore, the time complexity is <script type="math/tex; mode=display">O(n^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pass-hash-table">Approach 2: Two-pass Hash Table</h4>
<p>To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.</p>
<p>We reduce the look up time from <script type="math/tex; mode=display">O(n)</script> to <script type="math/tex; mode=display">O(1)</script> by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in <em>near</em> constant time. I say "near" because if a collision occurred, a look up could degenerate to <script type="math/tex; mode=display">O(n)</script> time. But look up in hash table should be amortized <script type="math/tex; mode=display">O(1)</script> time as long as the hash function was chosen carefully.</p>
<p>A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement (<script type="math/tex; mode=display">target - nums[i]</script>) exists in the table. Beware that the complement must not be <script type="math/tex; mode=display">nums[i]</script> itself!</p>
<iframe src="https://leetcode.com/playground/QhqBrfm7/shared" frameborder="0" width="100%" height="276" name="QhqBrfm7"></iframe>

<p><strong>Complexity Analysis:</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
We traverse the list containing <script type="math/tex; mode=display">n</script> elements exactly twice. Since the hash table reduces the look up time to <script type="math/tex; mode=display">O(1)</script>, the time complexity is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
The extra space required depends on the number of items stored in the hash table, which stores exactly <script type="math/tex; mode=display">n</script> elements.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-one-pass-hash-table">Approach 3: One-pass Hash Table</h4>
<p>It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.</p>
<iframe src="https://leetcode.com/playground/fbBQEjxv/shared" frameborder="0" width="100%" height="242" name="fbBQEjxv"></iframe>

<p><strong>Complexity Analysis:</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
We traverse the list containing <script type="math/tex; mode=display">n</script> elements only once. Each look up in the table costs only <script type="math/tex; mode=display">O(1)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
The extra space required depends on the number of items stored in the hash table, which stores at most <script type="math/tex; mode=display">n</script> elements.</p>
</li>
</ul>
          </div>
        
      </div>