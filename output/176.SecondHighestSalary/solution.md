<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-sub-query-and-limit-clause-accepted">Approach: Using sub-query and LIMIT clause [Accepted]</a></li>
<li><a href="#approach-using-ifnull-and-limit-clause-accepted">Approach: Using IFNULL and LIMIT clause [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-sub-query-and-limit-clause-accepted">Approach: Using sub-query and <code>LIMIT</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Sort the distinct salary in descend order and then utilize the <a href="https://dev.mysql.com/doc/refman/5.7/en/select.html"><code>LIMIT</code></a> clause to get the second highest salary.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="k">DISTINCT</span>
    <span class="n">Salary</span> <span class="k">AS</span> <span class="n">SecondHighestSalary</span>
<span class="k">FROM</span>
    <span class="n">Employee</span>
<span class="k">ORDER</span> <span class="k">BY</span> <span class="n">Salary</span> <span class="k">DESC</span>
<span class="k">LIMIT</span> <span class="mi">1</span> <span class="k">OFFSET</span> <span class="mi">1</span>
</pre></div>


<p>However, this solution will be judged as 'Wrong Answer' if there is no such second highest salary since there might be only one record in this table. To overcome this issue, we can take this as a temp table.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="p">(</span><span class="k">SELECT</span> <span class="k">DISTINCT</span>
            <span class="n">Salary</span>
        <span class="k">FROM</span>
            <span class="n">Employee</span>
        <span class="k">ORDER</span> <span class="k">BY</span> <span class="n">Salary</span> <span class="k">DESC</span>
        <span class="k">LIMIT</span> <span class="mi">1</span> <span class="k">OFFSET</span> <span class="mi">1</span><span class="p">)</span> <span class="k">AS</span> <span class="n">SecondHighestSalary</span>
<span class="p">;</span>
</pre></div>


<h4 id="approach-using-ifnull-and-limit-clause-accepted">Approach: Using <code>IFNULL</code> and <code>LIMIT</code> clause [Accepted]</h4>
<p>Another way to solve the 'NULL' problem is to use <code>IFNULL</code> funtion as below.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">IFNULL</span><span class="p">(</span>
      <span class="p">(</span><span class="k">SELECT</span> <span class="k">DISTINCT</span> <span class="n">Salary</span>
       <span class="k">FROM</span> <span class="n">Employee</span>
       <span class="k">ORDER</span> <span class="k">BY</span> <span class="n">Salary</span> <span class="k">DESC</span>
        <span class="k">LIMIT</span> <span class="mi">1</span> <span class="k">OFFSET</span> <span class="mi">1</span><span class="p">),</span>
    <span class="k">NULL</span><span class="p">)</span> <span class="k">AS</span> <span class="n">SecondHighestSalary</span>
</pre></div>
          </div>
        
      </div>