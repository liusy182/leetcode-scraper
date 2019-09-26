<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-using-mod-function-accepted">Approach: Using MOD() function [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-using-mod-function-accepted">Approach: Using <code>MOD()</code> function [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We can use the <code>mod(id,2)=1</code> to determine the odd id, and then add a <code>description != 'boring'</code> should address this problem.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">select</span> <span class="o">*</span>
<span class="k">from</span> <span class="n">cinema</span>
<span class="k">where</span> <span class="k">mod</span><span class="p">(</span><span class="n">id</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">and</span> <span class="n">description</span> <span class="o">!=</span> <span class="s1">'boring'</span>
<span class="k">order</span> <span class="k">by</span> <span class="n">rating</span> <span class="k">DESC</span>
<span class="p">;</span>
</pre></div>
          </div>
        
      </div>