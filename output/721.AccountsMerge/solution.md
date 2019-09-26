<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
<li><a href="#approach-2-union-find-accepted">Approach #2: Union-Find [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Draw an edge between two emails if they occur in the same account.  The problem comes down to finding connected components of this graph.</p>
<p><strong>Algorithm</strong></p>
<p>For each account, draw the edge from the first email to all other emails.  Additionally, we'll remember a map from emails to names on the side.  After finding each connected component using a depth-first search, we'll add that to our answer.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">accountsMerge</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">accounts</span><span class="p">):</span>
        <span class="n">em_to_name</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">graph</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">defaultdict</span><span class="p">(</span><span class="nb">set</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">acc</span> <span class="ow">in</span> <span class="n">accounts</span><span class="p">:</span>
            <span class="n">name</span> <span class="o">=</span> <span class="n">acc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">email</span> <span class="ow">in</span> <span class="n">acc</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span>
                <span class="n">graph</span><span class="p">[</span><span class="n">acc</span><span class="p">[</span><span class="mi">1</span><span class="p">]]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">email</span><span class="p">)</span>
                <span class="n">graph</span><span class="p">[</span><span class="n">email</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">acc</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                <span class="n">em_to_name</span><span class="p">[</span><span class="n">email</span><span class="p">]</span> <span class="o">=</span> <span class="n">name</span>

        <span class="n">seen</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="n">ans</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">email</span> <span class="ow">in</span> <span class="n">graph</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">email</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">seen</span><span class="p">:</span>
                <span class="n">seen</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">email</span><span class="p">)</span>
                <span class="n">stack</span> <span class="o">=</span> <span class="p">[</span><span class="n">email</span><span class="p">]</span>
                <span class="n">component</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="k">while</span> <span class="n">stack</span><span class="p">:</span>
                    <span class="n">node</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
                    <span class="n">component</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                    <span class="k">for</span> <span class="n">nei</span> <span class="ow">in</span> <span class="n">graph</span><span class="p">[</span><span class="n">node</span><span class="p">]:</span>
                        <span class="k">if</span> <span class="n">nei</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">seen</span><span class="p">:</span>
                            <span class="n">seen</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">nei</span><span class="p">)</span>
                            <span class="n">stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">nei</span><span class="p">)</span>
                <span class="n">ans</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">em_to_name</span><span class="p">[</span><span class="n">email</span><span class="p">]]</span> <span class="o">+</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">component</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">List</span><span class="o">&lt;</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="nf">accountsMerge</span><span class="o">(</span><span class="n">List</span><span class="o">&lt;</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="n">accounts</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">String</span><span class="o">,</span> <span class="n">String</span><span class="o">&gt;</span> <span class="n">emailToName</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">String</span><span class="o">,</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="n">graph</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">account</span><span class="o">:</span> <span class="n">accounts</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">String</span> <span class="n">name</span> <span class="o">=</span> <span class="s">""</span><span class="o">;</span>
            <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">email</span><span class="o">:</span> <span class="n">account</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">name</span> <span class="o">==</span> <span class="s">""</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">name</span> <span class="o">=</span> <span class="n">email</span><span class="o">;</span>
                    <span class="k">continue</span><span class="o">;</span>
                <span class="o">}</span>
                <span class="n">graph</span><span class="o">.</span><span class="na">computeIfAbsent</span><span class="o">(</span><span class="n">email</span><span class="o">,</span> <span class="n">x</span><span class="o">-&gt;</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;()).</span><span class="na">add</span><span class="o">(</span><span class="n">account</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="mi">1</span><span class="o">));</span>
                <span class="n">graph</span><span class="o">.</span><span class="na">computeIfAbsent</span><span class="o">(</span><span class="n">account</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="mi">1</span><span class="o">),</span> <span class="n">x</span><span class="o">-&gt;</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;()).</span><span class="na">add</span><span class="o">(</span><span class="n">email</span><span class="o">);</span>
                <span class="n">emailToName</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">email</span><span class="o">,</span> <span class="n">name</span><span class="o">);</span>
            <span class="o">}</span>
        <span class="o">}</span>

        <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">seen</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashSet</span><span class="o">();</span>
        <span class="n">List</span><span class="o">&lt;</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="n">ans</span> <span class="o">=</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">email</span><span class="o">:</span> <span class="n">graph</span><span class="o">.</span><span class="na">keySet</span><span class="o">())</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(!</span><span class="n">seen</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">email</span><span class="o">))</span> <span class="o">{</span>
                <span class="n">seen</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">email</span><span class="o">);</span>
                <span class="n">Stack</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">stack</span> <span class="o">=</span> <span class="k">new</span> <span class="n">Stack</span><span class="o">();</span>
                <span class="n">stack</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">email</span><span class="o">);</span>
                <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">component</span> <span class="o">=</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">();</span>
                <span class="k">while</span> <span class="o">(!</span><span class="n">stack</span><span class="o">.</span><span class="na">empty</span><span class="o">())</span> <span class="o">{</span>
                    <span class="n">String</span> <span class="n">node</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="na">pop</span><span class="o">();</span>
                    <span class="n">component</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">node</span><span class="o">);</span>
                    <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">nei</span><span class="o">:</span> <span class="n">graph</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">node</span><span class="o">))</span> <span class="o">{</span>
                        <span class="k">if</span> <span class="o">(!</span><span class="n">seen</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">nei</span><span class="o">))</span> <span class="o">{</span>
                            <span class="n">seen</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">nei</span><span class="o">);</span>
                            <span class="n">stack</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">nei</span><span class="o">);</span>
                        <span class="o">}</span>
                    <span class="o">}</span>
                <span class="o">}</span>
                <span class="n">Collections</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">component</span><span class="o">);</span>
                <span class="n">component</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">emailToName</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">email</span><span class="o">));</span>
                <span class="n">ans</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">component</span><span class="o">);</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(\sum a_i \log a_i)</script>, where <script type="math/tex; mode=display">a_i</script> is the length of <code>accounts[i]</code>.  Without the log factor, this is the complexity to build the graph and search for each component.  The log factor is for sorting each component at the end.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(\sum a_i)</script>, the space used by our graph and our search.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-union-find-accepted">Approach #2: Union-Find [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, our problem comes down to finding the connected components of a graph.  This is a natural fit for a <em>Disjoint Set Union</em> (DSU) structure.</p>
