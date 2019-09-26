<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursive-approach">Approach 1: Recursive Approach</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursive-approach">Approach 1: Recursive Approach</h4>
<p>To solve this problem, we need to understand "What is the use of median". In statistics, the median is used for:</p>
<blockquote>
<p>Dividing a set into two equal length subsets, that one subset is always greater than the other.</p>
</blockquote>
<p>If we understand the use of median for dividing, we are very close to the answer.</p>
<p>First let's cut <script type="math/tex; mode=display">\text{A}</script> into two parts at a random position <script type="math/tex; mode=display">i</script>:</p>
<div class="codehilite"><pre><span></span>          left_A             |        right_A
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
</pre></div>


<p>Since <script type="math/tex; mode=display">\text{A}</script> has <script type="math/tex; mode=display">m</script> elements, so there are <script type="math/tex; mode=display">m+1</script> kinds of cutting (<script type="math/tex; mode=display">i = 0 \sim m</script>).</p>
<p>And we know:</p>
<blockquote>
<p>
<script type="math/tex; mode=display">\text{len}(\text{left\_A}) = i, \text{len}(\text{right\_A}) = m - i</script>.</p>
<p>Note: when <script type="math/tex; mode=display">i = 0</script>, <script type="math/tex; mode=display">\text{left\_A}</script> is empty, and when <script type="math/tex; mode=display">i = m</script>, <script type="math/tex; mode=display">\text{right\_A}</script> is empty.</p>
</blockquote>
<p>With the same way, cut <script type="math/tex; mode=display">\text{B}</script> into two parts at a random position <script type="math/tex; mode=display">j</script>:</p>
<div class="codehilite"><pre><span></span>          left_B             |        right_B
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
</pre></div>


<p>Put <script type="math/tex; mode=display">\text{left\_A}</script> and <script type="math/tex; mode=display">\text{left\_B}</script> into one set, and put <script type="math/tex; mode=display">\text{right\_A}</script> and <script type="math/tex; mode=display">\text{right\_B}</script> into another set. Let's name them <script type="math/tex; mode=display">\text{left\_part}</script> and <script type="math/tex; mode=display">\text{right\_part}</script>:</p>
<div class="codehilite"><pre><span></span>          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
</pre></div>


<p>If we can ensure:</p>
<blockquote>
<ol>
<li>
<script type="math/tex; mode=display">\text{len}(\text{left\_part}) = \text{len}(\text{right\_part})</script>
</li>
<li>
<script type="math/tex; mode=display">\max(\text{left\_part}) \leq \min(\text{right\_part})</script>
</li>
</ol>
</blockquote>
<p>then we divide all elements in <script type="math/tex; mode=display">\{\text{A}, \text{B}\}</script> into two parts with equal length, and one part is always greater than the other. Then</p>
<p>
<script type="math/tex; mode=display">
\text{median} = \frac{\text{max}(\text{left}\_\text{part}) + \text{min}(\text{right}\_\text{part})}{2}
</script>
</p>
<p>To ensure these two conditions, we just need to ensure:</p>
<blockquote>
<ol>
<li>
<p>
<script type="math/tex; mode=display">i + j = m - i + n - j</script> (or: <script type="math/tex; mode=display">m - i + n - j + 1</script>)<br>
  if <script type="math/tex; mode=display">n \geq m</script>, we just need to set:  <script type="math/tex; mode=display"> \ i = 0 \sim m,\  j = \frac{m + n + 1}{2} - i \\</script>
