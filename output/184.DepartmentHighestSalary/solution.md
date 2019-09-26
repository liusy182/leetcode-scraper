<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-join-and-in-clause-accepted">Approach: Using JOIN and IN clause [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-join-and-in-clause-accepted">Approach: Using <code>JOIN</code> and <code>IN</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Since the <strong>Employee</strong> table contains the <em>Salary</em> and <em>DepartmentId</em> information, we can query the highest salary in a department.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">DepartmentId</span><span class="p">,</span> <span class="k">MAX</span><span class="p">(</span><span class="n">Salary</span><span class="p">)</span>
<span class="k">FROM</span>
    <span class="n">Employee</span>
<span class="k">GROUP</span> <span class="k">BY</span> <span class="n">DepartmentId</span><span class="p">;</span>
</pre></div>


<blockquote>
<p>Note: There might be multiple employees having the same highest salary, so it is safe not to include the employee name information in this query.</p>
</blockquote>
<div class="codehilite"><pre><span></span>| DepartmentId | MAX(Salary) |
|--------------|-------------|
| 1            | 90000       |
| 2            | 80000       |
</pre></div>


<p>Then, we can join table <strong>Employee</strong> and <strong>Department</strong>, and query the (DepartmentId, Salary) are in the temp table using <code>IN</code> statement as below.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">Department</span><span class="p">.</span><span class="n">name</span> <span class="k">AS</span> <span class="s1">'Department'</span><span class="p">,</span>
    <span class="n">Employee</span><span class="p">.</span><span class="n">name</span> <span class="k">AS</span> <span class="s1">'Employee'</span><span class="p">,</span>
    <span class="n">Salary</span>
<span class="k">FROM</span>
    <span class="n">Employee</span>
        <span class="k">JOIN</span>
    <span class="n">Department</span> <span class="k">ON</span> <span class="n">Employee</span><span class="p">.</span><span class="n">DepartmentId</span> <span class="o">=</span> <span class="n">Department</span><span class="p">.</span><span class="n">Id</span>
<span class="k">WHERE</span>
    <span class="p">(</span><span class="n">Employee</span><span class="p">.</span><span class="n">DepartmentId</span> <span class="p">,</span> <span class="n">Salary</span><span class="p">)</span> <span class="k">IN</span>
    <span class="p">(</span>   <span class="k">SELECT</span>
            <span class="n">DepartmentId</span><span class="p">,</span> <span class="k">MAX</span><span class="p">(</span><span class="n">Salary</span><span class="p">)</span>
        <span class="k">FROM</span>
            <span class="n">Employee</span>
        <span class="k">GROUP</span> <span class="k">BY</span> <span class="n">DepartmentId</span>
    <span class="p">)</span>
<span class="p">;</span>
</pre></div>


<div class="codehilite"><pre><span></span>| Department | Employee | Salary |
|------------|----------|--------|
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
</pre></div>
          </div>
        
      </div>