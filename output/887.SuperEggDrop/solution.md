<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming-with-binary-search">Approach 1: Dynamic Programming with Binary Search</a></li>
<li><a href="#approach-2-dynamic-programming-with-optimality-criterion">Approach 2: Dynamic Programming with Optimality Criterion</a></li>
<li><a href="#approach-3-mathematical">Approach 3: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming-with-binary-search">Approach 1: Dynamic Programming with Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>It's natural to attempt dynamic programming, as we encounter similar subproblems.  Our state is <code>(K, N)</code>: <code>K</code> eggs and <code>N</code> floors left.  When we drop an egg from floor <code>X</code>, it either survives and we have state <code>(K, N-X)</code>, or it breaks and we have state <code>(K-1, X-1)</code>.</p>
<p>This approach would lead to a <script type="math/tex; mode=display">O(K N^2)</script> algorithm, but this is not efficient enough for the given constraints.  However, we can try to speed it up.  Let <code>dp(K, N)</code> be the maximum number of moves needed to solve the problem in state <code>(K, N)</code>.  Then, by our reasoning above, we have:</p>
<p>
<script type="math/tex; mode=display">
\text{dp}(K, N) = \min\limits_{1 \leq X \leq N} \Big( \max(\text{dp}(K-1, X-1), \text{dp}(K, N-X)) \Big)
</script>
</p>
<p>Now for the key insight:  Because <script type="math/tex; mode=display">\text{dp}(K, N)</script> is a function that is increasing on <script type="math/tex; mode=display">N</script>, the first term <script type="math/tex; mode=display">\mathcal{T_1} = \text{dp}(K-1, X-1)</script> in our <script type="math/tex; mode=display">\max</script> expression is an increasing function on <script type="math/tex; mode=display">X</script>, and the second term <script type="math/tex; mode=display">\mathcal{T_2} = \text{dp}(K, N-X)</script> is a decreasing function on <script type="math/tex; mode=display">X</script>.  This means that we do not need to check every <script type="math/tex; mode=display">X</script> to find the minimum -- instead, we can binary search for the best <script type="math/tex; mode=display">X</script>.</p>
<p><strong>Algorithm</strong></p>
<p align="center">
    <img src="../Figures/891/sketch.png" alt="T1, T2 diagram" style="height: 300px;">
</p>

<p>Continuing our discussion, if <script type="math/tex; mode=display">\mathcal{T_1} < \mathcal{T_2}</script>, then the <script type="math/tex; mode=display">X</script> value chosen is too small; and if <script type="math/tex; mode=display">\mathcal{T_1} > \mathcal{T_2}</script>, then <script type="math/tex; mode=display">X</script> is too big.  However, this argument is not quite correct: when there are only two possible values of <script type="math/tex; mode=display">X</script>, we need to check both.</p>
<p>Using the above fact, we can use a binary search to find the correct value of <script type="math/tex; mode=display">X</script> more efficiently than checking all <script type="math/tex; mode=display">N</script> of them.</p>
<iframe src="https://leetcode.com/playground/4RDYQYDJ/shared" frameborder="0" width="100%" height="500" name="4RDYQYDJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(K * N \log N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(K * N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-with-optimality-criterion">Approach 2: Dynamic Programming with Optimality Criterion</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach 1</em>, we try to speed up our <script type="math/tex; mode=display">O(K N^2)</script> algorithm.  Again, for a state of <script type="math/tex; mode=display">K</script> eggs and <script type="math/tex; mode=display">N</script> floors, where <script type="math/tex; mode=display">\text{dp}(K, N)</script> is the answer for that state, we have:</p>
<p>
<script type="math/tex; mode=display">
\text{dp}(K, N) = \min\limits_{1 \leq X \leq N} \Big( \max(\text{dp}(K-1, X-1), \text{dp}(K, N-X)) \Big)
</script>
</p>
<p>Now, suppose <script type="math/tex; mode=display">X_{\emptyset} = \text{opt}(K, N)</script> is the smallest <script type="math/tex; mode=display">X</script> for which that minimum is attained: that is, the smallest value for which</p>
<p>
<script type="math/tex; mode=display">
\text{dp}(K, N) = \Big( \max(\text{dp}(K-1, X_{\emptyset}-1), \text{dp}(K, N-X_{\emptyset})) \Big)
</script>
</p>
<p>The key insight that we will develop below, is that <script type="math/tex; mode=display">\text{opt}(K, N)</script> is an increasing function in <script type="math/tex; mode=display">N</script>.</p>
<p align="center">
    <img src="../Figures/891/sketch2.png" alt="T1, T2 diagram" style="height: 300px;">
