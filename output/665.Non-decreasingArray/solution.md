<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-reduce-to-smaller-problem-accepted">Approach #2: Reduce to Smaller Problem [Accepted]</a></li>
<li><a href="#approach-3-locate-and-analyze-problem-index-accepted">Approach #3: Locate and Analyze Problem Index [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>For the given array <script type="math/tex; mode=display">\text{A}</script>, if we are changing at most one element <script type="math/tex; mode=display">\text{A[i]}</script>, we should change <script type="math/tex; mode=display">\text{A[i]}</script> to <script type="math/tex; mode=display">\text{A[i-1]}</script>, as it would be guaranteed that <script type="math/tex; mode=display">\text{A[i-1]} &leq; \text{A[i]}</script>, and <script type="math/tex; mode=display">\text{A[i]}</script> would be the smallest possible to try and achieve <script type="math/tex; mode=display">\text{A[i]} &leq; \text{A[i+1]}</script>.</p>
<p><strong>Algorithm</strong></p>
<p>For each possible change <script type="math/tex; mode=display">\text{A[i]}</script>, check if the sequence is monotone increasing.  We'll modify <script type="math/tex; mode=display">\text{new}</script>, a copy of the array <script type="math/tex; mode=display">\text{A}</script>.</p>
<iframe src="https://leetcode.com/playground/FK7JPfxR/shared" frameborder="0" name="FK7JPfxR" width="100%" height="343"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Let <script type="math/tex; mode=display">N</script> be the length of the given array.  For each element <script type="math/tex; mode=display">\text{A[i]}</script>, we check if some sequence is monotone increasing, which takes <script type="math/tex; mode=display">O(N)</script> steps.  In total, this is a complexity of <script type="math/tex; mode=display">O(N^2)</script>.</p>
</li>
<li>
<p>Space Complexity: To hold our array <script type="math/tex; mode=display">\text{new}</script>, we need <script type="math/tex; mode=display">O(N)</script> space.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-reduce-to-smaller-problem-accepted">Approach #2: Reduce to Smaller Problem [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If <script type="math/tex; mode=display">\text{A[0]} &leq; \text{A[1]} &leq; \text{A[2]}</script>, then we may remove <script type="math/tex; mode=display">\text{A[0]}</script> without changing the answer.  Similarly, if <script type="math/tex; mode=display">\text{A}\big[\text{len(A)-3}\big] &leq; \text{A}\big[\text{len(A)-2}\big] &leq; \text{A}\big[\text{len(A)-1}\big]</script>, we may remove <script type="math/tex; mode=display">\text{A[len(A)-1]}</script> without changing the answer.</p>
<p>If the problem is solvable, then after these removals, very few numbers will remain.</p>
<p><strong>Algorithm</strong></p>
<p>Consider the interval <script type="math/tex; mode=display">\text{[i, j]}</script> corresponding to the subarray <script type="math/tex; mode=display">\big[\text{A[i], A[i+1], ..., A[j]}\big]</script>.  When <script type="math/tex; mode=display">\text{A[i]} &leq; \text{A[i+1]} &leq; \text{A[i+2]}</script>, we know we do not need to modify <script type="math/tex; mode=display">\text{A[i]}</script>, and we can consider solving the problem on the interval <script type="math/tex; mode=display">\text{[i+1, j]}</script> instead.  We use a similar approach for <script type="math/tex; mode=display">j</script>.</p>
<p>Afterwards, with the length of the interval under consideration being <script type="math/tex; mode=display">\text{j - i + 1}</script>, if the interval has size 2 or less, then we did not find any problem.  </p>
<p>If our interval under consideration has 5 or more elements, then there are two disjoint problems that cannot be fixed with one replacement.  </p>
<p>Otherwise, our problem size is now at most 4 elements, which we can easily brute force.</p>
<iframe src="https://leetcode.com/playground/4ypTHUiy/shared" frameborder="0" name="4ypTHUiy" width="100%" height="343"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Let <script type="math/tex; mode=display">N</script> be the length of the given array.  Our pointers <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> move at most <script type="math/tex; mode=display">O(N)</script> times.  Our brute force is constant time as there are at most 4 elements in the array.  Hence, the complexity is <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity:  The extra array <script type="math/tex; mode=display">\text{A[i: j+1]}</script> only has at most 4 elements, so it is constant space, and so is the space used by our auxillary brute force algorithm.  In total, the space complexity is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-locate-and-analyze-problem-index-accepted">Approach #3: Locate and Analyze Problem Index [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Consider all indices <script type="math/tex; mode=display">p</script> for which <script type="math/tex; mode=display">\text{A[p]} > \text{A[p+1]}</script>.  If there are zero, the answer is <code>True</code>.  If there are 2 or more, the answer is <code>False</code>, as more than one element of the array must be changed for <script type="math/tex; mode=display">\text{A}</script> to be monotone increasing.</p>
<p>At the problem index <script type="math/tex; mode=display">p</script>, we only care about the surrounding elements.  Thus, immediately the problem is reduced to a very small size that can be analyzed by casework.</p>
<p><strong>Algorithm</strong></p>
<p>As before, let <script type="math/tex; mode=display">p</script> be the unique problem index for which <script type="math/tex; mode=display">\text{A[p]} > \text{A[p+1]}</script>.  If this is not unique or doesn't exist, the answer is <code>False</code> or <code>True</code> respectively.  We analyze the following cases:</p>
<ul>
<li>If <script type="math/tex; mode=display">\text{p = 0}</script>, then we could make the array good by setting <script type="math/tex; mode=display">\text{A[p] = A[p+1]}</script>.</li>
<li>If <script type="math/tex; mode=display">\text{p = len(A) - 2}</script>, then we could make the array good by setting <script type="math/tex; mode=display">\text{A[p+1] = A[p]}</script>.</li>
<li>Otherwise, <script type="math/tex; mode=display">\text{A[p-1], A[p], A[p+1], A[p+2]}</script> all exist, and:<ul>
<li>We could change <script type="math/tex; mode=display">\text{A[p]}</script> to be between <script type="math/tex; mode=display">\text{A[p-1]}</script> and <script type="math/tex; mode=display">\text{A[p+1]}</script> if possible, or;</li>
<li>We could change <script type="math/tex; mode=display">\text{A[p+1]}</script> to be between <script type="math/tex; mode=display">\text{A[p]}</script> and <script type="math/tex; mode=display">\text{A[p+2]}</script> if possible.</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/NGHYqESJ/shared" frameborder="0" name="NGHYqESJ" width="100%" height="241"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Let <script type="math/tex; mode=display">N</script> be the length of the given array.  We loop through the array once, so our time complexity is <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity:  We only use <script type="math/tex; mode=display">p</script> and <script type="math/tex; mode=display">i</script>, and the answer itself as the additional space.  The additional space complexity is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>