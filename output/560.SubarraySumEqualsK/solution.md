<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-using-cummulative-sum-accepted">Approach #2 Using Cummulative sum [Accepted]</a></li>
<li><a href="#approach-3-without-space-accepted">Approach #3 Without space [Accepted]</a></li>
<li><a href="#approach-4-using-hashmap-accepted">Approach #4 Using hashmap [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>The simplest method is to consider every possible subarray of the given <script type="math/tex; mode=display">nums</script> array, find the sum of the elements of each of those subarrays and check for the equality of the sum obtained with the given <script type="math/tex; mode=display">k</script>. Whenver the sum equals <script type="math/tex; mode=display">k</script>, we can increment the <script type="math/tex; mode=display">count</script> used to store the required result.</p>
<iframe src="https://leetcode.com/playground/uzdLhWrz/shared" frameborder="0" name="uzdLhWrz" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>. Considering every possible subarray takes <script type="math/tex; mode=display">O(n^2)</script> time. For each of the subarray we calculate the sum taking <script type="math/tex; mode=display">O(n)</script> time in the worst case, taking a total of <script type="math/tex; mode=display">O(n^3)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-cummulative-sum-accepted">Approach #2 Using Cummulative sum [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of determining the sum of elements everytime for every new subarray considered, we can make use of a cumulative sum array , <script type="math/tex; mode=display">sum</script>. Then, in order to calculate the sum of elements lying between two indices, we can subtract the cumulative sum corresponding to the two indices to obtain the sum directly, instead of iterating over the subarray to obtain the sum.</p>
<p>In this implementation, we make use of a cumulative sum array, <script type="math/tex; mode=display">sum</script>, such that <script type="math/tex; mode=display">sum[i]</script> is used to store the cumulative sum of <script type="math/tex; mode=display">nums</script> array upto the element corresponding to the <script type="math/tex; mode=display">(i-1)^{th}</script> index. Thus, to determine the sum of elements for the subarray <script type="math/tex; mode=display">nums[i:j]</script>, we can directly use <script type="math/tex; mode=display">sum[j+1] - sum[i]</script>.</p>
<iframe src="https://leetcode.com/playground/YnknRnC6/shared" frameborder="0" name="YnknRnC6" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Considering every possible subarray takes <script type="math/tex; mode=display">O(n^2)</script> time. Finding out the sum of any subarray takes <script type="math/tex; mode=display">O(1)</script> time after the initial processing of <script type="math/tex; mode=display">O(n)</script> for creating the cumulative sum array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Cumulative sum array <script type="math/tex; mode=display">sum</script> of size <script type="math/tex; mode=display">n+1</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-without-space-accepted">Approach #3 Without space [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of considering all the <script type="math/tex; mode=display">start</script> and <script type="math/tex; mode=display">end</script> points and then finding the sum for each subarray corresponding to those points, we can directly find the sum on the go while considering different <script type="math/tex; mode=display">end</script> points. i.e. We can choose a particular <script type="math/tex; mode=display">start</script> point and while iterating over the <script type="math/tex; mode=display">end</script> points, we can add the element corresponding to the <script type="math/tex; mode=display">end</script> point to the sum formed till now. Whenver the <script type="math/tex; mode=display">sum</script> equals the required <script type="math/tex; mode=display">k</script> value, we can update the <script type="math/tex; mode=display">count</script> value. We do so while iterating over all the <script type="math/tex; mode=display">end</script> indices possible for every <script type="math/tex; mode=display">start</script> index. Whenver, we update the <script type="math/tex; mode=display">start</script> index, we need to reset the <script type="math/tex; mode=display">sum</script> value to 0.</p>
<iframe src="https://leetcode.com/playground/MGuUEEUy/shared" frameborder="0" name="MGuUEEUy" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We need to consider every subarray possible.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-using-hashmap-accepted">Approach #4 Using hashmap [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>The idea behind this approach is as follows: If the cumulative sum(repreesnted by <script type="math/tex; mode=display">sum[i]</script> for sum upto <script type="math/tex; mode=display">i^{th}</script> index) upto two indices is the same, the sum of the elements lying in between those indices is zero. Extending the same thought further, if the cumulative sum upto two indices, say <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> is at a difference of <script type="math/tex; mode=display">k</script> i.e. if <script type="math/tex; mode=display">sum[i] - sum[j] = k</script>, the sum of elements lying between indices <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> is <script type="math/tex; mode=display">k</script>.</p>
<p>Based on these thoughts, we make use of a hashmap <script type="math/tex; mode=display">map</script> which is used to store the cumulative sum upto all the indices possible along with the number of times the same sum occurs. We store the data in the form: <script type="math/tex; mode=display">(sum_i, no. of occurences of sum_i)</script>. We traverse over the array <script type="math/tex; mode=display">nums</script> and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered, we also determine the number of times the sum <script type="math/tex; mode=display">sum-k</script> has occured already, since it will determine the number of times a subarray with sum <script type="math/tex; mode=display">k</script> has occured upto the current index. We increment the <script type="math/tex; mode=display">count</script> by the same amount. </p>
<p>After the complete array has been traversed, the <script type="math/tex; mode=display">count</script> gives the required result.</p>
<p>The animation below depicts the process.</p>
<p>!?!../Documents/560_Subarray.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/S6xciAtN/shared" frameborder="0" name="S6xciAtN" width="100%" height="292"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The entire <script type="math/tex; mode=display">nums</script> array is traversed only once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Hashmap <script type="math/tex; mode=display">map</script> can contain upto <script type="math/tex; mode=display">n</script> distinct entries in the worst case.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>