</p>

<p>The first term of our <script type="math/tex; mode=display">\max</script> expression, <script type="math/tex; mode=display">\mathcal{T_1} = \text{dp}(K-1, X-1)</script>, is increasing with respect to <script type="math/tex; mode=display">X</script>, but constant with respect to <script type="math/tex; mode=display">N</script>.  The second term, <script type="math/tex; mode=display">\mathcal{T_2} = \text{dp}(K, N-X)</script>, is decreasing with respect to <script type="math/tex; mode=display">X</script>, but increasing with respect to <script type="math/tex; mode=display">N</script>.</p>
<p>This means that as <script type="math/tex; mode=display">N</script> increases, the intersection point <script type="math/tex; mode=display">X_{\emptyset} = \text{opt}(K, N)</script> of these two lines is increasing, as we can see in the diagram.</p>
<p><strong>Algorithm</strong></p>
<p>Perform "bottom up" dynamic programming based on the recurrence below, keeping track of <script type="math/tex; mode=display">X_{\emptyset} = \text{opt}(K, N)</script>.  Again:</p>
<p>
<script type="math/tex; mode=display">
\text{dp}(K, N) = \min\limits_{1 \leq X \leq N} \Big( \max(\text{dp}(K-1, X-1), \text{dp}(K, N-X)) \Big)
</script>
</p>
<p>When we want to find <script type="math/tex; mode=display">\text{dp}(K, N+1)</script>, instead of searching for <script type="math/tex; mode=display">X</script> from <script type="math/tex; mode=display">1 \leq X \leq N</script>, we only have to search through <script type="math/tex; mode=display">X_{\emptyset} \leq X \leq N</script>.</p>
<p>Actually, (as illustrated by the diagram,) if ever the next <script type="math/tex; mode=display">X+1</script> is worse than the current <script type="math/tex; mode=display">X</script>, then we've searched too far, and we know our current <script type="math/tex; mode=display">X</script> is best for this <script type="math/tex; mode=display">N</script>.</p>
<iframe src="https://leetcode.com/playground/w346npK6/shared" frameborder="0" width="100%" height="500" name="w346npK6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(K * N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-mathematical">Approach 3: Mathematical</h4>
<p><strong>Intuition</strong></p>
<p>Let's ask the question in reverse: given <script type="math/tex; mode=display">T</script> moves (and <script type="math/tex; mode=display">K</script> eggs), what is the most number of floors <script type="math/tex; mode=display">f(T, K)</script> that we can still "solve" (find <script type="math/tex; mode=display">0 \leq F \leq f(T, K)</script> with certainty)?  Then, the problem is to find the least <script type="math/tex; mode=display">T</script> for which <script type="math/tex; mode=display">f(T, K) \geq N</script>.  Because more tries is always at least as good, <script type="math/tex; mode=display">f</script> is increasing on <script type="math/tex; mode=display">T</script>, which means we could binary search for the answer.</p>
<p>Now, we find a similar recurrence for <script type="math/tex; mode=display">f</script> as in the other approaches.  If in an optimal strategy we drop the egg from floor <script type="math/tex; mode=display">X_{\emptyset}</script>, then either it breaks and we can solve <script type="math/tex; mode=display">f(T-1, K-1)</script> lower floors (floors <script type="math/tex; mode=display">< X_{\emptyset}</script>); or it doesn't break and we can solve <script type="math/tex; mode=display">f(T-1, K)</script> higher floors (floors <script type="math/tex; mode=display">\geq X_{\emptyset}</script>).  In total,</p>
<p>
<script type="math/tex; mode=display">
f(T, K) = 1 + f(T-1, K-1) + f(T-1, K)
</script>
</p>
<p>Also, it is easily seen that <script type="math/tex; mode=display">f(t, 1) = t</script> when <script type="math/tex; mode=display">t \geq 1</script>, and <script type="math/tex; mode=display">f(1, k) = 1</script> when <script type="math/tex; mode=display">k \geq 1</script>.</p>
<p align="center">
    <img src="../Figures/891/sketch3.png" alt="T1, T2 diagram" style="height: 300px;">
