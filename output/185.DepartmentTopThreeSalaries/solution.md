<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-join-and-sub-query-accepted">Approach: Using JOIN and sub-query [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-join-and-sub-query-accepted">Approach: Using <code>JOIN</code> and sub-query [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>A top 3 salary in this company means there is no more than 3 salary bigger than itself in the company.</p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="n">e1</span><span class="p">.</span><span class="n">Name</span> <span class="k">as</span> <span class="s1">'Employee'</span><span class="p">,</span> <span class="n">e1</span><span class="p">.</span><span class="n">Salary</span>
<span class="k">from</span> <span class="n">Employee</span> <span class="n">e1</span>
<span class="k">where</span> <span class="mi">3</span> <span class="o">&gt;</span>
<span class="p">(</span>
    <span class="k">select</span> <span class="k">count</span><span class="p">(</span><span class="k">distinct</span> <span class="n">e2</span><span class="p">.</span><span class="n">Salary</span><span class="p">)</span>
    <span class="k">from</span> <span class="n">Employee</span> <span class="n">e2</span>
    <span class="k">where</span> <span class="n">e2</span><span class="p">.</span><span class="n">Salary</span> <span class="o">&gt;</span> <span class="n">e1</span><span class="p">.</span><span class="n">Salary</span>
<span class="p">)</span>
<span class="p">;</span>
</pre></div>


<p>In this code, we count the salary number of which is bigger than e1.Salary. So the output is as below for the sample data.</p>
<div class="codehilite"><pre><span></span>| Employee | Salary |
|----------|--------|
| Henry    | 80000  |
| Max      | 90000  |
| Randy    | 85000  |
</pre></div>


<p>Then, we need to join the <strong>Employee</strong> table with <strong>Department</strong> in order to retrieve the department information.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">d</span><span class="p">.</span><span class="n">Name</span> <span class="k">AS</span> <span class="s1">'Department'</span><span class="p">,</span> <span class="n">e1</span><span class="p">.</span><span class="n">Name</span> <span class="k">AS</span> <span class="s1">'Employee'</span><span class="p">,</span> <span class="n">e1</span><span class="p">.</span><span class="n">Salary</span>
<span class="k">FROM</span>
    <span class="n">Employee</span> <span class="n">e1</span>
        <span class="k">JOIN</span>
    <span class="n">Department</span> <span class="n">d</span> <span class="k">ON</span> <span class="n">e1</span><span class="p">.</span><span class="n">DepartmentId</span> <span class="o">=</span> <span class="n">d</span><span class="p">.</span><span class="n">Id</span>
<span class="k">WHERE</span>
    <span class="mi">3</span> <span class="o">&gt;</span> <span class="p">(</span><span class="k">SELECT</span>
            <span class="k">COUNT</span><span class="p">(</span><span class="k">DISTINCT</span> <span class="n">e2</span><span class="p">.</span><span class="n">Salary</span><span class="p">)</span>
        <span class="k">FROM</span>
            <span class="n">Employee</span> <span class="n">e2</span>
        <span class="k">WHERE</span>
            <span class="n">e2</span><span class="p">.</span><span class="n">Salary</span> <span class="o">&gt;</span> <span class="n">e1</span><span class="p">.</span><span class="n">Salary</span>
                <span class="k">AND</span> <span class="n">e1</span><span class="p">.</span><span class="n">DepartmentId</span> <span class="o">=</span> <span class="n">e2</span><span class="p">.</span><span class="n">DepartmentId</span>
        <span class="p">)</span>
<span class="p">;</span>
</pre></div>


<div class="codehilite"><pre><span></span>| Department | Employee | Salary |
|------------|----------|--------|
| IT         | Joe      | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
</pre></div>
          </div>
        
      </div>