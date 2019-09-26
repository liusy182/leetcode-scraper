<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-comparison-sorting">Approach 1: Comparison Sorting</a></li>
<li><a href="#approach-2-radix-sort">Approach 2: Radix Sort</a></li>
<li><a href="#approach-3-buckets-and-the-pigeonhole-principle">Approach 3: Buckets and The Pigeonhole Principle</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-comparison-sorting">Approach 1: Comparison Sorting</h4>
<p><strong>Intuition</strong></p>
<p>Do what the question says.</p>
<p><strong>Algorithm</strong></p>
<p>Sort the entire array. Then iterate over it to find the maximum gap between two successive elements.</p>
<iframe src="https://leetcode.com/playground/tE9iwqVk/shared" frameborder="0" width="100%" height="293" name="tE9iwqVk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n\log n)</script>.</p>
<p>Time taken to sort the array is <script type="math/tex; mode=display">O(n\log n)</script> (average case). Time taken for linear iteration through the array is of <script type="math/tex; mode=display">O(n)</script> complexity. Hence overall time complexity is <script type="math/tex; mode=display">O(n\log n)</script>.</p>
</li>
<li>
<p>Space complexity: No extra space needed, other than the input array (since sorting can usually be done in-place).
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-radix-sort">Approach 2: Radix Sort</h4>
<p><strong>Algorithm</strong></p>
<p>This approach is similar to <a href="#approach-1-comparison-sorting">Approach 1</a>, except we use <a href="https://en.wikipedia.org/wiki/Radix_sort">Radix Sort</a> instead of a traditional comparison sort.</p>
<iframe src="https://leetcode.com/playground/Ta7AXDt5/shared" frameborder="0" width="100%" height="500" name="Ta7AXDt5"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(d \cdot (n + k)) \approx O(n)</script>.</p>
<p>Since a linear iteration over the array (once it is sorted) is of linear (i.e. <script type="math/tex; mode=display">O(n)</script>) complexity, the performance of this approach is limited by the performance of Radix sort.</p>
<p>Radix sort uses <a href="https://en.wikipedia.org/wiki/Counting_sort">Counting sort</a> as a subroutine.</p>
<ul>
<li>
<p>Counting sort runs in <script type="math/tex; mode=display">O(n + k)</script> time (where <script type="math/tex; mode=display">k</script> is the radix or base of the digits comprising the <script type="math/tex; mode=display">n</script> elements in the array). If <script type="math/tex; mode=display">k \leq O(n)</script>, Counting sort would run in linear time. In our case, the radix is fixed (i.e. <script type="math/tex; mode=display">k = 10</script>). Hence our Counting sort subroutine runs in <script type="math/tex; mode=display">O(n)</script> linear time.</p>
</li>
<li>
<p>Radix sort works by running <script type="math/tex; mode=display">d</script> passes of the Counting sort subroutine (where the elements are composed of, maximally, <script type="math/tex; mode=display">d</script> digits). Hence effective runtime of Radix sort would be <script type="math/tex; mode=display">O(d \cdot (n + k))</script>. However, in our case an element can, maximally, be the maximum 32-bit signed integer <code>2,147,483,647</code>. Hence <script type="math/tex; mode=display">d \leq 10</script> is a constant.</p>
</li>
</ul>
<p>Thus Radix sort has a runtime performance complexity of about <script type="math/tex; mode=display">O(n)</script> for reasonably large input.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n + k) \approx O(n)</script> extra space.</p>
<p>Counting sort requires <script type="math/tex; mode=display">O(k)</script> extra space. Radix sort requires an auxiliary array of the same size as input array. However given that <script type="math/tex; mode=display">k</script> is a small fixed constant, the space required by Counting sort can be ignored for reasonably large input.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-3-buckets-and-the-pigeonhole-principle">Approach 3: Buckets and The Pigeonhole Principle</h4>
<p><strong>Intuition</strong></p>
<p>Sorting an entire array can be costly. At worst, it requires comparing each element with <em>every</em> other element.
What if we didn't need to compare all pairs of elements? That would be possible if we could somehow divide the elements into representative groups, or rather, <em>buckets</em>. Then we would only need to compare these buckets.</p>
<blockquote>
<p><strong>Digression: The Pigeonhole Principle</strong>
The <a href="https://en.wikipedia.org/wiki/Pigeonhole_principle">Pigeonhole Principle</a> states that if <script type="math/tex; mode=display">n</script> items are put into <script type="math/tex; mode=display">m</script> containers, with <script type="math/tex; mode=display">n > m</script>, then at least one container must contain more than one item.</p>
</blockquote>
<p>Suppose for each of the <script type="math/tex; mode=display">n</script> elements in our array, there was a bucket. Then each element would occupy one bucket. Now what if we reduced, the number of buckets? Some buckets would have to accommodate more than one element.</p>
<p>Now let's talk about the gaps between the elements. Let's take the best case, where all elements of the array are sorted and have a uniform gap between them. This means every adjacent pair of elements differ by the same constant value. So for <script type="math/tex; mode=display">n</script> elements of the array, there are <script type="math/tex; mode=display">n-1</script> gaps, each of width, say, <script type="math/tex; mode=display">t</script>. It is trivial to deduce that <script type="math/tex; mode=display">t = (max - min)/(n-1)</script> (where <script type="math/tex; mode=display">max</script> and <script type="math/tex; mode=display">min</script> are the minimum and maximum elements of the array). This width is the maximal width/gap between two adjacent elements in the array; precisely the quantity we are looking for!</p>
<p>One can safely argue that this value of <script type="math/tex; mode=display">t</script>, is in fact, the smallest value that <script type="math/tex; mode=display">t</script> can ever accomplish of any array with the same number of elements (i.e. <script type="math/tex; mode=display">n</script>) and the same range (i.e. <script type="math/tex; mode=display">(max - min)</script>). To test this fact, you can start with a uniform width array (as described above) and try to reduce the gap between any two adjacent elements. If you reduce the gap between <script type="math/tex; mode=display">arr[i-1]</script> and <script type="math/tex; mode=display">arr[i]</script> to some value <script type="math/tex; mode=display">t - p</script>, then you will notice that the gap between <script type="math/tex; mode=display">arr[i]</script> and <script type="math/tex; mode=display">arr[i+1]</script> would have increased to <script type="math/tex; mode=display">t + p</script>. Hence the maximum attainable gap would have become <script type="math/tex; mode=display">t + p</script> from <script type="math/tex; mode=display">t</script>. Thus the value of the <strong>maximum gap</strong> <script type="math/tex; mode=display">t</script> can only increase.</p>
<p><strong>Buckets!</strong></p>
<p>Coming back to our problem, we have already established by application of the Pigeonhole Principle, that if we used <em>buckets</em> instead of individual elements as our base for comparison, the number of comparisons would reduce if we could accommodate more than one element in a single bucket. That does not immediately solve the problem though. What if we had to compare elements <em>within</em> a bucket? We would end up no better.</p>
<p>So the current motivation remains: somehow, if we only had to compare among the buckets, and <em>not</em> the elements <em>within</em> the buckets, we would be good. It would also solve our sorting problem: we would just distribute the elements to the right buckets. Since the buckets can be already ordered, and we only compare among buckets, we wouldn't have to compare all elements to sort them!</p>
<p>But if we only had buckets to compare, we would have to <em>ensure</em>, that the gap between the buckets itself represent the maximal gap in the input array. How do we go about doing that?</p>
<p>We could do that just by setting the buckets to be smaller than <script type="math/tex; mode=display">t = (max - min)/(n-1)</script> (as described above). Since the gaps (between elements) within the same bucket would only be <script type="math/tex; mode=display">\leq t</script>, we could deduce that the maximal gap would <em>indeed</em> occur <strong>only between two adjacent buckets</strong>.</p>
<p>Hence by setting bucket size <script type="math/tex; mode=display">b</script> to be <script type="math/tex; mode=display">1 < b \leq (max - min)/(n-1)</script>, we can ensure that at least one of the gaps between adjacent buckets would serve as the <strong>maximal gap.</strong></p>
<p><strong>Clarifications</strong></p>
<p>A few clarifications are in order:</p>
<ul>
<li>
<p><strong>Would the buckets be of uniform size?</strong>
Yes. Each of them would be of the same size <script type="math/tex; mode=display">b</script>.</p>
</li>
<li>
<p><strong>But, then wouldn't the gap between them be uniform/constant as well?</strong>
Yes it would be. The gap between them would be <script type="math/tex; mode=display">1</script> integer unit wide. That means a two adjacent buckets of size <script type="math/tex; mode=display">3</script> could hold integers with values, say, <script type="math/tex; mode=display">3 - 6</script> and <script type="math/tex; mode=display">7 - 9</script>. We avoid overlapping buckets.</p>
</li>
<li>
<p><strong>Then what are you talking about when you say the gap between two adjacent buckets could be the maximal gap?</strong>
When we are talking about the size of a bucket, we are talking about its holding capacity. That is the range of values the bucket can represent (or <em>hold</em>). However the actual extent of the bucket are determined by the values of the maximum and minimum element a bucket holds. For example a bucket of size <script type="math/tex; mode=display">5</script> could have a capacity to hold values between <script type="math/tex; mode=display">6 - 10</script>. However, if it only holds the elements <script type="math/tex; mode=display">7, 8</script> and <script type="math/tex; mode=display">9</script>, then its actual extent is only <script type="math/tex; mode=display">(9 - 7) + 1 = 3</script> which is not the same as the capacity of the bucket.</p>
</li>
<li>
<p><strong>Then how do you compare adjacent buckets?</strong>
We do that by comparing their extents. Thus we compare the minimum element of the next bucket to the maximum element of the current bucket. For example: if we have two buckets of size <script type="math/tex; mode=display">5</script> each, holding elements <script type="math/tex; mode=display">[1, 2, 3]</script> and <script type="math/tex; mode=display">[9, 10]</script> respectively, then the gap between the buckets would essentially refer to the value <script type="math/tex; mode=display">9 - 3 = 6</script> (which is larger than the size of either bucket).</p>
</li>
<li>
<p><strong>But then aren't we comparing elements again?!</strong>
We are, yes! But only compare about twice the elements as the number of buckets (i.e. the minimum and maximum elements of each bucket). If you followed the above, you would realize that this amount is certainly less than the actual number of elements in the array, given a suitable bucket size was chosen.</p>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<ul>
<li>
<p>We choose a bucket size <script type="math/tex; mode=display">b</script> such that <script type="math/tex; mode=display">1 < b \leq (max - min)/(n-1)</script>. Let's just choose <script type="math/tex; mode=display">b = \lfloor (max - min)/(n-1) \rfloor</script>.</p>
</li>
<li>
<p>Thus all the <script type="math/tex; mode=display">n</script> elements would be divided among <script type="math/tex; mode=display">k = \lceil (max - min)/b \rceil</script> buckets.</p>
</li>
<li>
<p>Hence the <script type="math/tex; mode=display">i^{th}</script> bucket would hold the range of values: <script type="math/tex; mode=display">\bigg [min + (i-1) * b, \space min + i*b \bigg )</script> (<code>1</code>-based indexing).</p>
</li>
<li>
<p>It is trivial to calculate the index of the bucket to which a particular element belongs. That is given by <script type="math/tex; mode=display">\lfloor (num - min)/b \rfloor</script> (<code>0</code>-based indexing) where <script type="math/tex; mode=display">num</script> is the element in question.</p>
</li>
<li>
<p>Once all <script type="math/tex; mode=display">n</script> elements have been distributed, we compare <script type="math/tex; mode=display">k-1</script> adjacent bucket pairs to find the maximum gap.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/XPXwrKmS/shared" frameborder="0" width="100%" height="500" name="XPXwrKmS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n + b) \approx O(n)</script>.</p>
<p>Distributing the elements of the array takes one linear pass (i.e. <script type="math/tex; mode=display">O(n)</script> complexity). Finding the maximum gap among the buckets takes a linear pass over the bucket storage (i.e. <script type="math/tex; mode=display">O(b)</script> complexity). Hence overall process takes linear runtime.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(2 \cdot b) \approx O(b)</script> extra space.</p>
<p>Each bucket stores a maximum and a minimum element. Hence extra space linear to the number of buckets is required.</p>
</li>
</ul>
          </div>
        
      </div>