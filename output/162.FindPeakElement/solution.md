<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-linear-scan">Approach 1: Linear Scan</a></li>
<li><a href="#approach-2-recursive-binary-search">Approach 2: Recursive Binary Search</a></li>
<li><a href="#approach-3-iterative-binary-search">Approach 3: Iterative Binary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-linear-scan">Approach 1: Linear Scan</h4>
<p>In this approach, we make use of the fact that two consecutive numbers <script type="math/tex; mode=display">nums[j]</script> and <script type="math/tex; mode=display">nums[j + 1]</script> are never equal. Thus, we can traverse over the <script type="math/tex; mode=display">nums</script> array starting from the beginning. Whenever, we find a number <script type="math/tex; mode=display">nums[i]</script>, we only need to check if it is larger than the next number <script type="math/tex; mode=display">nums[i+1]</script> for determining if <script type="math/tex; mode=display">nums[i]</script> is the peak element. The reasoning behind this can be understood by taking the following three cases which cover every case into which any problem can be divided.</p>
<p>Case 1. All the numbers appear in a descending order. In this case, the first element corresponds to the peak element. We start off by checking if the current element is larger than the next one. The first element satisfies this criteria, and is hence identified as the peak correctly. In this case, we didn't reach a point where we needed to compare <script type="math/tex; mode=display">nums[i]</script> with <script type="math/tex; mode=display">nums[i-1]</script> also, to determine if it is the peak element or not.</p>
<p align="center"><img alt="Graph" src="../Figures/162/Find_Peak_Case1.PNG"></p>
<p>Case 2. All the elements appear in ascending order. In this case, we keep on comparing <script type="math/tex; mode=display">nums[i]</script> with <script type="math/tex; mode=display">nums[i+1]</script> to determine if <script type="math/tex; mode=display">nums[i]</script> is the peak element or not. None of the elements satisfy this criteria, indicating that we are currently on a rising slope and not on a peak. Thus, at the end, we need to return the last element as the peak element, which turns out to be correct. In this case also, we need not compare <script type="math/tex; mode=display">nums[i]</script> with <script type="math/tex; mode=display">nums[i-1]</script>, since being on the rising slope is a sufficient condition to ensure that <script type="math/tex; mode=display">nums[i]</script> isn't the peak element.</p>
<p align="center"><img alt="Graph" src="../Figures/162/Find_Peak_Case2.PNG"></p>
<p>Case 3. The peak appears somewhere in the middle. In this case, when we are traversing on the rising edge, as in Case 2, none of the elements will satisfy <script type="math/tex; mode=display">nums[i] > nums[i + 1]</script>. We need not compare <script type="math/tex; mode=display">nums[i]</script> with <script type="math/tex; mode=display">nums[i-1]</script> on the rising slope as discussed above. When we finally reach the peak element, the condition <script type="math/tex; mode=display">nums[i] > nums[i + 1]</script> is satisfied. We again, need not compare <script type="math/tex; mode=display">nums[i]</script> with <script type="math/tex; mode=display">nums[i-1]</script>. This is because, we could reach <script type="math/tex; mode=display">nums[i]</script> as the current element only when the check <script type="math/tex; mode=display">nums[i] > nums[i + 1]</script> failed for the previous(<script type="math/tex; mode=display">(i-1)^{th}</script> element, indicating that <script type="math/tex; mode=display">nums[i-1] < nums[i]</script>. Thus, we are able to identify the peak element correctly in this case as well.</p>
<p align="center"><img alt="Graph" src="../Figures/162/Find_Peak_Case3.PNG"></p>
<iframe src="https://leetcode.com/playground/MLfS4Quj/shared" frameborder="0" width="100%" height="208" name="MLfS4Quj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We traverse the <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> once only.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursive-binary-search">Approach 2: Recursive Binary Search</h4>
<p><strong>Algorithm</strong></p>
<p>We can view any given sequence in <script type="math/tex; mode=display">nums</script> array as alternating ascending and descending sequences. By making use of this, and the fact that we can return any peak as the result, we can make use of Binary Search to find the required peak element.</p>
<p>In case of simple Binary Search, we work on a sorted sequence of numbers and try to find out the required number by reducing the search space at every step. In this case, we use a modification of this simple Binary Search to our advantage. We start off by finding the middle element, <script type="math/tex; mode=display">mid</script> from the given <script type="math/tex; mode=display">nums</script> array. If this element happens to be lying in a descending sequence of numbers. or a local falling slope(found by comparing <script type="math/tex; mode=display">nums[i]</script> to its right neighbour), it means that the peak will always lie towards the left of this element. Thus, we reduce the search space to the left of <script type="math/tex; mode=display">mid</script>(including itself) and perform the same process on left subarray.</p>
<p>If the middle element, <script type="math/tex; mode=display">mid</script> lies in an ascending sequence of numbers, or a rising slope(found by comparing <script type="math/tex; mode=display">nums[i]</script> to its right neighbour), it obviously implies that the peak lies towards the right of this element. Thus, we reduce the search space to the right of <script type="math/tex; mode=display">mid</script> and perform the same process on the right subarray.</p>
<p>In this way, we keep on reducing the search space till we eventually reach a state where only one element is remaining in the search space. This single element is the peak element.</p>
<p>To see how it works, let's consider the three cases discussed above again.</p>
<p>Case 1. In this case, we firstly find <script type="math/tex; mode=display">3</script> as the middle element. Since it lies on a falling slope, we reduce the search space to <code>[1, 2, 3]</code>. For this subarray, <script type="math/tex; mode=display">2</script> happens to be the middle element, which again lies on a falling slope, reducing the search space to <code>[1, 2]</code>. Now, <script type="math/tex; mode=display">1</script> acts as the middle element and it lies on a falling slope, reducing the search space to <code>[1]</code> only. Thus, <script type="math/tex; mode=display">1</script> is returned as the peak correctly.</p>
<p>!?!../Documents/Find_Peak_Case1.json:1000,563!?!</p>
<p>Case 2. In this case, we firstly find <script type="math/tex; mode=display">3</script> as the middle element. Since it lies on a rising slope, we reduce the search space to <code>[4, 5]</code>. Now, <script type="math/tex; mode=display">4</script> acts as the middle element for this subarray and it lies on a rising slope, reducing the search space to <code>[5]</code> only. Thus, <script type="math/tex; mode=display">5</script> is returned as the peak correctly.</p>
<p>!?!../Documents/Find_Peak_Case2.json:1000,563!?!</p>
<p>Case 3. In this case, the peak lies somewhere in the middle. The first middle element is <script type="math/tex; mode=display">4</script>. It lies on a rising slope, indicating that the peak lies towards its right. Thus, the search space is reduced to <code>[5, 1]</code>. Now, <script type="math/tex; mode=display">5</script> happens to be the on a falling slope(relative to its right neighbour), reducing the search space to <code>[5]</code> only. Thus, <script type="math/tex; mode=display">5</script> is identified as the peak element correctly.</p>
<p>!?!../Documents/Find_Peak_Case3.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/3MGjFqJ4/shared" frameborder="0" width="100%" height="276" name="3MGjFqJ4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(log_2(n)\big)</script>. We reduce the search space in half at every step. Thus, the total search space will be consumed in <script type="math/tex; mode=display">log_2(n)</script> steps. Here, <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O\big(log_2(n)\big)</script>. We reduce the search space in half at every step. Thus, the total search space will be consumed in <script type="math/tex; mode=display">log_2(n)</script> steps. Thus, the depth of recursion tree will go upto <script type="math/tex; mode=display">log_2(n)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-iterative-binary-search">Approach 3: Iterative Binary Search</h4>
<p><strong>Algorithm</strong></p>
<p>The binary search discussed in the previous approach used a recursive method. We can do the same process in an iterative fashion also. This is done in the current approach.</p>
<iframe src="https://leetcode.com/playground/EnevWycv/shared" frameborder="0" width="100%" height="276" name="EnevWycv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(log_2(n)\big)</script>. We reduce the search space in half at every step. Thus, the total search space will be consumed in <script type="math/tex; mode=display">log_2(n)</script> steps. Here, <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
          </div>
        
      </div>