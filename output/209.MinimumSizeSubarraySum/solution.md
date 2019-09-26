<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-a-better-brute-force-accepted">Approach #2 A better brute force [Accepted]</a></li>
<li><a href="#approach-3-using-binary-search-accepted">Approach #3 Using Binary search [Accepted]</a></li>
<li><a href="#approach-4-using-2-pointers-accepted">Approach #4 Using 2 pointers [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>Do as directed in question. Find the sum for all the possible subarrays and update the <script type="math/tex; mode=display">\text{ans}</script> as and when we get a better subarray that fulfill the requirements (<script type="math/tex; mode=display">\text{sum} \geq \text{s}</script>).</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize <script type="math/tex; mode=display">\text{ans}=\text{INT_MAX}</script>
</li>
<li>Iterate the array from left to right using <script type="math/tex; mode=display">i</script>:<ul>
<li>Iterate from the current element to the end of vector using <script type="math/tex; mode=display">j</script>:<ul>
<li>Find the <script type="math/tex; mode=display">\text{sum}</script> of elements from index <script type="math/tex; mode=display">i</script> to <script type="math/tex; mode=display">j</script>
</li>
<li>If sum is greater then <script type="math/tex; mode=display">s</script>:<ul>
<li>Update <script type="math/tex; mode=display">\text{ans} = \min(\text{ans}, (j - i + 1))</script>
</li>
<li>Start the next <script type="math/tex; mode=display">i</script>th iteration, since, we got the smallest subarray with <script type="math/tex; mode=display">\text{sum} \geq s</script> starting from the current index.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/VzAVPq7w/shared" frameborder="0" name="VzAVPq7w" width="100%" height="360"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n^3)</script>.</p>
<ul>
<li>For each element of array, we find all the subarrays starting from that index which is <script type="math/tex; mode=display">O(n^2)</script>.</li>
<li>Time complexity to find the sum of each subarray is <script type="math/tex; mode=display">O(n)</script>.</li>
<li>Thus, the total time complexity : <script type="math/tex; mode=display">O(n^2 * n) = O(n^3)</script>
</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script> extra space.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-a-better-brute-force-accepted">Approach #2 A better brute force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>In Approach #1, you may notice that the sum is calculated for every surarray in <script type="math/tex; mode=display">O(n)</script> time. But, we could easily find the sum in O(1) time by storing the cumulative sum from the beginning(Memoization). After we have stored the cumulative sum in <script type="math/tex; mode=display">\text{sums}</script>, we could easily find the sum of any subarray from <script type="math/tex; mode=display">i</script> to <script type="math/tex; mode=display">j</script>.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>The algorithm is similar to Approach #1.</li>
<li>The only difference is in the way of finding the sum of subarrays:<ul>
<li>Create a vector <script type="math/tex; mode=display">\text{sums}</script> of size of <script type="math/tex; mode=display">\text{nums}</script>
</li>
<li>Initialize <script type="math/tex; mode=display">\text{sums}[0]=\text{nums}[0]</script>
</li>
<li>Iterate over the <script type="math/tex; mode=display">\text{sums}</script> vector:<ul>
<li>Update <script type="math/tex; mode=display">\text{sums}[i] = \text{sums}[i-1] + \text{nums}[i]</script>
</li>
</ul>
</li>
<li>Sum of subarray from <script type="math/tex; mode=display">i</script> to <script type="math/tex; mode=display">j</script> is calculated as:
<script type="math/tex; mode=display">\text{sum}=\text{sums}[j] - \text{sums}[i] +\text{nums}[i]</script>, , wherein <script type="math/tex; mode=display">\text{sums}[j] - \text{sums}[i]</script> is the sum from (<script type="math/tex; mode=display">i+1</script>)th element to the <script type="math/tex; mode=display">j</script>th element.</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/zpQxiiBt/shared" frameborder="0" name="zpQxiiBt" width="100%" height="411"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n^2)</script>.</p>
<ul>
<li>Time complexity to find all the subarrays is <script type="math/tex; mode=display">O(n^2)</script>.</li>
<li>Sum of the subarrays is calculated in <script type="math/tex; mode=display">O(1)</script> time.</li>
<li>Thus, the total time complexity: <script type="math/tex; mode=display">O(n^2 * 1) = O(n^2)</script>
</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script> extra space.</p>
<ul>
<li>Additional <script type="math/tex; mode=display">O(n)</script> space for <script type="math/tex; mode=display">\text{sums}</script> vector than in Approach #1.</li>
</ul>
</li>
</ul>
<hr>
<h4 id="approach-3-using-binary-search-accepted">Approach #3 Using Binary search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We could further improve the Approach #2 using the binary search. Notice that we find the subarray with <script type="math/tex; mode=display">\text{sum} >=\text{s}</script> starting with an index <script type="math/tex; mode=display">i</script> in <script type="math/tex; mode=display">O(n)</script> time. But, we could reduce the time to <script type="math/tex; mode=display">O(\log(n))</script> using binary search. Note that in Approach #2, we search for subarray starting with index <script type="math/tex; mode=display">i</script>, until we find <script type="math/tex; mode=display">\text{sum}=\text{sums}[j] - \text{sums}[i] +\text{nums}[i]</script> that is greater than <script type="math/tex; mode=display">\text{s}</script>. So, instead of iterating linearly to find the sum, we could use binary search to find the index that is not lower than  <script type="math/tex; mode=display">\text{s}-\text{sums[i]}</script> in the <script type="math/tex; mode=display">\text{sums}</script>, which can be done using <script type="math/tex; mode=display">\text{lower_bound}</script> function in C++ STL or could be implemented manually.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>
<p>Create vector <script type="math/tex; mode=display">sums</script> of size <script type="math/tex; mode=display">n+1</script> with :
<script type="math/tex; mode=display">\text{sums}[0]=0\text{, }\text{sums}[i]=\text{sums}[i-1]+\text{nums}[i-1]</script>
</p>
</li>
<li>
<p>Iterate from <script type="math/tex; mode=display">i=1</script> to <script type="math/tex; mode=display">n</script>:</p>
<ul>
<li>Find the value <script type="math/tex; mode=display">\text{to_find}</script> in <script type="math/tex; mode=display">\text{sum}</script> required for minimum subarray starting from index <script type="math/tex; mode=display">i</script> to have sum greater than <script type="math/tex; mode=display">s</script>, that is:
<script type="math/tex; mode=display">\text{to_find}=\text{s}+\text{sums}[i-1]</script>
</li>
<li>Find the index in <script type="math/tex; mode=display">\text{sums}</script> such that value at that index is not lower than the <script type="math/tex; mode=display">\text{to_find}</script> value, say <script type="math/tex; mode=display">\text{bound}</script>
</li>
<li>If we find the <script type="math/tex; mode=display">\text{to_find}</script> in <script type="math/tex; mode=display">\text{sums}</script>, then:<ul>
<li>Size of current subarray is given by:
  <script type="math/tex; mode=display">\text{bound} - (\text{sums.begin}()+i-1)</script>
