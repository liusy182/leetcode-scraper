<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-binary-search">Approach 1: Binary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-binary-search">Approach 1: Binary Search</h4>
<p><strong>Intuition</strong></p>
<p>A very brute way of solving this question is to search the entire array and find the minimum element. The time complexity for that would be <script type="math/tex; mode=display">O(N)</script> given that <code>N</code> is the size of the array.</p>
<p>A very cool way of solving this problem is using the <code>Binary Search</code> algorithm. In binary search we find out the mid point and decide to either search on the left or right depending on some condition.</p>
<p>Since the given array is sorted, we can make use of binary search. However, the array is rotated. So simply applying the binary search won't work here.</p>
<p>In this question we would essentially apply a modified version of binary search where the <code>condition</code> that decides the search direction would be different than in a standard binary search.</p>
<p>We want to find the smallest element in a rotated sorted array. What if the array is not rotated? How do we check that?</p>
<p>If the array is not rotated and the array is in ascending order, then <code>last element &gt; first element</code>.</p>
<p></p><center>
<img src="../Figures/153/153_Minimum_Rotated_Sorted_Array_1.png" width="500">
</center>
<p>In the above example <code>7 &gt; 2</code>. This means that the array is still sorted and has no rotation.</p>
<p></p><center>
<img src="../Figures/153/153_Minimum_Rotated_Sorted_Array_2.png" width="500">
</center>
<p>In the above example <code>3 &lt; 4</code>. Hence the array is rotated. This happens because the array was initially <code>[2, 3 ,4 ,5 ,6 ,7]</code>. But after the rotation the smaller elements<code>[2,3]</code> go at the back. i.e. [4, 5, 6, 7, <code>2, 3]</code>. Because of this the first element <code>[4]</code> in the rotated array becomes greater than the last element.</p>
<p>This means there is a point in the array at which you would notice a change. This is the point which would help us in this question. We call this the <code>Inflection Point</code>.</p>
<p></p><center>
<img src="../Figures/153/153_Minimum_Rotated_Sorted_Array_3.png" width="500">
</center>
<p>In this modified version of binary search algorithm, we are looking for this point. In the above example notice the <code>Inflection Point</code> .</p>
<blockquote>
<p>All the elements to the left of inflection point &gt; first element of the array.<br>
All the elements to the right of inflection point &lt; first element of the array.</p>
</blockquote>
<p><strong>Algorithm</strong></p>
<ol>
<li>
<p>Find the <code>mid</code> element of the array.</p>
</li>
<li>
<p>If <code>mid element &gt; first element of array</code> this means that we need to look for the inflection point on the right of <code>mid</code>.</p>
</li>
<li>If <code>mid element &lt; first element of array</code> this that we need to look for the inflection point on the left of <code>mid</code>.</li>
</ol>
<p></p><center>
<img src="../Figures/153/153_Minimum_Rotated_Sorted_Array_4.png" width="500">
</center>
<p>In the above example mid element <code>6</code> is greater than first element <code>4</code>. Hence we continue our search for the inflection point to the right of mid.</p>
<p>4 . We stop our search when we find the inflection point, when either of the two conditions is satisfied:</p>
<p><code>nums[mid] &gt; nums[mid + 1]</code> Hence, <strong>mid+1</strong> is the smallest.</p>
<p><code>nums[mid - 1] &gt; nums[mid]</code> Hence, <strong>mid</strong> is the smallest.</p>
<p></p><center>
<img src="../Figures/153/153_Minimum_Rotated_Sorted_Array_5.png" width="500">
</center>
<p>In the above example. With the marked left and right pointers. The mid element is <code>2</code>. The element just before <code>2</code> is <code>7</code> and <code>7&gt;2</code> i.e. <code>nums[mid - 1] &gt; nums[mid]</code>. Thus we have found the point of inflection and <code>2</code> is the smallest element.</p>
<iframe src="https://leetcode.com/playground/58ro3AWf/shared" frameborder="0" width="100%" height="500" name="58ro3AWf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity : Same as Binary Search <script type="math/tex; mode=display">O(\log N)</script>
</li>
<li>Space Complexity : <script type="math/tex; mode=display">O(1)</script>
<br><br></li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>