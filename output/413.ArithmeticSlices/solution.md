<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</a></li>
<li><a href="#approach-2-better-brute-force-accepted">Approach #2 Better Brute Force [Accepted]</a></li>
<li><a href="#approach-3-using-recursion-accepted">Approach #3  Using Recursion [Accepted]</a></li>
<li><a href="#approach-5-dynamic-programming-accepted">Approach #5 Dynamic Programming [Accepted]:</a></li>
<li><a href="#approach-5-constant-space-dynamic-programming-accepted">Approach #5 Constant Space Dynamic Programming [Accepted]:</a></li>
<li><a href="#approach-6-using-formula-accepted">Approach #6 Using Formula [Accepted]:</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</h4>
<p>The most naive solution is to consider every pair of elements(with atleast 1 element between them), so that the range of elements lying between these two elements acts as a slice. Then, we can iterate over every such slice(range) to check if all the consecutive elements within this range have the same difference. For every such range found, we can increment the <script type="math/tex; mode=display">count</script> that is used to keep a track of the required result.</p>
<iframe src="https://leetcode.com/playground/HT3WjgGf/shared" frameborder="0" name="HT3WjgGf" width="100%" height="343"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>. We iterate over the range formed by every pair of elements. Here, <script type="math/tex; mode=display">n</script> refers to the number of elements in the given array <script type="math/tex; mode=display">A</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force-accepted">Approach #2 Better Brute Force [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we considered every possible range and then iterated over the range to check if the difference between every consercutive element in this range is the same. We can optimize this approach to some extent, by making a small observation. </p>
<p>We can see, that if we are currently considering the range bound by the elements, let's say, <script type="math/tex; mode=display">A[s]</script>(start) and <script type="math/tex; mode=display">A[e]</script>(end), we have checked the consecutive elements in this range to have the same difference. Now, when we move on to the next range between the indices <script type="math/tex; mode=display">s</script> and <script type="math/tex; mode=display">e+1</script>, we again perform a check on all the elements in the range <script type="math/tex; mode=display">s:e</script>, along with one additional pair <script type="math/tex; mode=display">A[e+1]</script> and <script type="math/tex; mode=display">A[e]</script>. We can remove this redundant check in the range <script type="math/tex; mode=display">s:e</script> and just check the last pair to have the same difference as the one used for the previous range(same <script type="math/tex; mode=display">s</script>, incremented <script type="math/tex; mode=display">e</script>).</p>
<p>Note that if the last range didn't constitute an arithmetic slice, the same elements will be a part of the updated range as well. Thus, we can omit the rest of the ranges consisting of the same starting index. The rest of the process remains the same as in the last approach.</p>
<iframe src="https://leetcode.com/playground/NPDEAgTz/shared" frameborder="0" name="NPDEAgTz" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Two for loops are used.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-recursion-accepted">Approach #3  Using Recursion [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>By making use of the observation discussed in the last approach, we know, that if a range of elements between the indices <script type="math/tex; mode=display">(i,j)</script> constitute an Arithmetic Slice, and another element <script type="math/tex; mode=display">A[j+1]</script> is included such that <script type="math/tex; mode=display">A[j+1]</script> and <script type="math/tex; mode=display">A[j]</script> have the same difference as that of the previous common difference, the ranges between <script type="math/tex; mode=display">(i,j+1)</script> will constitutes an arithmetic slice. Further, if the original range <script type="math/tex; mode=display">(i,j)</script> doesn't form an arithmetic slice, adding new elements to this range won't do us any good. Thus, no more arithmetic slices can be obtained by adding new elements to it.</p>
<p>By making use of this observation, we can develop a recursive solution for the given problem as well. Assume that a <script type="math/tex; mode=display">sum</script> variable is used to store the total number of arithmetic slices in the given array <script type="math/tex; mode=display">A</script>. We make use of a recursive function <code>slices(A,i)</code> which returns the number of Arithmetic Slices in the range <script type="math/tex; mode=display">(k,i)</script>, but which are not a part of any range <script type="math/tex; mode=display">(k,j)</script> such that <script type="math/tex; mode=display">j<i</script>. It also updates <script type="math/tex; mode=display">sum</script> with the number of arithmetic slices(total) in the current range. Thus, <script type="math/tex; mode=display">k</script> refers to  the minimum index such that the range <script type="math/tex; mode=display">(k,i)</script> constitutes a valid arithmetic slice.</p>
<p>Now, suppose we know the number of arithmetic slices in the range <script type="math/tex; mode=display">(0,i-1)</script> constituted by the elements <script type="math/tex; mode=display">[a_0,a_1,a_2,...a_(i-1)]</script>, to be say <script type="math/tex; mode=display">x</script>. If this range itself is an arithmetic slice, all the consecutive elements have the same difference(equal to say, <script type="math/tex; mode=display">a_(i-1)-a_(i-2)</script>). Now, adding a new element <script type="math/tex; mode=display">a_i</script> to it to extend the range to <script type="math/tex; mode=display">(0,i)</script> will constitute an arithmetic slice only if this new element satisfies <script type="math/tex; mode=display">a_i-a_(i-1)=a_(i-1)-a_(i-2)</script>. Thus, now, the addition of this new element, will lead to an addition of <script type="math/tex; mode=display">ap</script> number of arithmetic slices to the ones obtained in the range <script type="math/tex; mode=display">(0,i-1)</script>. The new arithmetic slices will be the ones constituting the ranges <script type="math/tex; mode=display">(0,i), (1,i), ... (i-2,i)</script>, which are a total of  <script type="math/tex; mode=display">x+1</script> additional arithmetic slices. This is because, apart from the range <script type="math/tex; mode=display">(0,i)</script> the rest of the ranges <script type="math/tex; mode=display">(1,i), (2,i),...(i-2,i)</script> can be mapped to <script type="math/tex; mode=display">(0,i-1), (1,i-1),...(i-3,i-1)</script>, with count equal to <script type="math/tex; mode=display">x</script>. </p>
<p>Thus, in every call to <code>slices</code>, if the <script type="math/tex; mode=display">i^{th}</script> element has the same common difference with the last element as the previous common difference, we can find the number of new arithmetic slices added by the use of this element, <script type="math/tex; mode=display">ap</script> and also update the <script type="math/tex; mode=display">sum</script> to include this <script type="math/tex; mode=display">ap</script> into it, apart from the count obtained by the smaller ranges. But, if the new element doesn't have the same common difference, extra arithmetic slices can't be contributed by it and hence, no addition is done to <script type="math/tex; mode=display">sum</script> for the current element. But, of course <script type="math/tex; mode=display">sum</script> will be updated as per the count obtained from the smaller ranges.</p>
<iframe src="https://leetcode.com/playground/WGzuREMw/shared" frameborder="0" name="WGzuREMw" width="100%" height="360"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The recursive function is called at most <script type="math/tex; mode=display">n-2</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree goes upto <script type="math/tex; mode=display">n-2</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-5-dynamic-programming-accepted">Approach #5 Dynamic Programming [Accepted]:</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we start with the full range <script type="math/tex; mode=display">(0,n-1)</script>, where <script type="math/tex; mode=display">n</script> is the number of elements in the given <script type="math/tex; mode=display">A</script> array. We can observe that the result for the range <script type="math/tex; mode=display">(0,i)</script> only depends on the elements in the range <script type="math/tex; mode=display">(0,i)</script> and not on any element beyond this range. Thus, we can make use of Dynamic Programming to solve the given problem.</p>
<p>We can make use of a 1-D <script type="math/tex; mode=display">dp</script> with number of elements equal to <script type="math/tex; mode=display">n</script>. <script type="math/tex; mode=display">dp[i]</script> is used to store the number of arithmetic slices possible in the range <script type="math/tex; mode=display">(k,i)</script> and not in any range <script type="math/tex; mode=display">(k,j)</script> such that <script type="math/tex; mode=display">j<i</script>. Again, <script type="math/tex; mode=display">k</script> refers to the minimum index possible such that <script type="math/tex; mode=display">(k,j)</script> constitutes a valid Arithmetic Slice.</p>
<p>Instead of going in the reverse order as in the recursive approach, we can start filling the <script type="math/tex; mode=display">dp</script> in a forward manner. The intuition remains the same as in the last approach. For the <script type="math/tex; mode=display">i^{th}</script> element being considered, we check if this element satsfies the common difference criteria with the previous element. If so, we know the number of new arithmetic slices added will be <script type="math/tex; mode=display">1+dp[i-1]</script> as discussed in the last approach. The <script type="math/tex; mode=display">sum</script> is also updated by the same count to reflect the new arithmetic slices added.  </p>
<p>The following animation illustrates the <script type="math/tex; mode=display">dp</script> filling process.</p>
<p>!?!../Documents/413_Arithmetic_Slices.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/w8UZ2q6u/shared" frameborder="0" name="w8UZ2q6u" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We traverse over the given <script type="math/tex; mode=display">A</script> array with <script type="math/tex; mode=display">n</script> elements once only.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. 1-D <script type="math/tex; mode=display">dp</script> of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-5-constant-space-dynamic-programming-accepted">Approach #5 Constant Space Dynamic Programming [Accepted]:</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we can observe that we only require the element <script type="math/tex; mode=display">dp[i-1]</script> to determine the value to be entered at <script type="math/tex; mode=display">dp[i]</script>. Thus, instead of making use of a 1-D array to store the required data, we can simply keep a track of just the last element. </p>
<iframe src="https://leetcode.com/playground/mGEcWWi3/shared" frameborder="0" name="mGEcWWi3" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We traverse over the given <script type="math/tex; mode=display">A</script> array with <script type="math/tex; mode=display">n</script> elements once only.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-6-using-formula-accepted">Approach #6 Using Formula [Accepted]:</h4>
<p><strong>Algorithm</strong></p>
<p>From the <script type="math/tex; mode=display">dp</script> solution, we can observe that for <script type="math/tex; mode=display">k</script> consecutive elements sastisfying the common difference criteria, we update the <script type="math/tex; mode=display">sum</script> for each such element by <script type="math/tex; mode=display">1, 2, 3, ..., k</script> counts in that order. Thus, instead of updating the <script type="math/tex; mode=display">sum</script> at the same time, we can just keep a track of the number of consecutive elements satisfying the common differnce criteria in a <script type="math/tex; mode=display">count</script> variable and just update the <script type="math/tex; mode=display">sum</script> directly as <script type="math/tex; mode=display">count*(count+1)/2</script> whenver an element not satisfying this criteria is found. At the same time, we also need to reset the <script type="math/tex; mode=display">count</script> value. </p>
<iframe src="https://leetcode.com/playground/fQULWrDF/shared" frameborder="0" name="fQULWrDF" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We iterate over <script type="math/tex; mode=display">A</script> with <script type="math/tex; mode=display">n</script> elements exactly once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>