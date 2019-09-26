<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-naive-linear-search-time-limit-exceeded">Approach #1 (Naive Linear Search) [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-sorting-accepted">Approach #2 (Sorting) [Accepted]</a></li>
<li><a href="#approach-3-hash-table-accepted">Approach #3 (Hash Table) [Accepted]</a></li>
</ul>
</li>
<li><a href="#see-also">See Also</a></li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for beginners. It introduces the following ideas:
Loop Invariant, Linear Search, Sorting and Hash Table.</p>
<h2 id="solution">Solution</h2>
<h4 id="approach-1-naive-linear-search-time-limit-exceeded">Approach #1 (Naive Linear Search) [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>For an array of <script type="math/tex; mode=display">n</script> integers, there are <script type="math/tex; mode=display">C(n,2) = \frac{n(n+1)}{2}</script> pairs of integers. Thus, we may check all <script type="math/tex; mode=display">\frac{n(n+1)}{2}</script> pairs and see if there is any pair with duplicates.</p>
<p><strong>Algorithm</strong></p>
<p>To apply this idea, we employ the linear search algorithm which is the simplest search algorithm. Linear search is a method of finding if a particular value is in a list by checking each of its elements, one at a time and in sequence until the desired one is found.</p>
<p>For our problem, we loop through all <script type="math/tex; mode=display">n</script> integers. For the <script type="math/tex; mode=display">i</script>th integer <code>nums[i]</code>, we search in the previous <code>i-1</code> integers for the duplicate of <code>nums[i]</code>. If we find one, we return true; if not, we continue. Return false at the end of the program.</p>
<p>To prove the correctness of the algorithm, we define the loop invariant. A loop invariant is a property that holds before (and after) each iteration. Knowing its invariant(s) is essential for understanding the effect of a loop. Here is the <em>loop invariant</em>:</p>
<blockquote>
<p>Before the next search, there are no duplicate integers in the searched integers.</p>
</blockquote>
<p>The loop invariant holds true before the loop because there is no searched integer.
Each time through the loop we look for any any possible duplicate of the current element.
If we found a duplicate, the function exits by returning true; If not, the invariant still holds true.</p>
<p>Therefore, if the loop finishes, the invariant tells us that there is no duplicate in all <script type="math/tex; mode=display">n</script> integers.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">containsDuplicate</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">i</span><span class="o">;</span> <span class="o">++</span><span class="n">j</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">nums</span><span class="o">[</span><span class="n">j</span><span class="o">]</span> <span class="o">==</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">])</span> <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>  
        <span class="o">}</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
<span class="o">}</span>
<span class="c1">// Time Limit Exceeded</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. In the worst case, there are <script type="math/tex; mode=display">\frac{n(n+1)}{2}</script> pairs of integers to check. Therefore, the time complexity is <script type="math/tex; mode=display">O(n^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
We only used constant extra space.</p>
</li>
</ul>
<p><strong>Note</strong></p>
<p>This approach will get Time Limit Exceeded on LeetCode. Usually, if an algorithm is <script type="math/tex; mode=display">O(n^2)</script>, it can handle <script type="math/tex; mode=display">n</script> up to around <script type="math/tex; mode=display">10^4</script>. It gets Time Limit Exceeded when <script type="math/tex; mode=display">n \geq 10^5</script>.</p>
<hr>
<h4 id="approach-2-sorting-accepted">Approach #2 (Sorting) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If there are any duplicate integers, they will be consecutive after sorting.</p>
<p><strong>Algorithm</strong></p>
<p>This approach employs sorting algorithm. Since comparison sorting algorithm like <em>heapsort</em> is known to provide <script type="math/tex; mode=display">O(n \log n)</script> worst-case performance, sorting is often a good preprocessing step. After sorting, we can sweep the sorted array to find if there are any two consecutive duplicate elements.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">containsDuplicate</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">Arrays</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">nums</span><span class="o">);</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">==</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="o">])</span> <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n \log n)</script>.
Sorting is <script type="math/tex; mode=display">O(n \log n)</script> and the sweeping is <script type="math/tex; mode=display">O(n)</script>. The entire algorithm is dominated by the sorting step, which is <script type="math/tex; mode=display">O(n \log n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
Space depends on the sorting implementation which, usually, costs <script type="math/tex; mode=display">O(1)</script> auxiliary space if <code>heapsort</code> is used.</p>
</li>
</ul>
<p><strong>Note</strong></p>
<p>The implementation here modifies the original array by sorting it. In general, it is not a good practice to modify the input unless it is clear to the caller that the input will be modified. One may make a copy of <code>nums</code> and operate on the copy instead.</p>
<hr>
<h4 id="approach-3-hash-table-accepted">Approach #3 (Hash Table) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Utilize a dynamic data structure that supports fast search and insert operations.</p>
<p><strong>Algorithm</strong></p>
<p>From <a href="#approach-1-naive-linear-search-time-limit-exceeded">Approach #1</a> we know that search operations is <script type="math/tex; mode=display">O(n)</script> in an unsorted array and we did so repeatedly. Utilizing a data structure with faster search time will speed up the entire algorithm.</p>
<p>There are many data structures commonly used as dynamic sets such as Binary Search Tree and Hash Table. The operations we need to support here are <code>search()</code> and <code>insert()</code>. For a self-balancing Binary Search Tree (TreeSet or TreeMap in Java), <code>search()</code> and <code>insert()</code> are both <script type="math/tex; mode=display">O(\log n)</script> time. For a Hash Table (HashSet or HashMap in Java), <code>search()</code> and <code>insert()</code> are both <script type="math/tex; mode=display">O(1)</script> on average. Therefore, by using hash table, we can achieve linear time complexity for finding the duplicate in an unsorted array.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">containsDuplicate</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">Set</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span> <span class="n">set</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashSet</span><span class="o">&lt;&gt;(</span><span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">);</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">:</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">set</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
        <span class="n">set</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">x</span><span class="o">);</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
We do <code>search()</code> and <code>insert()</code> for <script type="math/tex; mode=display">n</script> times and each operation takes constant time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
The space used by a hash table is linear with the number of elements in it.</p>
</li>
</ul>
<p><strong>Note</strong></p>
<p>For certain test cases with not very large <script type="math/tex; mode=display">n</script>, the runtime of this method can be slower than <a href="#approach-2-sorting-accepted">Approach #2</a>. The reason is hash table has some overhead in maintaining its property. One should keep in mind that real world performance can be different from what the Big-O notation says. The Big-O notation only tells us that for <em>sufficiently</em> large input, one will be faster than the other. Therefore, when <script type="math/tex; mode=display">n</script> is not sufficiently large, an <script type="math/tex; mode=display">O(n)</script> algorithm can be slower than an <script type="math/tex; mode=display">O(n \log n)</script> algorithm.</p>
<h2 id="see-also">See Also</h2>
<ul>
<li><a href="https://leetcode.com/articles/contains-duplicate-ii/">Problem 219 Contains Duplicate II</a></li>
<li><a href="https://leetcode.com/articles/contains-duplicate-iii/">Problem 220 Contains Duplicate III</a></li>
</ul>
          </div>
        
      </div>