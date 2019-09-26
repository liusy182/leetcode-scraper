<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-better-brute-force-accepted">Approach #2 Better Brute Force [Accepted]</a></li>
<li><a href="#approach-3-backtracking-accepted">Approach #3 Backtracking [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>In the brute force method, we can find out all the arrays that can be formed using the numbers from 1 to N(by creating every possible permutation of the given elements). Then, we iterate over all the elements of every permutation generated and check for the required conditions of divisibility.</p>
<p>In order to generate all the possible pairings, we make use of a function <code>permute(nums, current_index)</code>. This function creates all the possible permutations of the elements of the given array.</p>
<p>To do so, <code>permute</code> takes the index of the current element <script type="math/tex; mode=display">current_index</script> as one of the arguments. Then, it swaps the current element with every other element in the array, lying towards its right, so as to generate a new ordering of the array elements. After the swapping has been done, it makes another call to permute but this time with the index of the next element in the array. While returning back, we reverse the swapping done in the current function call.</p>
<p>Thus, when we reach the end of the array, a new ordering of the array's elements is generated. The following animation depicts the process of generating the permutations.</p>
<p>!?!../Documents/561_Array.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/PqSksc2S/shared" frameborder="0" name="PqSksc2S" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n!)</script>. A total of <script type="math/tex; mode=display">n!</script> permutations will be generated for an array of length <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script>. <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force-accepted">Approach #2 Better Brute Force [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the brute force approach, we create the full array for every permutation and then check the array for the given divisibilty conditions. But this method can be optimized to a great extent. To do so, we can keep checking the elements while being added to the permutation array at every step for the divisibility condition and  can stop creating it any further as soon as we find out the element just added to the permutation violates the divisiblity condition. </p>
<iframe src="https://leetcode.com/playground/WQVaxmVy/shared" frameborder="0" name="WQVaxmVy" width="100%" height="513"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(k)</script>. <script type="math/tex; mode=display">k</script> refers to the number of valid permutations.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of recursion tree can go upto <script type="math/tex; mode=display">n</script>. Further, <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> is used, where, <script type="math/tex; mode=display">n</script> is the given number.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-backtracking-accepted">Approach #3 Backtracking [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>The idea behind this approach is simple. We try to create all the permutations of numbers from 1 to N. We can fix one number at a particular position and check for the divisibility criteria of that number at the particular position. But, we need to keep a track of the numbers which have already been considered earlier so that they aren't reconsidered while generating the permutations. If the current 
number doesn't satisfy the divisibility criteria, we can leave all the permutations that can be generated with that number at the particular position. This helps to prune the search space of the permutations to a great extent. We do so by trying to place each of the numbers at each position.</p>
<p>We make use of a visited array of size <script type="math/tex; mode=display">N</script>. Here, <script type="math/tex; mode=display">visited[i]</script> refers to the <script type="math/tex; mode=display">i^{th}</script> number being already placed/not placed in the array being formed till now(True indicates that the number has already been placed).</p>
<p>We make use of a <code>calculate</code> function, which puts all the numbers pending numbers from 1 to N(i.e. not placed till now in the array), indicated by a <script type="math/tex; mode=display">False</script> at the corresponding <script type="math/tex; mode=display">visited[i]</script> position, and tries to create all the permutations with those numbers starting from the <script type="math/tex; mode=display">pos</script> index onwards in the current array. While putting the <script type="math/tex; mode=display">pos^{th}</script> number, we check whether the <script type="math/tex; mode=display">i^{th}</script> number satisfies the divisibility criteria on the go i.e. we continue forward with creating the permutations with the number <script type="math/tex; mode=display">i</script> at the <script type="math/tex; mode=display">pos^{th}</script> position only if the number <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">pos</script> satisfy the given criteria. Otherwise, we continue with putting the next numbers at the same position and keep on generating the permutations.</p>
<p>Look at the animation below for a better understanding of the methodology:</p>
<p>!?!../Documents/526_Beautiful.json:1000,563!?!</p>
<p>Below code is inspired by <a href="https://leetcode.com/shawngao">@shawngao</a></p>
<iframe src="https://leetcode.com/playground/cBVwozT4/shared" frameborder="0" name="cBVwozT4" width="100%" height="377"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(k)</script>. <script type="math/tex; mode=display">k</script> refers to the number of valid permutations.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">visited</script> array of size <script type="math/tex; mode=display">n</script> is used. The depth of recursion tree will also go upto <script type="math/tex; mode=display">n</script>. Here, <script type="math/tex; mode=display">n</script> refers to the given integer <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>