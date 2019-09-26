<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-collectionsort">Approach 1: Using Collection.sort()</a></li>
<li><a href="#approach-2-binary-search-and-two-pointers">Approach 2: Binary Search and Two Pointers</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-collectionsort">Approach 1: Using Collection.sort()</h4>
<p><strong>Algorithm</strong></p>
<p>Intuitively, we can sort the elements in list <code>arr</code> by their absolute difference values to the target <code>x</code>. Then the sublist of the first k elements is the result after sorting the elements by the natural order.</p>
<iframe src="https://leetcode.com/playground/pPUrT4oY/shared" frameborder="0" width="100%" height="157" name="pPUrT4oY"></iframe>

<p>Note: This solution is inspired by <a href="https://discuss.leetcode.com/user/compton_scatter">@compton_scatter</a>.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n\log n)</script>. Collections.sort() uses binary sort so it has a <script type="math/tex; mode=display">O(n\log n)</script> complexity.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(k)</script>. The in-place sorting does not consume any extra space. However, generating a k length sublist will take some space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-binary-search-and-two-pointers">Approach 2: Binary Search and Two Pointers</h4>
<p><strong>Algorithm</strong></p>
<p>The original array has been sorted so we can take this advantage by the following steps.
1. If the target <code>x</code> is less or equal than the first element in the sorted array, the first <code>k</code> elements are the result.
2. Similarly, if the target <code>x</code> is more or equal than the last element in the sorted array, the last <code>k</code> elements are the result.
3. Otherwise, we can use binary search to find the <code>index</code> of the element, which is equal (when this list has <code>x</code>) or a little bit larger than <code>x</code> (when this list does not have it). Then set <code>low</code> to its left <code>k-1</code> position, and <code>high</code> to the right <code>k-1</code> position of this <code>index</code> as a start. The desired k numbers must in this rang [index-k-1, index+k-1]. So we can shrink this range to get the result using the following rules.
    * If <code>low</code> reaches the lowest index <code>0</code> or the <code>low</code> element is closer to <code>x</code> than the <code>high</code> element, decrease the <code>high</code> index.
    * If <code>high</code> reaches to the highest index <code>arr.size()-1</code> or it is nearer to <code>x</code> than the <code>low</code> element, increase the <code>low</code> index.
    * The looping ends when there are exactly k elements in [low, high], the subList of which is the result.</p>
<iframe src="https://leetcode.com/playground/kS5bGpg6/shared" frameborder="0" width="100%" height="480" name="kS5bGpg6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log n +k)</script>. <script type="math/tex; mode=display">O(\log n)</script> is for the time of binary search, while <script type="math/tex; mode=display">O(k)</script> is for shrinking the index range to k elements.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(k)</script>. It is to generate the required sublist.</p>
</li>
</ul>
<p>Analysis written by: <a href="https://discuss.leetcode.com/user/mr-bin">@Mr.Bin</a></p>
          </div>
        
      </div>