</p>
</li>
<li>
<p>
<script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i]</script> and <script type="math/tex; mode=display">\text{A}[i-1] \leq \text{B}[j]</script>
</p>
</li>
</ol>
</blockquote>
<p>ps.1 For simplicity, I presume <script type="math/tex; mode=display">\text{A}[i-1], \text{B}[j-1], \text{A}[i], \text{B}[j]</script> are always valid even if <script type="math/tex; mode=display">i=0</script>, <script type="math/tex; mode=display">i=m</script>, <script type="math/tex; mode=display">j=0</script>, or <script type="math/tex; mode=display">j=n</script>.
I will talk about how to deal with these edge values at last.</p>
<p>ps.2 Why <script type="math/tex; mode=display">n \geq m</script>? Because I have to make sure <script type="math/tex; mode=display">j</script> is non-negative since <script type="math/tex; mode=display">0 \leq i \leq m</script> and <script type="math/tex; mode=display">j = \frac{m + n + 1}{2} - i</script>. If <script type="math/tex; mode=display">n < m</script>, then <script type="math/tex; mode=display">j</script> may be negative, that will lead to wrong result.</p>
<p>So, all we need to do is:</p>
<blockquote>
<p>Searching <script type="math/tex; mode=display">i</script> in <script type="math/tex; mode=display">[0, m]</script>, to find an object <script type="math/tex; mode=display">i</script> such that:</p>
<p>
<script type="math/tex; mode=display">\qquad \text{B}[j-1] \leq \text{A}[i]\ </script> and <script type="math/tex; mode=display">\ \text{A}[i-1] \leq \text{B}[j],\ </script> where <script type="math/tex; mode=display">j = \frac{m + n + 1}{2} - i</script>
</p>
</blockquote>
<p>And we can do a binary search following steps described below:</p>
<ol>
<li>Set <script type="math/tex; mode=display">\text{imin} = 0</script>, <script type="math/tex; mode=display">\text{imax} = m</script>, then start searching in <script type="math/tex; mode=display">[\text{imin}, \text{imax}]</script>
</li>
<li>Set <script type="math/tex; mode=display">i = \frac{\text{imin} + \text{imax}}{2}</script>, <script type="math/tex; mode=display">j = \frac{m + n + 1}{2} - i</script>
</li>
<li>
<p>Now we have <script type="math/tex; mode=display">\text{len}(\text{left}\_\text{part})=\text{len}(\text{right}\_\text{part})</script>. And there are only 3 situations that we may encounter:  </p>
<ul>
<li>
<p>
<script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i]</script> and <script type="math/tex; mode=display">\text{A}[i-1] \leq \text{B}[j]</script>
<br>
  Means we have found the object <script type="math/tex; mode=display">i</script>, so stop searching.  </p>
</li>
<li>
<p>
<script type="math/tex; mode=display">\text{B}[j-1] > \text{A}[i]</script>
<br>
  Means <script type="math/tex; mode=display">\text{A}[i]</script> is too small. We must adjust <script type="math/tex; mode=display">i</script> to get <script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i]</script>.<br>
  Can we increase <script type="math/tex; mode=display">i</script>?<br>
        Yes. Because when <script type="math/tex; mode=display">i</script> is increased, <script type="math/tex; mode=display">j</script> will be decreased.<br>
        So <script type="math/tex; mode=display">\text{B}[j-1]</script> is decreased and <script type="math/tex; mode=display">\text{A}[i]</script> is increased, and <script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i]</script> may<br>
        be satisfied.<br>
  Can we decrease <script type="math/tex; mode=display">i</script>?<br>
        No! Because when <script type="math/tex; mode=display">i</script> is decreased, <script type="math/tex; mode=display">j</script> will be increased.<br>
        So <script type="math/tex; mode=display">\text{B}[j-1]</script> is increased and <script type="math/tex; mode=display">\text{A}[i]</script> is decreased, and <script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i]</script> will<br>
        be never satisfied.<br>
  So we must increase <script type="math/tex; mode=display">i</script>. That is, we must adjust the searching range to <script type="math/tex; mode=display">[i+1, \text{imax}]</script>.<br>
  So, set <script type="math/tex; mode=display">\text{imin} = i+1</script>, and goto 2.</p>
</li>
<li>
<p>
<script type="math/tex; mode=display">\text{A}[i-1] > \text{B}[j]</script>:<br>
  Means <script type="math/tex; mode=display">\text{A}[i-1]</script> is too big. And we must decrease <script type="math/tex; mode=display">i</script> to get   <script type="math/tex; mode=display">\text{A}[i-1]\leq \text{B}[j]</script>.<br>
  That is, we must adjust the searching range to <script type="math/tex; mode=display">[\text{imin}, i-1]</script>.<br>
  So, set <script type="math/tex; mode=display">\text{imax} = i-1</script>, and goto 2.</p>