</p>

<p>From here, we don't need to solve the recurrence mathematically - we could simply use it to generate all <script type="math/tex; mode=display">O(K * \max(T))</script> possible values of <script type="math/tex; mode=display">f(T, K)</script>.</p>
<p>However, there is a mathematical solution to this recurrence.  If <script type="math/tex; mode=display">g(t, k) = f(t, k) - f(t, k-1)</script>, [the difference between the <script type="math/tex; mode=display">k-1</script>th and <script type="math/tex; mode=display">k</script>th term,] then subtracting the two equations:</p>
<p>
<script type="math/tex; mode=display">
f(T, K) = 1 + f(T-1, K-1) + f(T-1, K)
</script>
</p>
<p>
<script type="math/tex; mode=display">
f(T, K-1) = 1 + f(T-1, K-2) + f(T-1, K-1)
</script>
</p>
<p>we get:</p>
<p>
<script type="math/tex; mode=display">
g(t, k) = g(t-1, k) + g(t-1, k-1)
</script>
</p>
<p>This is a binomial recurrence with solution <script type="math/tex; mode=display">g(t, k) = \binom{t}{k+1}</script>, so that indeed,</p>
<p>
<script type="math/tex; mode=display">
f(t, k) = \sum\limits_{1 \leq x \leq K} g(t, x) = \sum \binom{t}{x}
</script>
</p>
<p><strong>Alternative Mathematical Derivation</strong></p>
<p>Alternatively, when we have <script type="math/tex; mode=display">t</script> tries and <script type="math/tex; mode=display">K</script> eggs, the result of our <script type="math/tex; mode=display">t</script> throws must be a <script type="math/tex; mode=display">t</script>-length sequence of successful and failed throws, with at most K failed throws.  The number of sequences with <script type="math/tex; mode=display">0</script> failed throws is <script type="math/tex; mode=display">\binom{t}{0}</script>, the number of sequences with <script type="math/tex; mode=display">1</script> failed throw is <script type="math/tex; mode=display">\binom{t}{1}</script> etc., so that the number of such sequences is <script type="math/tex; mode=display">\sum\limits_{0 \leq x \leq K} \binom{t}{x}</script>.</p>
<p>Hence, we can only distinguish at most these many floors in <script type="math/tex; mode=display">t</script> tries (as each sequence can only map to 1 answer per sequence.)  This process includes distinguishing <script type="math/tex; mode=display">F = 0</script>, so that the corresponding value of <script type="math/tex; mode=display">N</script> is one less than this sum.</p>
<p>However, this is also a lower bound for the number of floors that can be distinguished, as the result of a throw on floor <script type="math/tex; mode=display">X</script> will bound the answer to be either at most <script type="math/tex; mode=display">X</script> or greater than <script type="math/tex; mode=display">X</script>.  Hence, in an optimal throwing strategy, each such sequence actually maps to a unique answer.</p>
<p><strong>Algorithm</strong></p>
<p>Recapping our algorithm, we have the increasing [wrt <script type="math/tex; mode=display">t</script>] function <script type="math/tex; mode=display">f(t, K) = \sum\limits_{1 \leq x \leq K} \binom{t}{x}</script>, and we want the least <script type="math/tex; mode=display">t</script> so that <script type="math/tex; mode=display">f(t, K) \geq N</script>.  We binary search for the correct <script type="math/tex; mode=display">t</script>.</p>
<p>To evaluate <script type="math/tex; mode=display">f(t, K)</script> quickly, we can transform the previous binomial coefficient to the next (in the summand) by the formula <script type="math/tex; mode=display">\binom{n}{k} * \frac{n-k}{k+1} = \binom{n}{k+1}</script>.</p>
<iframe src="https://leetcode.com/playground/FXFk48xy/shared" frameborder="0" width="100%" height="480" name="FXFk48xy"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(K * \log N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>