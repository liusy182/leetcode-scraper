<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-better-brute-force">Approach 2: Better Brute Force</a></li>
<li><a href="#approach-3-using-sorting">Approach 3: Using Sorting</a></li>
<li><a href="#approach-4-using-map">Approach 4: Using Map</a></li>
<li><a href="#approach-5-using-extra-array">Approach 5: Using Extra Array</a></li>
<li><a href="#approach-6-using-constant-space">Approach 6: Using Constant Space</a></li>
<li><a href="#approach-7-using-xor">Approach 7: Using XOR</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>The most naive solution is to consider each number from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>, and traverse over the whole <script type="math/tex; mode=display">nums</script> array to check if the current number occurs twice in <script type="math/tex; mode=display">nums</script>
or doesn't occur at all. We need to set the duplicate number, <script type="math/tex; mode=display">dup</script> and the missing number, <script type="math/tex; mode=display">missing</script>, appropriately in such cases respectively.</p>
<iframe src="https://leetcode.com/playground/ugiTepy3/shared" frameborder="0" width="100%" height="344" name="ugiTepy3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We traverse over the <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> for each of the numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force">Approach 2: Better Brute Force</h4>
<p>In the last approach, we continued the search process, even when we've already found the duplicate and the missing number. But, as per the problem statement, 
we know that only one number will be repeated and only one number will be missing. Thus, we can optimize the last approach to some extent, by stopping 
the search process as soon as we find these two required numbers.</p>
<iframe src="https://leetcode.com/playground/PcMPwwzf/shared" frameborder="0" width="100%" height="378" name="PcMPwwzf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We traverse over the <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> for each of the numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>, in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-sorting">Approach 3: Using Sorting</h4>
<p><strong>Algorithm</strong></p>
<p>One way to further optimize the last approach is to sort the given <script type="math/tex; mode=display">nums</script> array. This way, the numbers which are equal will always lie together. 
Further, we can easily identify the missing number by checking if every two consecutive elements in the sorted <script type="math/tex; mode=display">nums</script> array are just one count apart or not.</p>
<iframe src="https://leetcode.com/playground/Dj9BhAnK/shared" frameborder="0" width="100%" height="276" name="Dj9BhAnK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n\log n)</script>. Sorting takes <script type="math/tex; mode=display">O(n\log n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log n)</script>. Sorting takes <script type="math/tex; mode=display">O(\log n)</script> space. 
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-using-map">Approach 4: Using Map</h4>
<p><strong>Algorithm</strong></p>
<p>The given problem can also be solved easily if we can somehow keep a track of the number of times each element of the <script type="math/tex; mode=display">nums</script> array occurs. One way to 
do so is to make an entry for each element of <script type="math/tex; mode=display">nums</script> in a HashMap <script type="math/tex; mode=display">map</script>. This <script type="math/tex; mode=display">map</script> stores the entries in the form <script type="math/tex; mode=display">(num_i, count_i)</script>. Here, <script type="math/tex; mode=display">num</script> refers to
the <script type="math/tex; mode=display">i^{th}</script> element in <script type="math/tex; mode=display">nums</script> and <script type="math/tex; mode=display">count_i</script> refers to the number of times this element occurs in <script type="math/tex; mode=display">nums</script>.
  Whenever, the same element occurs again, we can increment the count corresponding to the 
same. </p>
<p>After this, we can consider every number from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>, and check for its presence in <script type="math/tex; mode=display">map</script>. If it isn't present, we can update the <script type="math/tex; mode=display">missing</script> variable 
appropriately. But, if the <script type="math/tex; mode=display">count</script> corresponding to the current number is <script type="math/tex; mode=display">2</script>, we can update the <script type="math/tex; mode=display">dup</script> variable with the current number.</p>
<iframe src="https://leetcode.com/playground/kz9G9DPq/shared" frameborder="0" width="100%" height="344" name="kz9G9DPq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Traversing over <script type="math/tex; mode=display">nums</script> of size <script type="math/tex; mode=display">n</script> takes <script type="math/tex; mode=display">O(n)</script> time. Considering each number from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script> also takes <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">map</script> can contain atmost <script type="math/tex; mode=display">n</script> entries for each of the numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-using-extra-array">Approach 5: Using Extra Array</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we make use of a <script type="math/tex; mode=display">map</script> to store the elements of <script type="math/tex; mode=display">nums</script> along with their corresponding counts. But, we can note, that each entry in <script type="math/tex; mode=display">map</script> 
requires two entries. Thus, putting up <script type="math/tex; mode=display">n</script> entries requires <script type="math/tex; mode=display">2n</script> space actually. We can reduce this space required to <script type="math/tex; mode=display">n</script> by making use of an array, <script type="math/tex; mode=display">arr</script> instead.
Now, the indices of <script type="math/tex; mode=display">arr</script> can be used instead of storing the elements again. Thus, we make use of <script type="math/tex; mode=display">arr</script> in such a way that, <script type="math/tex; mode=display">arr[i]</script> is used to store 
the number of occurences of the element <script type="math/tex; mode=display">i+1</script>. The rest of the process remains the same as in the last approach.</p>
<iframe src="https://leetcode.com/playground/QJRi2ZuU/shared" frameborder="0" width="100%" height="327" name="QJRi2ZuU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Traversing over <script type="math/tex; mode=display">nums</script> of size <script type="math/tex; mode=display">n</script> takes <script type="math/tex; mode=display">O(n)</script> time. Considering each number from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script> also takes <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">arr</script> can contain atmost <script type="math/tex; mode=display">n</script> elements for each of the numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-6-using-constant-space">Approach 6: Using Constant Space</h4>
<p><strong>Algorithm</strong></p>
<p>We can save the space used in the last approach, if we can somehow, include the information regarding the duplicacy of an element or absence of an element
 in the <script type="math/tex; mode=display">nums</script> array. Let's see how this can be done.</p>
