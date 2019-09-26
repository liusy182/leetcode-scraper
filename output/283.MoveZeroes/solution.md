<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-space-sub-optimal-accepted">Approach #1 (Space Sub-Optimal) [Accepted]</a></li>
<li><a href="#approach-2-space-optimal-operation-sub-optimal-accepted">Approach #2 (Space Optimal, Operation Sub-Optimal) [Accepted]</a></li>
<li><a href="#approach-3-optimal-accepted">Approach #3 (Optimal) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<p>This question comes under a broad category of "Array Transformation". This category is the meat of tech interviews. Mostly because arrays are such a simple and easy to use data structure. Traversal or representation doesn't require any boilerplate code and most of your code will look like the Pseudocode itself.</p>
<p>The 2 requirements of the question are:</p>
<ol>
<li>
<p>Move all the 0's to the end of array.</p>
</li>
<li>
<p>All the non-zero elements must retain their original order.</p>
</li>
</ol>
<p>It's good to realize here that both the requirements are mutually exclusive, i.e., you can solve the individual sub-problems and then combine them for the final solution.</p>
<h4 id="approach-1-space-sub-optimal-accepted">Approach #1 (Space Sub-Optimal) [Accepted]</h4>
<p><strong>C++</strong></p>
<div class="codehilite"><pre><span></span><span class="kt">void</span> <span class="nf">moveZeroes</span><span class="p">(</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;&amp;</span> <span class="n">nums</span><span class="p">)</span> <span class="p">{</span>
    <span class="kt">int</span> <span class="n">n</span> <span class="o">=</span> <span class="n">nums</span><span class="p">.</span><span class="n">size</span><span class="p">();</span>

    <span class="c1">// Count the zeroes</span>
    <span class="kt">int</span> <span class="n">numZeroes</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">numZeroes</span> <span class="o">+=</span> <span class="p">(</span><span class="n">nums</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">);</span>
    <span class="p">}</span>

    <span class="c1">// Make all the non-zero elements retain their original order.</span>
    <span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span> <span class="n">ans</span><span class="p">;</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">nums</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">ans</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">nums</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
        <span class="p">}</span>
    <span class="p">}</span>

    <span class="c1">// Move all zeroes to the end</span>
    <span class="k">while</span> <span class="p">(</span><span class="n">numZeroes</span><span class="o">--</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">ans</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span>
    <span class="p">}</span>

    <span class="c1">// Combine the result</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">nums</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">ans</span><span class="p">[</span><span class="n">i</span><span class="p">];</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<p>Space Complexity : <script type="math/tex; mode=display">O(n)</script>. Since we are creating the "ans" array to store results.</p>
<p>Time Complexity: <script type="math/tex; mode=display">O(n)</script>. However, the total number of operations are sub-optimal. We can achieve the same result in less number of operations.</p>
<p>If asked in an interview, the above solution would be a good start. You can explain the interviewer(not code) the above and build your base for the next Optimal Solution.</p>
<hr>
<h4 id="approach-2-space-optimal-operation-sub-optimal-accepted">Approach #2 (Space Optimal, Operation Sub-Optimal) [Accepted]</h4>
<p>This approach works the same way as above, i.e. , first fulfills one requirement and then another. The catch? It does it in a clever way. The above problem can also be stated in alternate way, " Bring all the non 0 elements to the front of array keeping their relative order same".</p>
<p>This is a 2 pointer approach. The fast pointer which is denoted by variable "cur" does the job of processing new elements. If the newly found element is not a 0, we record it just after the last found non-0 element. The position of last found non-0 element is denoted by the slow pointer "lastNonZeroFoundAt" variable. As we keep finding new non-0 elements, we just overwrite them at the "lastNonZeroFoundAt + 1" 'th index. This overwrite will not result in any loss of data because we already processed what was there(if it were non-0,it already is now written at it's corresponding index,or if it were 0 it will be handled later in time).</p>
<p>After the "cur" index reaches the end of array, we now know that all the non-0 elements have been moved to beginning of array in their original order. Now comes the time to fulfil other requirement, "Move all 0's to the end". We now simply need to fill all the indexes after the "lastNonZeroFoundAt" index with 0.</p>
<p><strong>C++</strong></p>
<div class="codehilite"><pre><span></span><span class="kt">void</span> <span class="nf">moveZeroes</span><span class="p">(</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;&amp;</span> <span class="n">nums</span><span class="p">)</span> <span class="p">{</span>
    <span class="kt">int</span> <span class="n">lastNonZeroFoundAt</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>
    <span class="c1">// If the current element is not 0, then we need to</span>
    <span class="c1">// append it just in front of last non 0 element we found. </span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="p">.</span><span class="n">size</span><span class="p">();</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">nums</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">nums</span><span class="p">[</span><span class="n">lastNonZeroFoundAt</span><span class="o">++</span><span class="p">]</span> <span class="o">=</span> <span class="n">nums</span><span class="p">[</span><span class="n">i</span><span class="p">];</span>
        <span class="p">}</span>
    <span class="p">}</span>
    <span class="c1">// After we have finished processing new elements,</span>
    <span class="c1">// all the non-zero elements are already at beginning of array.</span>
    <span class="c1">// We just need to fill remaining array with 0's.</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="n">lastNonZeroFoundAt</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="p">.</span><span class="n">size</span><span class="p">();</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">nums</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<p>Space Complexity : <script type="math/tex; mode=display">O(1)</script>. Only constant space is used.</p>
