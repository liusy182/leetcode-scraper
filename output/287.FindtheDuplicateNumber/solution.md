<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#note">Note</a></li>
<li><a href="#proof">Proof</a></li>
<li><a href="#approach-1-sorting-accepted">Approach #1 Sorting [Accepted]</a></li>
<li><a href="#approach-2-set-accepted">Approach #2 Set [Accepted]</a></li>
<li><a href="#approach-3-floyds-tortoise-and-hare-cycle-detection-accepted">Approach #3 Floyd's Tortoise and Hare (Cycle Detection) [Accepted]</a></li>
</ul>
</div>
<h4 id="note">Note</h4>
<p>The first two approaches mentioned do not satisfy the constraints given in
the prompt, but they are solutions that you might be likely to come up with
during a technical interview. As an interviewer, I personally would <em>not</em>
expect someone to come up with the cycle detection solution unless they have
heard it before.</p>
<h4 id="proof">Proof</h4>
<p>Proving that at least one duplicate must exist in <code>nums</code> is simple
application of the
<a href="https://en.wikipedia.org/wiki/Pigeonhole_principle">pigeonhole principle</a>.
Here, each number in <code>nums</code> is a "pigeon" and each distinct number that can
appear in <code>nums</code> is a "pigeonhole". Because there are <script type="math/tex; mode=display">n+1</script> numbers are
<script type="math/tex; mode=display">n</script> distinct possible numbers, the pigeonhole principle implies that at
least one of the numbers is duplicated.</p>
<h4 id="approach-1-sorting-accepted">Approach #1 Sorting [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If the numbers are sorted, then any duplicate numbers will be adjacent in the
sorted array.</p>
<p><strong>Algorithm</strong></p>
<p>Given the intuition, the algorithm follows fairly simply. First, we sort the
array, and then we compare each element to the previous element. Because
there is exactly one duplicated element in the array, we know that the array
is of at least length 2, and we can return the duplicate element as soon as
we find it.</p>
<iframe src="https://leetcode.com/playground/bQGYqfgj/shared" frameborder="0" width="100%" height="259" name="bQGYqfgj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(nlgn)</script>
</p>
<p>The <code>sort</code> invocation costs <script type="math/tex; mode=display">O(nlgn)</script> time in Python and Java, so it
dominates the subsequent linear scan.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script> (or <script type="math/tex; mode=display">O(n)</script>)</p>
<p>Here, we sort <code>nums</code> in place, so the memory footprint is constant. If we
cannot modify the input array, then we must allocate linear space for a
copy of <code>nums</code> and sort that instead.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-set-accepted">Approach #2 Set [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If we store each element as we iterate over the array, we can simply check
each element as we iterate over the array.</p>
<p><strong>Algorithm</strong></p>
<p>In order to achieve linear time complexity, we need to be able to insert
elements into a data structure (and look them up) in constant time. A <code>Set</code>
satisfies these constraints nicely, so we iterate over the array and insert
each element into <code>seen</code>. Before inserting it, we check whether it is already
there. If it is, then we found our duplicate, so we return it.</p>
<iframe src="https://leetcode.com/playground/jP4YUkB7/shared" frameborder="0" width="100%" height="276" name="jP4YUkB7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p><code>Set</code> in both Python and Java rely on underlying hash tables, so
insertion and lookup have amortized constant time complexities. The
algorithm is therefore linear, as it consists of a <code>for</code> loop that
performs constant work <script type="math/tex; mode=display">n</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>In the worst case, the duplicate element appears twice, with one of its
appearances at array index <script type="math/tex; mode=display">n-1</script>. In this case, <code>seen</code> will contain
<script type="math/tex; mode=display">n-1</script> distinct values, and will therefore occupy <script type="math/tex; mode=display">O(n)</script> space.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-floyds-tortoise-and-hare-cycle-detection-accepted">Approach #3 Floyd's Tortoise and Hare (Cycle Detection) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If we interpret <code>nums</code> such that for each pair of index <script type="math/tex; mode=display">i</script> and value
<script type="math/tex; mode=display">v_i</script>, the "next" value <script type="math/tex; mode=display">v_j</script> is at index <script type="math/tex; mode=display">v_i</script>, we can reduce this
problem to cycle detection. See the solution to
<a href="https://leetcode.com/problems/linked-list-cycle-ii/solution/">Linked List Cycle II</a>
for more details.</p>
<p><strong>Algorithm</strong></p>
<p>First off, we can easily show that the constraints of the problem imply that
a cycle <em>must</em> exist. Because each number in <code>nums</code> is between <script type="math/tex; mode=display">1</script> and
<script type="math/tex; mode=display">n</script>, it will necessarily point to an index that exists. Therefore, the list
can be traversed infinitely, which implies that there is a cycle.
Additionally, because <script type="math/tex; mode=display">0</script> cannot appear as a value in <code>nums</code>, <code>nums[0]</code>
cannot be part of the cycle. Therefore, traversing the array in this manner
from <code>nums[0]</code> is equivalent to traversing a cyclic linked list. Given this,
the problem can be solved just like
<a href="https://leetcode.com/problems/linked-list-cycle-ii/">Linked List Cycle II</a>.</p>
<p>To see the algorithm in action, check out the animation below:</p>
<p>!?!../Documents/287_Find_the_Duplicate_Number.json:1280,720!?!</p>
<iframe src="https://leetcode.com/playground/RMBz6AQR/shared" frameborder="0" width="100%" height="412" name="RMBz6AQR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>For detailed analysis, refer to 
<a href="https://leetcode.com/problems/linked-list-cycle-ii/solution/#approach-2-floyds-tortoise-and-hare-accepted">Linked List Cycle II</a>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>
</p>
<p>For detailed analysis, refer to 
<a href="https://leetcode.com/problems/linked-list-cycle-ii/solution/#approach-2-floyds-tortoise-and-hare-accepted">Linked List Cycle II</a>.</p>
</li>
</ul>
<hr>
<p>Analysis and solutions written by: <a href="https://leetcode.com/emptyset">@emptyset</a></p>
          </div>
        
      </div>