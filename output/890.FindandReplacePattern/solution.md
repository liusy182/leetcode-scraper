<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-maps">Approach 1: Two Maps</a></li>
<li><a href="#approach-2-one-map">Approach 2: One Map</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-maps">Approach 1: Two Maps</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>If say, the first letter of the pattern is <code>"a"</code>, and the first letter of the word is <code>"x"</code>, then in the permutation, <code>"a"</code> must map to <code>"x"</code>.</p>
<p>We can write this bijection using two maps: a forward map <script type="math/tex; mode=display">\text{m1}</script> and a backwards map <script type="math/tex; mode=display">\text{m2}</script>.</p>
<p>
<script type="math/tex; mode=display">
\text{m1} : \text{"a"} \rightarrow \text{"x"}
</script>
<script type="math/tex; mode=display">
\text{m2} : \text{"x"} \rightarrow \text{"a"}
</script>
</p>
<p>Then, if there is a contradiction later, we can catch it via one of the two maps.  For example, if the <code>(word, pattern)</code> is <code>("aa", "xy")</code>, we will catch the mistake in <script type="math/tex; mode=display">\text{m1}</script> (namely, <script type="math/tex; mode=display">\text{m1}(\text{"a"}) = \text{"x"} = \text{"y"}</script>).  Similarly, with <code>(word, pattern) = ("ab", "xx")</code>, we will catch the mistake in <script type="math/tex; mode=display">\text{m2}</script>.</p>
<iframe src="https://leetcode.com/playground/9TL6xVWm/shared" frameborder="0" width="100%" height="480" name="9TL6xVWm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N * K)</script>, where <script type="math/tex; mode=display">N</script> is the number of words, and <script type="math/tex; mode=display">K</script> is the length of each word.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N * K)</script>, the space used by the answer.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-one-map">Approach 2: One Map</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in <em>Approach 1</em>, we can have some forward map <script type="math/tex; mode=display">\text{m1} : \mathbb{L} \rightarrow \mathbb{L}</script>, where <script type="math/tex; mode=display">\mathbb{L}</script> is the set of letters.  </p>
<p>However, instead of keeping track of the reverse map <script type="math/tex; mode=display">\text{m2}</script>, we could simply make sure that every value <script type="math/tex; mode=display">\text{m1}(x)</script> in the codomain is reached at most once.  This would guarantee the desired permutation exists.</p>
<p>So our algorithm is this: after defining <script type="math/tex; mode=display">\text{m1}(x)</script> in the same way as <em>Approach 1</em> (the forward map of the permutation), afterwards we make sure it reaches distinct values.</p>
<iframe src="https://leetcode.com/playground/3vbeWuoq/shared" frameborder="0" width="100%" height="497" name="3vbeWuoq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N * K)</script>, where <script type="math/tex; mode=display">N</script> is the number of words, and <script type="math/tex; mode=display">K</script> is the length of each word.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N * K)</script>, the space used by the answer.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>