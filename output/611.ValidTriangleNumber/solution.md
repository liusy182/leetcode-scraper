<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-using-binary-search">Approach 2: Using Binary Search</a></li>
<li><a href="#approach-3-linear-scan">Approach 3: Linear Scan</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>The condition for the triplets <script type="math/tex; mode=display">(a, b, c)</script> representing the lengths of the sides of a triangle, to form a valid triangle, is that the sum of any two sides should always be greater than the third side alone. i.e. <script type="math/tex; mode=display">a + b > c</script>, <script type="math/tex; mode=display">b + c > a</script>, <script type="math/tex; mode=display">a + c > b</script>. </p>
<p>The simplest method to check this is to consider every possible triplet in the given <script type="math/tex; mode=display">nums</script> array and checking if the triplet satisfies the three inequalities mentioned above. Thus, we can keep a track of the <script type="math/tex; mode=display">count</script> of the number of triplets satisfying these inequalities. When all the triplets have been considered, the <script type="math/tex; mode=display">count</script> gives the required result.</p>
<iframe src="https://leetcode.com/playground/RNWbLEyd/shared" frameborder="0" width="100%" height="293" name="RNWbLEyd"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>. Three nested loops are there to check every triplet.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-binary-search">Approach 2: Using Binary Search</h4>
<p><strong>Algorithm</strong></p>
<p>If we sort the given <script type="math/tex; mode=display">nums</script> array once, we can solve the given problem in a better way. This is because, if we consider a triplet <script type="math/tex; mode=display">(a, b, c)</script> such that <script type="math/tex; mode=display">a &leq; b &leq; c</script>, we need not check all the three inequalities for checking the validity of the triangle formed by them. But, only one condition <script type="math/tex; mode=display">a + b > c</script> would suffice. This happens because <script type="math/tex; mode=display">c &geq; b</script> and <script type="math/tex; mode=display">c &geq; a</script>. Thus, adding any number to <script type="math/tex; mode=display">c</script> will always produce a sum which is greater than either <script type="math/tex; mode=display">a</script> or <script type="math/tex; mode=display">b</script> considered alone. Thus, the inequalities <script type="math/tex; mode=display">c + a > b</script> and <script type="math/tex; mode=display">c + b > a</script> are satisfied implicitly by virtue of the  property <script type="math/tex; mode=display">a < b < c</script>.</p>
<p>From this, we get the idea that we can sort the given <script type="math/tex; mode=display">nums</script> array. Then, for every pair <script type="math/tex; mode=display">(nums[i], nums[j])</script> considered starting from the beginning of the array, such that <script type="math/tex; mode=display">j > i</script>(leading to <script type="math/tex; mode=display">nums[j] &geq; nums[i]</script>), we can find out the count of elements <script type="math/tex; mode=display">nums[k]</script>(<script type="math/tex; mode=display">k > j</script>), which satisfy the inequality <script type="math/tex; mode=display">nums[k] > nums[i] + nums[j]</script>. We can do so for every pair <script type="math/tex; mode=display">(i, j)</script> considered and get the required result.</p>
<p>We can also observe that, since we've sorted the <script type="math/tex; mode=display">nums</script> array, as we traverse towards the right for choosing the index <script type="math/tex; mode=display">k</script>(for number <script type="math/tex; mode=display">nums[k]</script>), the value of <script type="math/tex; mode=display">nums[k]</script> could increase or remain the same(doesn't decrease relative to the previous value). Thus, there will exist a right limit on the value of index <script type="math/tex; mode=display">k</script>, such that the elements satisfy <script type="math/tex; mode=display">nums[k] > nums[i] + nums[j]</script>. Any elements beyond this value of <script type="math/tex; mode=display">k</script> won't satisfy this inequality as well, which is obvious.</p>
<p>Thus, if we are able to find this right limit value of <script type="math/tex; mode=display">k</script>(indicating the element just greater than <script type="math/tex; mode=display">nums[i] + nums[j]</script>), we can conclude that all the elements in <script type="math/tex; mode=display">nums</script> array in the range <script type="math/tex; mode=display">(j+1, k-1)</script>(both included) satisfy the required inequality. Thus, the <script type="math/tex; mode=display">count</script> of elements satisfying the inequality will be given by <script type="math/tex; mode=display">(k-1) - (j+1) + 1 = k - j - 1</script>.</p>
<p>Since the <script type="math/tex; mode=display">nums</script> array has been sorted now, we can make use of Binary Search to find this right limit of <script type="math/tex; mode=display">k</script>. The following animation shows how Binary Search can be used to find the right limit for a simple example.</p>
<p>!?!../Documents/Valid_Triangle_Binary.json:1000,563!?!</p>
<p>Another point to be observed is that once we find a right limit index <script type="math/tex; mode=display">k_{(i,j)}</script> for a particular pair <script type="math/tex; mode=display">(i, j)</script> chosen, when we choose a higher value of <script type="math/tex; mode=display">j</script> for the same value of <script type="math/tex; mode=display">i</script>, we need not start searching for the right limit <script type="math/tex; mode=display">k_{(i,j+1)}</script> from the index <script type="math/tex; mode=display">j+2</script>. Instead, we can start off from the index <script type="math/tex; mode=display">k_{(i,j)}</script> directly where we left off for the last <script type="math/tex; mode=display">j</script> chosen. </p>
<p>This holds correct because when we choose a higher value of <script type="math/tex; mode=display">j</script>(higher or equal <script type="math/tex; mode=display">nums[j]</script> than the previous one), all the <script type="math/tex; mode=display">nums[k]</script>, such that <script type="math/tex; mode=display">k < k_{(i,j)}</script> will obviously satisfy <script type="math/tex; mode=display">nums[i] + nums[j] > nums[k]</script> for the new value of <script type="math/tex; mode=display">j</script> chosen.</p>
<p>By taking advantage of this observation, we can limit the range of Binary Search for <script type="math/tex; mode=display">k</script> to shorter values for increasing values of <script type="math/tex; mode=display">j</script> considered while choosing the pairs <script type="math/tex; mode=display">(i, j)</script>.</p>
<iframe src="https://leetcode.com/playground/xn8dMtEH/shared" frameborder="0" width="100%" height="463" name="xn8dMtEH"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2 \log n)</script>. In worst case inner loop will take <script type="math/tex; mode=display">n\log n</script> (binary search applied <script type="math/tex; mode=display">n</script> times).</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log n)</script>. Sorting takes <script type="math/tex; mode=display">O(\log n)</script> space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-linear-scan">Approach 3: Linear Scan</h4>
<p><strong>Algorithm</strong></p>
<p>As discussed in the last approach, once we sort the given <script type="math/tex; mode=display">nums</script> array, we need to find the right limit of the index <script type="math/tex; mode=display">k</script> for a pair of indices <script type="math/tex; mode=display">(i, j)</script> chosen to find the <script type="math/tex; mode=display">count</script> of elements satisfying <script type="math/tex; mode=display">nums[i] + nums[j] > nums[k]</script> for the triplet <script type="math/tex; mode=display">(nums[i], nums[j], nums[k])</script> to form a valid triangle. </p>
<p>We can find this right limit by simply traversing the index <script type="math/tex; mode=display">k</script>'s values starting from the index <script type="math/tex; mode=display">k=j+1</script> for a pair <script type="math/tex; mode=display">(i, j)</script> chosen and stopping at the first value of <script type="math/tex; mode=display">k</script> not satisfying the above inequality. Again, the <script type="math/tex; mode=display">count</script> of elements <script type="math/tex; mode=display">nums[k]</script> satisfying <script type="math/tex; mode=display">nums[i] + nums[j] > nums[k]</script> for the pair of indices <script type="math/tex; mode=display">(i, j)</script> chosen is given by <script type="math/tex; mode=display">k - j - 1</script> as discussed in the last approach.</p>
<p>Further, as discussed in the last approach, when we choose a higher value of index <script type="math/tex; mode=display">j</script> for a particular <script type="math/tex; mode=display">i</script> chosen, we need not start from the index <script type="math/tex; mode=display">j + 1</script>. Instead, we can start off directly from the value of <script type="math/tex; mode=display">k</script> where we left for the last index <script type="math/tex; mode=display">j</script>. This helps to save redundant computations.</p>
<p>The following animation depicts the process:</p>
<p>!?!../Documents/Valid_Triangle_Linear.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/Djhygc6q/shared" frameborder="0" width="100%" height="310" name="Djhygc6q"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Loop of <script type="math/tex; mode=display">k</script> and <script type="math/tex; mode=display">j</script> will be executed <script type="math/tex; mode=display">O(n^2)</script> times in total, because, we do not reinitialize the value of <script type="math/tex; mode=display">k</script> for a new value of <script type="math/tex; mode=display">j</script> chosen(for the same <script type="math/tex; mode=display">i</script>). Thus the complexity will be <script type="math/tex; mode=display">O(n^2+n^2)=O(n^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log n)</script>. Sorting takes <script type="math/tex; mode=display">O(\log n)</script> space.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>