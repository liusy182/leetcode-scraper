<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-simple-sorting">Approach 1: Simple Sorting</a></li>
<li><a href="#approach-2-insertion-sort">Approach 2: Insertion Sort</a></li>
<li><a href="#approach-3-two-heaps">Approach 3: Two Heaps</a></li>
<li><a href="#approach-4-multiset-and-two-pointers">Approach 4: Multiset and Two Pointers</a></li>
<li><a href="#further-thoughts">Further Thoughts</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-simple-sorting">Approach 1: Simple Sorting</h4>
<p><strong>Intuition</strong></p>
<p>Do what the question says.</p>
<p><strong>Algorithm</strong></p>
<p>Store the numbers in a resize-able container. Every time you need to output the median, sort the container and output the median.</p>
<iframe src="https://leetcode.com/playground/uuj7LQjt/shared" frameborder="0" width="100%" height="378" name="uuj7LQjt"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n\log n) + O(1) \simeq O(n\log n)</script>.</p>
<ul>
<li>Adding a number takes amortized <script type="math/tex; mode=display">O(1)</script> time for a container with an efficient resizing scheme.</li>
<li>Finding the median is primarily dependent on the sorting that takes place. This takes <script type="math/tex; mode=display">O(n\log n)</script> time for a standard comparative sort.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script> linear space to hold input in a container. No extra space other than that needed (since sorting can usually be done in-place).</p>
</li>
</ul>
<hr>
<h4 id="approach-2-insertion-sort">Approach 2: Insertion Sort</h4>
<p><strong>Intuition</strong></p>
<p>Keeping our input container always sorted (i.e. maintaining the sorted nature of the container as an <em>invariant</em>).</p>
<p><strong>Algorithm</strong></p>
<p>Which algorithm allows a number to be added to a sorted list of numbers and yet keeps the entire list sorted? Well, for one, <strong>insertion sort!</strong></p>
<p>We assume that the current list is already sorted. When a new number comes, we have to add it to the list while maintaining the sorted nature of the list. This is achieved easily by finding the correct place to insert the incoming number, using a <strong>binary search</strong> (remember, the list is <em>always sorted</em>). Once the position is found, we need to shift all higher elements by one space to make room for the incoming number.</p>
<p>This method would work well when the amount of insertion queries is lesser or about the same as the amount of median finding queries.</p>
<iframe src="https://leetcode.com/playground/fzps5txK/shared" frameborder="0" width="100%" height="395" name="fzps5txK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n) + O(\log n) \approx O(n)</script>.</p>
<ul>
<li>Binary Search takes <script type="math/tex; mode=display">O(\log n)</script> time to find correct insertion position.</li>
<li>Insertion can take up to <script type="math/tex; mode=display">O(n)</script> time since elements have to be shifted inside the container to make room for the new element.</li>
</ul>
</li>
</ul>
<blockquote>
<p><strong>Pop quiz:</strong> Can we use a <em>linear</em> search instead of a <em>binary</em> search to find insertion position, without incurring any significant runtime penalty?</p>
</blockquote>
<ul>
<li>Space complexity: <script type="math/tex; mode=display">O(n)</script> linear space to hold input in a container.</li>
</ul>
<hr>
<h4 id="approach-3-two-heaps">Approach 3: Two Heaps</h4>
<p><strong>Intuition</strong></p>
<p>The above two approaches gave us some valuable insights on how to tackle this problem. Concretely, one can infer two things:</p>
<ol>
<li>If we could maintain direct access to median elements at all times, then finding the median would take a constant amount of time.</li>
<li>If we could find a reasonably fast way of adding numbers to our containers, additional penalties incurred could be lessened.</li>
</ol>
<p>But perhaps the most important insight, which is not readily observable, is the fact that we <em>only</em> need a consistent way to access the median elements. Keeping the <em>entire</em> input sorted is <strong>not a requirement.</strong></p>
<blockquote>
<p>Well, if only there were a data structure which could handle our needs.</p>
</blockquote>
<p>As it turns out there are two data structures for the job:</p>
<ul>
<li>Heaps (or Priority Queues <sup id="fnref:note-1"><a class="footnote-ref" href="#fn:note-1" rel="footnote">1</a></sup>)</li>
<li>Self-balancing Binary Search Trees (we'll talk more about them in <a href="#approach-4-multiset-and-two-pointers">Approach 4</a>)</li>
</ul>
<p>Heaps are a natural ingredient for this dish! Adding elements to them take logarithmic order of time. They also give direct access to the maximal/minimal elements in a group.</p>
<p>If we could maintain <em>two</em> heaps in the following way:</p>
<ul>
<li>A max-heap to store the smaller half of the input numbers</li>
<li>A min-heap to store the larger half of the input numbers</li>
</ul>
<p>This gives access to median values in the input: they comprise the top of the heaps!</p>
<p><strong>Wait, what? How?</strong></p>
<p>If the following conditions are met:</p>
<ol>
<li>Both the heaps are balanced (or nearly balanced)</li>
<li>The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers</li>
</ol>
<p>then we can say that:</p>
<ol>
<li>All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it <script type="math/tex; mode=display">x</script>)</li>
<li>All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it <script type="math/tex; mode=display">y</script>)</li>
</ol>
<p>Then <script type="math/tex; mode=display">x</script> and/or <script type="math/tex; mode=display">y</script> are smaller than (or equal to) almost half of the elements and larger than (or equal to) the other half. That is <em>the</em> definition of <strong>median</strong> elements.</p>
<p>This leads us to a huge point of pain in this approach: <strong>balancing the two heaps!</strong></p>
<p><strong>Algorithm</strong></p>
<ul>
<li>
<p>Two priority queues:</p>
<ol>
<li>A max-heap <code>lo</code> to store the smaller half of the numbers</li>
<li>A min-heap <code>hi</code> to store the larger half of the numbers</li>
</ol>
</li>
<li>
<p>The max-heap <code>lo</code> is allowed to store, at worst, one more element more than the min-heap <code>hi</code>. Hence if we have processed <script type="math/tex; mode=display">k</script> elements:</p>
<ul>
<li>If <script type="math/tex; mode=display">k = 2*n + 1 \quad (\forall \, n \in \mathbb{Z})</script>, then <code>lo</code> is allowed to hold <script type="math/tex; mode=display">n+1</script> elements, while <code>hi</code> can hold <script type="math/tex; mode=display">n</script> elements.</li>
<li>If <script type="math/tex; mode=display">k = 2*n \quad (\forall \, n \in \mathbb{Z})</script>, then both heaps are balanced and hold <script type="math/tex; mode=display">n</script> elements each.</li>
</ul>
<p>This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops of both heaps. Otherwise, the top of the max-heap <code>lo</code> holds the legitimate median.</p>
</li>
<li>
<p>Adding a number <code>num</code>:</p>
<ul>
<li>Add <code>num</code> to max-heap <code>lo</code>. Since <code>lo</code> received a new element, we must do a balancing step for <code>hi</code>. So remove the largest element from <code>lo</code> and offer it to <code>hi</code>.</li>
<li>The min-heap <code>hi</code> might end holding more elements than the max-heap <code>lo</code>, after the previous operation. We fix that by removing the smallest element from <code>hi</code> and offering it to <code>lo</code>.</li>
</ul>
<p>The above step ensures that we do not disturb the nice little size property we just mentioned.</p>
</li>
</ul>
<p>A little example will clear this up! Say we take input from the stream <code>[41, 35, 62, 5, 97, 108]</code>. The run-though of the algorithm looks like this:</p>
<div class="codehilite"><pre><span></span>Adding number <span class="m">41</span>
MaxHeap lo<span class="o">:</span> <span class="p">[</span><span class="m">41</span><span class="p">]</span>           <span class="o">//</span> MaxHeap stores the largest value at the top <span class="p">(</span>index <span class="m">0</span><span class="p">)</span>
MinHeap hi<span class="o">:</span> <span class="p">[]</span>             <span class="o">//</span> MinHeap stores the smallest value at the top <span class="p">(</span>index <span class="m">0</span><span class="p">)</span>
Median is <span class="m">41</span>
<span class="o">=======================</span>
Adding number <span class="m">35</span>
MaxHeap lo<span class="o">:</span> <span class="p">[</span><span class="m">35</span><span class="p">]</span>
MinHeap hi<span class="o">:</span> <span class="p">[</span><span class="m">41</span><span class="p">]</span>
Median is <span class="m">38</span>
<span class="o">=======================</span>
Adding number <span class="m">62</span>
MaxHeap lo<span class="o">:</span> <span class="p">[</span><span class="m">41</span><span class="p">,</span> <span class="m">35</span><span class="p">]</span>
MinHeap hi<span class="o">:</span> <span class="p">[</span><span class="m">62</span><span class="p">]</span>
Median is <span class="m">41</span>
<span class="o">=======================</span>
Adding number <span class="m">4</span>
MaxHeap lo<span class="o">:</span> <span class="p">[</span><span class="m">35</span><span class="p">,</span> <span class="m">4</span><span class="p">]</span>
MinHeap hi<span class="o">:</span> <span class="p">[</span><span class="m">41</span><span class="p">,</span> <span class="m">62</span><span class="p">]</span>
Median is <span class="m">38</span>
<span class="o">=======================</span>
Adding number <span class="m">97</span>
MaxHeap lo<span class="o">:</span> <span class="p">[</span><span class="m">41</span><span class="p">,</span> <span class="m">35</span><span class="p">,</span> <span class="m">4</span><span class="p">]</span>
MinHeap hi<span class="o">:</span> <span class="p">[</span><span class="m">62</span><span class="p">,</span> <span class="m">97</span><span class="p">]</span>
Median is <span class="m">41</span>
<span class="o">=======================</span>
Adding number <span class="m">108</span>
MaxHeap lo<span class="o">:</span> <span class="p">[</span><span class="m">41</span><span class="p">,</span> <span class="m">35</span><span class="p">,</span> <span class="m">4</span><span class="p">]</span>
MinHeap hi<span class="o">:</span> <span class="p">[</span><span class="m">62</span><span class="p">,</span> <span class="m">97</span><span class="p">,</span> <span class="m">108</span><span class="p">]</span>
Median is <span class="m">51.5</span>
</pre></div>


