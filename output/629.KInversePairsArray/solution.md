<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-using-recursion-with-memoization">Approach 2: Using Recursion with Memoization</a></li>
<li><a href="#approach-3-dynamic-programming">Approach 3: Dynamic Programming</a></li>
<li><a href="#approach-4-dynamic-programming-with-cumulative-sum">Approach 4: Dynamic Programming with Cumulative Sum</a></li>
<li><a href="#approach-5-another-optimized-dynamic-programming-approach">Approach 5: Another Optimized Dynamic Programming Approach</a></li>
<li><a href="#approach-6-once-again-memoization">Approach 6: Once Again Memoization</a></li>
<li><a href="#approach-7-1-d-dynamic-programmming">Approach 7: 1-D Dynamic Programmming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>The most naive solution is to generate every permutation of the array consisting of numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>. Then, we can find out the number of inverse pairs in every array to determine if it is equal to 1. We can find out the count of permutations with the required number of inverse pairs. But, this solution is very terrible in terms of time complexity. Thus, we move on to the better approaches directly.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(n! \cdot n \log n\big)</script>. A total of <script type="math/tex; mode=display">n!</script> permutations will be generated. We need <script type="math/tex; mode=display">O\big(n \log n\big)</script> time to find the number of inverse pairs in every such permutation, by making use of merge sort. Here, <script type="math/tex; mode=display">n</script> refers to the given integer <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Each array generated during the permutations will require <script type="math/tex; mode=display">n</script> space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-recursion-with-memoization">Approach 2: Using Recursion with Memoization</h4>
<p>Before we discuss the solution, let's look at the idea behind it. Let's say, <script type="math/tex; mode=display">n</script> represents the given number defining the upper limit of the elements in the arrays being considered and <script type="math/tex; mode=display">k</script> represents the number of inverse pairs in the current array.</p>
<p>Let's start with a simple example with <script type="math/tex; mode=display">n=4</script>, no <script type="math/tex; mode=display">k</script> is defined right now. Now, for <script type="math/tex; mode=display">k=0</script>, the only possible arrangement for the given array <script type="math/tex; mode=display">a_0</script> will be <code>[1,2,3,4]</code>, since all the greater elements lie after the smaller elements. Now, in order to generate an arrangement with any arbitrary <script type="math/tex; mode=display">k</script> value, we need to shift, an arbitrary number of elements(let's say <script type="math/tex; mode=display">x</script> elements) in the array <script type="math/tex; mode=display">a_0</script> towards the left, with each displacement(shift) being <script type="math/tex; mode=display">s_1, s_2, ...., s_x</script>, such that the sum of these shifts equals <script type="math/tex; mode=display">k</script>.</p>
<p>To see what we mean by the above statement, let's look at the case for <code>[1,2,4,3]</code>. The number of inverse pairs in this array is 1. This array is obtained by shifting the number 4 by one position towards the left. </p>
<p>Similarly, consider the case for <code>[2,4,1,3]</code>. This array can be obtained from <script type="math/tex; mode=display">a_0</script> by shifting 2 by one position towards the left first and then shifting 4 by 2 positions towards the left. Thus, the total number of displacements is 3, which is equal to the number of inverse pairs in the new array. </p>
<p>This rule of displacements holds true because, whenever a number is shifted <script type="math/tex; mode=display">y</script> times towards the left starting from the array <script type="math/tex; mode=display">a_0</script>, after the shift, <script type="math/tex; mode=display">y</script> numbers smaller than it lie towards its right, giving a total of <script type="math/tex; mode=display">y</script> inverse pairs. </p>
<p>Now, let's say, we start with the one of the arrangements <script type="math/tex; mode=display">a_3</script>
<code>[2,4,1,3]</code>, with <script type="math/tex; mode=display">k=3</script>. Now, if we want to add a new number 5 to this array to consider an array with <script type="math/tex; mode=display">n=5</script>, let's say, initially, we append it to the end of <script type="math/tex; mode=display">a_3</script>. Now, the new array will be <code>[2,4,1,3,5]</code>. Since, the largest number is added at the end, the new number 5 doesn't add any new inverse pair to the total set of inverse pairs relative to the ones in <script type="math/tex; mode=display">a_3</script>(3). </p>
<p>Now, all the numbers in <script type="math/tex; mode=display">a_3</script> are smaller than 5. Thus, if we add 5 at a position <script type="math/tex; mode=display">y</script> steps from the right, <script type="math/tex; mode=display">y</script> smaller numbers will lie towards its right. Thus, a total of <script type="math/tex; mode=display">y</script> inverse pairs will exist with 5 being one of the elements in these pairs. </p>
<p>Thus, adding 5 at <script type="math/tex; mode=display">y</script> steps from the right adds a total of <script type="math/tex; mode=display">y</script> inverse pairs to the total set of inverse pairs in <script type="math/tex; mode=display">a_3</script> giving a total of <script type="math/tex; mode=display">3+y</script> inverse pairs now.</p>
<p>Looking at the same statement from another point of view, we can say that, if we know the number of inverse pairs(say <script type="math/tex; mode=display">x</script>) in any arbitrary array <script type="math/tex; mode=display">b</script> with some <script type="math/tex; mode=display">n</script>, we can add a new element <script type="math/tex; mode=display">n+1</script> to this array <script type="math/tex; mode=display">b</script> at a position <script type="math/tex; mode=display">p</script> steps from the right, such that <script type="math/tex; mode=display">x+p=k</script> to generate an array with a total of <script type="math/tex; mode=display">k</script> inverse pairs. </p>
<p>Extending this idea further, suppose we know the number of arrangements of an array with <script type="math/tex; mode=display">n-1</script> elements, with the number of inverse pairs being <script type="math/tex; mode=display">0, 1, 2,..., k</script>, let's say being equal to <script type="math/tex; mode=display">count_0, count_1, count_2,.., count_k</script>. Now, we can determine the number of arrangements of an array with <script type="math/tex; mode=display">n</script> elements with exactly <script type="math/tex; mode=display">k</script> inverse pairs easily. </p>
<p>To generate the arrangements with exactly <script type="math/tex; mode=display">k</script> inverse pairs and <script type="math/tex; mode=display">n</script> elements, we can add the new number <script type="math/tex; mode=display">n</script> to all the arrangements with <script type="math/tex; mode=display">k</script> inverse pairs at the last position. For the arrangements with <script type="math/tex; mode=display">k-1</script> inverse pairs , we can add <script type="math/tex; mode=display">n</script> at a position 1 step from the right. </p>
<p>Similarly, for an element with <script type="math/tex; mode=display">k-i</script> number of inverse pairs, we can add this new number <script type="math/tex; mode=display">n</script> at a position <script type="math/tex; mode=display">i</script> steps from the right. Each of these updations to the arrays leads to a new arrangement, each with the number of inverse pairs being equal to <script type="math/tex; mode=display">k</script>. </p>
<p>The following image shows an example of how this is done for n=5 and k=4:</p>
<p align="center"><img alt="Inversions" src="../Figures/629/629_kinverse.PNG"></p>
<p>Thus, to obtain the number of arrangements with exactly <script type="math/tex; mode=display">k</script> inverse pairs and <script type="math/tex; mode=display">n</script> numbers will be given by <script type="math/tex; mode=display">count_0 + count_1 + ... + count_k</script>.</p>
<p>From the above discussion, we can obtain the recursive formula for finding the number of arrangements with exactly <script type="math/tex; mode=display">k</script> inverse pairs as follows. Let's say <script type="math/tex; mode=display">count(i,j)</script> represents the number of arrangements with <script type="math/tex; mode=display">i</script> elements and exactly <script type="math/tex; mode=display">j</script> inverse pairs.</p>
<ol>
<li>
<p>If <script type="math/tex; mode=display">n=0</script>, no inverse pairs exist. Thus, <script type="math/tex; mode=display">count(0,k)=0</script>.</p>
</li>
<li>
<p>If <script type="math/tex; mode=display">k=0</script>, only one arrangement is possible, which is all numbers sorted in ascending order. Thus, <script type="math/tex; mode=display">count(n,0)=1</script>.</p>
</li>
<li>
<p>Otherwise, <script type="math/tex; mode=display">count(n,k) = \sum_{i=0}^{min(k,n-1)} count(n-1, k-i)</script>. </p>
</li>
</ol>
<p>Note that the upper limit on the summation is <script type="math/tex; mode=display">\text{min}(k,n-1)</script>. This is because for <script type="math/tex; mode=display">i>k</script>, <script type="math/tex; mode=display">k-i<0</script>. No arrangement exists with negative number of inverse pairs. The reason for the other factor can be seen as follows. </p>
<p>To generate a new arrangement adding <script type="math/tex; mode=display">k-i</script> new inverse pairs after adding the <script type="math/tex; mode=display">n^{th}</script> number, we need to add this number at the <script type="math/tex; mode=display">i^{th}</script> position from the right. For an array with size <script type="math/tex; mode=display">n</script>, only <script type="math/tex; mode=display">n-1</script> maximum shifts are possible.</p>
<p>We need to take the modulus at every step to keep the answer within integral limits.</p>
<p>We can see that a lot of duplicate function calls are made in the normal recursive solution. We can remove this redundancy by making use of a memoization array which stores the result for any function call <code>kInversePairs(i,j)</code> in <script type="math/tex; mode=display">memo[i][j]</script>. Thus, whenver a duplicate function call is made again, we can return the result directly from this memoization array. This prunes the search space to a great extent.</p>
<iframe src="https://leetcode.com/playground/yuGJPYGb/shared" frameborder="0" width="100%" height="327" name="yuGJPYGb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2*k)</script>. The function <code>kInversePairs</code> is called <script type="math/tex; mode=display">n^2</script> times to fill the <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">k</script>. Each function call itself takes <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">memo</script> array of constant size <script type="math/tex; mode=display">1001</script>x<script type="math/tex; mode=display">1001</script> is used. The depth of recursion tree can go upto <script type="math/tex; mode=display">n</script>. 
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming">Approach 3: Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>As we've seen in the discussion above, the solution for if we know the solutions for <script type="math/tex; mode=display">count(n-1,0)</script>, <script type="math/tex; mode=display">count(n-1, 1)</script>..., <script type="math/tex; mode=display">count(n-1,k)</script>, we can directly obtain the solution for <script type="math/tex; mode=display">count(n,k)</script> as <script type="math/tex; mode=display">count(n,k)=\sum_{0}^{min(k,n-1)} count(n-1, k-i)</script>.</p>
<p>From this, we deduce that we can make use of Dynamic Programming to solve the given problem. To solve the given problem, we make use of a 2-D <script type="math/tex; mode=display">dp</script>, where <script type="math/tex; mode=display">dp[i][j]</script> is used to store the number of arrangements with <script type="math/tex; mode=display">i</script> elements and exactly <script type="math/tex; mode=display">j</script> inverse pairs. Based on the discussions above, the <script type="math/tex; mode=display">dp</script> updation equations become:</p>
<ol>
<li>
<p>If <script type="math/tex; mode=display">n=0</script>, no inverse pairs exist. Thus, <script type="math/tex; mode=display">dp[0][k]=0</script>.</p>
</li>
<li>
<p>If <script type="math/tex; mode=display">k=0</script>, only one arrangement is possible, which is all numbers sorted in ascending order. Thus, <script type="math/tex; mode=display">dp[n][0]=1</script>.</p>
</li>
<li>
<p>Otherwise, <script type="math/tex; mode=display">dp[i,j] = \sum_{p=0}^{min(j,i-1)} count(i-1, j-p)</script>.</p>
</li>
</ol>
<p>Again, the limit <script type="math/tex; mode=display">\text{min}(j, i-1)</script> is used to account for the cases where the number of inverse pairs needed becomes negative(<script type="math/tex; mode=display">p>j</script>) or the case where the new inverse pairs needed by adding the <script type="math/tex; mode=display">n^{th}</script> number is more than <script type="math/tex; mode=display">n-1</script> which isn't possible, since the new number can be added at <script type="math/tex; mode=display">(n-1)^{th}</script> position at most from the right.</p>
<p>We start filling the <script type="math/tex; mode=display">dp</script> in a row-wise order starting from the first row. At the end, the value of <script type="math/tex; mode=display">dp[n][k]</script> gives the required result.</p>
<p>The following animation shows how the <script type="math/tex; mode=display">dp</script> is filled for n=4 and k=5:</p>
<p>!?!../Documents/629_dp4.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/jc3NbwaZ/shared" frameborder="0" width="100%" height="327" name="jc3NbwaZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2*k)</script>. <script type="math/tex; mode=display">dp</script> of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">k</script> is filled once. Filling each <script type="math/tex; mode=display">dp</script> entry takes <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n*k)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">k</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-dynamic-programming-with-cumulative-sum">Approach 4: Dynamic Programming with Cumulative Sum</h4>
<p><strong>Algorithm</strong></p>
<p>From the last approach, we've observed that we need to traverse back to some limit in the previous row of the <script type="math/tex; mode=display">dp</script> array to fill in the current <script type="math/tex; mode=display">dp</script> entry. Instead of doing this traversal to find the sum of the required elements, we can ease the process if we fill the cumulative sum upto the current element in a row in any <script type="math/tex; mode=display">dp</script> entry, instead of the actual value. </p>
<p>Thus, now, <script type="math/tex; mode=display">dp[i][j]=count(i,j)+\sum_{k=0}^{j-1} dp[i][k]</script>. Here, <script type="math/tex; mode=display">count(i,j)</script> refers to the number of arrangements with <script type="math/tex; mode=display">i</script> elements and exactly <script type="math/tex; mode=display">j</script> inverse pairs. Thus, each entry contains the sum of all the previous elements in the same row along with its own result.</p>
<p>Now, we need to determine the value of <script type="math/tex; mode=display">count(i,j)</script> to be added to the sum of previous elements in a row, in order to update the <script type="math/tex; mode=display">dp[i][j]</script> entry. But, we need not traverse back in the previous row , since it contains entries representing the cumulative sums now.
Thus, to obtain the sum of elements from <script type="math/tex; mode=display">dp[i-1][j-i+1]</script>  to <script type="math/tex; mode=display">dp[i-1][j]</script>(including both), we can directly use <script type="math/tex; mode=display">dp[i-1][j] - dp[i-1][j-i]</script>. </p>
<p>Now, to reflect the condition <script type="math/tex; mode=display">\text{min}(j, i-1)</script> used in the previous approaches, we can note that, we need to take the sum of only <script type="math/tex; mode=display">i</script> elements in the previous row, if <script type="math/tex; mode=display">i</script> elements exist till we reach the end of the array while traversing backwards. Otherwise, we simply take the sum of all the elements. </p>
<p>Only <script type="math/tex; mode=display">i</script> elements are considered because for generating <script type="math/tex; mode=display">j</script> new inverse pairs, by adding <script type="math/tex; mode=display">i</script> as the new number at the <script type="math/tex; mode=display">j^{th}</script> position, <script type="math/tex; mode=display">j</script> could reach only upto <script type="math/tex; mode=display">i-1</script>, as discussed in the last approaches as well. Thus, we need to consider the sum of elements from <script type="math/tex; mode=display">dp[i-1][j-(i-1)]</script> to  <script type="math/tex; mode=display">dp[i-1][j]</script>(including both) using <script type="math/tex; mode=display">dp[i-1][j] - dp[i-1][j-i]</script> if <script type="math/tex; mode=display">j-i &geq; 0</script>.</p>
<p>Otherwise, we add all the elements of the previous row upto the current column <script type="math/tex; mode=display">j</script> being considered. In other words, we can use <script type="math/tex; mode=display">dp[i-1][j]</script> directly as the required sum.</p>
<p>At the end, while returning the result, we need to return <script type="math/tex; mode=display">dp[n][k]-dp[n][k-1]</script> to obtain the required result from the cumulative sums. </p>
<p>The following animation illustrates the process of filling the <script type="math/tex; mode=display">dp</script> array.</p>
<p>!?!../Documents/629_dp5.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/GDndaXt6/shared" frameborder="0" width="100%" height="344" name="GDndaXt6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n*k)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">k</script> is filled once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n*k)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">k</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-another-optimized-dynamic-programming-approach">Approach 5: Another Optimized Dynamic Programming Approach</h4>
<p><strong>Algorithm</strong></p>
<p>Another way to use the Dynamic Programming Approach could be if we can somehow directly store the required <script type="math/tex; mode=display">count(i,j)</script> in <script type="math/tex; mode=display">dp[i][j]</script> entry, but still we should not need to traverse back in the previous row to find the sum of the required elements. </p>
<p>To do so, we can note that for the <script type="math/tex; mode=display">i^{th}</script> row, we need to add the elements from <script type="math/tex; mode=display">dp[i-1][j-i+1]</script> to <script type="math/tex; mode=display">dp[i-1][j]</script>(including both) if <script type="math/tex; mode=display">(j-1) > 0</script>. Otherwise, we need to add all the elements from <script type="math/tex; mode=display">dp[i-1][0]</script> to <script type="math/tex; mode=display">dp[i-1][j]</script>. This has already been discussed previously. </p>
<p>Now, when we go for filling in <script type="math/tex; mode=display">dp[i][j+1]</script> after filling <script type="math/tex; mode=display">dp[i][j]</script>, we know <script type="math/tex; mode=display">dp[i][j]</script> already corresponds to the sum of the elements from <script type="math/tex; mode=display">dp[i-1][j-i+1]</script> to <script type="math/tex; mode=display">dp[i-1][j]</script>. But, for filling <script type="math/tex; mode=display">dp[i][j+1]</script>, we require the sum of the elements from <script type="math/tex; mode=display">dp[i-1][(j-i+1)+1]</script> to <script type="math/tex; mode=display">dp[i-1][j+1]</script>. </p>
<p>We can observe that this sum only excludes <script type="math/tex; mode=display">dp[i-1][j-i+1]</script> from the previous sum(<script type="math/tex; mode=display">dp[i][j]</script>) and requires addition of only one new element(<script type="math/tex; mode=display">dp[i-1][j+1]</script>) to the to this sum. If the value <script type="math/tex; mode=display">j-i+1<0</script>, we need not remove any value.</p>
<p>Thus, we can directly obtain <script type="math/tex; mode=display">dp[i][j]</script> value as <script type="math/tex; mode=display">dp[i][j] = dp[i-1][j] - dp[i-1][j-i] + dp[i-1][j]</script>, if <script type="math/tex; mode=display">j-i &geq; 0</script>. Otherwise, we can use:  <script type="math/tex; mode=display">dp[i][j] = dp[i-1][j] + dp[i-1][j]</script>. </p>
<p>We can also note that, since, here <script type="math/tex; mode=display">j</script> represents the number of inverse pairs that need to be currently considered, we can place another upper limit on <script type="math/tex; mode=display">j</script> as well. The maximum number of inverse pairs for any arbitrary <script type="math/tex; mode=display">n</script> occur only when the array is sorted in descending order leading to <code>[n,n-1,....,3,2,1]</code> as the arrangement. </p>
<p>This arrangement has a total of <script type="math/tex; mode=display">n*(n-1)/2</script> inverse pairs. Thus, for an array with <script type="math/tex; mode=display">i</script> as the number of elements, the maximum number of inverse pairs possible is <script type="math/tex; mode=display">i*(i-1)/2</script> only. Thus, for fillling in the <script type="math/tex; mode=display">i^{th}</script> row of <script type="math/tex; mode=display">dp</script>, we can place this limit on <script type="math/tex; mode=display">j</script>'s value.</p>
<p>The following animation shows the <script type="math/tex; mode=display">dp</script> filling process.</p>
<p>!?!../Documents/629_dp6.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/XK2QkFyb/shared" frameborder="0" width="100%" height="395" name="XK2QkFyb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n*k)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">(n+1)</script>x<script type="math/tex; mode=display">(k+1)</script> is filled once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n*k)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">(n+1)</script>x<script type="math/tex; mode=display">(k+1)</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-6-once-again-memoization">Approach 6: Once Again Memoization</h4>
<p><strong>Algorithm</strong></p>
<p>The Dynamic Programming solution discussed in Approach 5 can also be written down in the form of a recursive solution. But, again, that will include a lot of duplicate function calls. Thus, a better solution would be to use memoization to store the results of the previous function calls.</p>
<iframe src="https://leetcode.com/playground/Tkq2Z36Y/shared" frameborder="0" width="100%" height="361" name="Tkq2Z36Y"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n*k)</script>. <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">k</script> entries in the <script type="math/tex; mode=display">memo</script> array are filled once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. <script type="math/tex; mode=display">memo</script> array of constant size <script type="math/tex; mode=display">1001</script>x<script type="math/tex; mode=display">1001</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-7-1-d-dynamic-programmming">Approach 7: 1-D Dynamic Programmming</h4>
<p><strong>Algorithm</strong></p>
<p>From the Dynamic Programming solution, we can also note that we only need the values of the previous row in the <script type="math/tex; mode=display">dp</script> array, and not any other row. Thus, instead of storing the whole 2-D <script type="math/tex; mode=display">dp</script> in memory, we can make use of a 1-D <script type="math/tex; mode=display">dp</script> to store the previous row's entries only. The updations can be done in a 1-D <script type="math/tex; mode=display">temp</script> array of the same size as <script type="math/tex; mode=display">dp</script> and <script type="math/tex; mode=display">dp</script> can be updated using this <script type="math/tex; mode=display">temp</script> everytime a row is finished.</p>
<iframe src="https://leetcode.com/playground/qZUxznzm/shared" frameborder="0" width="100%" height="327" name="qZUxznzm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n*k)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">k+1</script> is filled <script type="math/tex; mode=display">n+1</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(k)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">(k+1)</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>