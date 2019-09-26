<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-binary-search-tree">Approach 2: Binary Search Tree</a></li>
<li><a href="#approach-3-bit">Approach 3: BIT</a></li>
<li><a href="#approach-4-modified-merge-sort">Approach 4: Modified Merge Sort</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>Do as directed in the question. We can simply check all the pairs if they are important reverse pairs or not.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">\text{size} - 1</script>
<ul>
<li>Iterate over <script type="math/tex; mode=display">j</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">i - 1</script>
<ul>
<li>If <script type="math/tex; mode=display">\text{nums[j]} > 2 * \text{nums[i]}</script>, increment <script type="math/tex; mode=display">\text{count}</script>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/WaK47bnJ/shared" frameborder="0" width="100%" height="259" name="WaK47bnJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n^2)</script>
<ul>
<li>We iterate over all the possible pairs wherein (<script type="math/tex; mode=display">i<j</script>) in the array which is <script type="math/tex; mode=display">O(n^2)</script>
</li>
</ul>
</li>
<li>Space complexity: <script type="math/tex; mode=display">O(1)</script> only constant extra space is required for <script type="math/tex; mode=display">n</script>, <script type="math/tex; mode=display">count</script> etc.</li>
</ul>
<p><strong>Trivia</strong></p>
<p>The above code can be expressed as one-liner in Python:</p>
<iframe src="https://leetcode.com/playground/dppX7gUQ/shared" frameborder="0" width="100%" height="89" name="dppX7gUQ"></iframe>

