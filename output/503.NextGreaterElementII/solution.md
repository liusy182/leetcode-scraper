<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-using-double-length-array-time-limit-exceeded">Approach #1 Brute Force (using Double Length Array) [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-better-brute-force-accepted">Approach #2 Better Brute Force [Accepted]</a></li>
<li><a href="#approach-3-using-stack-accepted">Approach #3 Using Stack [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-using-double-length-array-time-limit-exceeded">Approach #1 Brute Force (using Double Length Array) [Time Limit Exceeded]</h4>
<p>In this method, we make use of an array <script type="math/tex; mode=display">doublenums</script> which is formed by concatenating two copies of the given <script type="math/tex; mode=display">nums</script> array one after the other. Now, when we need to find out the next greater element for <script type="math/tex; mode=display">nums[i]</script>, we can simply scan all the elements <script type="math/tex; mode=display">doublenums[j]</script>, such that <script type="math/tex; mode=display">i < j < length(doublenums)</script>. The first element found satisfying the given condition is the required result for <script type="math/tex; mode=display">nums[i]</script>. If no such element is found, we put a <script type="math/tex; mode=display">\text{-1}</script> at the appropriate position in the <script type="math/tex; mode=display">res</script> array.</p>
<iframe src="https://leetcode.com/playground/tRcR8Lx3/shared" frameborder="0" name="tRcR8Lx3" width="100%" height="377"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. The complete <script type="math/tex; mode=display">doublenums</script> array(of size <script type="math/tex; mode=display">\text{2n}</script>) is scanned for all the elements of <script type="math/tex; mode=display">nums</script> in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">doublenums</script> array of size <script type="math/tex; mode=display">\text{2n}</script> is used. <script type="math/tex; mode=display">res</script> array of size <script type="math/tex; mode=display">\text{n}</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force-accepted">Approach #2 Better Brute Force [Accepted]</h4>
<p>Instead of making a double length copy of <script type="math/tex; mode=display">nums</script> array , we can traverse circularly in the <script type="math/tex; mode=display">nums</script> array by making use of the <script type="math/tex; mode=display">\text{%(modulus)}</script> operator. For every element <script type="math/tex; mode=display">nums[i]</script>, we start searching in the <script type="math/tex; mode=display">nums</script> array(of length <script type="math/tex; mode=display">n</script>) from the index <script type="math/tex; mode=display">(i+1)%n</script> and look at the next(cicularly) <script type="math/tex; mode=display">n-1</script> elements. For <script type="math/tex; mode=display">nums[i]</script> we do so by scanning over <script type="math/tex; mode=display">nums[j]</script>, such that
<script type="math/tex; mode=display">(i+1)%n &leq; j &leq; (i+(n-1))%n</script>, and we look for the first greater element found. If no such element is found, we put a <script type="math/tex; mode=display">\text{-1}</script> at the appropriate position in the <script type="math/tex; mode=display">res</script> array.</p>
<iframe src="https://leetcode.com/playground/LCG759JD/shared" frameborder="0" name="LCG759JD" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. The complete <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> is scanned for all the elements of <script type="math/tex; mode=display">nums</script> in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">res</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-stack-accepted">Approach #3 Using Stack [Accepted]</h4>
<p>This approach makes use of a stack. This stack stores the indices of the appropriate elements from <script type="math/tex; mode=display">nums</script> array.  The top of the stack refers to the index of the Next Greater Element found so far. We store the indices instead of the elements since there could be duplicates in the <script type="math/tex; mode=display">nums</script> array. The description of the method will make the above statement clearer.</p>
<p>We start traversing the <script type="math/tex; mode=display">nums</script> array from right towards the left. For an element <script type="math/tex; mode=display">nums[i]</script> encountered, we pop all the elements
<script type="math/tex; mode=display">stack[top]</script> from the stack such that <script type="math/tex; mode=display">nums\big[stack[top]\big] &le; nums[i]</script>. We continue the popping till we encounter a <script type="math/tex; mode=display">stack[top]</script> satisfying <script type="math/tex; mode=display">nums\big[stack[top]\big] > nums[i]</script>. Now, it is obvious that the current <script type="math/tex; mode=display">stack[top]</script> only can act as the
Next Greater Element for <script type="math/tex; mode=display">nums[i]</script>(right now, considering only the elements lying to the right of <script type="math/tex; mode=display">nums[i]</script>).</p>
<p>If no element remains on the top of the stack, it means no larger element than <script type="math/tex; mode=display">nums[i]</script> exists to its right. Along with this, we also push the index of the element just encountered(<script type="math/tex; mode=display">nums[i]</script>), i.e. <script type="math/tex; mode=display">i</script> over the top of the stack, so that <script type="math/tex; mode=display">nums[i]</script>(or <script type="math/tex; mode=display">stack[top</script>) now acts as the Next Greater Element for the elements lying to its left.</p>
<p>We go through two such passes over the complete <script type="math/tex; mode=display">nums</script> array. This is done so as to complete a circular traversal over the <script type="math/tex; mode=display">nums</script> array. The first pass could make some wrong entries in the <script type="math/tex; mode=display">res</script> array since it considers only the elements lying to the right of <script type="math/tex; mode=display">nums[i]</script>, without a circular traversal. But, these entries are corrected in the second pass.  </p>
<p>Further, to ensure the correctness of the method, let's look at the following cases.</p>
<p>Assume that <script type="math/tex; mode=display">nums[j]</script> is the correct Next Greater Element for <script type="math/tex; mode=display">nums[i]</script>, such that <script type="math/tex; mode=display">i < j &le; stack[top]</script>. Now, whenever we encounter <script type="math/tex; mode=display">nums[j]</script>, if <script type="math/tex; mode=display">nums[j] > nums\big[stack[top]\big]</script>, it would have already popped the previous <script type="math/tex; mode=display">stack[top]</script> and <script type="math/tex; mode=display">j</script> would have become the topmost element. On the other hand, if  <script type="math/tex; mode=display">nums[j] < nums\big[stack[top]\big]</script>, it would have become the topmost element by being pushed above the previous <script type="math/tex; mode=display">stack[top]</script>. In both the cases, if <script type="math/tex; mode=display">nums[j] > nums[i]</script>, it will be correctly determined to be the Next Greater Element.</p>
<p>The following example makes the procedure clear:</p>
<!--![Next_Greater_Element_II](../Figures/503_Next_Greater_Element_II.gif)-->

<p>!?!../Documents/503_Next_Greater2.json:1000,563!?!</p>
<p>As the animation above depicts, after the first pass, there are a number of wrong entries(marked as <script type="math/tex; mode=display">\text{-1}</script>) in the <script type="math/tex; mode=display">res</script> array, because only the elements lying to the corresponding right(non-circular) have been considered till now. But, after the second pass, the correct values are substituted.</p>
<iframe src="https://leetcode.com/playground/in37fqRd/shared" frameborder="0" name="in37fqRd" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Only two traversals of the <script type="math/tex; mode=display">nums</script> array are done. Further, atmost <script type="math/tex; mode=display">\text{2n}</script> elements are pushed and popped from the stack.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. A stack of size <script type="math/tex; mode=display">n</script> is used. <script type="math/tex; mode=display">res</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>