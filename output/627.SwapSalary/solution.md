<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-update-and-casewhen-accepted">Approach: Using UPDATE and CASE...WHEN [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-update-and-casewhen-accepted">Approach: Using <code>UPDATE</code> and <code>CASE...WHEN</code> [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>To dynamically set a value to a column, we can use <a href="https://dev.mysql.com/doc/refman/5.7/en/update.html"><code>UPDATE</code></a> statement together when <a href="https://dev.mysql.com/doc/refman/5.7/en/case.html"><code>CASE...WHEN...</code></a> flow control statement.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">UPDATE</span> <span class="n">salary</span>
<span class="k">SET</span>
    <span class="n">sex</span> <span class="o">=</span> <span class="k">CASE</span> <span class="n">sex</span>
        <span class="k">WHEN</span> <span class="s1">'m'</span> <span class="k">THEN</span> <span class="s1">'f'</span>
        <span class="k">ELSE</span> <span class="s1">'m'</span>
    <span class="k">END</span><span class="p">;</span>
</pre></div>
          </div>
        
      </div>