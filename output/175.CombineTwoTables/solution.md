<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-outer-join-accepted">Approach: Using outer join [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-outer-join-accepted">Approach: Using <code>outer join</code> [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Since the <em>PersonId</em> in table <strong>Address</strong> is the foreign key of table <strong>Person</strong>, we can join this two table to get the address information of a person.</p>
<p>Considering there might not be an address information for every person, we should use <code>outer join</code> instead of the default <code>inner join</code>.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="n">FirstName</span><span class="p">,</span> <span class="n">LastName</span><span class="p">,</span> <span class="n">City</span><span class="p">,</span> <span class="k">State</span>
<span class="k">from</span> <span class="n">Person</span> <span class="k">left</span> <span class="k">join</span> <span class="n">Address</span>
<span class="k">on</span> <span class="n">Person</span><span class="p">.</span><span class="n">PersonId</span> <span class="o">=</span> <span class="n">Address</span><span class="p">.</span><span class="n">PersonId</span>
<span class="p">;</span>
</pre></div>


<blockquote>
<p>Note: Using <code>where</code> clause to filter the records will fail if there is no address information for a person because it will not display the name information.</p>
</blockquote>
          </div>
        
      </div>