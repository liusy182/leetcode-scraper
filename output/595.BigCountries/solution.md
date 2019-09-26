<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-i-using-where-clause-and-or-accepted">Approach I: Using WHERE clause and OR [Accepted]</a></li>
<li><a href="#approach-ii-using-where-clause-and-union-accepted">Approach II: Using WHERE clause and UNION [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-i-using-where-clause-and-or-accepted">Approach I: Using <code>WHERE</code> clause and <code>OR</code> [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Use <code>WHERE</code> clause in SQL to filter these records and get the target countries.</p>
<p><strong>Algorithm</strong></p>
<p>According to the definition, a big country meets at least one of the following two conditions:
1. It has an area of bigger than 3 million square km.
2. It has a population of more than 25 million.</p>
<p>So for the first condition, we can use the following code to get the big countries of this type.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="n">name</span><span class="p">,</span> <span class="n">population</span><span class="p">,</span> <span class="n">area</span> <span class="k">FROM</span> <span class="n">world</span> <span class="k">WHERE</span> <span class="n">area</span> <span class="o">&gt;</span> <span class="mi">3000000</span>
</pre></div>


<p>In addition, we can use below code to get big countries of more than 25 million people.</p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span> <span class="n">name</span><span class="p">,</span> <span class="n">population</span><span class="p">,</span> <span class="n">area</span> <span class="k">FROM</span> <span class="n">world</span> <span class="k">WHERE</span> <span class="n">population</span> <span class="o">&gt;</span> <span class="mi">25000000</span>
</pre></div>


<p>As most people may already come into mind, we can use <code>OR</code> to combine these two solutions for the two sub-problems together.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">name</span><span class="p">,</span> <span class="n">population</span><span class="p">,</span> <span class="n">area</span>
<span class="k">FROM</span>
    <span class="n">world</span>
<span class="k">WHERE</span>
    <span class="n">area</span> <span class="o">&gt;</span> <span class="mi">3000000</span> <span class="k">OR</span> <span class="n">population</span> <span class="o">&gt;</span> <span class="mi">25000000</span>
<span class="p">;</span>
</pre></div>


<h4 id="approach-ii-using-where-clause-and-union-accepted">Approach II: Using <code>WHERE</code> clause and <code>UNION</code> [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>The idea of this approach is the same as the first one. However, we use <code>UNION</code> instead of <code>OR</code>.</p>
<p><strong>MySQL</strong></p>
<div class="codehilite"><pre><span></span><span class="k">SELECT</span>
    <span class="n">name</span><span class="p">,</span> <span class="n">population</span><span class="p">,</span> <span class="n">area</span>
<span class="k">FROM</span>
    <span class="n">world</span>
<span class="k">WHERE</span>
    <span class="n">area</span> <span class="o">&gt;</span> <span class="mi">3000000</span>

<span class="k">UNION</span>

<span class="k">SELECT</span>
    <span class="n">name</span><span class="p">,</span> <span class="n">population</span><span class="p">,</span> <span class="n">area</span>
<span class="k">FROM</span>
    <span class="n">world</span>
<span class="k">WHERE</span>
    <span class="n">population</span> <span class="o">&gt;</span> <span class="mi">25000000</span>
<span class="p">;</span>
</pre></div>


<blockquote>
<p>Note: This solution runs a little bit faster than the first one. However, they do not have big difference.</p>
</blockquote>
          </div>
        
      </div>