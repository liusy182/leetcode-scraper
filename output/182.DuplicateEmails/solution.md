<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-i-using-group-by-and-a-temporary-table-accepted">Approach I: Using GROUP BY and a temporary table [Accepted]</a></li>
<li><a href="#approach-ii-using-group-by-and-having-condition-accepted">Approach II: Using GROUP BY and HAVING condition [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-i-using-group-by-and-a-temporary-table-accepted">Approach I: Using <code>GROUP BY</code> and a temporary table [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Duplicated emails existed more than one time. To count the times each email exists, we can use the following code.</p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="n">Email</span><span class="p">,</span> <span class="k">count</span><span class="p">(</span><span class="n">Email</span><span class="p">)</span> <span class="k">as</span> <span class="n">num</span>
<span class="k">from</span> <span class="n">Person</span>
<span class="k">group</span> <span class="k">by</span> <span class="n">Email</span><span class="p">;</span>
</pre></div>


<div class="codehilite"><pre><span></span>| Email   | num |
|---------|-----|
| a@b.com | 2   |
| c@d.com | 1   |
</pre></div>


<p>Taking this as a temporary table, we can get a solution as below.</p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="n">Email</span> <span class="k">from</span>
<span class="p">(</span>
  <span class="k">select</span> <span class="n">Email</span><span class="p">,</span> <span class="k">count</span><span class="p">(</span><span class="n">Email</span><span class="p">)</span> <span class="k">as</span> <span class="n">num</span>
  <span class="k">from</span> <span class="n">Person</span>
  <span class="k">group</span> <span class="k">by</span> <span class="n">Email</span>
<span class="p">)</span> <span class="k">as</span> <span class="n">statistic</span>
<span class="k">where</span> <span class="n">num</span> <span class="o">&gt;</span> <span class="mi">1</span>
<span class="p">;</span>
</pre></div>


<h4 id="approach-ii-using-group-by-and-having-condition-accepted">Approach II: Using <code>GROUP BY</code> and <code>HAVING</code> condition [Accepted]</h4>
<p>A more common used way to add a condition to a <code>GROUP BY</code> is to use the <code>HAVING</code> clause, which is much simpler and more efficient.</p>
<p>So we can rewrite the above solution to this one.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="n">Email</span>
<span class="k">from</span> <span class="n">Person</span>
<span class="k">group</span> <span class="k">by</span> <span class="n">Email</span>
<span class="k">having</span> <span class="k">count</span><span class="p">(</span><span class="n">Email</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">;</span>
</pre></div>
          </div>
        
      </div>