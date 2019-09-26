<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-sub-query-and-not-in-clause-accepted">Approach: Using sub-query and NOT IN clause [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-sub-query-and-not-in-clause-accepted">Approach: Using sub-query and <code>NOT IN</code> clause [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>If we have a list of customers who have ever ordered, it will be easy to know who never ordered.</p>
<p>We can use the following code to get such list.</p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="n">customerid</span> <span class="k">from</span> <span class="n">orders</span><span class="p">;</span>
</pre></div>


<p>Then, we can use <code>NOT IN</code> to query the customers who are not in this list.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="n">customers</span><span class="p">.</span><span class="n">name</span> <span class="k">as</span> <span class="s1">'Customers'</span>
<span class="k">from</span> <span class="n">customers</span>
<span class="k">where</span> <span class="n">customers</span><span class="p">.</span><span class="n">id</span> <span class="k">not</span> <span class="k">in</span>
<span class="p">(</span>
    <span class="k">select</span> <span class="n">customerid</span> <span class="k">from</span> <span class="n">orders</span>
<span class="p">);</span>
</pre></div>
          </div>
        
      </div>