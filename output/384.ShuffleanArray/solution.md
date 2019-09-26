<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#initial-thoughts">Initial Thoughts</a></li>
<li><a href="#approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</a></li>
<li><a href="#approach-2-fisher-yates-algorithm-accepted">Approach #2 Fisher-Yates Algorithm [Accepted]</a></li>
</ul>
</div>
<h4 id="initial-thoughts">Initial Thoughts</h4>
<p>Normally I would display more than two approaches, but shuffling is
deceptively easy to do <em>almost</em> properly, and the Fisher-Yates algorithm is
both the canonical solution and asymptotically optimal.</p>
<p>A few notes on randomness are necessary before beginning - both approaches
displayed below assume that the languages' pseudorandom number generators
(PRNGs) are sufficiently random. The sample code uses the simplest techniques
available for getting pseudorandom numbers, but for each possible permutation
of the array to be truly equally likely, more care must be taken. For
example, an array of length <script type="math/tex; mode=display">n</script> has <script type="math/tex; mode=display">n!</script> distinct permutations. Therefore, in
order to encode all permutations in an integer space, <script type="math/tex; mode=display">\lceil lg(n!)\rceil</script>
bits are necessary, which may not be guaranteed by the default PRNG.</p>
<h4 id="approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If we put each number in a "hat" and draw them out at random, the order in
which we draw them will define a random ordering.</p>
<p><strong>Algorithm</strong></p>
<p>The brute force algorithm essentially puts each number in the aforementioned
"hat", and draws them at random (without replacement) until there are none
left. Mechanically, this is performed by copying the contents of <code>array</code> into
a second auxiliary array named <code>aux</code> before overwriting each element of
<code>array</code> with a randomly selected one from <code>aux</code>. After selecting each random
element, it is removed from <code>aux</code> to prevent duplicate draws. The
implementation of <code>reset</code> is simple, as we just store the original state of
<code>nums</code> on construction.</p>
<p>The correctness of the algorithm follows from the fact that an element
(without loss of generality) is equally likely to be selected during all
iterations of the <code>for</code> loop. To prove this, observe that the probability of a
particular element <script type="math/tex; mode=display">e</script> being chosen on the <script type="math/tex; mode=display">k</script>th iteration (indexed from 0)
is simply <script type="math/tex; mode=display">P(e</script> being chosen during the <script type="math/tex; mode=display">k</script>th iteration<script type="math/tex; mode=display">)\cdot P(e</script> not being
chosen before the <script type="math/tex; mode=display">k</script>th iteration<script type="math/tex; mode=display">)</script>. Given that the array to be shuffled has
<script type="math/tex; mode=display">n</script> elements, this probability is more concretely stated as the following:</p>
<p>
<script type="math/tex; mode=display">
   \frac{1}{n-k} \cdot \prod_{i=1}^{k} \frac{n-i}{n-i+1}
</script>
</p>
<p>When expanded (and rearranged), it looks like this (for sufficiently large
<script type="math/tex; mode=display">k</script>):</p>
<p>
<script type="math/tex; mode=display">
   (\frac{n-1}{n}
   \cdot \frac{n-2}{n-1}
   \cdot (\ldots)
   \cdot \frac{n-k+1}{n-k+2}
   \cdot \frac{n-k}{n-k+1})
   \cdot \frac{1}{n-k}
</script>
</p>
<p>For the base case (<script type="math/tex; mode=display">k = 0</script>), it is trivial to see that
<script type="math/tex; mode=display">\frac{1}{n-k} = \frac{1}{n}</script>. For <script type="math/tex; mode=display">k > 0</script>, the numerator of each fraction
can be cancelled with the denominator of the next, leaving the <script type="math/tex; mode=display">n</script> from the
0th draw as the only uncancelled denominator. Therefore, no matter on which
draw an element is drawn, it is drawn with a <script type="math/tex; mode=display">\frac{1}{n}</script> chance, so each
array permutation is equally likely to arise.</p>
<iframe src="https://leetcode.com/playground/FWMsaXQ7/shared" frameborder="0" width="100%" height="500" name="FWMsaXQ7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>
</p>
<p>The quadratic time complexity arises from the calls to <code>list.remove</code> (or
<code>list.pop</code>), which run in linear time. <script type="math/tex; mode=display">n</script> linear list removals occur,
which results in a fairly easy quadratic analysis.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>Because the problem also asks us to implement <code>reset</code>, we must use linear
additional space to store the original array. Otherwise, it would be lost
upon the first call to <code>shuffle</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-fisher-yates-algorithm-accepted">Approach #2 Fisher-Yates Algorithm [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can cut down the time and space complexities of <code>shuffle</code> with a bit of
cleverness - namely, by swapping elements around within the array itself, we
can avoid the linear space cost of the auxiliary array and the linear time
cost of list modification.</p>
<p><strong>Algorithm</strong></p>
<p>The Fisher-Yates algorithm is remarkably similar to the brute force solution.
On each iteration of the algorithm, we generate a random integer between the
current index and the last index of the array. Then, we swap the elements at
the current index and the chosen index - this simulates drawing (and
removing) the element from the hat, as the next range from which we select a
random index will not include the most recently processed one. One small, yet important
detail is that it is possible to swap an element with itself - otherwise, some
array permutations would be more likely than others. To see this illustrated more
clearly, consider the animation below:</p>
<p>!?!../Documents/384_Shuffle_an_Array.json:697,161!?!</p>
<iframe src="https://leetcode.com/playground/ftmztsv8/shared" frameborder="0" width="100%" height="500" name="ftmztsv8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>The Fisher-Yates algorithm runs in linear time, as generating a random
index and swapping two values can be done in constant time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>Although we managed to avoid using linear space on the auxiliary array
from the brute force approach, we still need it for <code>reset</code>, so we're
stuck with linear space complexity.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/emptyset">@emptyset</a></p>
          </div>
        
      </div>