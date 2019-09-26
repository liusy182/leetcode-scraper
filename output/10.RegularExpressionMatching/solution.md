<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>If there were no Kleene stars (the <code>*</code> wildcard character for regular expressions), the problem would be easier - we simply check from left to right if each character of the text matches the pattern.</p>
<p>When a star is present, we may need to check many different suffixes of the text and see if they match the rest of the pattern.  A recursive solution is a straightforward way to represent this relationship.</p>
<p><strong>Algorithm</strong></p>
<p>Without a Kleene star, our solution would look like this:</p>
<iframe src="https://leetcode.com/playground/Z2XSmAHG/shared" frameborder="0" width="100%" height="123" name="Z2XSmAHG"></iframe>

<p>If a star is present in the pattern, it will be in the second position <script type="math/tex; mode=display">\text{pattern[1]}</script>.  Then, we may ignore this part of the pattern, or delete a matching character in the text.  If we have a match on the remaining strings after any of these operations, then the initial inputs matched.</p>
<iframe src="https://leetcode.com/playground/EX8cYcs3/shared" frameborder="0" width="100%" height="293" name="EX8cYcs3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Let <script type="math/tex; mode=display">T, P</script> be the lengths of the text and the pattern respectively.  In the worst case, a call to <code>match(text[i:], pattern[2j:])</code> will be made <script type="math/tex; mode=display">\binom{i+j}{i}</script> times, and strings of the order <script type="math/tex; mode=display">O(T - i)</script> and <script type="math/tex; mode=display">O(P - 2*j)</script> will be made.  Thus, the complexity has the order <script type="math/tex; mode=display">\sum_{i = 0}^T \sum_{j = 0}^{P/2} \binom{i+j}{i} O(T+P-i-2j)</script>.  With some effort outside the scope of this article, we can show this is bounded by <script type="math/tex; mode=display">O\big((T+P)2^{T + \frac{P}{2}}\big)</script>.</p>
</li>
<li>
<p>Space Complexity:  For every call to <code>match</code>, we will create those strings as described above, possibly creating duplicates.  If memory is not freed, this will also take a total of <script type="math/tex; mode=display">O\big((T+P)2^{T + \frac{P}{2}}\big)</script> space, even though there are only order <script type="math/tex; mode=display">O(T^2 + P^2)</script> unique suffixes of <script type="math/tex; mode=display">P</script> and  <script type="math/tex; mode=display">T</script> that are actually required.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>As the problem has an <strong>optimal substructure</strong>, it is natural to cache intermediate results.  We ask the question <script type="math/tex; mode=display">\text{dp(i, j)}</script>: does <script type="math/tex; mode=display">\text{text[i:]}</script> and <script type="math/tex; mode=display">\text{pattern[j:]}</script> match?  We can describe our answer in terms of answers to questions involving smaller strings.</p>
<p><strong>Algorithm</strong></p>
<p>We proceed with the same recursion as in <a href="#approach-1-recursion">Approach 1</a>, except because calls will only ever be made to <code>match(text[i:], pattern[j:])</code>, we use <script type="math/tex; mode=display">\text{dp(i, j)}</script> to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.</p>
<p><em>Top-Down Variation</em>
<iframe src="https://leetcode.com/playground/Fpg6LXEX/shared" frameborder="0" width="100%" height="500" name="Fpg6LXEX"></iframe></p>
<p><em>Bottom-Up Variation</em></p>
<iframe src="https://leetcode.com/playground/dmAyPDG3/shared" frameborder="0" width="100%" height="395" name="dmAyPDG3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Let <script type="math/tex; mode=display">T, P</script> be the lengths of the text and the pattern respectively.  The work for every call to <code>dp(i, j)</code> for <script type="math/tex; mode=display">i=0, ... ,T</script>; <script type="math/tex; mode=display">j=0, ... ,P</script> is done once, and it is <script type="math/tex; mode=display">O(1)</script> work.  Hence, the time complexity is <script type="math/tex; mode=display">O(TP)</script>.</p>
</li>
<li>
<p>Space Complexity:  The only memory we use is the <script type="math/tex; mode=display">O(TP)</script> boolean entries in our cache.  Hence, the space complexity is <script type="math/tex; mode=display">O(TP)</script>.</p>
</li>
</ul>
          </div>
        
      </div>