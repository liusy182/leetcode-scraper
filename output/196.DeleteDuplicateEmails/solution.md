<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-delete-and-where-clause-accepted">Approach: Using DELETE and WHERE clause [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-delete-and-where-clause-accepted">Approach: Using <code>DELETE</code> and <code>WHERE</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>By joining this table with itself on the <em>Email</em> column, we can get the following code.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="n">p1</span><span class="p">.</span><span class="o">*</span>
<span class="k">FROM</span> <span class="n">Person</span> <span class="n">p1</span><span class="p">,</span>
    <span class="n">Person</span> <span class="n">p2</span>
<span class="k">WHERE</span>
    <span class="n">p1</span><span class="p">.</span><span class="n">Email</span> <span class="o">=</span> <span class="n">p2</span><span class="p">.</span><span class="n">Email</span>
<span class="p">;</span>
</pre></div>


<p>Then we need to find the bigger id having same email address with other records. So we can add a new condition to the <code>WHERE</code> clause like this.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="n">p1</span><span class="p">.</span><span class="o">*</span>
<span class="k">FROM</span> <span class="n">Person</span> <span class="n">p1</span><span class="p">,</span>
    <span class="n">Person</span> <span class="n">p2</span>
<span class="k">WHERE</span>
    <span class="n">p1</span><span class="p">.</span><span class="n">Email</span> <span class="o">=</span> <span class="n">p2</span><span class="p">.</span><span class="n">Email</span> <span class="k">AND</span> <span class="n">p1</span><span class="p">.</span><span class="n">Id</span> <span class="o">&gt;</span> <span class="n">p2</span><span class="p">.</span><span class="n">Id</span>
<span class="p">;</span>
</pre></div>


<p>As we already get the records to be deleted, we can alter this statement to <code>DELETE</code> in the end.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">DELETE</span> <span class="n">p1</span> <span class="k">FROM</span> <span class="n">Person</span> <span class="n">p1</span><span class="p">,</span>
    <span class="n">Person</span> <span class="n">p2</span>
<span class="k">WHERE</span>
    <span class="n">p1</span><span class="p">.</span><span class="n">Email</span> <span class="o">=</span> <span class="n">p2</span><span class="p">.</span><span class="n">Email</span> <span class="k">AND</span> <span class="n">p1</span><span class="p">.</span><span class="n">Id</span> <span class="o">&gt;</span> <span class="n">p2</span><span class="p">.</span><span class="n">Id</span>
</pre></div>
          </div>
        
      </div>