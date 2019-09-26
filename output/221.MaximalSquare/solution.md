<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</a></li>
<li><a href="#approach-2-dynamic-programming-accepted">Approach #2 (Dynamic Programming) [Accepted]</a></li>
<li><a href="#approach-3-better-dynamic-programming-accepted">Approach #3 (Better Dynamic Programming) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>We need to find the largest square comprising of all ones in the given <script type="math/tex; mode=display">m \times n</script> matrix. In other words we need to find the largest set of connected ones in the given matrix that forms a square.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</h4>
<p>The simplest approach consists of trying to find out every possible square of 1’s that can be formed from within the matrix. The question now is – how to go for it?</p>
<p>We use a variable to contain the size of the largest square found so far and another variable to store the size of the current, both initialized to 0. Starting from the left uppermost point in the matrix, we search for a 1. No operation needs to be done for a 0. Whenever a 1 is found, we try to find out the largest square that can be formed including that 1. For this, we move diagonally (right and downwards), i.e. we increment the row index and column index temporarily and then check whether all the elements of that row and column are 1 or not. If all the elements happen to be 1, we move diagonally further as previously. If even one element turns out to be 0, we stop this diagonal movement and update the size of the largest square. Now we, continue the traversal of the matrix from the element next to the initial 1 found, till all the elements of the matrix have been traversed.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">maximalSquare</span><span class="o">(</span><span class="kt">char</span><span class="o">[][]</span> <span class="n">matrix</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">rows</span> <span class="o">=</span> <span class="n">matrix</span><span class="o">.</span><span class="na">length</span><span class="o">,</span> <span class="n">cols</span> <span class="o">=</span> <span class="n">rows</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="o">?</span> <span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span> <span class="o">:</span> <span class="mi">0</span><span class="o">;</span>
        <span class="kt">int</span> <span class="n">maxsqlen</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">rows</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">cols</span><span class="o">;</span> <span class="n">j</span><span class="o">++)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'1'</span><span class="o">)</span> <span class="o">{</span>
                    <span class="kt">int</span> <span class="n">sqlen</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span>
                    <span class="kt">boolean</span> <span class="n">flag</span> <span class="o">=</span> <span class="kc">true</span><span class="o">;</span>
                    <span class="k">while</span> <span class="o">(</span><span class="n">sqlen</span> <span class="o">+</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">rows</span> <span class="o">&amp;&amp;</span> <span class="n">sqlen</span> <span class="o">+</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">cols</span> <span class="o">&amp;&amp;</span> <span class="n">flag</span><span class="o">)</span> <span class="o">{</span>
                        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">k</span> <span class="o">=</span> <span class="n">j</span><span class="o">;</span> <span class="n">k</span> <span class="o">&lt;=</span> <span class="n">sqlen</span> <span class="o">+</span> <span class="n">j</span><span class="o">;</span> <span class="n">k</span><span class="o">++)</span> <span class="o">{</span>
                            <span class="k">if</span> <span class="o">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">i</span> <span class="o">+</span> <span class="n">sqlen</span><span class="o">][</span><span class="n">k</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'0'</span><span class="o">)</span> <span class="o">{</span>
                                <span class="n">flag</span> <span class="o">=</span> <span class="kc">false</span><span class="o">;</span>
                                <span class="k">break</span><span class="o">;</span>
                            <span class="o">}</span>
                        <span class="o">}</span>
                        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">k</span> <span class="o">=</span> <span class="n">i</span><span class="o">;</span> <span class="n">k</span> <span class="o">&lt;=</span> <span class="n">sqlen</span> <span class="o">+</span> <span class="n">i</span><span class="o">;</span> <span class="n">k</span><span class="o">++)</span> <span class="o">{</span>
                            <span class="k">if</span> <span class="o">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">k</span><span class="o">][</span><span class="n">j</span> <span class="o">+</span> <span class="n">sqlen</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'0'</span><span class="o">)</span> <span class="o">{</span>
                                <span class="n">flag</span> <span class="o">=</span> <span class="kc">false</span><span class="o">;</span>
                                <span class="k">break</span><span class="o">;</span>
                            <span class="o">}</span>
                        <span class="o">}</span>
                        <span class="k">if</span> <span class="o">(</span><span class="n">flag</span><span class="o">)</span>
                            <span class="n">sqlen</span><span class="o">++;</span>
                    <span class="o">}</span>
                    <span class="k">if</span> <span class="o">(</span><span class="n">maxsqlen</span> <span class="o">&lt;</span> <span class="n">sqlen</span><span class="o">)</span> <span class="o">{</span>
                        <span class="n">maxsqlen</span> <span class="o">=</span> <span class="n">sqlen</span><span class="o">;</span>
                    <span class="o">}</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">maxsqlen</span> <span class="o">*</span> <span class="n">maxsqlen</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O\big((mn)^2\big)</script>. In worst case, we need to traverse the complete matrix for every 1.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space is used.</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-accepted">Approach #2 (Dynamic Programming) [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We will explain this approach with the help of an example.</p>
<div class="codehilite"><pre><span></span>0 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 1 1 1 1
0 0 1 1 1
</pre></div>


