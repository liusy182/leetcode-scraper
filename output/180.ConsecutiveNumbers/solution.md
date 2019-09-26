<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-distinct-and-where-clause-accepted">Approach: Using DISTINCT and WHERE clause [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-distinct-and-where-clause-accepted">Approach: Using <code>DISTINCT</code> and <code>WHERE</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Consecutive appearing means the Id of the Num are next to each others. Since this problem asks for numbers appearing at least three times consecutively, we can use 3 aliases for this table <strong>Logs</strong>, and then check whether 3 consecutive numbers are all the same.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="o">*</span>
<span class="k">FROM</span>
    <span class="n">Logs</span> <span class="n">l1</span><span class="p">,</span>
    <span class="n">Logs</span> <span class="n">l2</span><span class="p">,</span>
    <span class="n">Logs</span> <span class="n">l3</span>
<span class="k">WHERE</span>
    <span class="n">l1</span><span class="p">.</span><span class="n">Id</span> <span class="o">=</span> <span class="n">l2</span><span class="p">.</span><span class="n">Id</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="k">AND</span> <span class="n">l2</span><span class="p">.</span><span class="n">Id</span> <span class="o">=</span> <span class="n">l3</span><span class="p">.</span><span class="n">Id</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="k">AND</span> <span class="n">l1</span><span class="p">.</span><span class="n">Num</span> <span class="o">=</span> <span class="n">l2</span><span class="p">.</span><span class="n">Num</span>
    <span class="k">AND</span> <span class="n">l2</span><span class="p">.</span><span class="n">Num</span> <span class="o">=</span> <span class="n">l3</span><span class="p">.</span><span class="n">Num</span>
<span class="p">;</span>
</pre></div>


<table>
<thead>
<tr>
<th>Id</th>
<th>Num</th>
<th>Id</th>
<th>Num</th>
<th>Id</th>
<th>Num</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>1</td>
</tr>
<tr>
<td>&gt;Note: The first two columns are from l1, then the next two are from l2, and the last two are from l3.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Then we can select any <em>Num</em> column from the above table to get the target data. However, we need to add a keyword <code>DISTINCT</code> because it will display a duplicated number if one number appears more than 3 times consecutively.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="k">DISTINCT</span>
    <span class="n">l1</span><span class="p">.</span><span class="n">Num</span> <span class="k">AS</span> <span class="n">ConsecutiveNums</span>
<span class="k">FROM</span>
    <span class="n">Logs</span> <span class="n">l1</span><span class="p">,</span>
    <span class="n">Logs</span> <span class="n">l2</span><span class="p">,</span>
    <span class="n">Logs</span> <span class="n">l3</span>
<span class="k">WHERE</span>
    <span class="n">l1</span><span class="p">.</span><span class="n">Id</span> <span class="o">=</span> <span class="n">l2</span><span class="p">.</span><span class="n">Id</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="k">AND</span> <span class="n">l2</span><span class="p">.</span><span class="n">Id</span> <span class="o">=</span> <span class="n">l3</span><span class="p">.</span><span class="n">Id</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="k">AND</span> <span class="n">l1</span><span class="p">.</span><span class="n">Num</span> <span class="o">=</span> <span class="n">l2</span><span class="p">.</span><span class="n">Num</span>
    <span class="k">AND</span> <span class="n">l2</span><span class="p">.</span><span class="n">Num</span> <span class="o">=</span> <span class="n">l3</span><span class="p">.</span><span class="n">Num</span>
<span class="p">;</span>
</pre></div>
          </div>
        
      </div>