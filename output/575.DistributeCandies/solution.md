<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-better-brute-force">Approach 2: Better Brute Force</a></li>
<li><a href="#approach-3-using-sorting">Approach 3: Using Sorting</a></li>
<li><a href="#approach-4-using-set">Approach 4: Using Set</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>The brute force approach is really simple. We can generate all the permutations of the given <script type="math/tex; mode=display">nums</script> array representing the candies and determine the number of unique elements in the first half of the generated array.</p>
<p>In order to determine the number of unique elements in the first half of the array, we put all the required elements in a set and count the number of elements in the set. We count such unique elements in the first half of the generated arrays for all the permutations possible and return the size of the largest set.</p>
<iframe src="https://leetcode.com/playground/5bJc432F/shared" frameborder="0" width="100%" height="497" name="5bJc432F"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n!)</script>. A total of <script type="math/tex; mode=display">n!</script> permutations are possible for <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script>. </p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force">Approach 2: Better Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>Before looking into the idea behind this approach, firstly we need to observe one point. The maximum no. of unique candies which the girl can obtain could be atmost <script type="math/tex; mode=display">n/2</script>, where <script type="math/tex; mode=display">n</script> refers to the number of candies. Further, in case the number of unique candies are below <script type="math/tex; mode=display">n/2</script>, to maximize the number of unique candies that the girl will obtain, we'll assign all the unique candies to the girl. Thus, in such a case, the number of unique candies the girl gets is equal to the total number of unique candies in the given <script type="math/tex; mode=display">candies</script> array. </p>
<p>Now, let's look at the idea behind this approach. We need to find the total number of unique candies in the given <script type="math/tex; mode=display">candies</script> array. One way to find the number of unique candies is to traverse over the given <script type="math/tex; mode=display">candies</script> array. Whenever we encounter an element, say <script type="math/tex; mode=display">candies[j]</script>, we can mark all the elements which are the same as <script type="math/tex; mode=display">candies[j]</script> as invalid and increment the count of unique elements by 1.</p>
<p>Thus, we need to do such markings for all the elements of <script type="math/tex; mode=display">candies</script> array. At the end, <script type="math/tex; mode=display">count</script> gives the required number of unique candies that can be given to the girl. Further, the value to be returned is given by: <script type="math/tex; mode=display">\text{min}(\frac{n}{2}, count)</script>. Instead of finding the <script type="math/tex; mode=display">\text{min}</script>, we can stop the traversal over the given <script type="math/tex; mode=display">candies</script> array as soon as the <script type="math/tex; mode=display">count</script> exceeds <script type="math/tex; mode=display">\frac{n}{2}</script>. </p>
<iframe src="https://leetcode.com/playground/nLo4nPxj/shared" frameborder="0" width="100%" height="310" name="nLo4nPxj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We traverse over all the elements of <script type="math/tex; mode=display">candies</script> for every new element found. In the worst case, we do so for every element of <script type="math/tex; mode=display">candies</script> array. <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">candies</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-sorting">Approach 3: Using Sorting</h4>
<p><strong>Algorithm</strong></p>
<p>We can sort the given <script type="math/tex; mode=display">candies</script> array and find out the elements which are unique by comparing the adjacent elements of the sorted array. For every new element found(which isn't the same as the previous element), we need to update the <script type="math/tex; mode=display">count</script>. At the end, we can return the required result as <script type="math/tex; mode=display">\text{min}(n/2, count)</script>, as discussed in the previous approach.</p>
<iframe src="https://leetcode.com/playground/SyAnB5Zm/shared" frameborder="0" width="100%" height="225" name="SyAnB5Zm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n\log n)</script>. Sorting takes <script type="math/tex; mode=display">O(n\log n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-using-set">Approach 4: Using Set</h4>
<p><strong>Algorithm</strong></p>
<p>Another way to find the number of unique elements is to traverse over all the elements of the given <script type="math/tex; mode=display">candies</script> array and keep on putting the elements in a set. By the property of a set, it will contain only unique elements. At the end, we can count the number of elements in the set, given by, say <script type="math/tex; mode=display">count</script>. The value to be returned will again be given by <script type="math/tex; mode=display">\text{min}(count, n/2)</script>, as discussed in previous approaches. Here, <script type="math/tex; mode=display">n</script> refers to the size of the <script type="math/tex; mode=display">candies</script> array.</p>
<iframe src="https://leetcode.com/playground/ndMnccZV/shared" frameborder="0" width="100%" height="208" name="ndMnccZV"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The entire <script type="math/tex; mode=display">candies</script> array is traversed only once. Here, <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">candies</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">set</script> will be of size <script type="math/tex; mode=display">n</script> in the worst case.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>