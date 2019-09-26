<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</a></li>
<li><a href="#approach-2-similar-approach-accepted">Approach #2 Similar Approach [Accepted]</a></li>
<li><a href="#approach-3-dynamic-programming-accepted">Approach #3 Dynamic Programming [Accepted]:</a></li>
<li><a href="#approach-4-1-d-dynamic-programming-accepted">Approach #4 1-D Dynamic Programming [Accepted]:</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</h4>
<p>The idea behind the recursive approach is simple. The two players Player 1 and Player 2 will be taking turns alternately. For the Player 1 to be the winner, we need <script type="math/tex; mode=display">score_{Player\_1} &geq; score_{Player\_2}</script>. Or in other terms, <script type="math/tex; mode=display">score_{Player\_1} - score_{Player\_2} &geq; 0</script>. </p>
<p>Thus, for the turn of Player 1, we can add its score obtained to the total score and for Player 2's turn, we can substract its score from the total score. At the end, we can check if the total score is greater than or equal to zero(equal score of both players), to predict that Player 1 will be the winner.</p>
<p>Thus, by making use of a recursive function <code>winner(nums,s,e,turn)</code> which predicts the winner for the <script type="math/tex; mode=display">nums</script> array as the score array with the elements in the range of indices <script type="math/tex; mode=display">[s,e]</script> currently being considered, given a particular player's turn, indicated by <script type="math/tex; mode=display">turn=1</script> being Player 1's turn and <script type="math/tex; mode=display">turn=-1</script> being the Player 2's turn, we can predict the winner of the given problem by making the function call <code>winner(nums,0,n-1,1)</code>. Here, <script type="math/tex; mode=display">n</script> refers to the length of <script type="math/tex; mode=display">nums</script> array.</p>
<p>In every turn, we can either pick up the first(<script type="math/tex; mode=display">nums[s]</script>) or the last(<script type="math/tex; mode=display">nums[e]</script>) element of the current subarray. Since both the players are assumed to be playing smartly and making the best move at every step, both will tend to maximize their scores. Thus, we can make use of the same function <code>winner</code> to determine the maximum score possible for any of the players. </p>
<p>Now, at every step of the recursive process, we determine the maximum score possible for the current player. It will be the maximum one possible out of the scores obtained by picking the first or the last element of the current subarray. </p>
<p>To obtain the score possible from the remaining subarray, we can again make use of the same <code>winner</code> function and add the score corresponding to the point picked in the current function call. But, we need to take care of whether to add or subtract this score to the total score available. If it is Player 1's turn, we add the current number's score to the total score, otherwise, we need to subtract the same. </p>
<p>Thus, at every step, we need update the search space appropriately based on the element chosen and also invert the <script type="math/tex; mode=display">turn</script>'s value to indicate the turn change among the players and either add or subtract the current player's score from the total score available to determine the end result.</p>
<p>Further, note that the value returned at every step is given by <script type="math/tex; mode=display">turn *\text{max}(turn * a, turn * b)</script>. This is equivalent to the statement <script type="math/tex; mode=display">max(a,b)</script> for Player 1's turn and <script type="math/tex; mode=display">min(a,b)</script> for Player 2's turn. </p>
<p>This is done because, looking from Player 1's perspective, for any move made by Player 1, it tends to leave the remaining subarray in a situation which minimizes the best score possible for Player 2, even if it plays in the best possible manner. But, when the turn passes to Player 1 again, for Player 1 to win, the remaining subarray should be left in a state such that the score obtained from this subarrray is maximum(for Player 1). </p>
<p>This is a general criteria for any arbitrary two player game and is commonly known as the 
<a href="https://en.wikipedia.org/wiki/Minimax">Min-Max algorithm</a>.</p>
<p>The following image shows how the scores are passed to determine the end result for a simple example.</p>
<p align="center"><img alt="Recursive_Tree" src="../Figures/486/486_Predict_the_winner_new.PNG"></p>
<iframe src="https://leetcode.com/playground/3SDSCR7V/shared" frameborder="0" name="3SDSCR7V" width="100%" height="275"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^n)</script>. Size of recursion tree will be <script type="math/tex; mode=display">2^n</script>. Here, <script type="math/tex; mode=display">n</script> refers to the length of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-similar-approach-accepted">Approach #2 Similar Approach [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We can omit the use of <script type="math/tex; mode=display">turn</script> to keep a track of the player for the current turn. To do so, we can make use of a simple observation. If the current turn belongs to, say Player 1, we pick up an element, say <script type="math/tex; mode=display">x</script>, from either end, and give the turn to Player 2. Thus, if we obtain the score for the remaining elements(leaving <script type="math/tex; mode=display">x</script>), this score, now belongs to Player 2. Thus, since Player 2 is competing against Player 1, this score should be subtracted from Player 1's current(local) score(<script type="math/tex; mode=display">x</script>) to obtain the effective score of Player 1 at the current instant.</p>
<p>Similar argument holds true for Player 2's turn as well i.e. we can subtract Player 1's score for the remaining subarray from Player 2's current score to obtain its effective score. By making use of this observation, we can omit the use of <script type="math/tex; mode=display">turn</script> from <code>winner</code> to find the required result by making the slight change discussed above in the <code>winner</code>'s implementation.</p>
<p>While returning the result from <code>winner</code> for the current function call, we return the larger of the effective scores possible by choosing either the first or the last element from the currently available subarray. Rest of the process remains the same as the last approach.</p>
<p>Now, in order to remove the duplicate function calls, we can make use of a 2-D memoization array, <script type="math/tex; mode=display">memo</script>, such that we can store the result obtained for the function call <code>winner</code> for a subarray with starting and ending indices being <script type="math/tex; mode=display">s</script> and <script type="math/tex; mode=display">e</script> ] at <script type="math/tex; mode=display">memo[s][e]</script>. This helps to prune the search space to a great extent.</p>
<p>This approach is inspired by <a href="https://leetcode.com/chidong">@chidong</a></p>
<iframe src="https://leetcode.com/playground/RGPbqsDC/shared" frameborder="0" name="RGPbqsDC" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. The entire <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">n</script> is filled only once. Here, <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^2)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">n</script> is used for memoization.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming-accepted">Approach #3 Dynamic Programming [Accepted]:</h4>
<p><strong>Algorithm</strong></p>
<p>We can observe that the effective score for the current player for any given subarray <script type="math/tex; mode=display">nums[x:y]</script> only depends on the elements within the range <script type="math/tex; mode=display">[x,y]</script> in the array <script type="math/tex; mode=display">nums</script>. It mainly depends on whether the element <script type="math/tex; mode=display">nums[x]</script> or <script type="math/tex; mode=display">nums[y]</script> is chosen in the current turn and also on the maximum score possible for the other player from the remaining subarray left after choosing the current element. Thus, it is certain that the current effective score isn't dependent on the elements outside the range <script type="math/tex; mode=display">[x,y]</script>. </p>
<p>Based on the above observation, we can say that if know the maximum effective score possible for the subarray <script type="math/tex; mode=display">nums[x+1,y]</script> and <script type="math/tex; mode=display">nums[x,y-1]</script>, we can easily determine the maximum effective score possible for the subarray <script type="math/tex; mode=display">nums[x,y]</script> as <script type="math/tex; mode=display">\text{max}(nums[x]-score_{[x+1,y]}, nums[y]-score_{[x,y-1]})</script>. These equations are deduced based on the last approach. </p>
<p>From this,  we conclude that we can make use of Dynamic Programming to determine the required maximum effective score for the array <script type="math/tex; mode=display">nums</script>. We can make use of a 2-D <script type="math/tex; mode=display">dp</script> array, such that <script type="math/tex; mode=display">dp[i][j]</script> is used to store the maximum effective score possible for the subarray <script type="math/tex; mode=display">nums[i,j]</script>. The <script type="math/tex; mode=display">dp</script> updation equation becomes: </p>
<p>
<script type="math/tex; mode=display">dp[i,j] = nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]</script>.</p>
<p>We can fill in the <script type="math/tex; mode=display">dp</script> array starting from the last row. At the end, the value for <script type="math/tex; mode=display">dp[0][n-1]</script> gives the required result. Here, <script type="math/tex; mode=display">n</script> refers to the length of <script type="math/tex; mode=display">nums</script> array.</p>
<p>Look at the animation below to clearly understand the <script type="math/tex; mode=display">dp</script> filling process.</p>
<p>!?!../Documents/486_Predict_the_winner.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/EFGjsVXp/shared" frameborder="0" name="EFGjsVXp" width="100%" height="275"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. <script type="math/tex; mode=display">((n+1)</script>x<script type="math/tex; mode=display">n)/2</script> entries in <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">(n+1)</script>x<script type="math/tex; mode=display">n</script> is filled once. Here, <script type="math/tex; mode=display">n</script> refers to the length of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^2)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">(n+1)</script>x<script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-1-d-dynamic-programming-accepted">Approach #4 1-D Dynamic Programming [Accepted]:</h4>
<p><strong>Algorithm</strong></p>
<p>From the last approach, we see that the <script type="math/tex; mode=display">dp</script> updation equation is: </p>
<p>
<script type="math/tex; mode=display">dp[i,j] = nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]</script>. </p>
<p>Thus, for filling in any entry in <script type="math/tex; mode=display">dp</script> array, only the entries in the next row(same column) and the previous column(same row) are needed.</p>
<p>Instead of making use of a new row in <script type="math/tex; mode=display">dp</script> array for the current <script type="math/tex; mode=display">dp</script> row's updations, we can overwrite the values in the previous row itself and consider the values as belonging to the new row's entries, since the older values won't be needed ever in the future again. Thus, instead of making use of a 2-D <script type="math/tex; mode=display">dp</script> array, we can make use of a 1-D <script type="math/tex; mode=display">dp</script> array and make the updations appropriately.</p>
<iframe src="https://leetcode.com/playground/k9vrYN2X/shared" frameborder="0" name="k9vrYN2X" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. The elements of <script type="math/tex; mode=display">dp</script> array are updated <script type="math/tex; mode=display">1+2+3+...+n</script> times. Here, <script type="math/tex; mode=display">n</script> refers to the length of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. 1-D <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>