<p>We initialize another matrix (dp) with the same dimensions as the original one initialized with all 0’s.</p>
<p>dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix. </p>
<p>Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as </p>
<p>
<script type="math/tex; mode=display">
\text{dp}(i,\  j) = \min \big( \text{dp}(i-1,\  j),\  \text{dp}(i-1,\  j-1),\  \text{dp}(i,\  j-1) \big) + 1.
</script>
</p>
<p>We also remember the size of the largest square found so far. In this way, we traverse the original matrix once and find out the required maximum size. This gives the side length of the square (say <script type="math/tex; mode=display">maxsqlen</script>). The required result is the area <script type="math/tex; mode=display">maxsqlen^2</script>.</p>
<p>To understand how this solution works, see the figure below.</p>
<p><img alt="Max Square" src="https://leetcode.com/media/original_images/221_Maximal_Square.PNG?raw=true"></p>
<p>An entry 2 at <script type="math/tex; mode=display">(1, 3)</script> implies that we have a square of side 2 up to that index in the original matrix. Similarly, a 2 at <script type="math/tex; mode=display">(1, 2)</script> and <script type="math/tex; mode=display">(2, 2)</script> implies that a square of side 2 exists up to that index in the original matrix. Now to make a square of side 3, only a single entry of 1 is pending at <script type="math/tex; mode=display">(2, 3)</script>. So, we enter a 3 corresponding to that position in the dp array.</p>
<p>Now consider the case for the index <script type="math/tex; mode=display">(3, 4)</script>. Here, the entries at index <script type="math/tex; mode=display">(3, 3)</script> and <script type="math/tex; mode=display">(2, 3)</script> imply that a square of side 3 is possible up to their indices. But, the entry 1 at index <script type="math/tex; mode=display">(2, 4)</script> indicates that a square of side 1 only can be formed up to its index. Therefore, while making an entry at the index <script type="math/tex; mode=display">(3, 4)</script>, this element obstructs the formation of a square having a side larger than 2. Thus, the maximum sized square that can be formed up to this index is of size <script type="math/tex; mode=display">2\times2</script>.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">maximalSquare</span><span class="o">(</span><span class="kt">char</span><span class="o">[][]</span> <span class="n">matrix</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">rows</span> <span class="o">=</span> <span class="n">matrix</span><span class="o">.</span><span class="na">length</span><span class="o">,</span> <span class="n">cols</span> <span class="o">=</span> <span class="n">rows</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="o">?</span> <span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span> <span class="o">:</span> <span class="mi">0</span><span class="o">;</span>
        <span class="kt">int</span><span class="o">[][]</span> <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">rows</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">cols</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
        <span class="kt">int</span> <span class="n">maxsqlen</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">rows</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">cols</span><span class="o">;</span> <span class="n">j</span><span class="o">++)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">i</span><span class="o">-</span><span class="mi">1</span><span class="o">][</span><span class="n">j</span><span class="o">-</span><span class="mi">1</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'1'</span><span class="o">){</span>
                    <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="o">],</span> <span class="n">dp</span><span class="o">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="o">][</span><span class="n">j</span><span class="o">]),</span> <span class="n">dp</span><span class="o">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="o">][</span><span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="o">])</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
                    <span class="n">maxsqlen</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">max</span><span class="o">(</span><span class="n">maxsqlen</span><span class="o">,</span> <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">]);</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">maxsqlen</span> <span class="o">*</span> <span class="n">maxsqlen</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(mn)</script>. Single pass.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(mn)</script>. Another matrix of same size is used for dp.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-better-dynamic-programming-accepted">Approach #3 (Better Dynamic Programming) [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the previous approach for calculating dp of <script type="math/tex; mode=display">i^{th}</script> row we are using only the previous element and the <script type="math/tex; mode=display">(i-1)^{th}</script> row. Therefore, we don't need 2D dp matrix as 1D dp array will be sufficient for this.</p>
<p>Initially the dp array contains all 0's. As we scan the elements of the original matrix across a row, we keep on updating the dp array as per the equation <script type="math/tex; mode=display">dp[j]=min(dp[j-1],dp[j],prev)</script>, where prev refers to the old <script type="math/tex; mode=display">dp[j-1]</script>. For every row, we repeat the same process and update in the same dp array.</p>
<p><img alt=" Max Square " src="https://leetcode.com/media/original_images/221_Maximal_Square1.png?raw=true"></p>
<p><strong>java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">maximalSquare</span><span class="o">(</span><span class="kt">char</span><span class="o">[][]</span> <span class="n">matrix</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">rows</span> <span class="o">=</span> <span class="n">matrix</span><span class="o">.</span><span class="na">length</span><span class="o">,</span> <span class="n">cols</span> <span class="o">=</span> <span class="n">rows</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="o">?</span> <span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span> <span class="o">:</span> <span class="mi">0</span><span class="o">;</span>
        <span class="kt">int</span><span class="o">[]</span> <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">cols</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
        <span class="kt">int</span> <span class="n">maxsqlen</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">prev</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">rows</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;=</span> <span class="n">cols</span><span class="o">;</span> <span class="n">j</span><span class="o">++)</span> <span class="o">{</span>
                <span class="kt">int</span> <span class="n">temp</span> <span class="o">=</span> <span class="n">dp</span><span class="o">[</span><span class="n">j</span><span class="o">];</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="o">][</span><span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'1'</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">dp</span><span class="o">[</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">dp</span><span class="o">[</span><span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="o">],</span> <span class="n">prev</span><span class="o">),</span> <span class="n">dp</span><span class="o">[</span><span class="n">j</span><span class="o">])</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
                    <span class="n">maxsqlen</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">max</span><span class="o">(</span><span class="n">maxsqlen</span><span class="o">,</span> <span class="n">dp</span><span class="o">[</span><span class="n">j</span><span class="o">]);</span>
                <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
                    <span class="n">dp</span><span class="o">[</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
                <span class="o">}</span>
                <span class="n">prev</span> <span class="o">=</span> <span class="n">temp</span><span class="o">;</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">maxsqlen</span> <span class="o">*</span> <span class="n">maxsqlen</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(mn)</script>. Single pass.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Another array which stores elements in a row is used for dp.</p>
</li>
</ul>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>