<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-notes">Approach Notes</a></li>
<li><a href="#approach-1-three-pointer">Approach 1: Three Pointer</a></li>
<li><a href="#approach-2-counting-with-cases">Approach 2: Counting with Cases</a></li>
<li><a href="#approach-3-adapt-from-three-sum">Approach 3: Adapt from Three Sum</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-notes">Approach Notes</h4>
<p>The approaches described below assume some familiarity with the two pointer technique that can be used to solve the LeetCode problem "Two Sum".</p>
<p>In the problem, we have a sorted array <code>A</code> of unique elements, and want to know how many <code>i &lt; j</code> with <code>A[i] + A[j] == target</code>.</p>
<p>The idea that does it in linear time, is that for each <code>i</code> in increasing order, the <code>j</code>'s that satisfy the equation <code>A[i] + A[j] == target</code> are decreasing.</p>
<div class="codehilite"><pre><span></span><span class="k">def</span> <span class="nf">solve</span><span class="p">(</span><span class="n">A</span><span class="p">,</span> <span class="n">target</span><span class="p">):</span>
    <span class="c1"># Assume A already sorted</span>
    <span class="n">i</span><span class="p">,</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">j</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">A</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="n">A</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">target</span><span class="p">:</span>
            <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">elif</span> <span class="n">A</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="n">A</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">target</span><span class="p">:</span>
            <span class="n">j</span> <span class="o">-=</span> <span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">ans</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">j</span> <span class="o">-=</span> <span class="mi">1</span>
    <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p>This is not a complete explanation.  For more on this problem, please review the LeetCode problem "Two Sum".</p>
<hr>
<h4 id="approach-1-three-pointer">Approach 1: Three Pointer</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Sort the array.  For each <code>i</code>, set <code>T = target - A[i]</code>, the remaining target.  We can try using a two-pointer technique to find <code>A[j] + A[k] == T</code>.  This approach is the natural continuation of trying to make the two-pointer technique we know from previous problems, work on this problem.</p>
<p>Because some elements are duplicated, we have to be careful.  In a typical case, the target is say, <code>8</code>, and we have a remaining array (<code>A[i+1:]</code>) of <code>[2,2,2,2,3,3,4,4,4,5,5,5,6,6]</code>.  We can analyze this situation with cases.</p>
<p>Whenever <code>A[j] + A[k] == T</code>, we should count the multiplicity of <code>A[j]</code> and <code>A[k]</code>.  In this example, if <code>A[j] == 2</code> and <code>A[k] == 6</code>, the multiplicities are <code>4</code> and <code>2</code>, and the total number of pairs is <code>4 * 2 = 8</code>.  We then move to the remaining window <code>A[j:k+1]</code> of <code>[3,3,4,4,4,5,5,5]</code>.</p>
<p>As a special case, if <code>A[j] == A[k]</code>, then our manner of counting would be incorrect.  If for example the remaining window is <code>[4,4,4]</code>, there are only 3 such pairs.  In general, when <code>A[j] == A[k]</code>, we have <script type="math/tex; mode=display">\binom{M}{2} = \frac{M*(M-1)}{2}</script> pairs <code>(j,k)</code> (with <code>j &lt; k</code>) that satisfy <code>A[j] + A[k] == T</code>, where <script type="math/tex; mode=display">M</script> is the multiplicity of <code>A[j]</code> (in this case <script type="math/tex; mode=display">M=3</script>).</p>
<p>For more details, please see the inline comments.</p>
<iframe src="https://leetcode.com/playground/TCrTgDfK/shared" frameborder="0" width="100%" height="500" name="TCrTgDfK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-counting-with-cases">Approach 2: Counting with Cases</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <code>count[x]</code> be the number of times that <code>x</code> occurs in <code>A</code>.  For every <code>x+y+z == target</code>, we can try to count the correct contribution to the answer.  There are a few cases:</p>
<ul>
<li>
<p>If <code>x</code>, <code>y</code>, and <code>z</code> are all different, then the contribution is <code>count[x] * count[y] * count[z]</code>.</p>
</li>
<li>
<p>If <code>x == y != z</code>, the contribution is <script type="math/tex; mode=display">\binom{\text{count[x]}}{2} * \text{count[z]}</script>.</p>
</li>
<li>
<p>If <code>x != y == z</code>, the contribution is <script type="math/tex; mode=display">\text{count[x]} * \binom{\text{count[y]}}{2}</script>.</p>
</li>
<li>
<p>If <code>x == y == z</code>, the contribution is <script type="math/tex; mode=display">\binom{\text{count[x]}}{3}</script>.</p>
</li>
</ul>
<p>(<em>Here, <script type="math/tex; mode=display">\binom{n}{k}</script> denotes the binomial coefficient <script type="math/tex; mode=display">\frac{n!}{(n-k)!k!}</script>.</em>)</p>
<p>Each case is commented in the implementations below.</p>
<iframe src="https://leetcode.com/playground/9nU5mTcv/shared" frameborder="0" width="100%" height="500" name="9nU5mTcv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + W^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">W</script> is the maximum possible value of <code>A[i]</code>.  (Note that this solution can be adapted to be <script type="math/tex; mode=display">O(N^2)</script> even in the case that <script type="math/tex; mode=display">W</script> is very large.)</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(W)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-adapt-from-three-sum">Approach 3: Adapt from Three Sum</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in <em>Approach 2</em>, let <code>count[x]</code> be the number of times that <code>x</code> occurs in <code>A</code>.  Also, let <code>keys</code> be a sorted list of unique values of <code>A</code>.  We will try to adapt a 3Sum algorithm to work on <code>keys</code>, but add the correct answer contributions.</p>
<p>For example, if <code>A = [1,1,2,2,3,3,4,4,5,5]</code> and <code>target = 8</code>, then <code>keys = [1,2,3,4,5]</code>.  When doing 3Sum on <code>keys</code> (with <code>i &lt;= j &lt;= k</code>), we will encounter some tuples that sum to the target, like <code>(x,y,z) = (1,2,5), (1,3,4), (2,2,4), (2,3,3)</code>.  We can then use <code>count</code> to calculate how many such tuples there are in each case.</p>
<p>This approach assumes familiarity with <em>3Sum</em>.  For more, please visit the associated LeetCode problem here <a href="https://leetcode.com/problems/3sum">https://leetcode.com/problems/3sum</a>.</p>
<iframe src="https://leetcode.com/playground/Ph3ok9qb/shared" frameborder="0" width="100%" height="500" name="Ph3ok9qb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>