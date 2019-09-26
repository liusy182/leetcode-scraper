<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-mathematical-accepted">Approach #1: Mathematical [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-mathematical-accepted">Approach #1: Mathematical [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in the problem statement, if the <code>XOR</code> of the entire array is <code>0</code>, then Alice wins.</p>
<p>If the <code>XOR</code> condition is never triggered, then clearly Alice wins if and only if there are an even number of elements, as every player always has a move.</p>
<p>Now for the big leap in intuition.  Actually, Alice always has a move when there are an even number of elements.  If <script type="math/tex; mode=display"> S = x_1 \oplus x_2 \oplus \cdots x_n \neq 0 </script>, but there are no possible moves (<script type="math/tex; mode=display"> S \oplus x_i = 0 </script>), then <script type="math/tex; mode=display">(S \oplus x_1) \oplus (S \oplus x_2) \oplus \cdots \oplus (S \oplus x_n) = (S \oplus \cdots \oplus S) \oplus (x_1 \oplus x_2 \oplus \cdots \oplus x_n) = 0 \oplus S \neq 0</script>, a contradiction.</p>
<p>Similarly, if there are an odd number of elements, then Bob always faces an even number of elements, and has a move.  So the answer is just the parity of the number of elements in the array.</p>
<p>Those that are familiar with the Sprague-Grundy theorem may know that this game is a misère-form game, meaning the theorem does not apply, and giving a big hint that there may exist a simpler solution.</p>
<iframe src="https://leetcode.com/playground/bz5ugFJG/shared" frameborder="0" width="100%" height="174" name="bz5ugFJG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>