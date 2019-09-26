<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-i-using-where-clause-accepted">Approach I: Using WHERE clause [Accepted]</a></li>
<li><a href="#approach-i-using-join-clause-accepted">Approach I: Using JOIN clause [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-i-using-where-clause-accepted">Approach I: Using <code>WHERE</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>As this table has the employee's manager information, we probably need to select information from it twice.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="o">*</span>
<span class="k">FROM</span> <span class="n">Employee</span> <span class="k">AS</span> <span class="n">a</span><span class="p">,</span> <span class="n">Employee</span> <span class="k">AS</span> <span class="n">b</span>
<span class="p">;</span>
</pre></div>


<blockquote>
<p>Note: The keyword 'AS' is optional.</p>
</blockquote>
<table>
<thead>
<tr>
<th>Id</th>
<th>Name</th>
<th>Salary</th>
<th>ManagerId</th>
<th>Id</th>
<th>Name</th>
<th>Salary</th>
<th>ManagerId</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
</tr>
<tr>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
</tr>
<tr>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
</tr>
<tr>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
</tr>
<tr>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
</tr>
<tr>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
</tr>
<tr>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
</tr>
<tr>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Henry</td>
<td>80000</td>
<td>4</td>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
<td>4</td>
<td>Max</td>
<td>90000</td>
<td></td>
</tr>
<tr>
<td>&gt; The first 3 columns are from a and the last 3 ones are from b.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Select from two tables will get the <a href="https://en.wikipedia.org/wiki/Cartesian_product">Cartesian product</a> of these two tables. In this case, the output will be 4*4 = 16 records. However, what we interest is the employee's salary higher than his/her manager. So we should add two conditions in a <code>WHERE</code> clause like below.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="o">*</span>
<span class="k">FROM</span>
    <span class="n">Employee</span> <span class="k">AS</span> <span class="n">a</span><span class="p">,</span>
    <span class="n">Employee</span> <span class="k">AS</span> <span class="n">b</span>
<span class="k">WHERE</span>
    <span class="n">a</span><span class="p">.</span><span class="n">ManagerId</span> <span class="o">=</span> <span class="n">b</span><span class="p">.</span><span class="n">Id</span>
        <span class="k">AND</span> <span class="n">a</span><span class="p">.</span><span class="n">Salary</span> <span class="o">&gt;</span> <span class="n">b</span><span class="p">.</span><span class="n">Salary</span>
<span class="p">;</span>
</pre></div>


<table>
<thead>
<tr>
<th>Id</th>
<th>Name</th>
<th>Salary</th>
<th>ManagerId</th>
<th>Id</th>
<th>Name</th>
<th>Salary</th>
<th>ManagerId</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Joe</td>
<td>70000</td>
<td>3</td>
<td>3</td>
<td>Sam</td>
<td>60000</td>
<td></td>
</tr>
</tbody>
</table>
<p>As we only need to output the employee's name, so we modify the above code a little to get a solution.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">a</span><span class="p">.</span><span class="n">Name</span> <span class="k">AS</span> <span class="s1">'Employee'</span>
<span class="k">FROM</span>
    <span class="n">Employee</span> <span class="k">AS</span> <span class="n">a</span><span class="p">,</span>
    <span class="n">Employee</span> <span class="k">AS</span> <span class="n">b</span>
<span class="k">WHERE</span>
    <span class="n">a</span><span class="p">.</span><span class="n">ManagerId</span> <span class="o">=</span> <span class="n">b</span><span class="p">.</span><span class="n">Id</span>
        <span class="k">AND</span> <span class="n">a</span><span class="p">.</span><span class="n">Salary</span> <span class="o">&gt;</span> <span class="n">b</span><span class="p">.</span><span class="n">Salary</span>
<span class="p">;</span>
</pre></div>


<h4 id="approach-i-using-join-clause-accepted">Approach I: Using <code>JOIN</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Actually, <code>JOIN</code> is a more common and efficient way to link tables together, and we can use <code>ON</code> to specify some conditions.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
     <span class="n">a</span><span class="p">.</span><span class="n">NAME</span> <span class="k">AS</span> <span class="n">Employee</span>
<span class="k">FROM</span> <span class="n">Employee</span> <span class="k">AS</span> <span class="n">a</span> <span class="k">JOIN</span> <span class="n">Employee</span> <span class="k">AS</span> <span class="n">b</span>
     <span class="k">ON</span> <span class="n">a</span><span class="p">.</span><span class="n">ManagerId</span> <span class="o">=</span> <span class="n">b</span><span class="p">.</span><span class="n">Id</span>
     <span class="k">AND</span> <span class="n">a</span><span class="p">.</span><span class="n">Salary</span> <span class="o">&gt;</span> <span class="n">b</span><span class="p">.</span><span class="n">Salary</span>
<span class="p">;</span>
</pre></div>
          </div>
        
      </div>