<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-mathematical">Approach 1: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-mathematical">Approach 1: Mathematical</h4>
<p><strong>Intuition</strong></p>
<p>Call the move that takes the <code>K</code>th letter from the beginning and puts it on the end, a "<em><code>K</code>-kick</em>" move.</p>
<p>Examining 1-kick moves, they let us consider the string as a "necklace" that may be rotated freely, where each bead of the necklace corresponds to a letter in the string.  (Formally, this is the equivalence class under 1-kick moves.)</p>
<p>Examining 2-kick moves (in the context of treating the string as a necklace), they allow us to swap the positions of two adjacent beads.  Thus, with 2-kick moves, every permutation of necklace is possible.  (To actually construct the necklace, we bring the second smallest bead to be after the smallest, then the third smallest to be after the second smallest, and so on.)</p>
<p>The previous insight may be difficult to find.  Another strategy is to write a brute force program to examine the result of 2-kick moves - then we might notice that 2-kick moves allow any permutation of the string.</p>
<p>Yet another strategy might be to explicitly construct new moves based on previous moves.  If we perform a 2 kick move followed by many 1 kick moves, we can move a string like <code>"xyzzzzzz" -&gt; "xzzzzzzy" -&gt; "yxzzzzzz"</code>, proving we can swap the positions of any two adjacent letters.</p>
<p><strong>Algorithm</strong></p>
<p>If <code>K = 1</code>, only rotations of <code>S</code> are possible, and the answer is the smallest rotation.</p>
<p>If <code>K &gt; 1</code>, any permutation of <code>S</code> is possible, and the answer is the letters of <code>S</code> written in lexicographic order.</p>
<iframe src="https://leetcode.com/playground/DCwCw7ZJ/shared" frameborder="0" width="100%" height="327" name="DCwCw7ZJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>