<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-meet-in-the-middle-accepted">Approach #1: Meet in the Middle [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-meet-in-the-middle-accepted">Approach #1: Meet in the Middle [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>First, let's get a sense of the condition that <code>average(B) = average(C)</code>, where <code>B, C</code> are defined in the problem statement.</p>
<p>Say <code>A</code> (the input array) has <code>N</code> elements which sum to <code>S</code>, and <code>B</code> (one of the splitting sets) has <code>K</code> elements which sum to <code>X</code>.  Then the equation for <code>average(B) = average(C)</code> becomes <script type="math/tex; mode=display">\frac{X}{K} = \frac{S-X}{N-K}</script>.  This reduces to <script type="math/tex; mode=display">X(N-K) = (S-X)K</script> which is <script type="math/tex; mode=display">\frac{X}{K} = \frac{S}{N}</script>.  That is, <code>average(B) = average(A)</code>.</p>
<p>Now, we could delete <code>average(A)</code> from each element <code>A[i]</code> without changing our choice for <code>B</code>.  (<code>A[i] -= mu</code>, where <code>mu = average(A)</code>).  This means we just want to choose a set <code>B</code> that sums to <code>0</code>.</p>
<p>Trying all <script type="math/tex; mode=display">2^N</script> sets is still too many choices, so we will create sets of sums <code>left, right</code> of the approximately <script type="math/tex; mode=display">2^{N/2}</script> choices on the left and on the right separately.  (That is, <code>left</code> is a set of sums of every powerset in the first half of A, and <code>right</code> is the set of sums of every powerset in the second half of A).  Then, it is true if we find <script type="math/tex; mode=display">0</script> in these powersets, or if two sums in different halves cancel out (<code>-x in right for x in left</code>), except for one minor detail below.</p>
<p>Care must be taken that we do not specify sets that would make the original <code>B</code> or <code>C</code> empty.  If <code>sleft = A[0] + A[1] + ... + A[N/2 - 1]</code>, and <code>sright = A[N/2] + ... + A[N-1]</code>, (where <code>A[i]</code> was transformed to the new <code>A[i] - average(A)</code>) then we cannot choose both (<code>sleft, sright</code>).  This is correct because if for example <code>sleft</code> was a sum reached by a strictly smaller powerset than <code>{A[0], A[1], ..., A[N/2 - 1]}</code>, then the difference between these sets would be non-empty and have sum <code>0</code>.</p>
<iframe src="https://leetcode.com/playground/MCygqyNn/shared" frameborder="0" width="100%" height="500" name="MCygqyNn"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^{N/2})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(2^{N/2})</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>