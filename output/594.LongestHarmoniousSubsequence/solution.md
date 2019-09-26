<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-better-brute-force">Approach 2: Better Brute Force</a></li>
<li><a href="#approach-3-using-sorting">Approach 3: Using Sorting</a></li>
<li><a href="#approach-4-using-hashmap">Approach 4: Using HashMap</a></li>
<li><a href="#approach-5-in-single-loop">Approach 5: In Single Loop</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>In the brute force solution, we consider every possible subsequence that can be formed using the elements of the given array. For every subsequence, we find the maximum and minimum values in the subsequence. If the difference between the maximum and the minimum values obtained is 1, it means the current subsequence forms a harmonious subsequence. Thus, we can consider the number of elements in this subsequence to be compared with the length of the last longest harmonious subsequence. </p>
<p>In order to obtain all the subseqeuences possible, we make use of binary number representation of decimal numbers. For a binary number of size <script type="math/tex; mode=display">n</script>, a total of <script type="math/tex; mode=display">2^n</script> different binary numbers can be generated. We generate all these binary numbers from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">2^n</script>. For every binary number generated, we consider the subsequence to be comprised of only those elements of <script type="math/tex; mode=display">nums</script> which have a 1 at the corresponding position in the current binary number. The following figure shows an example of the way the elements of <script type="math/tex; mode=display">nums</script> are considered in the current subsequence.</p>
<p><img alt="Harmonic_Subsequence" src="../Figures/594_Harmonic_Subsequence_Binary.PNG"></p>
<iframe src="https://leetcode.com/playground/e4c9G2XS/shared" frameborder="0" width="100%" height="361" name="e4c9G2XS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^n)</script>. Number of subsequences generated will be <script type="math/tex; mode=display">2^n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space required.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force">Approach 2: Better Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we created every possible subsequence, and for every such subsequence, we found out if it satisfies the harmonicity condition. Instead of doing this, we can do as follows. We can consider every element of the given <script type="math/tex; mode=display">nums</script> array one by one. For <script type="math/tex; mode=display">nums[i]</script> chosen to be the current element, we determine the <script type="math/tex; mode=display">count</script> of all the elements in the <script type="math/tex; mode=display">nums</script> array, which satisfy the harmonicity condition with <script type="math/tex; mode=display">nums[i]</script>, i.e. the <script type="math/tex; mode=display">count</script> of all such <script type="math/tex; mode=display">nums[j]</script> satisfying <script type="math/tex; mode=display">nums[i] == nums[j]</script> or <script type="math/tex; mode=display">nums[i] == nums[j] + 1</script>. When we reach the end of the array for <script type="math/tex; mode=display">nums[i]</script> being the current element, we compare this <script type="math/tex; mode=display">count</script> obtained with the result obtained from the previous traversals and update the result appropriately. When all the elements of the array have been chosen as the element to be chosen as the base for harmonicity check, we get the required length of the longest harmonic subsequence.</p>
<p>The following animation illustrates the process:</p>
<p>!?!../Documents/594_Harmonic_Subsequence_1.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/Akkez8ms/shared" frameborder="0" width="100%" height="395" name="Akkez8ms"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Two nested loops are there.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space required.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-sorting">Approach 3: Using Sorting</h4>
<p><strong>Algorithm</strong></p>
<p>Since we are concerned only with the count of elements which are at a difference of 1, we can use sorting to our advantage. If we sort the given <script type="math/tex; mode=display">nums</script> array, the related elements will get arranged close to each other. Thus, we can traverse over the sorted array, and find the count of similar elements and elements one larger than the current ones, which occur consecutively(all the similar elements will be lying consecutively now). Initially, this value is stored in <script type="math/tex; mode=display">prev\_count</script> variable. Then, if we encounter an element which is just 1 larger than the last elements, we count the occurences of such elements as well. This value is stored in <script type="math/tex; mode=display">count</script> variable. </p>
<p>Thus, now for the harmonic subsequence comprised of only these two elements is a subsequence of length <script type="math/tex; mode=display">count + prev\_count</script>. This result is stored in <script type="math/tex; mode=display">res</script> for each subsequence found. When we move forward to considering the next set of similar consecutive elements, we need to update the <script type="math/tex; mode=display">prev\_count</script> with the <script type="math/tex; mode=display">count</script>'s value, since now <script type="math/tex; mode=display">count</script> will act as the count of the elements 1 lesser than the next elements encountered. The value of <script type="math/tex; mode=display">res</script> is always updated to be the larger of previous <script type="math/tex; mode=display">res</script> and the current <script type="math/tex; mode=display">count + prev\_count</script> value.</p>
<p>When we are done traversing over the whole array, the value of <script type="math/tex; mode=display">res</script> gives us the required result.</p>
<iframe src="https://leetcode.com/playground/XNQkjXFk/shared" frameborder="0" width="100%" height="463" name="XNQkjXFk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n\log n)</script>. Sorting takes <script type="math/tex; mode=display">O(n\log n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log n)</script>. <script type="math/tex; mode=display">\log n</script> space is required by sorting in average case.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-using-hashmap">Approach 4: Using HashMap</h4>
<p><strong>Algorithm</strong></p>
<p>In this approach, we make use of a hashmap <script type="math/tex; mode=display">map</script> which stores the number of times an element occurs in the array along with the element's value in the form <script type="math/tex; mode=display">(num: count\_num)</script>, where <script type="math/tex; mode=display">num</script> refers to an element in the array and <script type="math/tex; mode=display">count\_num</script> refers to the number of times this <script type="math/tex; mode=display">num</script> occurs in the <script type="math/tex; mode=display">nums</script> array. We traverse over the <script type="math/tex; mode=display">nums</script> array and fill this <script type="math/tex; mode=display">map</script> once.</p>
<p>After this, we traverse over the keys of the <script type="math/tex; mode=display">map</script> created. For every key of the <script type="math/tex; mode=display">map</script> considered, say <script type="math/tex; mode=display">key</script>, we find out if the map contains the <script type="math/tex; mode=display">key + 1</script>. Such an element is found, since only such elements can be counted for the harmonic subsequence if <script type="math/tex; mode=display">key</script> is considered as one of the element of the harmonic subsequence. We need not care about <script type="math/tex; mode=display">key - 1</script>, because if <script type="math/tex; mode=display">key</script> is present in the harmonic subsequence, at one time either <script type="math/tex; mode=display">key + 1</script> or <script type="math/tex; mode=display">key - 1</script> only could be included in the harmonic subsequence. The case of <script type="math/tex; mode=display">key - 1</script> being in the harmonic subsequence will automatically be considered, when <script type="math/tex; mode=display">key - 1</script> is encountered as the current key. </p>
<p>Now, whenver we find that <script type="math/tex; mode=display">key + 1</script> exists in the keys of <script type="math/tex; mode=display">map</script>, we determine the count of the current harmonic subsequence as <script type="math/tex; mode=display">count_{key} + count_{key+1}</script>, where <script type="math/tex; mode=display">count_i</script> refers to the value corresponding to the key <script type="math/tex; mode=display">i</script> in <script type="math/tex; mode=display">map</script>, which reprents the number of times <script type="math/tex; mode=display">i</script> occurs in the array <script type="math/tex; mode=display">nums</script>.</p>
<p>Look at the animation below for a pictorial view of the process:</p>
<p>!?!../Documents/594_Harmonic_Subsequence_2.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/VSkbtva7/shared" frameborder="0" width="100%" height="293" name="VSkbtva7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. One loop is required to fill <script type="math/tex; mode=display">map</script> and one for traversing the <script type="math/tex; mode=display">map</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. In worst case map size grows upto size <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-in-single-loop">Approach 5: In Single Loop</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of filling the <script type="math/tex; mode=display">map</script> first and then traversing over the <script type="math/tex; mode=display">map</script> to determine the lengths of the harmonic subsequences encountered, we can traverse over the <script type="math/tex; mode=display">nums</script> array, and while doing the traversals, we can determine the lengths of the harmonic subsequences possible till the current index of the <script type="math/tex; mode=display">nums</script> array. </p>
<p>The method of finding the length of harmonic subsequence remains the same as the last approach. But, this time, we need to consider the existence of both <script type="math/tex; mode=display">key + 1</script> and <script type="math/tex; mode=display">key - 1</script> exclusively and determine the counts corresponding to both the cases. This is needed now because it could be possible that <script type="math/tex; mode=display">key</script> has already been added to the <script type="math/tex; mode=display">map</script> and later on <script type="math/tex; mode=display">key - 1</script> is encountered. In this case, if we consider the presence of <script type="math/tex; mode=display">key + 1</script> only, we'll go in the wrong direction.</p>
<p>Thus, we consider the <script type="math/tex; mode=display">count</script>s corresponding to both the cases separately for every <script type="math/tex; mode=display">key</script> and determine the maximum out of them. 
Thus, now the same task can be done only in a single traveral of the <script type="math/tex; mode=display">nums</script> array.</p>
<p>See the animation below for understanding the process:</p>
<p>!?!../Documents/594_Harmonic_Subsequence_3.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/ZZGbSqyA/shared" frameborder="0" width="100%" height="293" name="ZZGbSqyA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Only one loop is there.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">map</script> size grows upto size <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>