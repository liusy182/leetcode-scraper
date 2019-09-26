<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-group-by-clause-and-sub-query-accepted">Approach: Using GROUP BY clause and sub-query [Accepted]</a></li>
<li><a href="#approach-using-group-by-and-having-condition-accepted">Approach: Using GROUP BY and HAVING condition [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-group-by-clause-and-sub-query-accepted">Approach: Using <code>GROUP BY</code> clause and <strong>sub-query</strong> [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>First, we can count the student number in each class. And then select the ones have more than 5 students.</p>
<p><strong>Algorithm</strong></p>
<p>To get the student number in each class. We can use <code>GROUP BY</code> and <code>COUNT</code>, which is very popular used to statistic bases on some character in a table.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="k">class</span><span class="p">,</span> <span class="k">COUNT</span><span class="p">(</span><span class="k">DISTINCT</span> <span class="n">student</span><span class="p">)</span>
<span class="k">FROM</span>
    <span class="n">courses</span>
<span class="k">GROUP</span> <span class="k">BY</span> <span class="k">class</span>
<span class="p">;</span>
</pre></div>


<blockquote>
<p>Note: We use <code>DISTINCT</code> here since the student name may duplicated in a class as it is mentioned int he problem description.</p>
</blockquote>
<div class="codehilite"><pre><span></span>| class    | COUNT(student) |
|----------|----------------|
| Biology  | 1              |
| Computer | 1              |
| English  | 1              |
| Math     | 6              |
</pre></div>


<p>To continue, we can filter the classes by taking the above query as a sub-query.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="k">class</span>
<span class="k">FROM</span>
    <span class="p">(</span><span class="k">SELECT</span>
        <span class="k">class</span><span class="p">,</span> <span class="k">COUNT</span><span class="p">(</span><span class="k">DISTINCT</span> <span class="n">student</span><span class="p">)</span> <span class="k">AS</span> <span class="n">num</span>
    <span class="k">FROM</span>
        <span class="n">courses</span>
    <span class="k">GROUP</span> <span class="k">BY</span> <span class="k">class</span><span class="p">)</span> <span class="k">AS</span> <span class="n">temp_table</span>
<span class="k">WHERE</span>
    <span class="n">num</span> <span class="o">&gt;=</span> <span class="mi">5</span>
<span class="p">;</span>
</pre></div>


<blockquote>
<p>Note: Make an alias of <code>COUNT(student)</code> ('num' in this case) so that you can use in the <code>WHERE</code> clause because it cannot be used directly over there.</p>
</blockquote>
<h4 id="approach-using-group-by-and-having-condition-accepted">Approach: Using <code>GROUP BY</code> and <code>HAVING</code> condition [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Using sub-query is one way to add some condition to a <code>GROUP BY</code> clause, however, using <a href="https://dev.mysql.com/doc/refman/5.7/en/group-by-handling.html"><code>HAVING</code></a> is another simpler and natural approach. So we can rewrite the above solution as below.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="k">class</span>
<span class="k">FROM</span>
    <span class="n">courses</span>
<span class="k">GROUP</span> <span class="k">BY</span> <span class="k">class</span>
<span class="k">HAVING</span> <span class="k">COUNT</span><span class="p">(</span><span class="k">DISTINCT</span> <span class="n">student</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">5</span>
<span class="p">;</span>
</pre></div>
          </div>
        
      </div>