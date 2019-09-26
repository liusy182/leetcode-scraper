<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-using-extra-array-accepted">Approach #2 Using Extra Array [Accepted]</a></li>
<li><a href="#approach-3-using-cyclic-replacements-accepted">Approach #3 Using Cyclic Replacements [Accepted]</a></li>
<li><a href="#approach-4-using-reverse-accepted">Approach #4 Using Reverse [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>We have to rotate the elements of the given array k times to the right.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p>The simplest approach is to rotate all the elements of the array in k steps
 by rotating the elements by 1 unit in each step.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">rotate</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">temp</span><span class="o">,</span> <span class="n">previous</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">k</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">previous</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">nums</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">];</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">j</span><span class="o">++)</span> <span class="o">{</span>
                <span class="n">temp</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">j</span><span class="o">];</span>
                <span class="n">nums</span><span class="o">[</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="n">previous</span><span class="o">;</span>
                <span class="n">previous</span> <span class="o">=</span> <span class="n">temp</span><span class="o">;</span>
            <span class="o">}</span>
        <span class="o">}</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n*k)</script>. All the numbers are shifted by one step(<script type="math/tex; mode=display">O(n)</script>)
 k times(<script type="math/tex; mode=display">O(k)</script>).</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.</li>
</ul>
<hr>
<h4 id="approach-2-using-extra-array-accepted">Approach #2 Using Extra Array [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We use an extra array in which we place every element of the array at its correct
position i.e. the number at index <script type="math/tex; mode=display">i</script> in the original array is placed at the
index <script type="math/tex; mode=display">(i+k)%(length of array)</script>. Then, we copy the new array to the original one.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">rotate</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span><span class="o">[]</span> <span class="n">a</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">];</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">a</span><span class="o">[(</span><span class="n">i</span> <span class="o">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">%</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">]</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">];</span>
        <span class="o">}</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">=</span> <span class="n">a</span><span class="o">[</span><span class="n">i</span><span class="o">];</span>
        <span class="o">}</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. One pass is used to put the numbers in the new array.
 And another pass to copy the new array to the original one.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Another array of the same size is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-cyclic-replacements-accepted">Approach #3 Using Cyclic Replacements [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We can directly place every number of the array at its required correct position.
But if we do that, we will destroy the original element. Thus, we need to store
the number being replaced in a <script type="math/tex; mode=display">temp</script> variable. Then, we can place the replaced
 number(<script type="math/tex; mode=display">temp</script>) at its correct position and so on, <script type="math/tex; mode=display">n</script> times, where <script type="math/tex; mode=display">n</script> is
 the length of array. We have chosen <script type="math/tex; mode=display">n</script> to be the number of replacements since we have 
 to shift all the elements of the array(which is <script type="math/tex; mode=display">n</script>). But, there could be a problem with this method, if <script type="math/tex; mode=display">n%k=0</script>
 where <script type="math/tex; mode=display">k = k%n</script>(since a value of <script type="math/tex; mode=display">k</script> larger than <script type="math/tex; mode=display">n</script> eventually leads to a <script type="math/tex; mode=display">k</script> equivalent to <script type="math/tex; mode=display">k%n</script>). In this case, while picking up numbers to be placed at the
 correct position, we will eventually reach the number from which we originally started. Thus, in such a case, when
 we hit the original number's index again, we start the same process with the number following it.</p>
<p>Now let's look at the proof of how the above method works. Suppose, we have <script type="math/tex; mode=display">n</script> as the number of elements in the array and
 <script type="math/tex; mode=display">k</script> is the number of shifts required. Further, assume <script type="math/tex; mode=display">n%k=0</script>. Now, when we start placing the elements at their correct position, in the first cycle all the numbers with their index <script type="math/tex; mode=display">i</script> satisfying <script type="math/tex; mode=display">i%k=0</script> get placed at their required position. This happens because when we jump k steps every time, we will only hit the numbers k steps apart. We start with index <script type="math/tex; mode=display">i=0</script>, having <script type="math/tex; mode=display">i%k=0</script>. Thus, we hit all the numbers satisfying the above condition in the first cycle. When we reach back the original index, we have placed <script type="math/tex; mode=display">\frac{n}{k}</script> elements at their correct position, since we hit only that many elements in the first cycle. Now, we increment the index for replacing the numbers. This time, we place other <script type="math/tex; mode=display">\frac{n}{k}</script> elements at their correct position, different from the ones placed correctly in the first cycle, because this time we hit all the numbers satisfy the condition <script type="math/tex; mode=display">i%k=1</script>. When we hit the starting number again, we increment the index and repeat the same process from <script type="math/tex; mode=display">i=1</script> for all the indices satisfying <script type="math/tex; mode=display">i%k==1</script>. This happens till we reach the number with the index <script type="math/tex; mode=display">i%k=0</script> again, which occurs for <script type="math/tex; mode=display">i=k</script>. We will reach such a number after a total of k cycles. Now, the total count of numbers exclusive numbers placed at their correct position will be <script type="math/tex; mode=display">k \times \frac{n}{k}=n</script>. Thus, all the numbers will be placed at their correct position.</p>
