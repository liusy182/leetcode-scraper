<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-greatest-common-divisor">Approach 2: Greatest Common Divisor</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>We can try every possible <code>X</code>.  </p>
<p><strong>Algorithm</strong></p>
<p>Since we divide the deck of <code>N</code> cards into say, <code>K</code> piles of <code>X</code> cards each, we must have <code>N % X == 0</code>.</p>
<p>Then, say the deck has <code>C_i</code> copies of cards with number <code>i</code>.  Each group with number <code>i</code> has <code>X</code> copies, so we must have <code>C_i % X == 0</code>.  These are necessary and sufficient conditions.</p>
<iframe src="https://leetcode.com/playground/FCdXEDEB/shared" frameborder="0" width="100%" height="446" name="FCdXEDEB"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2 \log \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of cards.  It is outside the scope of this article to prove that the number of divisors of <script type="math/tex; mode=display">N</script> is bounded by <script type="math/tex; mode=display">O(N \log \log N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-greatest-common-divisor">Approach 2: Greatest Common Divisor</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Again, say there are <code>C_i</code> cards of number <code>i</code>.  These must be broken down into piles of <code>X</code> cards each, ie. <code>C_i % X == 0</code> for all <code>i</code>.</p>
<p>Thus, <code>X</code> must divide the greatest common divisor of <code>C_i</code>.  If this greatest common divisor <code>g</code> is greater than <code>1</code>, then <code>X = g</code> will satisfy.  Otherwise, it won't.</p>
<iframe src="https://leetcode.com/playground/biA9HRs5/shared" frameborder="0" width="100%" height="429" name="biA9HRs5"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log^2 N)</script>, where <script type="math/tex; mode=display">N</script> is the number of votes.  If there are <script type="math/tex; mode=display">C_i</script> cards with number <script type="math/tex; mode=display">i</script>, then each <code>gcd</code> operation is naively <script type="math/tex; mode=display">O(\log^2 C_i)</script>.  Better bounds exist, but are outside the scope of this article to develop.</p>
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