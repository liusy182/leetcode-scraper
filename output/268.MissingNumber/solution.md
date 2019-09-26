<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-sorting-accepted">Approach #1 Sorting [Accepted]</a></li>
<li><a href="#approach-2-hashset-accepted">Approach #2 HashSet [Accepted]</a></li>
<li><a href="#approach-3-bit-manipulation-accepted">Approach #3 Bit Manipulation [Accepted]</a></li>
<li><a href="#approach-4-gauss-formula-accepted">Approach #4 Gauss' Formula [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-sorting-accepted">Approach #1 Sorting [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If <code>nums</code> were in order, it would be easy to see which number is missing.</p>
<p><strong>Algorithm</strong></p>
<p>First, we sort <code>nums</code>. Then, we check the two special cases that can be
handled in constant time - ensuring that 0 is at the beginning and that <script type="math/tex; mode=display">n</script>
is at the end. Given that those assumptions hold, the missing number must
somewhere between (but not including) 0 and <script type="math/tex; mode=display">n</script>. To find it, we ensure that
the number we expect to be at each index is indeed there. Because we handled
the edge cases, this is simply the previous number plus 1. Thus, as soon as
we find an unexpected number, we can simply return the expected number.</p>
<iframe src="https://leetcode.com/playground/BpPhWC2o/shared" frameborder="0" width="100%" height="480" name="BpPhWC2o"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(nlgn)</script>
</p>
<p>The only elements of the algorithm that have asymptotically nonconstant
time complexity are the main <code>for</code> loop (which runs in <script type="math/tex; mode=display">\mathcal{O}(n)</script> time), and
the <code>sort</code> invocation (which runs in <script type="math/tex; mode=display">\mathcal{O}(nlgn)</script> time for Python and Java).
Therefore, the runtime is dominated by <code>sort</code>, and the entire runtime is
<script type="math/tex; mode=display">\mathcal{O}(nlgn)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(1)</script> (or <script type="math/tex; mode=display">\mathcal{O}(n)</script>)</p>
<p>In the sample code, we sorted <code>nums</code> in place, allowing us to avoid
allocating additional space. If modifying <code>nums</code> is forbidden, we can
allocate an <script type="math/tex; mode=display">\mathcal{O}(n)</script> size copy and sort that instead.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-hashset-accepted">Approach #2 HashSet [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>A brute force method for solving this problem would be to simply check for
the presence of each number that we expect to be present. The naive
implementation might use a linear scan of the array to check for containment,
but we can use a <code>HashSet</code> to get constant time containment queries and
overall linear runtime.</p>
<p><strong>Algorithm</strong></p>
<p>This algorithm is almost identical to the brute force approach, except we
first insert each element of <code>nums</code> into a set, allowing us to later query
for containment in <script type="math/tex; mode=display">\mathcal{O}(1)</script> time.</p>
<iframe src="https://leetcode.com/playground/UBNtYrmj/shared" frameborder="0" width="100%" height="293" name="UBNtYrmj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(n)</script>
</p>
<p>Because the set allows for <script type="math/tex; mode=display">\mathcal{O}(1)</script> containment queries, the main loop
runs in <script type="math/tex; mode=display">\mathcal{O}(n)</script> time. Creating <code>num_set</code> costs <script type="math/tex; mode=display">\mathcal{O}(n)</script> time, as each set insertion
runs in amortized <script type="math/tex; mode=display">\mathcal{O}(1)</script> time, so the overall runtime is <script type="math/tex; mode=display">\mathcal{O}(n + n) = \mathcal{O}(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(n)</script>
</p>
<p><code>nums</code> contains <script type="math/tex; mode=display">n-1</script> distinct elements, so it costs <script type="math/tex; mode=display">\mathcal{O}(n)</script> space to
store a set containing all of them.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-bit-manipulation-accepted">Approach #3 Bit Manipulation [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can harness the fact that XOR is its own inverse to find the missing
element in linear time.</p>
<p><strong>Algorithm</strong></p>
<p>Because we know that <code>nums</code> contains <script type="math/tex; mode=display">n</script> numbers and that it is missing
exactly one number on the range <script type="math/tex; mode=display">[0..n-1]</script>, we know that <script type="math/tex; mode=display">n</script> definitely
replaces the missing number in <code>nums</code>. Therefore, if we initialize an integer
to <script type="math/tex; mode=display">n</script> and XOR it with every index and value, we will be left with the
missing number. Consider the following example (the values have been sorted
for intuitive convenience, but need not be):</p>
<p></p><table>
  <tr>
    <th>Index</th>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <th>Value</th>
    <td>0</td>
    <td>1</td>
    <td>3</td>
    <td>4</td>
  </tr>
</table> 
<p>
<script type="math/tex; mode=display">
\begin{align}
    missing &= 4 \wedge (0 \wedge 0) \wedge (1 \wedge 1) \wedge (2 \wedge 3) \wedge (3 \wedge 4) \\
            &= (4 \wedge 4) \wedge (0 \wedge 0) \wedge (1 \wedge 1) \wedge (3 \wedge 3) \wedge 2 \\
            &= 0 \wedge 0 \wedge 0 \wedge 0 \wedge 2 \\ 
            &= 2
\end{align}
</script>
</p>
<iframe src="https://leetcode.com/playground/SFZgajWR/shared" frameborder="0" width="100%" height="208" name="SFZgajWR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(n)</script>
</p>
<p>Assuming that XOR is a constant-time operation, this algorithm does
constant work on <script type="math/tex; mode=display">n</script> iterations, so the runtime is overall linear.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(1)</script>
</p>
<p>This algorithm allocates only constant additional space.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-gauss-formula-accepted">Approach #4 Gauss' Formula [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>One of the most well-known stories in mathematics is of a young Gauss, forced
to find the sum of the first 100 natural numbers by a lazy teacher. Rather
than add the numbers by hand, he deduced a <a href="https://brilliant.org/wiki/sum-of-n-n2-or-n3/">closed-form
expression</a> for the sum, or so
the story goes. You can see the formula below:</p>
<p>
<script type="math/tex; mode=display">
    \sum_{i=0}^{n}i = \frac{n(n+1)}{2}
</script>
</p>
<p><strong>Algorithm</strong></p>
<p>We can compute the sum of <code>nums</code> in linear time, and by Gauss' formula, we
can compute the sum of the first <script type="math/tex; mode=display">n</script> natural numbers in constant time. Therefore,
the number that is missing is simply the result of Gauss' formula minus the sum of <code>nums</code>,
as <code>nums</code> consists of the first <script type="math/tex; mode=display">n</script> natural numbers minus some number.</p>
<iframe src="https://leetcode.com/playground/3NM3eQvx/shared" frameborder="0" width="100%" height="191" name="3NM3eQvx"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(n)</script>
</p>
<p>Although Gauss' formula can be computed in <script type="math/tex; mode=display">\mathcal{O}(1)</script> time, summing <code>nums</code>
costs us <script type="math/tex; mode=display">\mathcal{O}(n)</script> time, so the algorithm is overall linear. Because we have
no information about <em>which</em> number is missing, an adversary could always
design an input for which any algorithm that examines fewer than <script type="math/tex; mode=display">n</script>
numbers fails. Therefore, this solution is asymptotically optimal.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(1)</script>
</p>
<p>This approach only pushes a few integers around, so it has constant
memory usage.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/emptyset">@emptyset</a></p>
          </div>
        
      </div>