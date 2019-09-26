<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-single-pass-approach">Approach 2: Single Pass Approach</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>We need to find the next lexicographic permutation of the given list of numbers than the number formed by the given array.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>In this approach, we find out every possible permutation of list formed by the elements of the given array and find out the permutation which is
just larger than the given one. But this one will be a very naive approach, since it requires us to find out every possible permutation
 which will take really long time and the implementation is complex.
 Thus, this approach is not acceptable at all. Hence, we move on directly to the correct approach.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n!)</script>. Total possible permutations is <script type="math/tex; mode=display">n!</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Since an array will be used to store the permutations.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-single-pass-approach">Approach 2: Single Pass Approach</h4>
<p><strong>Algorithm</strong></p>
<p>First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.
 For example, no next permutation is possible for the following array:
 <code>[9, 5, 4, 3, 1]</code></p>
<p>We need to find the first pair of two successive numbers <script type="math/tex; mode=display">a[i]</script> and <script type="math/tex; mode=display">a[i-1]</script>, from the right, which satisfy
 <script type="math/tex; mode=display">a[i] > a[i-1]</script>. Now, no rearrangements to the right of <script type="math/tex; mode=display">a[i-1]</script> can create a larger permutation since that subarray consists of numbers in descending order.
 Thus, we need to rearrange the numbers to the right of <script type="math/tex; mode=display">a[i-1]</script> including itself.</p>
<p>Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number <script type="math/tex; mode=display">a[i-1]</script> with the number which is just larger than itself among the numbers lying to its right section, say <script type="math/tex; mode=display">a[j]</script>.</p>
<p><img alt=" Next Permutation " src="https://leetcode.com/media/original_images/31_nums_graph.png"></p>
<p>We swap the numbers <script type="math/tex; mode=display">a[i-1]</script> and <script type="math/tex; mode=display">a[j]</script>. We now have the correct number at index <script type="math/tex; mode=display">i-1</script>. But still the current permutation isn't the permutation
    that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of <script type="math/tex; mode=display">a[i-1]</script>. Therefore, we need to place those
     numbers in ascending order to get their smallest permutation.</p>
<p>But, recall that while scanning the numbers from the right, we simply kept decrementing the index
      until we found the pair <script type="math/tex; mode=display">a[i]</script> and <script type="math/tex; mode=display">a[i-1]</script> where,  <script type="math/tex; mode=display">a[i] > a[i-1]</script>. Thus, all numbers to the right of <script type="math/tex; mode=display">a[i-1]</script> were already sorted in descending order.
      Furthermore, swapping <script type="math/tex; mode=display">a[i-1]</script> and <script type="math/tex; mode=display">a[j]</script> didn't change that order.
      Therefore, we simply need to reverse the numbers following <script type="math/tex; mode=display">a[i-1]</script> to get the next smallest lexicographic permutation.</p>
<p>The following animation will make things clearer:</p>
<p><img alt="Next Permutation" src="https://leetcode.com/media/original_images/31_Next_Permutation.gif"></p>
<iframe src="https://leetcode.com/playground/tJPs3ERV/shared" frameborder="0" width="100%" height="500" name="tJPs3ERV"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. In worst case, only two scans of the whole array are needed.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used. In place replacements are done.</p>
</li>
</ul>
          </div>
        
      </div>