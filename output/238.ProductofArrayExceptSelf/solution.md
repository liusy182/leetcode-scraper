<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-left-and-right-product-lists">Approach 1: Left and Right product lists</a></li>
<li><a href="#approach-2-o1-space-approach">Approach 2: O(1) space approach</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>From the looks of it, this seems like a simple enough problem to solve in linear time and space. We can simply take the product of all the elements in the given array and then, for each of the elements <script type="math/tex; mode=display">x</script> of the array, we can simply find <code>product of array except self</code> value by dividing the product by <script type="math/tex; mode=display">x</script>. </p>
<p>Doing this for each of the elements would solve the problem. However, there's a note in the problem which says that we are not allowed to use division operation. That makes solving this problem a bit harder. 
<br>
<br></p>
<hr>
<h4 id="approach-1-left-and-right-product-lists">Approach 1: Left and Right product lists</h4>
<p>It's much easier to build an intuition for solving this problem without division once you visualize how the different <code>products except self</code> look like for each of the elements. So, let's take a look at an example array and the different products.</p>
<p></p><center>
<img src="../Figures/238/diag-1.png" width="700"></center>
<p>Looking at the figure about we can figure another way of computing those different product values. </p>
<blockquote>
<p>Instead of dividing the product of all the numbers in the array by the number at a given index to get the corresponding product, we can make use of the product of all the numbers to the left and all the numbers to the right of the index. Multiplying these two individual products would give us the desired result as well.</p>
</blockquote>
<p>For every given index, <script type="math/tex; mode=display">i</script>, we will make use of the product of all the numbers to the left of it and multiply it by the product of all the numbers to the right. This will give us the product of all the numbers except the one at the given index <script type="math/tex; mode=display">i</script>. Let's look at a formal algorithm describing this idea more concretely.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize two empty arrays, <code>L</code> and <code>R</code> where for a given index <code>i</code>, <code>L[i]</code> would contain the product of all the numbers to the left of <code>i</code> and <code>R[i]</code> would contain the product of all the numbers to the right of <code>i</code>. </li>
<li>We would need two different loops to fill in values for the two arrays. For the array <code>L</code>, <script type="math/tex; mode=display">L[0]</script> would be <code>1</code> since there are no elements to the left of the first element. For the rest of the elements, we simply use <script type="math/tex; mode=display">L[i] = L[i - 1] * nums[i - 1]</script>. Remember that <code>L[i]</code> represents product of all the elements <em>to the left of element at index i</em>.</li>
<li>For the other array, we do the same thing but in reverse i.e. we start with the initial value of <code>1</code> in <script type="math/tex; mode=display">R[length - 1]</script> where <script type="math/tex; mode=display">length</script> is the number of elements in the array, and keep updating <code>R[i]</code> in reverse. Essentially, <script type="math/tex; mode=display">R[i] = R[i + 1] * nums[i + 1]</script>. Remember that <code>R[i]</code> represents product of all the elements <em>to the right of element at index i</em>.</li>
<li>Once we have the two arrays set up properly, we simply iterate over the input array one element at a time, and for each element at index <code>i</code>, we find the <code>product except self</code> as <script type="math/tex; mode=display">L[i] * R[i]</script>. </li>
</ol>
<p>Let's go over a simple run of the algorithm that clearly depicts the construction of the two intermediate arrays and finally the answer array.</p>
<p>!?!../Documents/238_anim1.json:770,460!?!</p>
<p>For the given array <script type="math/tex; mode=display">[4,5,1,8,2]</script>, the <code>L</code> and <code>R</code> arrays would finally be:</p>
<p></p><center>
<img src="../Figures/238/products.png" width="700"></center>
<iframe src="https://leetcode.com/playground/S3Gu9CJk/shared" frameborder="0" width="100%" height="500" name="S3Gu9CJk"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> represents the number of elements in the input array. We use one iteration to construct the array <script type="math/tex; mode=display">L</script>, one to construct the array <script type="math/tex; mode=display">R</script> and one last to construct the <script type="math/tex; mode=display">answer</script> array using <script type="math/tex; mode=display">L</script> and <script type="math/tex; mode=display">R</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(N)</script> used up by the two intermediate arrays that we constructed to keep track of product of elements to the left and right.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-o1-space-approach">Approach 2: O(1) space approach</h4>
<p>Although the above solution is good enough to solve the problem since we are not using division anymore, there's a follow-up component as well which asks us to solve this using constant space. Understandably so, the output array <em>does not</em> count towards the space complexity. This approach is essentially an extension of the approach above. Basically, we will be using the output array as one of <code>L</code> or <code>R</code> and we will be constructing the other one on the fly. Let's look at the algorithm based on this idea.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize the empty <code>answer</code> array where for a given index <code>i</code>, <code>answer[i]</code> would contain the product of all the numbers to the left of <code>i</code>. </li>
<li>We construct the <code>answer</code> array the same way we constructed the <code>L</code> array in the previous approach. These two algorithms are exactly the same except that we are trying to save up on space.</li>
<li>The only change in this approach is that we don't explicitly build the <code>R</code> array from before. Instead, we simply use a variable to keep track of the running product of elements to the right and we keep updating the <code>answer</code> array by doing <script type="math/tex; mode=display">answer[i] = answer[i] * R</script>. For a given index <code>i</code>, <code>answer[i]</code> contains the product of all the elements to the left and <code>R</code> would contain product of all the elements to the right. We then update <code>R</code> as <script type="math/tex; mode=display">R = R * nums[i]</script>
</li>
</ol>
<iframe src="https://leetcode.com/playground/o43uky8K/shared" frameborder="0" width="100%" height="500" name="o43uky8K"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> represents the number of elements in the input array. We use one iteration to construct the array <script type="math/tex; mode=display">L</script>, one to update the array <script type="math/tex; mode=display">answer</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script> since don't use any additional array for our computations. The problem statement mentions that using the <script type="math/tex; mode=display">answer</script> array doesn't add to the space complexity.
<br></li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>