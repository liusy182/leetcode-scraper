<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-i-using-flow-control-statement-case-accepted">Approach I: Using flow control statement CASE [Accepted]</a></li>
<li><a href="#approach-ii-using-bit-manipulation-and-coalesce-accepted">Approach II: Using bit manipulation and COALESCE() [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-i-using-flow-control-statement-case-accepted">Approach I: Using flow control statement <code>CASE</code> [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>For students with odd id, the new id is (id+1) after switch unless it is the last seat. And for students with even id, the new id is (id-1). In order to know how many seats in total, we can use a subquery:</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="k">COUNT</span><span class="p">(</span><span class="o">*</span><span class="p">)</span> <span class="k">AS</span> <span class="n">counts</span>
<span class="k">FROM</span>
    <span class="n">seat</span>
</pre></div>


<p>Then, we can use the <code>CASE</code> statement and <code>MOD()</code> function to alter the seat id of each student.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="p">(</span><span class="k">CASE</span>
        <span class="k">WHEN</span> <span class="k">MOD</span><span class="p">(</span><span class="n">id</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span> <span class="k">AND</span> <span class="n">counts</span> <span class="o">!=</span> <span class="n">id</span> <span class="k">THEN</span> <span class="n">id</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">WHEN</span> <span class="k">MOD</span><span class="p">(</span><span class="n">id</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span> <span class="k">AND</span> <span class="n">counts</span> <span class="o">=</span> <span class="n">id</span> <span class="k">THEN</span> <span class="n">id</span>
        <span class="k">ELSE</span> <span class="n">id</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="k">END</span><span class="p">)</span> <span class="k">AS</span> <span class="n">id</span><span class="p">,</span>
    <span class="n">student</span>
<span class="k">FROM</span>
    <span class="n">seat</span><span class="p">,</span>
    <span class="p">(</span><span class="k">SELECT</span>
        <span class="k">COUNT</span><span class="p">(</span><span class="o">*</span><span class="p">)</span> <span class="k">AS</span> <span class="n">counts</span>
    <span class="k">FROM</span>
        <span class="n">seat</span><span class="p">)</span> <span class="k">AS</span> <span class="n">seat_counts</span>
<span class="k">ORDER</span> <span class="k">BY</span> <span class="n">id</span> <span class="k">ASC</span><span class="p">;</span>
</pre></div>


<h4 id="approach-ii-using-bit-manipulation-and-coalesce-accepted">Approach II: Using bit manipulation and <code>COALESCE()</code> [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Bit manipulation expression <code>(id+1)^1-1</code> can calculate the new id after switch.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="n">id</span><span class="p">,</span> <span class="p">(</span><span class="n">id</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">^</span><span class="mi">1</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="n">student</span> <span class="k">FROM</span> <span class="n">seat</span><span class="p">;</span>
</pre></div>


<div class="codehilite"><pre><span></span>| id | (id+1)^1-1 | student |
|----|------------|---------|
| 1  | 2          | Abbot   |
| 2  | 1          | Doris   |
| 3  | 4          | Emerson |
| 4  | 3          | Green   |
| 5  | 6          | Jeames  |
</pre></div>


<p>Then, we can make a temp table and join seat with this table like below.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="o">*</span>
<span class="k">FROM</span>
    <span class="n">seat</span> <span class="n">s1</span>
        <span class="k">LEFT</span> <span class="k">JOIN</span>
    <span class="n">seat</span> <span class="n">s2</span> <span class="k">ON</span> <span class="p">(</span><span class="n">s1</span><span class="p">.</span><span class="n">id</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">^</span><span class="mi">1</span><span class="o">-</span><span class="mi">1</span> <span class="o">=</span> <span class="n">s2</span><span class="p">.</span><span class="n">id</span>
<span class="k">ORDER</span> <span class="k">BY</span> <span class="n">s1</span><span class="p">.</span><span class="n">id</span><span class="p">;</span>
</pre></div>


<div class="codehilite"><pre><span></span>| id | student | id | student |
|----|---------|----|---------|
| 1  | Abbot   | 2  | Doris   |
| 2  | Doris   | 1  | Abbot   |
| 3  | Emerson | 4  | Green   |
| 4  | Green   | 3  | Emerson |
| 5  | Jeames  |    |         |
</pre></div>


<blockquote>
<p>Note:The first two columns are from s1 and the last two are from s2.</p>
</blockquote>
<p>At last, we can output s1.id and s2.student. However, the s2.student is NULL for seat id '5' but s1.student is right. Thus, we we can use function <a href="https://dev.mysql.com/doc/refman/5.7/en/comparison-operators.html#function_coalesce"><code>COALESCE()</code></a> to generate the correct output for the last record.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">s1</span><span class="p">.</span><span class="n">id</span><span class="p">,</span> <span class="n">COALESCE</span><span class="p">(</span><span class="n">s2</span><span class="p">.</span><span class="n">student</span><span class="p">,</span> <span class="n">s1</span><span class="p">.</span><span class="n">student</span><span class="p">)</span> <span class="k">AS</span> <span class="n">student</span>
<span class="k">FROM</span>
    <span class="n">seat</span> <span class="n">s1</span>
        <span class="k">LEFT</span> <span class="k">JOIN</span>
    <span class="n">seat</span> <span class="n">s2</span> <span class="k">ON</span> <span class="p">((</span><span class="n">s1</span><span class="p">.</span><span class="n">id</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">^</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span> <span class="o">=</span> <span class="n">s2</span><span class="p">.</span><span class="n">id</span>
<span class="k">ORDER</span> <span class="k">BY</span> <span class="n">s1</span><span class="p">.</span><span class="n">id</span><span class="p">;</span>
</pre></div>


<blockquote>
<p>Note: This solution comes from <a href="https://discuss.leetcode.com/user/fangxiaofang">@FANGXIAOFANG</a>.</p>
</blockquote>
          </div>
        
      </div>