<p>Look at the following example to clarify the process:
 <code>nums: [1, 2, 3, 4, 5, 6]
k: 2</code></p>
<p><img alt="Rotate Array" src="https://leetcode.com/media/original_images/189_Rotate_Array.png"></p>
<p><strong>java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">rotate</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">k</span> <span class="o">=</span> <span class="n">k</span> <span class="o">%</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span>
        <span class="kt">int</span> <span class="n">count</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">start</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">count</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">start</span><span class="o">++)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">current</span> <span class="o">=</span> <span class="n">start</span><span class="o">;</span>
            <span class="kt">int</span> <span class="n">prev</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">start</span><span class="o">];</span>
            <span class="k">do</span> <span class="o">{</span>
                <span class="kt">int</span> <span class="n">next</span> <span class="o">=</span> <span class="o">(</span><span class="n">current</span> <span class="o">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">%</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span>
                <span class="kt">int</span> <span class="n">temp</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">next</span><span class="o">];</span>
                <span class="n">nums</span><span class="o">[</span><span class="n">next</span><span class="o">]</span> <span class="o">=</span> <span class="n">prev</span><span class="o">;</span>
                <span class="n">prev</span> <span class="o">=</span> <span class="n">temp</span><span class="o">;</span>
                <span class="n">current</span> <span class="o">=</span> <span class="n">next</span><span class="o">;</span>
                <span class="n">count</span><span class="o">++;</span>
            <span class="o">}</span> <span class="k">while</span> <span class="o">(</span><span class="n">start</span> <span class="o">!=</span> <span class="n">current</span><span class="o">);</span>
        <span class="o">}</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Only one pass is used.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-using-reverse-accepted">Approach #4 Using Reverse [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>This approach is based on the fact that when we rotate the array k times, <script type="math/tex; mode=display">k%n</script> elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.</p>
<p>In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest <script type="math/tex; mode=display">n-k</script> elements gives us the required result.</p>
<p>Let <script type="math/tex; mode=display">n=7</script> and <script type="math/tex; mode=display">k=3</script>.</p>
<div class="codehilite"><pre><span></span>Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --&gt; Result
</pre></div>


<p><strong>java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">rotate</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">k</span> <span class="o">%=</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span>
        <span class="n">reverse</span><span class="o">(</span><span class="n">nums</span><span class="o">,</span> <span class="mi">0</span><span class="o">,</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">);</span>
        <span class="n">reverse</span><span class="o">(</span><span class="n">nums</span><span class="o">,</span> <span class="mi">0</span><span class="o">,</span> <span class="n">k</span> <span class="o">-</span> <span class="mi">1</span><span class="o">);</span>
        <span class="n">reverse</span><span class="o">(</span><span class="n">nums</span><span class="o">,</span> <span class="n">k</span><span class="o">,</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">);</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">reverse</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">start</span><span class="o">,</span> <span class="kt">int</span> <span class="n">end</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">start</span> <span class="o">&lt;</span> <span class="n">end</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">temp</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">start</span><span class="o">];</span>
            <span class="n">nums</span><span class="o">[</span><span class="n">start</span><span class="o">]</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">end</span><span class="o">];</span>
            <span class="n">nums</span><span class="o">[</span><span class="n">end</span><span class="o">]</span> <span class="o">=</span> <span class="n">temp</span><span class="o">;</span>
            <span class="n">start</span><span class="o">++;</span>
            <span class="n">end</span><span class="o">--;</span>
        <span class="o">}</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">n</script> elements are reversed a total of three times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.</p>
</li>
</ul>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>