</li>
</ul>
</li>
</ol>
<p>When the object <script type="math/tex; mode=display">i</script> is found, the median is:</p>
<blockquote>
<p>
<script type="math/tex; mode=display">\max(\text{A}[i-1], \text{B}[j-1]), \ </script> when <script type="math/tex; mode=display">m + n</script> is odd</p>
<p>
<script type="math/tex; mode=display">\frac{\max(\text{A}[i-1], \text{B}[j-1]) + \min(\text{A}[i], \text{B}[j])}{2}, \ </script> when <script type="math/tex; mode=display">m + n</script> is even</p>
</blockquote>
<p>Now let's consider the edges values <script type="math/tex; mode=display">i=0,i=m,j=0,j=n</script> where <script type="math/tex; mode=display">\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]</script> may not exist.
Actually this situation is easier than you think.</p>
<p>What we need to do is ensuring that <script type="math/tex; mode=display">\text{max}(\text{left}\_\text{part}) \leq \text{min}(\text{right}\_\text{part})</script>. So, if <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> are not edges values (means <script type="math/tex; mode=display">\text{A}[i-1],
\text{B}[j-1],\text{A}[i],\text{B}[j]</script> all exist), then we must check both <script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i]</script> and <script type="math/tex; mode=display">\text{A}[i-1] \leq \text{B}[j]</script>.
But if some of <script type="math/tex; mode=display">\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]</script> don't exist, then we don't need to check one (or both) of these two conditions.
For example, if <script type="math/tex; mode=display">i=0</script>, then <script type="math/tex; mode=display">\text{A}[i-1]</script> doesn't exist, then we don't need to check <script type="math/tex; mode=display">\text{A}[i-1] \leq \text{B}[j]</script>.
So, what we need to do is:</p>
<blockquote>
<p>Searching <script type="math/tex; mode=display">i</script> in <script type="math/tex; mode=display">[0, m]</script>, to find an object <script type="math/tex; mode=display">i</script> such that:</p>
<p>
<script type="math/tex; mode=display">(j = 0</script> or <script type="math/tex; mode=display">i = m</script> or <script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i])</script> and<br>
<script type="math/tex; mode=display">(i = 0</script> or <script type="math/tex; mode=display">j = n</script> or <script type="math/tex; mode=display">\text{A}[i-1] \leq \text{B}[j]),</script>  where <script type="math/tex; mode=display">j = \frac{m + n + 1}{2} - i</script>
</p>
</blockquote>
<p>And in a searching loop, we will encounter only three situations:</p>
<blockquote>
<ol>
<li>
<script type="math/tex; mode=display">(j = 0</script> or <script type="math/tex; mode=display">i = m</script> or <script type="math/tex; mode=display">\text{B}[j-1] \leq \text{A}[i])</script> and<br>
<script type="math/tex; mode=display">(i = 0</script> or <script type="math/tex; mode=display">j = n</script> or <script type="math/tex; mode=display">\text{A}[i-1] \leq \text{B}[j])</script>
<br>
    Means <script type="math/tex; mode=display">i</script> is perfect, we can stop searching.</li>
<li>
<script type="math/tex; mode=display">j > 0</script> and <script type="math/tex; mode=display">i < m</script> and <script type="math/tex; mode=display">\text{B}[j - 1] > \text{A}[i]</script>
<br>
    Means <script type="math/tex; mode=display">i</script> is too small, we must increase it.</li>
<li>
<script type="math/tex; mode=display">i > 0</script> and <script type="math/tex; mode=display">j < n</script> and <script type="math/tex; mode=display">\text{A}[i - 1] > \text{B}[j]</script>
<br>
    Means <script type="math/tex; mode=display">i</script> is too big, we must decrease it.</li>
</ol>
</blockquote>
<p>Thanks to <a href="https://leetcode.com/Quentin.chen">@Quentin.chen</a> for pointing out that: <script type="math/tex; mode=display">i < m \implies j > 0</script> and <script type="math/tex; mode=display">i > 0 \implies j < n</script>. Because:</p>
<blockquote>
<p>
<script type="math/tex; mode=display">m \leq n,\  i < m \implies j = \frac{m+n+1}{2} - i > \frac{m+n+1}{2} - m \geq \frac{2m+1}{2} - m \geq 0</script>
</p>
<p>
<script type="math/tex; mode=display">m \leq n,\  i > 0 \implies j = \frac{m+n+1}{2} - i < \frac{m+n+1}{2} \leq \frac{2n+1}{2} \leq n</script>
</p>
</blockquote>
<p>So in situation 2. and 3. , we don't need to check whether <script type="math/tex; mode=display">j > 0</script> and whether <script type="math/tex; mode=display">j < n</script>.</p>
<iframe src="https://leetcode.com/playground/X5mgSxnd/shared" frameborder="0" width="100%" height="500" name="X5mgSxnd"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O\big(\log\big(\text{min}(m,n)\big)\big)</script>.<br>
At first, the searching range is <script type="math/tex; mode=display">[0, m]</script>.
And the length of this searching range will be reduced by half after each loop.
So, we only need <script type="math/tex; mode=display">\log(m)</script> loops. Since we do constant operations in each loop, so the time complexity is <script type="math/tex; mode=display">O\big(\log(m)\big)</script>.
Since <script type="math/tex; mode=display">m \leq n</script>, so the time complexity is <script type="math/tex; mode=display">O\big(\log\big(\text{min}(m,n)\big)\big)</script>.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script>.<br>
We only need constant memory to store <script type="math/tex; mode=display">9</script> local variables, so the space complexity is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>