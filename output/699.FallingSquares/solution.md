<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-framework">Approach Framework</a></li>
<li><a href="#approach-1-offline-propagation">Approach 1: Offline Propagation</a></li>
<li><a href="#approach-2-brute-force-with-coordinate-compression">Approach 2: Brute Force with Coordinate Compression</a></li>
<li><a href="#approach-3-block-square-root-decomposition">Approach 3: Block (Square Root) Decomposition</a></li>
<li><a href="#approach-4-segment-tree-with-lazy-propagation">Approach 4: Segment Tree with Lazy Propagation</a></li>
</ul>
</div>
<h4 id="approach-framework">Approach Framework</h4>
<p><strong>Intuition</strong></p>
<p>Intuitively, there are two operations: <code>update</code>, which updates our notion of the board (number line) after dropping a square; and <code>query</code>, which finds the largest height in the current board on some interval.  We will work on implementing these operations.</p>
<p><strong>Coordinate Compression</strong></p>
<p>In the below approaches, since there are only up to <code>2 * len(positions)</code> critical points, namely the left and right edges of each square, we can use a technique called <em>coordinate compression</em> to map these critical points to adjacent integers, as shown in the code snippets below.  </p>
<p>For brevity, these snippets are omitted from the remaining solutions.</p>
<iframe src="https://leetcode.com/playground/fMedPoC3/shared" frameborder="0" width="100%" height="242" name="fMedPoC3"></iframe>

<hr>
<h4 id="approach-1-offline-propagation">Approach 1: Offline Propagation</h4>
<p><strong>Intuition</strong></p>
<p>Instead of asking the question "what squares affect this query?", lets ask the question "what queries are affected by this square?"</p>
<p><strong>Algorithm</strong></p>
<p>Let <code>qans[i]</code> be the maximum height of the interval specified by <code>positions[i]</code>.  At the end, we'll return a running max of <code>qans</code>.</p>
<p>For each square <code>positions[i]</code>, the maximum height will get higher by the size of the square we drop.  Then, for any future squares that intersect the interval <code>[left, right)</code> (where <code>left = positions[i][0], right = positions[i][0] + positions[i][1]</code>), we'll update the maximum height of that interval.</p>
<iframe src="https://leetcode.com/playground/Pb4sS8fW/shared" frameborder="0" width="100%" height="500" name="Pb4sS8fW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>positions</code>.  We use two for-loops, each of complexity <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>qans</code> and <code>ans</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-brute-force-with-coordinate-compression">Approach 2: Brute Force with Coordinate Compression</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <code>N = len(positions)</code>.  After mapping the board to a board of length at most <script type="math/tex; mode=display">2* N \leq 2000</script>, we can brute force the answer by simulating each square's drop directly.</p>
<p>Our answer is either the current answer or the height of the square that was just dropped, and we'll update it appropriately.</p>
<iframe src="https://leetcode.com/playground/h2KhkM7T/shared" frameborder="0" width="100%" height="500" name="h2KhkM7T"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>positions</code>.  We use two for-loops, each of complexity <script type="math/tex; mode=display">O(N)</script> (because of coordinate compression.)</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>heights</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-block-square-root-decomposition">Approach 3: Block (Square Root) Decomposition</h4>
<p><strong>Intuition</strong></p>
<p>Whenever we perform operations (like <code>update</code> and <code>query</code>) on some interval in a domain, we could segment that domain with size <script type="math/tex; mode=display">W</script> into blocks of size <script type="math/tex; mode=display">\sqrt{W}</script>.  </p>
<p>Then, instead of a typical brute force where we update our array <code>heights</code> representing the board, we will also hold another array <code>blocks</code>, where <code>blocks[i]</code> represents the <script type="math/tex; mode=display">B = \lfloor \sqrt{W} \rfloor</script> elements <code>heights[B*i], heights[B*i + 1], ..., heights[B*i + B-1]</code>.  This allows us to write to the array in <script type="math/tex; mode=display">O(B)</script> operations.</p>
<p><strong>Algorithm</strong></p>
<p>Let's get into the details.  We actually need another array, <code>blocks_read</code>.  When we update some element <code>i</code> in block <code>b = i / B</code>, we'll also update <code>blocks_read[b]</code>.  If later we want to read the entire block, we can read from here (and stuff written to the whole block in <code>blocks[b]</code>.)</p>
<p>When we write to a block, we'll write in <code>blocks[b]</code>.  Later, when we want to read from an element <code>i</code> in block <code>b = i / B</code>, we'll read from <code>heights[i]</code> and <code>blocks[b]</code>.</p>
<p>Our process for managing <code>query</code> and <code>update</code> will be similar.  While <code>left</code> isn't a multiple of <code>B</code>, we'll proceed with a brute-force-like approach, and similarly for <code>right</code>.  At the end, <code>[left, right+1)</code> will represent a series of contiguous blocks: the interval will have length which is a multiple of <code>B</code>, and <code>left</code> will also be a multiple of <code>B</code>.</p>
<iframe src="https://leetcode.com/playground/ZY8qrszn/shared" frameborder="0" width="100%" height="500" name="ZY8qrszn"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N\sqrt{N})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>positions</code>.  Each <code>query</code> and <code>update</code> has complexity <script type="math/tex; mode=display">O(\sqrt{N})</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>heights</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-segment-tree-with-lazy-propagation">Approach 4: Segment Tree with Lazy Propagation</h4>
<p><strong>Intuition</strong></p>
<p>If we were familiar with the idea of a segment tree (which supports queries and updates on intervals), we can immediately crack the problem.  </p>
<p><strong>Algorithm</strong></p>
<p>Segment trees work by breaking intervals into a disjoint sum of component intervals, whose number is at most <code>log(width)</code>.  The motivation is that when we change an element, we only need to change <code>log(width)</code> many intervals that aggregate on an interval containing that element.</p>
<p>When we want to update an interval all at once, we need to use <em>lazy propagation</em> to ensure good run-time complexity.  This topic is covered in more depth <a href="https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/">here</a>.</p>
<p>With such an implementation in hand, the problem falls out immediately.</p>
<iframe src="https://leetcode.com/playground/SHMdZn9d/shared" frameborder="0" width="100%" height="500" name="SHMdZn9d"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>positions</code>.  This is the run-time complexity of using a segment tree.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by our tree.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>