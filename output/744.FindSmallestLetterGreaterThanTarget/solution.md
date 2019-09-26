<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-record-letters-seen-accepted">Approach #1: Record Letters Seen [Accepted]</a></li>
<li><a href="#approach-2-linear-scan-accepted">Approach #2: Linear Scan [Accepted]</a></li>
<li><a href="#approach-3-binary-search-accepted">Approach #3: Binary Search [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-record-letters-seen-accepted">Approach #1: Record Letters Seen [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's scan through <code>letters</code> and record if we see a letter or not.  We could do this with an array of size 26, or with a Set structure.</p>
<p>Then, for every next letter (starting with the letter that is one greater than the target), let's check if we've seen it.  If we have, it must be the answer.</p>
<iframe src="https://leetcode.com/playground/auZQ7CwK/shared" frameborder="0" width="100%" height="276" name="auZQ7CwK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>letters</code>.  We scan every element of the array.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the maximum size of <code>seen</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-linear-scan-accepted">Approach #2: Linear Scan [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Since <code>letters</code> are sorted, if we see something larger when scanning form left to right, it must be the answer.  Otherwise, (since <code>letters</code> is non-empty), the answer is <code>letters[0]</code>.</p>
<iframe src="https://leetcode.com/playground/RvMYaXpq/shared" frameborder="0" width="100%" height="174" name="RvMYaXpq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>letters</code>.  We scan every element of the array.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, as we maintain only pointers.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-binary-search-accepted">Approach #3: Binary Search [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Like in <em>Approach #2</em>, we want to find something larger than target in a sorted array.  This is ideal for a <em>binary search</em>: Let's find the rightmost position to insert <code>target</code> into <code>letters</code> so that it remains sorted.</p>
<p>Our binary search (a typical one) proceeds in a number of rounds.  At each round, let's maintain the <em>loop invariant</em> that the answer must be in the interval <code>[lo, hi]</code>.  Let <code>mi = (lo + hi) / 2</code>.  If <code>letters[mi] &lt;= target</code>, then we must insert it in the interval <code>[mi + 1, hi]</code>.  Otherwise, we must insert it in the interval <code>[lo, mi]</code>.</p>
<p>At the end, if our insertion position says to insert <code>target</code> into the last position <code>letters.length</code>, we return <code>letters[0]</code> instead.  This is what the modulo operation does.</p>
<iframe src="https://leetcode.com/playground/bQDjgxiu/shared" frameborder="0" width="100%" height="242" name="bQDjgxiu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(\log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>letters</code>.  We peek only at <script type="math/tex; mode=display">\log N</script> elements in the array.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, as we maintain only pointers.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>