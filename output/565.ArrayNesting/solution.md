<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-using-visited-array-accepted">Approach #2 Using Visited Array [Accepted]</a></li>
<li><a href="#approach-3-without-using-extra-space-accepted">Approach #3 Without Using Extra Space [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p>The simplest method is to iterate over all the indices of the given <script type="math/tex; mode=display">nums</script> array. For every index <script type="math/tex; mode=display">i</script> chosen, we find the element <script type="math/tex; mode=display">nums[i]</script> and increment the <script type="math/tex; mode=display">count</script> for a new element added for the current index <script type="math/tex; mode=display">i</script>. Since <script type="math/tex; mode=display">nums[i]</script> has to act as the new index for finding the next element belonging to the set corresponding to the index <script type="math/tex; mode=display">i</script>, the new index is <script type="math/tex; mode=display">j=nums[i]</script>.</p>
<p>We continue this process of index updation and keep on incrementing the <script type="math/tex; mode=display">count</script> for new elements added to the set corresponding to the index <script type="math/tex; mode=display">i</script>. Now, since all the elements in <script type="math/tex; mode=display">nums</script> lie in the range <script type="math/tex; mode=display">(0,..., N-1)</script>, the new indices generated will never lie outside the array size limits. But, we'll always reach a point where the current element becomes equal to the element  <script type="math/tex; mode=display">nums[i]</script> with which we started the nestings in the first place. Thus, after this, the new indices generated will be just the repetitions of the previously generated ones, and thus would not lead to an increase in the size of the current set. Thus, this condition of the current number being equal to the starting number acts as the terminating condition for <script type="math/tex; mode=display">count</script> incrementation for a particular index.</p>
<p>We do the same process for every index chosen as the starting index. At the end, the maximum value of <script type="math/tex; mode=display">count</script> obtained gives the size of the largest set.</p>
<iframe src="https://leetcode.com/playground/K6QuRdnw/shared" frameborder="0" name="K6QuRdnw" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. In worst case, for example- <code>[1,2,3,4,5,0]</code>, loop body will be executed <script type="math/tex; mode=display">n^2</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-visited-array-accepted">Approach #2 Using Visited Array [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we observed that in the worst case, all the elements of the <script type="math/tex; mode=display">nums</script> array are added to the sets corresponding to all the starting indices. But, all these sets correspond to the same set of elements only, leading to redundant calculations.</p>
<p>We consider a simple example and see how this problem can be resolved. From the figure below, we can see that the elements in the current nesting shown by arrows form a cycle. Thus, the same elements will be added to the current set irrespective of the first element chosen to be added to the set out of these marked elements.</p>
<p><img alt="Array_Nesting" src="../Figures/565/Array_Nesting.PNG"></p>
<p>Thus, when we add an element <script type="math/tex; mode=display">nums[j]</script> to a set corresponding to any of the indices, we mark its position as visited in a <script type="math/tex; mode=display">visited</script> array. This is done so that whenever this index is chosen as the starting index in the future, we do not go for redundant <script type="math/tex; mode=display">count</script> calculations, since we've already considered the elements linked with this index, which will be added to a new(duplicate) set.</p>
<p>By doing so, we ensure that the duplicate sets aren't considered again and again.</p>
<p>Further, we can also observe that no two elements at indices <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> will lead to a jump to the same index <script type="math/tex; mode=display">k</script>, since it would require <script type="math/tex; mode=display">nums[i] = nums[j] = k</script>, which isn't possible since all the elements are distinct. Also, because of the same reasoning, no element outside any cycle could lead to an element inside the cycle. Because of this, the use of <script type="math/tex; mode=display">visited</script> array goes correctly. </p>
<iframe src="https://leetcode.com/playground/XQA6FiH7/shared" frameborder="0" name="XQA6FiH7" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Every element of the <script type="math/tex; mode=display">nums</script> array will be considered atmost once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">visited</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-without-using-extra-space-accepted">Approach #3 Without Using Extra Space [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, the <script type="math/tex; mode=display">visited</script> array is used just to keep a track of the elements of the array which have already been visited. Instead of making use of a separate array to keep track of the same, we can mark the visited elements in the original array <script type="math/tex; mode=display">nums</script> itself. Since, the range of the elements can only be between 1 to 20,000, we can put a very large integer value <script type="math/tex; mode=display">\text{Integer.MAX_VALUE}</script> at the position which has been visited. The rest process of traversals remains the same as in the last approach.</p>
<iframe src="https://leetcode.com/playground/7DmKnygx/shared" frameborder="0" name="7DmKnygx" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Every element of the <script type="math/tex; mode=display">nums</script> array will be considered atmost once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant Space is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>