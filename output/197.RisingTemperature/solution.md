<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-join-and-datediff-clause-accepted">Approach: Using JOIN and DATEDIFF() clause [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-join-and-datediff-clause-accepted">Approach: Using <code>JOIN</code> and <code>DATEDIFF()</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>MySQL uses <a href="https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_datediff">DATEDIFF</a> to compare two date type values.</p>
<p>So, we can get the result by joining this table <strong>weather</strong> with itself and use this <code>DATEDIFF()</code> function.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">weather</span><span class="p">.</span><span class="n">id</span> <span class="k">AS</span> <span class="s1">'Id'</span>
<span class="k">FROM</span>
    <span class="n">weather</span>
        <span class="k">JOIN</span>
    <span class="n">weather</span> <span class="n">w</span> <span class="k">ON</span> <span class="n">DATEDIFF</span><span class="p">(</span><span class="n">weather</span><span class="p">.</span><span class="nb">date</span><span class="p">,</span> <span class="n">w</span><span class="p">.</span><span class="nb">date</span><span class="p">)</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="k">AND</span> <span class="n">weather</span><span class="p">.</span><span class="n">Temperature</span> <span class="o">&gt;</span> <span class="n">w</span><span class="p">.</span><span class="n">Temperature</span>
<span class="p">;</span>
</pre></div>
          </div>
        
      </div>