<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
<li><a href="#approach-2-prefix-hashmap-accepted">Approach #2: Prefix Hashmap [Accepted]</a></li>
<li><a href="#approach-3-trie-accepted">Approach #3: Trie [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each key in the map, if that key starts with the given prefix, then add it to the answer.</p>
<iframe src="https://leetcode.com/playground/jNhyy639/shared" frameborder="0" name="jNhyy639" width="100%" height="360"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Every insert operation is <script type="math/tex; mode=display">O(1)</script>.  Every sum operation is <script type="math/tex; mode=display">O(N * P)</script> where <script type="math/tex; mode=display">N</script> is the number of items in the map, and <script type="math/tex; mode=display">P</script> is the length of the input prefix.</p>
</li>
<li>
<p>Space Complexity: The space used by <code>map</code> is linear in the size of all input <code>key</code> and <code>val</code> values combined.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-prefix-hashmap-accepted">Approach #2: Prefix Hashmap [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can remember the answer for all possible prefixes in a HashMap <code>score</code>.  When we get a new <code>(key, val)</code> pair, we update every prefix of <code>key</code> appropriately: each prefix will be changed by <code>delta = val - map[key]</code>, where <code>map</code> is the previous associated value of <code>key</code> (zero if undefined.)</p>
<iframe src="https://leetcode.com/playground/QYzALHGM/shared" frameborder="0" name="QYzALHGM" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Every insert operation is <script type="math/tex; mode=display">O(K^2)</script>, where <script type="math/tex; mode=display">K</script> is the length of the key, as <script type="math/tex; mode=display">K</script> strings are made of an average length of <script type="math/tex; mode=display">K</script>.  Every sum operation is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity: The space used by <code>map</code> and <code>score</code> is linear in the size of all input <code>key</code> and <code>val</code> values combined.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-trie-accepted">Approach #3: Trie [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Since we are dealing with prefixes, a Trie (prefix tree) is a natural data structure to approach this problem.  For every node of the trie corresponding to some prefix, we will remember the desired answer (score) and store it at this node.  As in <em>Approach #2</em>, this involves modifying each node by <code>delta = val - map[key]</code>.</p>
<iframe src="https://leetcode.com/playground/FbmbbgFJ/shared" frameborder="0" name="FbmbbgFJ" width="100%" height="513"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Every insert operation is <script type="math/tex; mode=display">O(K)</script>, where <script type="math/tex; mode=display">K</script> is the length of the key.  Every sum operation is <script type="math/tex; mode=display">O(K)</script>.</p>
</li>
<li>
<p>Space Complexity: The space used is linear in the size of the total input.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>