<p><strong>Algorithm</strong></p>
<p>As in <em>Approach #1</em>, draw edges between emails if they occur in the same account.  For easier interoperability between our DSU template, we will map each email to some integer index by using <code>emailToID</code>.  Then, <code>dsu.find(email)</code> will tell us a unique id representing what component that email is in.</p>
<p>For more information on DSU, please look at <em>Approach #2</em> in the <a href="https://leetcode.com/articles/redundant-connection/">article here</a>.  For brevity, the solutions showcased below do not use <em>union-by-rank</em>.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">DSU</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">p</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10001</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">):</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">p</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">!=</span> <span class="n">x</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">p</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">p</span><span class="p">[</span><span class="n">x</span><span class="p">])</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">p</span><span class="p">[</span><span class="n">x</span><span class="p">]</span>
    <span class="k">def</span> <span class="nf">union</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">p</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">x</span><span class="p">)]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">accountsMerge</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">accounts</span><span class="p">):</span>
        <span class="n">dsu</span> <span class="o">=</span> <span class="n">DSU</span><span class="p">()</span>
        <span class="n">em_to_name</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">em_to_id</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">acc</span> <span class="ow">in</span> <span class="n">accounts</span><span class="p">:</span>
            <span class="n">name</span> <span class="o">=</span> <span class="n">acc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">email</span> <span class="ow">in</span> <span class="n">acc</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span>
                <span class="n">em_to_name</span><span class="p">[</span><span class="n">email</span><span class="p">]</span> <span class="o">=</span> <span class="n">name</span>
                <span class="k">if</span> <span class="n">email</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">em_to_id</span><span class="p">:</span>
                    <span class="n">em_to_id</span><span class="p">[</span><span class="n">email</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span>
                    <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">dsu</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="n">em_to_id</span><span class="p">[</span><span class="n">acc</span><span class="p">[</span><span class="mi">1</span><span class="p">]],</span> <span class="n">em_to_id</span><span class="p">[</span><span class="n">email</span><span class="p">])</span>

        <span class="n">ans</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">email</span> <span class="ow">in</span> <span class="n">em_to_name</span><span class="p">:</span>
            <span class="n">ans</span><span class="p">[</span><span class="n">dsu</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">em_to_id</span><span class="p">[</span><span class="n">email</span><span class="p">])]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">email</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[[</span><span class="n">em_to_name</span><span class="p">[</span><span class="n">v</span><span class="p">[</span><span class="mi">0</span><span class="p">]]]</span> <span class="o">+</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">ans</span><span class="o">.</span><span class="n">values</span><span class="p">()]</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">List</span><span class="o">&lt;</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="nf">accountsMerge</span><span class="o">(</span><span class="n">List</span><span class="o">&lt;</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="n">accounts</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">DSU</span> <span class="n">dsu</span> <span class="o">=</span> <span class="k">new</span> <span class="n">DSU</span><span class="o">();</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">String</span><span class="o">,</span> <span class="n">String</span><span class="o">&gt;</span> <span class="n">emailToName</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">String</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">emailToID</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="kt">int</span> <span class="n">id</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">account</span><span class="o">:</span> <span class="n">accounts</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">String</span> <span class="n">name</span> <span class="o">=</span> <span class="s">""</span><span class="o">;</span>
            <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">email</span><span class="o">:</span> <span class="n">account</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">name</span> <span class="o">==</span> <span class="s">""</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">name</span> <span class="o">=</span> <span class="n">email</span><span class="o">;</span>
                    <span class="k">continue</span><span class="o">;</span>
                <span class="o">}</span>
                <span class="n">emailToName</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">email</span><span class="o">,</span> <span class="n">name</span><span class="o">);</span>
                <span class="k">if</span> <span class="o">(!</span><span class="n">emailToID</span><span class="o">.</span><span class="na">containsKey</span><span class="o">(</span><span class="n">email</span><span class="o">))</span> <span class="o">{</span>
                    <span class="n">emailToID</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">email</span><span class="o">,</span> <span class="n">id</span><span class="o">++);</span>
                <span class="o">}</span>
                <span class="n">dsu</span><span class="o">.</span><span class="na">union</span><span class="o">(</span><span class="n">emailToID</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">account</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="mi">1</span><span class="o">)),</span> <span class="n">emailToID</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">email</span><span class="o">));</span>
            <span class="o">}</span>
        <span class="o">}</span>

        <span class="n">Map</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="n">ans</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">email</span><span class="o">:</span> <span class="n">emailToName</span><span class="o">.</span><span class="na">keySet</span><span class="o">())</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">index</span> <span class="o">=</span> <span class="n">dsu</span><span class="o">.</span><span class="na">find</span><span class="o">(</span><span class="n">emailToID</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">email</span><span class="o">));</span>
            <span class="n">ans</span><span class="o">.</span><span class="na">computeIfAbsent</span><span class="o">(</span><span class="n">index</span><span class="o">,</span> <span class="n">x</span><span class="o">-&gt;</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">()).</span><span class="na">add</span><span class="o">(</span><span class="n">email</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">component</span><span class="o">:</span> <span class="n">ans</span><span class="o">.</span><span class="na">values</span><span class="o">())</span> <span class="o">{</span>
            <span class="n">Collections</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">component</span><span class="o">);</span>
            <span class="n">component</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">emailToName</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">component</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="mi">0</span><span class="o">)));</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">(</span><span class="n">ans</span><span class="o">.</span><span class="na">values</span><span class="o">());</span>
    <span class="o">}</span>
