<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-naive">Approach 1: Naive</a></li>
<li><a href="#approach-2-sqrt-decomposition">Approach 2: Sqrt Decomposition</a></li>
<li><a href="#approach-3-segment-tree">Approach 3: Segment Tree</a><ul>
<li><a href="#1-build-segment-tree">1. Build segment tree</a></li>
<li><a href="#2-update-segment-tree">2. Update segment tree</a></li>
<li><a href="#3-range-sum-query">3. Range Sum Query</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#further-thoughts">Further Thoughts</a></li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for intermediate level readers. It introduces the following concepts:
Range sum query, Sqrt decomposition, Segment tree.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-naive">Approach 1: Naive</h4>
<p><strong>Algorithm</strong></p>
<p>A trivial solution for Range Sum Query - <code>RSQ(i, j)</code> is to iterate the array from index <script type="math/tex; mode=display">i</script> to <script type="math/tex; mode=display">j</script> and sum each element.</p>
<iframe src="https://leetcode.com/playground/nzt96HJe/shared" frameborder="0" width="100%" height="276" name="nzt96HJe"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script> - range sum query, <script type="math/tex; mode=display">O(1)</script> - update query</p>
<p>For range sum query we access each element from the array for constant time and in the worst case we access <script type="math/tex; mode=display">n</script> elements. Therefore time complexity is <script type="math/tex; mode=display">O(n)</script>. Time complexity of update query is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-sqrt-decomposition">Approach 2: Sqrt Decomposition</h4>
<p><strong>Intuition</strong></p>
<p>The idea is to  split the array in blocks with length of <script type="math/tex; mode=display">\sqrt{n}</script>. Then we calculate the sum of each block and store it in auxiliary memory <code>b</code>.
To query <code>RSQ(i, j)</code>, we will add the sums of all the blocks lying inside and those that partially overlap with range <script type="math/tex; mode=display">[i \ldots j]</script>.</p>
<p><strong>Algorithm</strong></p>
<p align="center"><img alt="Range sum query using SQRT decomposition" src="https://leetcode.com/media/original_images/307_RSQ_Sqrt.png" width="539px"></p>
<p align="center"><em>Figure 1. Range sum query using SQRT decomposition.</em></p>
<p>In the example above, the array <code>nums</code>'s length is <code>9</code>, which is split into blocks of size <script type="math/tex; mode=display">\sqrt{9}</script>. To get <code>RSQ(1, 7)</code> we add <code>b[1]</code>.  It stores the sum of <code>range [3, 5]</code> and partially sums from <code>block 0</code>  and <code>block 2</code>, which are overlapping boundary blocks.</p>
<iframe src="https://leetcode.com/playground/MViGYc5D/shared" frameborder="0" width="100%" height="500" name="MViGYc5D"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script> - preprocessing, <script type="math/tex; mode=display">O(\sqrt{n})</script> - range sum query, <script type="math/tex; mode=display">O(1)</script> - update query</p>
<p>For range sum query in the worst-case scenario we have to sum approximately <script type="math/tex; mode=display">3 \sqrt{n}</script> elements. In this case the range includes <script type="math/tex; mode=display">\sqrt{n} - 2</script> blocks, which total sum costs <script type="math/tex; mode=display">\sqrt{n} - 2</script> operations. In addition to this we have to add the sum of the two boundary blocks. This takes another <script type="math/tex; mode=display">2 (\sqrt{n} - 1)</script> operations. The total amount of operations is around <script type="math/tex; mode=display">3 \sqrt{n}</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\sqrt{n})</script>.</p>
<p>We need additional <script type="math/tex; mode=display">\sqrt{n}</script> memory to store all block sums.
<br>
<br></p>
<hr>
<h4 id="approach-3-segment-tree">Approach 3: Segment Tree</h4>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>Segment tree is a very flexible data structure, because it is used to solve numerous range query problems like finding minimum, maximum, sum, greatest common divisor, least common denominator in array in logarithmic time.</p>
<p align="center"><img alt="Illustration of Segment tree" src="https://leetcode.com/media/original_images/307_RSQ_SegmentTree.png" width="539px"></p>
<p align="center"><em>Figure 2. Illustration of Segment tree.</em></p>
<p>The segment tree for array <script type="math/tex; mode=display">a[0, 1, \ldots ,n-1]</script> is a binary tree in which each node contains <strong>aggregate</strong> information (min, max, sum, etc.) for a subrange <script type="math/tex; mode=display">[i \ldots j]</script> of the array, as its left and right child hold information for range <script type="math/tex; mode=display">[i \ldots \frac{i+j}{2}]</script> and <script type="math/tex; mode=display">[\frac{i + j}{2} + 1, j]</script>.</p>
<p>Segment tree could be implemented using either an array or a tree. For an array implementation, if the element at index <script type="math/tex; mode=display">i</script> is not a leaf, its left and right child are stored at index <script type="math/tex; mode=display">2i</script> and <script type="math/tex; mode=display">2i + 1</script> respectively.</p>
<p>In the example above (Figure 2), every leaf node contains the initial array elements <code>{2,4,5,7,8,9}</code>. The internal nodes contain the sum of the corresponding elements in range - <code>(11)</code> for the elements from index 0 to index 2. The root <code>(35)</code> being the sum  of its children <code>(6)</code>;<code>(29)</code>, holds the total sum of the entire array.</p>
<p>Segment Tree can be broken down to the three following steps:</p>
<ol>
<li>Pre-processing step which builds the segment tree from a given array.</li>
<li>Update the segment tree when an element is modified.</li>
<li>Calculate the Range Sum Query using the segment tree.</li>
</ol>
<h5 id="1-build-segment-tree">1. Build segment tree</h5>
<p>We will use a very effective bottom-up approach to build segment tree. We already know from the above that if some node <script type="math/tex; mode=display">p</script> holds the sum of <script type="math/tex; mode=display">[i \ldots j]</script> range, its left and right children hold the sum for range <script type="math/tex; mode=display">[i \ldots \frac{i + j}{2}]</script> and <script type="math/tex; mode=display">[\frac{i + j}{2} + 1, j]</script> respectively.</p>
<p>Therefore to find the sum of node <script type="math/tex; mode=display">p</script>, we need to calculate the sum of its right and left child in advance.</p>
<p>We begin from the leaves, initialize them with input array elements <script type="math/tex; mode=display">a[0, 1, \ldots, n-1]</script>. Then we move upward to the higher level to calculate the parents' sum till we get to the root of the segment tree.</p>
<iframe src="https://leetcode.com/playground/EnAGDmuY/shared" frameborder="0" width="100%" height="310" name="EnAGDmuY"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>Time complexity is  <script type="math/tex; mode=display">O(n)</script>, because we calculate the sum of one node during each iteration of the for loop. There are approximately <script type="math/tex; mode=display">2n</script> nodes in a segment tree.</p>
<p>This could be proved in the following way: Segmented tree for array with <script type="math/tex; mode=display">n</script> elements has <script type="math/tex; mode=display">n</script> leaves (the array elements itself). The number of nodes in each level is half the number in the level below.</p>
<p>So if we sum the number by level we will get:</p>
<p>
<script type="math/tex; mode=display">
n + n/2  + n/4 + n/8 + \ldots + 1 \approx 2n
</script>
</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
<p>We used <script type="math/tex; mode=display">2n</script> extra space to store the segment tree.</p>
</li>
</ul>
<h5 id="2-update-segment-tree">2. Update segment tree</h5>
<p>When we update the array at some index <script type="math/tex; mode=display">i</script> we need to rebuild the segment tree, because there are tree nodes which contain the sum of the modified element. Again we will use a bottom-up approach. We update the leaf node that stores <script type="math/tex; mode=display">a[i]</script>. From there we will follow the path up to the root updating the value of each parent as a sum of its children values.</p>
<iframe src="https://leetcode.com/playground/SyzW2D6T/shared" frameborder="0" width="100%" height="327" name="SyzW2D6T"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log n)</script>.</p>
<p>Algorithm  has <script type="math/tex; mode=display">O(\log n)</script> time complexity, because there are a few tree nodes with range that include  <script type="math/tex; mode=display">i</script>th array element, one on each level. There are <script type="math/tex; mode=display">\log(n)</script>  levels.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<h5 id="3-range-sum-query">3. Range Sum Query</h5>
<p>We can find range sum query  <script type="math/tex; mode=display">[L, R]</script> using segment tree in the following way:</p>
<p>Algorithm hold loop invariant:</p>
<p>
<script type="math/tex; mode=display">l \le r</script> and sum of <script type="math/tex; mode=display">[L \ldots l]</script> and <script type="math/tex; mode=display">[r \ldots R]</script> has been calculated, where <script type="math/tex; mode=display">l</script> and <script type="math/tex; mode=display">r</script> are the left and right boundary of calculated sum.
Initially we set <script type="math/tex; mode=display">l</script> with left leaf <script type="math/tex; mode=display">L</script> and <script type="math/tex; mode=display">r</script> with right leaf <script type="math/tex; mode=display">R</script>.
Range <script type="math/tex; mode=display">[l, r]</script> shrinks on each iteration till range borders meets after approximately <script type="math/tex; mode=display">\log n</script> iterations of the algorithm</p>
<ul>
<li>Loop till <script type="math/tex; mode=display">l \le r</script>
<ul>
<li>Check if <script type="math/tex; mode=display">l</script> is right child of its parent <script type="math/tex; mode=display">P</script>
<ul>
<li>
<script type="math/tex; mode=display">l</script> is right child of <script type="math/tex; mode=display">P</script>. Then <script type="math/tex; mode=display">P</script> contains sum of range of <script type="math/tex; mode=display">l</script> and another  child which is outside the range <script type="math/tex; mode=display">[l, r]</script> and we don't need parent <script type="math/tex; mode=display">P</script> sum. Add <script type="math/tex; mode=display">l</script> to <script type="math/tex; mode=display">sum</script> without its parent <script type="math/tex; mode=display">P</script> and set <script type="math/tex; mode=display">l</script> to point to the right of <script type="math/tex; mode=display">P</script> on the upper level.</li>
<li>
<script type="math/tex; mode=display">l</script> is not right child of <script type="math/tex; mode=display">P</script>. Then parent <script type="math/tex; mode=display">P</script> contains sum of range which lies in <script type="math/tex; mode=display">[l, r]</script>. Add <script type="math/tex; mode=display">P</script> to <script type="math/tex; mode=display">sum</script> and set <script type="math/tex; mode=display">l</script> to point to the parent of <script type="math/tex; mode=display">P</script>
</li>
</ul>
</li>
<li>Check if <script type="math/tex; mode=display">r</script> is left child of its parent <script type="math/tex; mode=display">P</script>
<ul>
<li>
<script type="math/tex; mode=display">r</script> is left child of <script type="math/tex; mode=display">P</script>. Then <script type="math/tex; mode=display">P</script> contains sum of range of <script type="math/tex; mode=display">r</script> and another  child which is outside the range <script type="math/tex; mode=display">[l, r]</script> and we don't need parent <script type="math/tex; mode=display">P</script> sum. Add <script type="math/tex; mode=display">r</script>  to <script type="math/tex; mode=display">sum</script> without its parent <script type="math/tex; mode=display">P</script> and set <script type="math/tex; mode=display">r</script> to point to the left of <script type="math/tex; mode=display">P</script> on the upper level.</li>
<li>
<script type="math/tex; mode=display">r</script> is not left child of <script type="math/tex; mode=display">P</script>. Then parent <script type="math/tex; mode=display">P</script> contains sum of range which lies in <script type="math/tex; mode=display">[l, r]</script>. Add <script type="math/tex; mode=display">P</script> to <script type="math/tex; mode=display">sum</script> and set <script type="math/tex; mode=display">r</script> to point to the parent of <script type="math/tex; mode=display">P</script>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/Vfdts4QK/shared" frameborder="0" width="100%" height="395" name="Vfdts4QK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log n)</script>
</p>
<p>Time complexity is <script type="math/tex; mode=display">O(\log n)</script> because on each iteration of the algorithm we move one level up, either to the parent of the  current node or to the next sibling of parent to the left or right direction till the two boundaries meet. In the worst-case scenario this happens at the root after <script type="math/tex; mode=display">\log n</script> iterations of the algorithm.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<h2 id="further-thoughts">Further Thoughts</h2>
<p>The iterative version of Segment Trees was introduced in this article. A more intuitive, recursive version of Segment Trees to solve this problem is discussed <a href="https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/">here</a>. The concept of Lazy Propagation is also introduced there.</p>
<p>There is an alternative solution of the problem using Binary Indexed Tree. It is faster and simpler to code.
You can find it <a href="https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation">here</a>.</p>
<p>Analysis written by: @elmirap.</p>
          </div>
        
      </div>