<p>Time Complexity: <script type="math/tex; mode=display">O(n)</script>. However, the total number of operations are still sub-optimal. The total operations (array writes) that code does is <script type="math/tex; mode=display">n</script> (Total number of elements).</p>
<hr>
<h4 id="approach-3-optimal-accepted">Approach #3 (Optimal) [Accepted]</h4>
<p>The total number of operations of the previous approach is sub-optimal. For example, the array which has all (except last) leading zeroes: [0, 0, 0, ..., 0, 1].How many write operations to the array? For the previous approach, it writes 0's <script type="math/tex; mode=display">n-1</script> times, which is not necessary. We could have instead written just once. How?
..... 
By only fixing the non-0 element,i.e., 1.</p>
<p>The optimal approach is again a subtle extension of above solution. A simple realization is if the current element is non-0, its' correct position can at best be it's current position or a position earlier. If it's the latter one, the current position will be eventually occupied by a non-0 ,or a 0, which lies at a index greater than 'cur' index. We fill the current position by 0 right away,so that unlike the previous solution, we don't need to come back here in next iteration.</p>
<p>In other words, the code will maintain the following invariant:</p>
<blockquote>
<ol>
<li>
<p>All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.</p>
</li>
<li>
<p>All elements between the current and slow pointer are zeroes.</p>
</li>
</ol>
</blockquote>
<p>Therefore, when we encounter a non-zero element, we need to swap elements pointed by current and slow pointer, then advance both pointers. If it's zero element, we just advance current pointer.</p>
<p>With this invariant in-place, it's easy to see that the algorithm will work.</p>
<p><strong>C++</strong></p>
<div class="codehilite"><pre><span></span><span class="kt">void</span> <span class="nf">moveZeroes</span><span class="p">(</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;&amp;</span> <span class="n">nums</span><span class="p">)</span> <span class="p">{</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">lastNonZeroFoundAt</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">cur</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">cur</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="p">.</span><span class="n">size</span><span class="p">();</span> <span class="n">cur</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">nums</span><span class="p">[</span><span class="n">cur</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">swap</span><span class="p">(</span><span class="n">nums</span><span class="p">[</span><span class="n">lastNonZeroFoundAt</span><span class="o">++</span><span class="p">],</span> <span class="n">nums</span><span class="p">[</span><span class="n">cur</span><span class="p">]);</span>
        <span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<p>Space Complexity : <script type="math/tex; mode=display">O(1)</script>. Only constant space is used.</p>
<p>Time Complexity: <script type="math/tex; mode=display">O(n)</script>. However, the total number of operations are optimal. The total operations (array writes) that code does is Number of non-0 elements.This gives us a much better best-case (when most of the elements are 0) complexity than last solution. However, the worst-case (when all elements are non-0) complexity for both the algorithms is same.</p>
<p>Analysis written by: @spandan.pathak</p>
          </div>
        
      </div>