<p>Herein, we iterate over all the pairs and store the boolean values for <script type="math/tex; mode=display">\text{nums[i]}>2*\text{nums[j]}</script>. Finally, we count the number of <script type="math/tex; mode=display">\text{true}</script> in the array and return the result.
<br>
<br></p>
<hr>
<h4 id="approach-2-binary-search-tree">Approach 2: Binary Search Tree</h4>
<p><strong>Intuition</strong></p>
<p>In Approach 1, for each element <script type="math/tex; mode=display">i</script>, we searched the subarray <script type="math/tex; mode=display">[0,i)</script> for elements such that their value is greater than <script type="math/tex; mode=display">2*\text{nums[i]}</script>. In the previous approach, the search is linear. However, we need to make the process efficient. Maybe, memoization can help, but since, we need to compare the elements, we cannot find a linear DP solution.</p>
<p>Observe that the indices of the elements in subarray <script type="math/tex; mode=display">[0,i)</script> don't matter as we only require the count. So, we can sort the elements and perform binary search on the subarray. But, since the subarray keeps growing as we iterate to the next element, we need a data structure to store the previous result as well as to allow efficient searching(preferably <script type="math/tex; mode=display">O(\log n)</script>) - Binary Search Tree(BST) could be a good bet.   </p>
<p><em>Refreshing BST</em></p>
<p>BST is a rooted binary tree, wherein each node is associated with a value and has 2 distinguishable sub-trees namely <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> subtree. The left subtree contains only the nodes with lower values than the parent's value, while the right subtree conatins only the nodes with greater values than the parent's value.</p>
<p><em>Voila!</em></p>
<p>This is exactly what is required. So, if we store our elements in BST, then we can search the larger elements thus eliminating the search on smaller elements altogether.</p>
<p><strong>Algorithm</strong></p>
<p>Define the <script type="math/tex; mode=display">\text{Node}</script> of BST that stores the <script type="math/tex; mode=display">\text{val}</script> and pointers to the <script type="math/tex; mode=display">\text{left}</script> and <script type="math/tex; mode=display">\text{right}</script>. We also need a count of elements(say <script type="math/tex; mode=display">\text{count\_ge}</script>) in the subtree rooted at the current node that are greater than or equal to the current node's <script type="math/tex; mode=display">\text{val}</script>. <script type="math/tex; mode=display">\text{count\_ge}</script> is initialized to 1 for each node and <script type="math/tex; mode=display">\text{left}</script>, <script type="math/tex; mode=display">\text{right}</script> pointers are set to <script type="math/tex; mode=display">\text{NULL}</script>.</p>
<p>We define the <script type="math/tex; mode=display">\text{insert}</script> routine that recursively adds the given <script type="math/tex; mode=display">\text{val}</script> as an appropriate leaf node based on comparisons with the <script type="math/tex; mode=display">Node.val</script>. Each time, the given <script type="math/tex; mode=display">val</script> is smaller than <script type="math/tex; mode=display">Node.val</script>, we increment the <script type="math/tex; mode=display">\text{count\_ge}</script> and move the <script type="math/tex; mode=display">val</script> to the right subtree. While, if the <script type="math/tex; mode=display">val</script> is equal to the current <script type="math/tex; mode=display">Node</script>, we simply increment the <script type="math/tex; mode=display">\text{count\_ge}</script> and exit. While, we move to the left subtree in case <script type="math/tex; mode=display">(\text{val}<\text{Node.val})</script>.</p>
<p>We also require the <script type="math/tex; mode=display">search</script> routine that gives the count of number of elements greater than or equal to the <script type="math/tex; mode=display">\text{target}</script>. In the <script type="math/tex; mode=display">\text{search}</script> routine, if the <script type="math/tex; mode=display">head</script> is NULL, return 0. Otherwise, if <script type="math/tex; mode=display">\text{target}==\text{head.val}</script>, we know the count of values greater than or equal to the <script type="math/tex; mode=display">\text{target}</script>, hence simply return <script type="math/tex; mode=display">\text{head.count\_ge}</script>. In case, <script type="math/tex; mode=display">\text{target}<\text{head.val}</script>, the ans is calculated by adding <script type="math/tex; mode=display">\text{Node.count\_ge}</script> and recursively calling the <script type="math/tex; mode=display">\text{search}</script> routine with <script type="math/tex; mode=display">\text{head.left}</script>. And if <script type="math/tex; mode=display">\text{target}>\text{head.val}</script>, ans is obtained by recursively calling the <script type="math/tex; mode=display">\text{search}</script> routine with <script type="math/tex; mode=display">\text{head.right}</script>.</p>
<p>Now, we can get to our main logic:</p>
<ul>
<li>Iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">(size-1)</script> of <script type="math/tex; mode=display">\text{nums}</script> :<ul>
<li>Search the existing BST for <script type="math/tex; mode=display">\text{nums[i]} * 2 + 1</script> and add the result to <script type="math/tex; mode=display">\text{count}</script>
</li>
<li>Insert <script type="math/tex; mode=display">\text{nums[i]}</script> to the BST, hence updating the <script type="math/tex; mode=display">\text{count\_ge}</script> of the previous nodes</li>
</ul>
</li>
</ul>
<p>The algorithm can be better understood using the example below:
!?!../Documents/493_reverse_pairs.json:1000,662!?!</p>
<iframe src="https://leetcode.com/playground/uFc7tCxm/shared" frameborder="0" width="100%" height="500" name="uFc7tCxm"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n^2)</script>
<ul>
<li>The best case complexity for BST is <script type="math/tex; mode=display">O(\log n)</script> for search as well as insertion, wherein, the tree formed is complete binary tree</li>
<li>Whereas, in case like [1,2,3,4,5,6,7,8,...], insertion as well as search for an element becomes <script type="math/tex; mode=display">O(n)</script> in time, since, the tree is skewed in only one direction, and hence, is no better than the array</li>
<li>So, in worst case, for searching and insertion over n items, the complexity is <script type="math/tex; mode=display">O(n*n)</script>
</li>
</ul>
</li>
<li>Space complexity: <script type="math/tex; mode=display">O(n)</script> extra space for storing the BST in <script type="math/tex; mode=display">\text{Node}</script> class.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-3-bit">Approach 3: BIT</h4>
<p><strong>Intuition</strong></p>
<p>The problem with BST is that the tree can be skewed hence, making it <script type="math/tex; mode=display">O(n^2)</script> in complexity. So, need a data structure that remains balanced. We could either use a Red-black or AVL tree to make a balanced BST, but the implementation would be an overkill for the solution. We can use BIT (Binary Indexed Tree, also called Fenwick Tree) to ensure that the complexity is <script type="math/tex; mode=display">O(n\log n)</script> with only 12-15 lines of code.</p>
<p><em>BIT Overview:</em></p>
<p>Fenwick Tree or BIT provides a way to represent an array of numbers in an array(can be visualized as tree), allowing prefix/suffix sums to be calculated efficiently(<script type="math/tex; mode=display">O(\log n)</script>). BIT allows to update an element in <script type="math/tex; mode=display">O(\log n)</script> time.</p>
<p>We recommend having a look at BIT from the following links before getting into details:</p>
<ul>
<li><a href="https://www.youtube.com/watch?v=CWDQJGaN1gY">https://www.youtube.com/watch?v=CWDQJGaN1gY</a></li>
<li><a href="https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/">https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/</a></li>
</ul>
<p>So, BIT is very useful to accumulate information from front/back and hence, we can use it in the same way we used BST to get the count of elements that are greater than or equal to <script type="math/tex; mode=display">2 * \text{nums[i]} + 1</script> in the existing tree and then adding the current element to the tree.</p>
<p><strong>Algorithm</strong></p>
<p>First, lets review the BIT <script type="math/tex; mode=display">\text{query}</script> and <script type="math/tex; mode=display">\text{update}</script> routines of BIT. According to the convention, <script type="math/tex; mode=display">\text{query}</script> routine goes from <script type="math/tex; mode=display">\text{index}</script> to <script type="math/tex; mode=display">0</script>, i.e., <script type="math/tex; mode=display">\text{BIT[i]}</script> gives the sum for the range <script type="math/tex; mode=display">[0,index]</script>, and <script type="math/tex; mode=display">\text{update}</script> updates the values from current <script type="math/tex; mode=display">\text{index}</script> to the end of array. But, since, we require to find the numbers greater than the given index, as and when we update an index, we update all the ancestors of the node in the tree, and for <script type="math/tex; mode=display">\text{search}</script>, we go from the node to the end.   </p>
<p>The modified <script type="math/tex; mode=display">\text{update}</script> algorithm is:</p>
<div class="codehilite"><pre><span></span>update(BIT,index, val):
  while(index&lt;0):
    BIT[index]+=val
    index-=(index&amp;(-index))