<iframe src="https://leetcode.com/playground/tiYjWic8/shared" frameborder="0" width="100%" height="480" name="tiYjWic8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(5 \cdot \log n) + O(1) \approx O(\log n)</script>.</p>
<ul>
<li>At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about <script type="math/tex; mode=display">O(\log n)</script> time.</li>
<li>Finding the mean takes constant <script type="math/tex; mode=display">O(1)</script> time since the tops of heaps are directly accessible.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script> linear space to hold input in containers.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-multiset-and-two-pointers">Approach 4: Multiset and Two Pointers</h4>
<p><strong>Intuition</strong></p>
<p>Self-balancing Binary Search Trees (like an <a href="https://en.wikipedia.org/wiki/AVL_tree">AVL Tree</a>) have some <em>very</em> interesting properties. They maintain the tree's height to a logarithmic bound. Thus inserting a new element has reasonably good time performance. The median <strong>always</strong> winds up in the root of the tree and/or one of its children. Solving this problem using the same approach as <a href="#approach-3-two-heaps">Approach 3</a> but using a Self-balancing BST seems like a good choice. Except the fact that implementing such a tree is not trivial and prone to errors.</p>
<p><em>Why reinvent the wheel?</em> Most languages implement a <code>multiset</code> class which emulates such behavior. The only problem remains keeping track of the median elements. That is easily solved with <strong>pointers!</strong> <sup id="fnref:note-2"><a class="footnote-ref" href="#fn:note-2" rel="footnote">2</a></sup></p>
<p>We maintain two pointers: one for the lower median element and the other for the higher median element. When the total number of elements is odd, both the pointers point to the same median element (since there is only one median in this case). When the number of elements is even, the pointers point to two consecutive elements, whose mean is the representative median of the input.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>
<p>Two iterators/pointers <code>lo_median</code> and <code>hi_median</code>, which iterate over the <code>data</code> multiset.</p>
</li>
<li>
<p>While adding a number <code>num</code>, three cases arise:</p>
<ol>
<li>The container is currently <strong>empty.</strong> Hence we simply insert <code>num</code> and set both pointers to point to this element.</li>
<li>
<p>The container currently holds an <strong>odd</strong> number of elements. This means that both the pointers currently point to the same element.</p>
<ul>
<li>If <code>num</code> is not equal to the current median element, then <code>num</code> goes on either side of it. Whichever side it goes, the size of that part increases and hence the corresponding pointer is updated. For example, if <code>num</code> is less than the median element, the size of the lesser half of input increases by <script type="math/tex; mode=display">1</script> on inserting <code>num</code>. Thus it makes sense to decrement <code>lo_median</code>.</li>
<li>If <code>num</code> is equal to the current median element, then the action taken is dependent on how <code>num</code> is inserted into <code>data</code>. <strong>NOTE:</strong> In our given C++ code example, <code>std::multiset::insert</code> inserts an element <em>after</em> all elements of equal value. Hence we increment <code>hi_median</code>.</li>
</ul>
</li>
<li>
<p>The container currently holds an <strong>even</strong> number of elements. This means that the pointers currently point to consecutive elements.</p>
<ul>
<li>If <code>num</code> is a number between both median elements, then <code>num</code> becomes the new median. Both pointers must point to it.</li>
<li>Otherwise, <code>num</code> increases the size of either the lesser or higher half of the input. We update the pointers accordingly. It is important to remember that both the pointers <strong><em>must</em></strong> point to the same element now.</li>
</ul>
</li>
</ol>
</li>
<li>
<p>Finding the median is easy! It is simply the <strong>mean</strong> of the elements pointed to by the two pointers <code>lo_median</code> and <code>hi_median</code>.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/g6cgUGn5/shared" frameborder="0" width="100%" height="500" name="g6cgUGn5"></iframe>

