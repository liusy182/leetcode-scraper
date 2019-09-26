<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
<li><a href="#approach-2-mathematical">Approach 2: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>Let's change the game so that whenever Lee scores points, it deducts from Alex's score instead.</p>
<p>Let <code>dp(i, j)</code> be the largest score Alex can achieve where the piles remaining are <code>piles[i], piles[i+1], ..., piles[j]</code>.  This is natural in games with scoring: we want to know what the value of each position of the game is.</p>
<p>We can formulate a recursion for <code>dp(i, j)</code> in terms of <code>dp(i+1, j)</code> and <code>dp(i, j-1)</code>, and we can use dynamic programming to not repeat work in this recursion.  (This approach can output the correct answer, because the states form a DAG (directed acyclic graph).)</p>
<p><strong>Algorithm</strong></p>
<p>When the piles remaining are <code>piles[i], piles[i+1], ..., piles[j]</code>, the player who's turn it is has at most 2 moves.</p>
<p>The person who's turn it is can be found by comparing <code>j-i</code> to <code>N</code> modulo 2.</p>
<p>If the player is Alex, then she either takes <code>piles[i]</code> or <code>piles[j]</code>, increasing her score by that amount.  Afterwards, the total score is either <code>piles[i] + dp(i+1, j)</code>, or <code>piles[j] + dp(i, j-1)</code>; and we want the maximum possible score.</p>
<p>If the player is Lee, then he either takes <code>piles[i]</code> or <code>piles[j]</code>, decreasing Alex's score by that amount.  Afterwards, the total score is either <code>-piles[i] + dp(i+1, j)</code>, or <code>-piles[j] + dp(i, j-1)</code>; and we want the <em>minimum</em> possible score.</p>
<iframe src="https://leetcode.com/playground/4azVgCpr/shared" frameborder="0" width="100%" height="412" name="4azVgCpr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of piles.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, the space used storing the intermediate results of each subgame.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-mathematical">Approach 2: Mathematical</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Alex clearly always wins the 2 pile game.  With some effort, we can see that she always wins the 4 pile game.</p>
<p>If Alex takes the first pile initially, she can always take the third pile.  If she takes the fourth pile initially, she can always take the second pile.  At least one of <code>first + third, second + fourth</code> is larger, so she can always win.</p>
<p>We can extend this idea to <code>N</code> piles.  Say the first, third, fifth, seventh, etc. piles are white, and the second, fourth, sixth, eighth, etc. piles are black.  Alex can always take either all white piles or all black piles, and one of the colors must have a sum number of stones larger than the other color.</p>
<p>Hence, Alex always wins the game.</p>
<iframe src="https://leetcode.com/playground/TdjR4pTJ/shared" frameborder="0" width="100%" height="157" name="TdjR4pTJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>