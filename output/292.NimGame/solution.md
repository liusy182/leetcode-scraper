<div class="article-body">
        
          <div class="block-markdown">
            <h2 id="solution">Solution</h2>
<p>You can <em>always</em> win a Nim game if the number of stones <script type="math/tex; mode=display">n</script> in the pile is not divisible by <script type="math/tex; mode=display">4</script>.</p>
<p><strong>Reasoning</strong></p>
<p>Let us think of the small cases. It is clear that if there are only one, two, or three stones in the pile, and it is your turn, you can win the game by taking all of them. Like the problem description says, if there are exactly four stones in the pile, you will lose. Because no matter how many you take, you will leave some stones behind for your opponent to take and win the game. So in order to win, you have to ensure that you never reach the situation where there are exactly four stones on the pile on your turn.</p>
<p>Similarly, if there are five, six, or seven stones you can win by taking just enough to leave four stones for your opponent so that they lose. But if there are eight stones on the pile, you will inevitably lose, because regardless whether you pick one, two or three stones from the pile, your opponent can pick three, two or one stone to ensure that, again, four stones will be left to you on your turn.</p>
<p>It is obvious that the same pattern repeats itself for <script type="math/tex; mode=display">n=4,8,12,16,\dots</script>, basically all multiples of <script type="math/tex; mode=display">4</script>.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">canWinNim</span><span class="o">(</span><span class="kt">int</span> <span class="n">n</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">return</span> <span class="o">(</span><span class="n">n</span> <span class="o">%</span> <span class="mi">4</span> <span class="o">!=</span> <span class="mi">0</span><span class="o">);</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<p>Time complexity is <script type="math/tex; mode=display">O(1)</script>, since only one check is performed. No additional space is used, so space complexity is also <script type="math/tex; mode=display">O(1)</script>.</p>
<p><strong>References</strong></p>
<p><a href="https://www.cs.umd.edu/~gordon/ysp/nim.pdf">Lecture on Nim Games</a> from University of Maryland: MATH 199: Math, Game Theory and the Theory of Games, Summer 2006.</p>
<p>Analysis written by: @noran</p>
          </div>
        
      </div>