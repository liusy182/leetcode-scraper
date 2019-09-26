<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#hints">Hints</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-pointers">Approach 1: Two Pointers</a></li>
<li><a href="#approach-2-two-pointers-when-elements-to-remove-are-rare">Approach 2: Two Pointers - when elements to remove are rare</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This is a pretty easy problem, but one may get confused by the term "in-place" and think it is impossible to remove an element from the array without making a copy of the array.</p>
<h2 id="hints">Hints</h2>
<ol>
<li>Try two pointers.</li>
<li>Did you use the fact that the order of elements can be changed?</li>
<li>What happens when the elements to remove are rare?</li>
</ol>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-pointers">Approach 1: Two Pointers</h4>
<p><strong>Intuition</strong></p>
<p>Since this question is asking us to remove all elements of the given value in-place, we have to handle it with <script type="math/tex; mode=display">O(1)</script> extra space. How to solve it? We can keep two pointers <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script>, where <script type="math/tex; mode=display">i</script> is the slow-runner while <script type="math/tex; mode=display">j</script> is the fast-runner.</p>
<p><strong>Algorithm</strong></p>
<p>When <script type="math/tex; mode=display">nums[j]</script> equals to the given value, skip this element by incrementing <script type="math/tex; mode=display">j</script>. As long as <script type="math/tex; mode=display">nums[j] \neq val</script>, we copy <script type="math/tex; mode=display">nums[j]</script> to <script type="math/tex; mode=display">nums[i]</script> and increment both indexes at the same time. Repeat the process until <script type="math/tex; mode=display">j</script> reaches the end of the array and the new length is <script type="math/tex; mode=display">i</script>.</p>
<p>This solution is very similar to the solution to <a href="https://leetcode.com/articles/remove-duplicates-from-sorted-array/">Remove Duplicates from Sorted Array</a>.</p>
<iframe src="https://leetcode.com/playground/5ypGn6XG/shared" frameborder="0" width="100%" height="225" name="5ypGn6XG"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
Assume the array has a total of <script type="math/tex; mode=display">n</script> elements, both <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> traverse at most <script type="math/tex; mode=display">2n</script> steps.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pointers-when-elements-to-remove-are-rare">Approach 2: Two Pointers - when elements to remove are rare</h4>
<p><strong>Intuition</strong></p>
<p>Now consider cases where the array contains few elements to remove. For example, <script type="math/tex; mode=display">nums = [1,2,3,5,4], val = 4</script>. The previous algorithm will do unnecessary copy operation of the first four elements. Another example is <script type="math/tex; mode=display">nums = [4,1,2,3,5], val = 4</script>. It seems unnecessary to move elements <script type="math/tex; mode=display">[1,2,3,5]</script> one step left as the problem description mentions that the order of elements could be changed.</p>
<p><strong>Algorithm</strong></p>
<p>When we encounter <script type="math/tex; mode=display">nums[i] = val</script>, we can swap the current element out with the last element and dispose the last one. This essentially reduces the array's size by 1.</p>
<p>Note that the last element that was swapped in could be the value you want to remove itself. But don't worry, in the next iteration we will still check this element.</p>
<iframe src="https://leetcode.com/playground/bNr9hpND/shared" frameborder="0" width="100%" height="293" name="bNr9hpND"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
Both <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">n</script> traverse at most <script type="math/tex; mode=display">n</script> steps. In this approach, the number of assignment operations is equal to the number of elements to remove. So it is more efficient if elements to remove are rare.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>