</pre></div>


<p>Herein, we find get the next index using: <script type="math/tex; mode=display">\text{index-=index&(-index)}</script>, which is essentially subtracting the rightmost 1 from the <script type="math/tex; mode=display">\text{index}</script> binary representation. We update the previous indices since, if an element is greater than the index</p>
<p>And the modified <script type="math/tex; mode=display">\text{query}</script> algorithm is:</p>
<div class="codehilite"><pre><span></span>query(BIT,index):
  sum=0
  while(index&lt;BIT.size):
    sum+=BIT[index]
    index+=(index&amp;(-index))
</pre></div>


<p>Herein, we find get the next index using: <script type="math/tex; mode=display">\text{index+=index&(-index)}</script>. This gives the suffix sum from <script type="math/tex; mode=display">index</script> to the end.</p>
<p>So, the main idea is to count the number of elements greater than <script type="math/tex; mode=display">2*\text{nums[i]}</script> in range <script type="math/tex; mode=display">[0,i)</script> as we iterate from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">\text{size-1}</script>. The steps are as follows:</p>
<ul>
<li>Create a copy of <script type="math/tex; mode=display">\text{nums}</script>, say <script type="math/tex; mode=display">\text{nums\_copy}</script> ans sort <script type="math/tex; mode=display">\text{nums\_copy}</script>. This array is actually used for creating the Binary indexed tree</li>
<li>Initialize <script type="math/tex; mode=display">\text{count}=0</script> and <script type="math/tex; mode=display">\text{BIT}</script> array of size <script type="math/tex; mode=display">\text{size(nums)} + 1</script> to store the BIT</li>
<li>Iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">\text{size(nums)}-1</script> :<ul>
<li>Search the index of element not less than <script type="math/tex; mode=display">2*\text{nums[i]}+1</script> in <script type="math/tex; mode=display">\text{nums\_copy}</script> array. <script type="math/tex; mode=display">\text{query}</script> the obtained index+1 in the <script type="math/tex; mode=display">\text{BIT}</script>, and add the result to <script type="math/tex; mode=display">\text{count}</script>
</li>
<li>Search for the index of element not less than <script type="math/tex; mode=display">nums[i]</script> in <script type="math/tex; mode=display">\text{nums\_copy}</script>. We need to <script type="math/tex; mode=display">\text{update}</script> the BIT for this index by 1. This essentially means that 1 is added to this index(or number of elements greater than this index is incremented). The effect of adding <script type="math/tex; mode=display">1</script> to the index is passed to the ancestors as shown in <script type="math/tex; mode=display">\text{update}</script> algorithm</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/VGR92H8T/shared" frameborder="0" width="100%" height="500" name="VGR92H8T"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n\log n)</script>
<ul>
<li>In <script type="math/tex; mode=display">\text{query}</script> and <script type="math/tex; mode=display">\text{update}</script> operations, we see that the loop iterates at most the number of bits in <script type="math/tex; mode=display">\text{index}</script> which can be at most <script type="math/tex; mode=display">n</script>. Hence, the complexity of both the operations is <script type="math/tex; mode=display">O(\log n)</script>(Number of bits in <script type="math/tex; mode=display">n</script> is <script type="math/tex; mode=display">\log n</script>)</li>
<li>The in-built operation <script type="math/tex; mode=display">\text{lower\_bound}</script> is binary search hence <script type="math/tex; mode=display">O(\log n)</script>
</li>
<li>We perform the operations for <script type="math/tex; mode=display">n</script> elements, hence the total complexity is <script type="math/tex; mode=display">O(n\log n)</script>
</li>
</ul>
</li>
<li>Space complexity: <script type="math/tex; mode=display">O(n)</script>. Additional space for <script type="math/tex; mode=display">\text{BITS}</script> array
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-4-modified-merge-sort">Approach 4: Modified Merge Sort</h4>
<p><strong>Intuition</strong></p>
<p>In BIT and BST, we iterate over the array, dividing the array into 3 sections: already visited and hence added to the tree, current node and section to be visited. Another approach could be divide the problem into smaller subproblems, solving them and combining these problems to get the final result - Divide and conquer. We see that the problem has a great resemblance to the merge sort routine. The question is to find the inversions such that <script type="math/tex; mode=display">\text{nums[i]}>2 * \text{nums[j]}</script> and <script type="math/tex; mode=display">i<j</script>. So, we can easily modify the merge sort to count the inversions as required.</p>
<p><em>Mergesort</em></p>
<p>Mergesort is a divide-and-conquer based sorting technique that operates in <script type="math/tex; mode=display">O(n\log n)</script> time. The basic idea to divide the array into several sub-arrays until each sub-array is single element long and merging these sublists recursively that results in the final sorted array.</p>
<p><strong>Algorithm</strong></p>
<p>We define <script type="math/tex; mode=display">\text{mergesort\_and\_count}</script> routine that takes parameters an array say <script type="math/tex; mode=display">A</script> and <script type="math/tex; mode=display">\text{start}</script> and <script type="math/tex; mode=display">\text{end}</script> indices:</p>
<ul>
<li>If <script type="math/tex; mode=display">\text{start}</script>&gt;=<script type="math/tex; mode=display">\text{end}</script> this implies that elements can no longer be broken further and hence we return 0</li>
<li>Otherwise, set <script type="math/tex; mode=display">\text{mid}=(\text{start} + \text{end})/2</script>
</li>
<li>Store <script type="math/tex; mode=display">count</script> by recursively calling <script type="math/tex; mode=display">\text{mergesort\_and\_count}</script> on range <script type="math/tex; mode=display">\text{[start,mid]}</script> and <script type="math/tex; mode=display">\text{[mid+1,end]}</script> and adding the results. This is the divide step on our routine, breaking it into the 2 ranges, and finding the results for each range separately</li>
<li>Now, we that we have separately calculated the results for ranges <script type="math/tex; mode=display">\text{[start,mid]}</script> and <script type="math/tex; mode=display">\text{[mid+1,end]}</script>, but we still have to count the elements in <script type="math/tex; mode=display">\text{[start,mid]}</script> that are greater than 2 * elements in <script type="math/tex; mode=display">\text{[mid+1,end]}</script>. Count all such elements and add the result to <script type="math/tex; mode=display">\text{count}</script>
</li>
<li>Finally, <script type="math/tex; mode=display">\text{merge}</script> the array from <script type="math/tex; mode=display">\text{start}</script> to <script type="math/tex; mode=display">\text{end}</script>
<ul>
<li>Make 2 array : <script type="math/tex; mode=display">L</script> from elements in range <script type="math/tex; mode=display">\text{[start,mid]}</script> and <script type="math/tex; mode=display">R</script> from elements in range <script type="math/tex; mode=display">\text{R[mid+1,end]}</script>
</li>
<li>Keep pointers <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> to <script type="math/tex; mode=display">L</script> and <script type="math/tex; mode=display">R</script> respectively both initialized to start to the arrays</li>
<li>Iterate over <script type="math/tex; mode=display">k</script> from <script type="math/tex; mode=display">\text{start}</script> to <script type="math/tex; mode=display">\text{end}</script> and set <script type="math/tex; mode=display">\text{A[k]}</script> to the smaller of <script type="math/tex; mode=display">\text{L[i]}</script> or <script type="math/tex; mode=display">\text{R[j]}</script> and increment the respective index</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/soSDw7xo/shared" frameborder="0" width="100%" height="500" name="soSDw7xo"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n\log n)</script>
<ul>
<li>In each step we divide the array into 2 sub-arrays, and hence, the maximum times we need to divide is equal to <script type="math/tex; mode=display">O(\log n)</script>
</li>
<li>Additional <script type="math/tex; mode=display">O(n)</script> work needs to be done to count the inversions and to merge the 2 sub-arrays after sorting. Hence total time complexity is <script type="math/tex; mode=display">O(n\log n)</script>
</li>
</ul>
</li>
<li>Space complexity: <script type="math/tex; mode=display">O(n)</script>. Additional space for storing <script type="math/tex; mode=display">L</script> and <script type="math/tex; mode=display">R</script> arrays</li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/abhinavbansal0">@abhinavbansal0</a>.</p>
<p>Shoutout to <a href="https://discuss.leetcode.com/user/fun4leetcode">@FUN4LEETCODE</a> for the brilliant post!</p>
          </div>
        
      </div>