<span class="o">}</span>
<span class="kd">class</span> <span class="nc">DSU</span> <span class="o">{</span>
    <span class="kt">int</span><span class="o">[]</span> <span class="n">parent</span><span class="o">;</span>
    <span class="kd">public</span> <span class="nf">DSU</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">parent</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="mi">10001</span><span class="o">];</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="mi">10000</span><span class="o">;</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span>
            <span class="n">parent</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">=</span> <span class="n">i</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">find</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">parent</span><span class="o">[</span><span class="n">x</span><span class="o">]</span> <span class="o">!=</span> <span class="n">x</span><span class="o">)</span> <span class="n">parent</span><span class="o">[</span><span class="n">x</span><span class="o">]</span> <span class="o">=</span> <span class="n">find</span><span class="o">(</span><span class="n">parent</span><span class="o">[</span><span class="n">x</span><span class="o">]);</span>
        <span class="k">return</span> <span class="n">parent</span><span class="o">[</span><span class="n">x</span><span class="o">];</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">union</span><span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">,</span> <span class="kt">int</span> <span class="n">y</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">parent</span><span class="o">[</span><span class="n">find</span><span class="o">(</span><span class="n">x</span><span class="o">)]</span> <span class="o">=</span> <span class="n">find</span><span class="o">(</span><span class="n">y</span><span class="o">);</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(A \log A)</script>, where <script type="math/tex; mode=display">A = \sum a_i</script>, and <script type="math/tex; mode=display">a_i</script> is the length of <code>accounts[i]</code>.  If we used union-by-rank, this complexity improves to <script type="math/tex; mode=display">O(A \alpha(A)) \approx O(A)</script>, where <script type="math/tex; mode=display">\alpha</script> is the <em>Inverse-Ackermann</em> function.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(A)</script>, the space used by our DSU structure.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>