</li>
<li>Compare <script type="math/tex; mode=display">ans</script> with the current subarray size and store minimum in <script type="math/tex; mode=display">ans</script>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/hVhQq7az/shared" frameborder="0" name="hVhQq7az" width="100%" height="411"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n\log(n))</script>.<ul>
<li>For each element in the vector, find the subarray starting from that index, and having sum greater than <script type="math/tex; mode=display">s</script> using binary search. Hence, the time required is <script type="math/tex; mode=display">O(n)</script> for iteration over the vector and <script type="math/tex; mode=display">O(\log(n))</script> for finding the subarray for each index using binary search.</li>
<li>Therefore, total time complexity = <script type="math/tex; mode=display">O(n*\log(n))</script>
</li>
</ul>
</li>
<li>Space complexity: <script type="math/tex; mode=display">O(n)</script>. Additional <script type="math/tex; mode=display">O(n)</script> space for <script type="math/tex; mode=display">\text{sums}</script> vector</li>
</ul>
<hr>
<h4 id="approach-4-using-2-pointers-accepted">Approach #4 Using 2 pointers [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Until now, we have kept the starting index of subarray fixed, and found the last position. Instead, we could move the starting index of the current subarray as soon as we know that no better could be done with this index as the starting index. We could keep 2 pointer,one for the start and another for the end of the current subarray, and make optimal moves so as to keep the <script type="math/tex; mode=display">\text{sum}</script> greater than <script type="math/tex; mode=display">s</script> as well as maintain the lowest size possible.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize <script type="math/tex; mode=display">\text{left}</script> pointer to 0 and <script type="math/tex; mode=display">\text{sum}</script> to 0</li>
<li>Iterate over the <script type="math/tex; mode=display">\text{nums}</script>:<ul>
<li>Add <script type="math/tex; mode=display">\text{nums}[i]</script> to <script type="math/tex; mode=display">\text{sum}</script>
</li>
<li>While <script type="math/tex; mode=display">\text{sum}</script> is greater than or equal to <script type="math/tex; mode=display">s</script>:<ul>
<li>Update <script type="math/tex; mode=display">\text{ans}=\min(\text{ans},i+1-\text{left})</script>, where <script type="math/tex; mode=display">i+1-\text{left}</script> is the size of current subarray</li>
<li>It means that the first index can safely be incremented, since, the minimum subarray starting with this index with <script type="math/tex; mode=display">\text{sum} \geq s</script> has been achieved</li>
<li>Subtract <script type="math/tex; mode=display">\text{nums[left]}</script> from <script type="math/tex; mode=display">\text{sum}</script> and increment <script type="math/tex; mode=display">\text{left}</script>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/TxnK5kAo/shared" frameborder="0" name="TxnK5kAo" width="100%" height="309"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n)</script>. Single iteration of <script type="math/tex; mode=display">O(n)</script>.<ul>
<li>Each element can be visited atmost twice, once by the right pointer(<script type="math/tex; mode=display">i</script>) and (atmost)once by the <script type="math/tex; mode=display">\text{left}</script> pointer.</li>
</ul>
</li>
<li>Space complexity: <script type="math/tex; mode=display">O(1)</script> extra space. Only constant space required for <script type="math/tex; mode=display">\text{left}</script>, <script type="math/tex; mode=display">\text{sum}</script>, <script type="math/tex; mode=display">\text{ans}</script> and <script type="math/tex; mode=display">i</script>.</li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/abhinavbansal0">@abhinavbansal0</a>.</p>
          </div>
        
      </div>