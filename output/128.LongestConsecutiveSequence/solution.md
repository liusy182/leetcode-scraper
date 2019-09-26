<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-sorting">Approach 2: Sorting</a></li>
<li><a href="#approach-3-hashset-and-intelligent-sequence-building">Approach 3: HashSet and Intelligent Sequence Building</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>Because a sequence could start at any number in <code>nums</code>, we can exhaust the
entire search space by building as long a sequence as possible from every
number.</p>
<p><strong>Algorithm</strong></p>
<p>The brute force algorithm does not do anything clever - it just considers
each number in <code>nums</code>, attempting to count as high as possible from that
number using only numbers in <code>nums</code>. After it counts too high (i.e.
<code>currentNum</code> refers to a number that <code>nums</code> does not contain), it records the
length of the sequence if it is larger than the current best. The algorithm
is necessarily optimal because it explores every possibility.</p>
<iframe src="https://leetcode.com/playground/puxLaX5E/shared" frameborder="0" width="100%" height="500" name="puxLaX5E"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>.</p>
<p>The outer loop runs exactly <script type="math/tex; mode=display">n</script> times, and because <code>currentNum</code>
increments by 1 during each iteration of the <code>while</code> loop, it runs in
<script type="math/tex; mode=display">O(n)</script> time. Then, on each iteration of the <code>while</code> loop, an <script type="math/tex; mode=display">O(n)</script>
lookup in the array is performed. Therefore, this brute force algorithm
is really three nested <script type="math/tex; mode=display">O(n)</script> loops, which compound multiplicatively to a
cubic runtime.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>The brute force algorithm only allocates a handful of integers, so it uses constant
additional space.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-2-sorting">Approach 2: Sorting</h4>
<p><strong>Intuition</strong></p>
<p>If we can iterate over the numbers in ascending order, then it will be
easy to find sequences of consecutive numbers. To do so, we can sort the
array.</p>
<p><strong>Algorithm</strong></p>
<p>Before we do anything, we check for the base case input of the empty array.
The longest sequence in an empty array is, of course, 0, so we can simply
return that. For all other cases, we sort <code>nums</code> and consider each number
after the first (because we need to compare each number to its previous
number). If the current number and the previous are equal, then our current
sequence is neither extended nor broken, so we simply move on to the next
number. If they are unequal, then we must check whether the current number
extends the sequence (i.e. <code>nums[i] == nums[i-1] + 1</code>). If it does, then we
add to our current count and continue. Otherwise, the sequence is broken, so
we record our current sequence and reset it to 1 (to include the number that
broke the sequence). It is possible that the last element of <code>nums</code> is part
of the longest sequence, so we return the maximum of the current sequence and
the longest one.</p>
<p align="center"><img alt="Sorting Example" src="../Figures/128/sorting.png"></p>
<p>Here, an example array is sorted before the linear scan identifies all consecutive sequences.
The longest sequence is colored in red.</p>
<iframe src="https://leetcode.com/playground/M9Rxw5qk/shared" frameborder="0" width="100%" height="497" name="M9Rxw5qk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(nlgn)</script>.</p>
<p>The main <code>for</code> loop does constant work <script type="math/tex; mode=display">n</script> times, so the algorithm's time
complexity is dominated by the invocation of <code>sort</code>, which will run in
<script type="math/tex; mode=display">O(nlgn)</script> time for any sensible implementation.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script> (or <script type="math/tex; mode=display">O(n)</script>).</p>
<p>For the implementations provided here, the space complexity is constant
because we sort the input array in place. If we are not allowed to modify
the input array, we must spend linear space to store a sorted copy.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-3-hashset-and-intelligent-sequence-building">Approach 3: HashSet and Intelligent Sequence Building</h4>
<p><strong>Intuition</strong></p>
<p>It turns out that our initial brute force solution was on the right track, but missing
a few optimizations necessary to reach <script type="math/tex; mode=display">O(n)</script> time complexity.</p>
<p><strong>Algorithm</strong></p>
<p>This optimized algorithm contains only two changes from the brute force
approach: the numbers are stored in a <code>HashSet</code> (or <code>Set</code>, in Python) to
allow <script type="math/tex; mode=display">O(1)</script> lookups, and we only attempt to build sequences from numbers
that are not already part of a longer sequence. This is accomplished by first
ensuring that the number that would immediately precede the current number in
a sequence is not present, as that number would necessarily be part of a
longer sequence.</p>
<iframe src="https://leetcode.com/playground/KbUGJ84k/shared" frameborder="0" width="100%" height="497" name="KbUGJ84k"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
<p>Although the time complexity appears to be quadratic due to the <code>while</code>
loop nested within the <code>for</code> loop, closer inspection reveals it to be
linear. Because the <code>while</code> loop is reached only when <code>currentNum</code> marks
the beginning of a sequence (i.e. <code>currentNum-1</code> is not present in
<code>nums</code>), the <code>while</code> loop can only run for <script type="math/tex; mode=display">n</script> iterations throughout the
entire runtime of the algorithm. This means that despite looking like
<script type="math/tex; mode=display">O(n \cdot n)</script> complexity, the nested loops actually run in <script type="math/tex; mode=display">O(n + n) = O(n)</script>
time. All other computations occur in constant time, so the overall
runtime is linear.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
<p>In order to set up <script type="math/tex; mode=display">O(1)</script> containment lookups, we allocate linear space
for a hash table to store the <script type="math/tex; mode=display">O(n)</script> numbers in <code>nums</code>. Other than that,
the space complexity is identical to that of the brute force solution.</p>
</li>
</ul>
          </div>
        
      </div>