<p>A much shorter (but harder to understand), <strong><em>one</em></strong> <em>pointer</em> version <sup id="fnref:note-3"><a class="footnote-ref" href="#fn:note-3" rel="footnote">3</a></sup> of this solution is given below:</p>
<iframe src="https://leetcode.com/playground/PBHKZtFa/shared" frameborder="0" width="100%" height="500" name="PBHKZtFa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(\log n) + O(1) \approx O(\log n)</script>.</p>
<ul>
<li>Inserting a number takes <script type="math/tex; mode=display">O(\log n)</script> time for a standard <code>multiset</code> scheme. <sup id="fnref:note-4"><a class="footnote-ref" href="#fn:note-4" rel="footnote">4</a></sup></li>
<li>Finding the mean takes constant <script type="math/tex; mode=display">O(1)</script> time since the median elements are directly accessible from the two pointers.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script> linear space to hold input in container.</p>
</li>
</ul>
<hr>
<h4 id="further-thoughts">Further Thoughts</h4>
<p>There are so many ways around this problem, that frankly, it is scary. Here are a few more that I came across:</p>
<ul>
<li>
<p><strong>Buckets!</strong> If the numbers in the stream are statistically distributed, then it is easier to keep track of buckets where the median would land, than the entire array. Once you know the correct bucket, simply sort it find the median. If the bucket size is significantly smaller than the size of input processed, this results in huge time saving. <a href="https://leetcode.com/mitbbs8080/">@mitbbs8080</a> has an interesting implementation <a href="https://leetcode.com/problems/find-median-from-data-stream/discuss/74057/Tired-of-TWO-HEAPSET-solutions-See-this-segment-dividing-solution-(c%2B%2B)">here.</a></p>
</li>
<li>
<p><strong>Reservoir Sampling.</strong> Following along the lines of using buckets: if the stream is statistically distributed, you can rely on Reservoir Sampling. Basically, if you could maintain just one good bucket (or <em>reservoir</em>) which could hold a representative sample of the entire stream, you could estimate the median of the entire stream from just this one bucket. This means good time and memory performance. Reservoir Sampling lets you do just that. Determining a <strong>"good"</strong> size for your reservoir? <em>Now, that's a whole other challenge.</em> A good explanation for this can be found in <a href="https://stackoverflow.com/a/10693752/2844164">this StackOverflow answer.</a></p>
</li>
<li>
<p><strong>Segment Trees</strong> are a great data structure if you need to do a lot of insertions or a lot of read queries over a limited range of input values. They allow us to do all such operations <em>fast</em> and in roughly the <em>same amount of time</em>, <strong>always.</strong> The only problem is that they are far from trivial to implement. Take a look at my <a href="https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/">introductory article on Segment Trees</a> if you are interested.</p>
</li>
<li>
<p><strong>Order Statistic Trees</strong> are data structures which seem to be tailor-made for this problem. They have all the nice features of a BST, but also let you find the <script type="math/tex; mode=display">k^{th}</script> order element stored in the tree. They are a pain to implement and no standard interview would require you to code these up. But they are fun to use if they are already implemented in the language of your choice. <sup id="fnref:note-5"><a class="footnote-ref" href="#fn:note-5" rel="footnote">5</a></sup></p>
</li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/babhishek21">@babhishek21</a>.</p>
<div class="footnote">
<hr>
<ol>
<li id="fn:note-1">
<p>Priority Queues queue out elements based on a predefined priority. They are an abstract concept and can, as such, be implemented in many different ways. Heaps are an efficient way to implement Priority Queues. <a class="footnote-backref" href="#fnref:note-1" rev="footnote" title="Jump back to footnote 1 in the text">↩</a></p>
</li>
<li id="fn:note-2">
<p>Shout-out to <a href="https://leetcode.com/pharese/">@pharese</a> for this approach. <a class="footnote-backref" href="#fnref:note-2" rev="footnote" title="Jump back to footnote 2 in the text">↩</a></p>
</li>
<li id="fn:note-3">
<p>Inspired from <a href="https://leetcode.com/problems/sliding-window-median/discuss/96340/on-log-k-c-using-multiset-and-updating-middle-iterator">this post</a> by <a href="https://leetcode.com/stefanpochmann">@StefanPochmann</a>. <a class="footnote-backref" href="#fnref:note-3" rev="footnote" title="Jump back to footnote 3 in the text">↩</a></p>
</li>
<li id="fn:note-4">
<p><a href="http://en.cppreference.com/w/cpp/container/multiset/insert">Hinting</a> can reduce that to amortized constant <script type="math/tex; mode=display">O(1)</script> time. <a class="footnote-backref" href="#fnref:note-4" rev="footnote" title="Jump back to footnote 4 in the text">↩</a></p>
</li>
<li id="fn:note-5">
<p><a href="https://gcc.gnu.org/onlinedocs/libstdc++/manual/policy_based_data_structures_test.html"><strong>GNU</strong> <code>libstdc++</code></a> users are in luck! Take a look at <a href="https://stackoverflow.com/a/11228573/2844164">this StackOverflow answer.</a> <a class="footnote-backref" href="#fnref:note-5" rev="footnote" title="Jump back to footnote 5 in the text">↩</a></p>
</li>
</ol>
</div>
          </div>
        
      </div>