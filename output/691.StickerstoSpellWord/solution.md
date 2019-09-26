<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-optimized-exhaustive-search">Approach 1: Optimized Exhaustive Search</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
</ul>
</div>
<h4 id="approach-1-optimized-exhaustive-search">Approach 1: Optimized Exhaustive Search</h4>
<p><br></p>
<p><strong>Intuition</strong></p>
<p>A natural answer is to exhaustively search combinations of stickers.  Because the data is randomized, there are many heuristics available to us that will make this faster.</p>
<ul>
<li>
<p>For all stickers, we can ignore any letters that are not in the target word.</p>
</li>
<li>
<p>When our candidate answer won't be smaller than an answer we have already found, we can stop searching this path.</p>
</li>
<li>
<p>We should try to have our exhaustive search bound the answer as soon as possible, so the effect described in the above point happens more often.</p>
</li>
<li>
<p>When a sticker dominates another, we shouldn't include the dominated sticker in our sticker collection.  [Here, we say a sticker <code>A</code> dominates <code>B</code> if <code>A.count(letter) &gt;= B.count(letter)</code> for all letters.]</p>
</li>
</ul>
<p><br></p>
<p><strong>Algorithm</strong></p>
<p>Firstly, for each sticker, let's create a count of that sticker (a mapping <code>letter -&gt; sticker.count(letter)</code>) that does not consider letters not in the target word.  Let <code>A</code> be an array of these counts.  Also, let's create <code>t_count</code>, a count of our <code>target</code> word.</p>
<p>Secondly, let's remove dominated stickers.  Because dominance is a transitive relation, we only need to check if a sticker is not dominated by any other sticker once - the ones that aren't dominated are included in our collection.</p>
<p>We are now ready to begin our exhaustive search.  A call to <code>search(ans)</code> denotes that we want to decide the minimum number of stickers we can used in <code>A</code> to satisfy the target count <code>t_count</code>.  <code>ans</code> will store the currently formed answer, and <code>best</code> will store the current best answer.</p>
<p>If our current answer can't beat our current best answer, we should stop searching.  Also, if there are no stickers left and our target is satisfied, we should update our answer.</p>
<p>Otherwise, we want to know the maximum number of this sticker we can use.  For example, if this sticker is <code>'abb'</code> and our target is <code>'aaabbbbccccc'</code>, then we could use a maximum of 3 stickers.  This is the maximum of <code>math.ceil(target.count(letter) / sticker.count(letter))</code>, taken over all <code>letter</code>s in <code>sticker</code>.  Let's call this quantity <code>used</code>.</p>
<p>After, for the sticker we are currently considering, we try to use <code>used</code> of them, then <code>used - 1</code>, <code>used - 2</code> and so on.  The reason we do it in this order is so that we can arrive at a value for <code>best</code> more quickly, which will stop other branches of our exhaustive search from continuing.</p>
<p>The Python version of this solution showcases using <code>collections.Counter</code> as a way to simplify some code sections, whereas the Java solution sticks to arrays.</p>
<iframe src="https://leetcode.com/playground/KP3fS7G3/shared" frameborder="0" name="KP3fS7G3" width="100%" height="515"></iframe>

<p><br></p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Let <script type="math/tex; mode=display">N</script> be the number of stickers, and <script type="math/tex; mode=display">T</script> be the number of letters in the target word.  A bound for time complexity is <script type="math/tex; mode=display">O(N^{T+1} T^2)</script>: for each sticker, we'll have to try using it up to <script type="math/tex; mode=display">T+1</script> times, and updating our target count costs <script type="math/tex; mode=display">O(T)</script>, which we do up to <script type="math/tex; mode=display">T</script> times.  Alternatively, since the answer is bounded at <script type="math/tex; mode=display">T</script>, we can prove that we can only search up to <script type="math/tex; mode=display">\binom{N+T-1}{T-1}</script> times.  This would be <script type="math/tex; mode=display">O(\binom{N+T-1}{T-1} T^2)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N+T)</script>, to store <code>stickersCount</code>, <code>targetCount</code>, and handle the recursive callstack when calling <code>search</code>.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p><br></p>
<p><strong>Intuition</strong></p>
<p>Suppose we need <code>dp[state]</code> stickers to satisfy all <code>target[i]</code>'s for which the <code>i</code>-th bit of <code>state</code> is set.  We would like to know <code>dp[(1 &lt;&lt; len(target)) - 1]</code>.</p>
<p><br></p>
<p><strong>Algorithm</strong></p>
<p>For each <code>state</code>, let's work with it as <code>now</code> and look at what happens to it after applying a sticker.  For each letter in the sticker that can satisfy an unset bit of <code>state</code>, we set the bit (<code>now |= 1 &lt;&lt; i</code>).  At the end, we know <code>now</code> is the result of applying that sticker to <code>state</code>, and we update our <code>dp</code> appropriately.</p>
<p>When using Python, we will need some extra techniques from <em>Approach #1</em> to pass in time.</p>
<iframe src="https://leetcode.com/playground/JTZ2SYco/shared" frameborder="0" name="JTZ2SYco" width="100%" height="515"></iframe>

<p><br></p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(2^T * S * T)</script> where <script type="math/tex; mode=display">S</script> be the total number of letters in all stickers, and <script type="math/tex; mode=display">T</script> be the number of letters in the target word.  We can examine each loop carefully to arrive at this conclusion.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(2^T)</script>, the space used by <code>dp</code>.</p>
</li>
</ul>
<p><br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  <a href="https://leetcode.com/contest/leetcode-weekly-contest-53/ranking">Approach #2</a> inspired by <a href="https://leetcode.com/dreamoon">@dreamoon</a>.</p>
          </div>
        
      </div>