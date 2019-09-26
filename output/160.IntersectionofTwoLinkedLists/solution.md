<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-hash-table">Approach 2: Hash Table</a></li>
<li><a href="#approach-3-two-pointers">Approach 3: Two Pointers</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>For each node a<sub>i</sub> in list A, traverse the entire list B and check if any node in list B coincides with a<sub>i</sub>.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(mn)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-hash-table">Approach 2: Hash Table</h4>
<p>Traverse list A and store the address / reference to each node in a hash set. Then check every node b<sub>i</sub> in list B: if b<sub>i</sub> appears in the hash set, then b<sub>i</sub> is the intersection node.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m+n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m)</script> or <script type="math/tex; mode=display">O(n)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-two-pointers">Approach 3: Two Pointers</h4>
<ul>
<li>Maintain two pointers <script type="math/tex; mode=display">pA</script> and <script type="math/tex; mode=display">pB</script> initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.</li>
<li>When <script type="math/tex; mode=display">pA</script> reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when <script type="math/tex; mode=display">pB</script> reaches the end of a list, redirect it the head of A.</li>
<li>If at any point <script type="math/tex; mode=display">pA</script> meets <script type="math/tex; mode=display">pB</script>, then <script type="math/tex; mode=display">pA</script>/<script type="math/tex; mode=display">pB</script> is the intersection node.</li>
<li>To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) &lt; A.length (=6), <script type="math/tex; mode=display">pB</script> would reach the end of the merged list first, because <script type="math/tex; mode=display">pB</script> traverses exactly 2 nodes less than <script type="math/tex; mode=display">pA</script> does. By redirecting <script type="math/tex; mode=display">pB</script> to head A, and <script type="math/tex; mode=display">pA</script> to head B, we now ask <script type="math/tex; mode=display">pB</script> to travel exactly 2 more nodes than <script type="math/tex; mode=display">pA</script> would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.</li>
<li>If two lists have intersection, then their last nodes must be the same one. So when <script type="math/tex; mode=display">pA</script>/<script type="math/tex; mode=display">pB</script> reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.</li>
</ul>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m+n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>