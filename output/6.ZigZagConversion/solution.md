<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort-by-row">Approach 1: Sort by Row</a></li>
<li><a href="#approach-2-visit-by-row">Approach 2: Visit by Row</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort-by-row">Approach 1: Sort by Row</h4>
<p><strong>Intuition</strong></p>
<p>By iterating through the string from left to right, we can easily determine which row in the Zig-Zag pattern that a character belongs to.</p>
<p><strong>Algorithm</strong></p>
<p>We can use <script type="math/tex; mode=display">\text{min}( \text{numRows}, \text{len}(s))</script> lists to represent the non-empty rows of the Zig-Zag Pattern.</p>
<p>Iterate through <script type="math/tex; mode=display">s</script> from left to right, appending each character to the appropriate row. The appropriate row can be tracked using two variables: the current row and the current direction.</p>
<p>The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.</p>
<iframe src="https://leetcode.com/playground/F7ATKV4h/shared" frameborder="0" width="100%" height="446" name="F7ATKV4h"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n == \text{len}(s)</script>
</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(n)</script>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-2-visit-by-row">Approach 2: Visit by Row</h4>
<p><strong>Intuition</strong></p>
<p>Visit the characters in the same order as reading the Zig-Zag pattern line by line.</p>
<p><strong>Algorithm</strong></p>
<p>Visit all characters in row 0 first, then row 1, then row 2, and so on...</p>
<p>For all whole numbers <script type="math/tex; mode=display">k</script>,</p>
<ul>
<li>Characters in row <script type="math/tex; mode=display">0</script> are located at indexes <script type="math/tex; mode=display">k \; (2 \cdot \text{numRows} - 2)</script>
</li>
<li>Characters in row <script type="math/tex; mode=display">\text{numRows}-1</script> are located at indexes <script type="math/tex; mode=display">k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1</script>
</li>
<li>Characters in inner row <script type="math/tex; mode=display">i</script> are located at indexes <script type="math/tex; mode=display">k \; (2 \cdot \text{numRows}-2)+i</script> and <script type="math/tex; mode=display">(k+1)(2 \cdot \text{numRows}-2)- i</script>.</li>
</ul>
<iframe src="https://leetcode.com/playground/Deg3hGi4/shared" frameborder="0" width="100%" height="395" name="Deg3hGi4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n == \text{len}(s)</script>. Each index is visited once.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(n)</script>. For the cpp implementation, <script type="math/tex; mode=display">O(1)</script> if return string is not considered extra space.</li>
</ul>
          </div>
        
      </div>