<p>We know that all the elements in the given <script type="math/tex; mode=display">nums</script> array are positive, and lie in the range <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script> only. Thus, we can pick up each element <script type="math/tex; mode=display">i</script> 
 from <script type="math/tex; mode=display">nums</script>. For every number <script type="math/tex; mode=display">i</script> picked up, we can invert the element at the index <script type="math/tex; mode=display">\left|i\right|</script>. By doing so,  if one of the elements <script type="math/tex; mode=display">j</script> occurs twice, 
when this number is encountered the second time,  the element <script type="math/tex; mode=display">nums[\left|i\right|]</script> will be found to be negative. 
Thus, while doing the inversions, we can check if a number found is already negative, to find the duplicate number.</p>
<p>After the inversions have been done, if all the elements in <script type="math/tex; mode=display">nums</script> are present correctly, the resultant <script type="math/tex; mode=display">nums</script> array will have all the elements as 
 negative now. But, if one of the numbers, <script type="math/tex; mode=display">j</script> is missing, the element at the <script type="math/tex; mode=display">j^{th}</script> index will be positive. This  can be used to determine the missing number.</p>
<iframe src="https://leetcode.com/playground/RJUw9UMo/shared" frameborder="0" width="100%" height="327" name="RJUw9UMo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Two traversals over the <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> are done.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-7-using-xor">Approach 7: Using XOR</h4>
<p><strong>Algorithm</strong></p>
<p>Before we dive into the solution to this problem, let's consider a simple problem. Consider an array with <script type="math/tex; mode=display">n-1</script> elements containing numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script> with one number missing out of them. Now, how to we find out this missing element. One of the solutions is to take the XOR of all the elements of this array with all the numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>. By doing so, we get the required missing number. This works because XORing a number with itself results in a 0 result. Thus, only the number which is missing can't get cancelled with this XORing.</p>
<p>Now, using this idea as the base, let's take it a step forward and use it for the current problem. By taking the XOR of all the elements of the given <script type="math/tex; mode=display">nums</script> array with all the numbers from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script>, we will get a result, <script type="math/tex; mode=display">xor</script>, as <script type="math/tex; mode=display">x^y</script>. Here, <script type="math/tex; mode=display">x</script> and <script type="math/tex; mode=display">y</script> refer to the repeated and the missing term in the given <script type="math/tex; mode=display">nums</script> array. This happens on the same grounds as in the first problem discussed above.</p>
<p>Now, in the resultant <script type="math/tex; mode=display">xor</script>, we'll get a 1 in the binary representation only at those bit positions which have a 1 in one out of the numbers <script type="math/tex; mode=display">x</script> and <script type="math/tex; mode=display">y</script>, and a 0 at the same bit position in the other one. In the current solution, we consider the rightmost bit which is 1 in the <script type="math/tex; mode=display">xor</script>, although any bit would work. Let's say, this position is called the <script type="math/tex; mode=display">rightmostbit</script>. </p>
<p>If we divide the elements of the given <script type="math/tex; mode=display">nums</script> array into two parts such that the first set contains the elements which have a 1 at the <script type="math/tex; mode=display">rightmostbit</script> position and the second set contains the elements having a 0 at the same position, we'll get one out of <script type="math/tex; mode=display">x</script> or <script type="math/tex; mode=display">y</script> in one set and the other one in the second set. Now, our problem has reduced somewhat to the simple problem discussed above.</p>
<p>To solve this reduced problem, we can find out the elements from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n</script> and consider them as a part of the previous sets only, with the allocation of the set depending on a 1 or 0 at the <script type="math/tex; mode=display">righmostbit</script> position. </p>
<p>Now, if we do the XOR of all the elements of the first set, all the elements will result in an XOR of 0, due to cancellation of the similar terms in both <script type="math/tex; mode=display">nums</script> and the numbers <script type="math/tex; mode=display">(1:n)</script>, except one term, which is either <script type="math/tex; mode=display">x</script> or <script type="math/tex; mode=display">y</script>. </p>
<p>For the other term, we can do the XOR of all the elements in the second set as well.</p>
<p>Consider the example <code>[1 2 4 4 5 6]</code></p>
<p><img alt="XOR" src="../Figures/645_Set_Mismatch.PNG"></p>
<p>One more traversal over the <script type="math/tex; mode=display">nums</script> can be used to identify the missing and the repeated number out of the two numbers found.</p>
<iframe src="https://leetcode.com/playground/USgeoHAo/shared" frameborder="0" width="100%" height="500" name="USgeoHAo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We iterate over <script type="math/tex; mode=display">n</script> elements five times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>