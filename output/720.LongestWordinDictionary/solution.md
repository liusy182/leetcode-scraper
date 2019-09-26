<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
<li><a href="#approach-2-trie-depth-first-search-accepted">Approach #2: Trie + Depth-First Search [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>For each word, check if all prefixes word[:k] are present.  We can use a <code>Set</code> structure to check this quickly.</p>
<p><strong>Algorithm</strong></p>
<p>Whenever our found word would be superior, we check if all it's prefixes are present, then replace our answer.</p>
<p>Alternatively, we could have sorted the words beforehand, so that we know the word we are considering would be the answer if all it's prefixes are present.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">longestWord</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">):</span>
    <span class="n">ans</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">wordset</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">words</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">words</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">ans</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">ans</span><span class="p">)</span> <span class="ow">and</span> <span class="n">word</span> <span class="o">&lt;</span> <span class="n">ans</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">all</span><span class="p">(</span><span class="n">word</span><span class="p">[:</span><span class="n">k</span><span class="p">]</span> <span class="ow">in</span> <span class="n">wordset</span> <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">))):</span>
                <span class="n">ans</span> <span class="o">=</span> <span class="n">word</span>

    <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><em>Alternate Implementation</em></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">longestWord</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">):</span>
        <span class="n">wordset</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">words</span><span class="p">)</span>
        <span class="n">words</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">c</span><span class="p">:</span> <span class="p">(</span><span class="o">-</span><span class="nb">len</span><span class="p">(</span><span class="n">c</span><span class="p">),</span> <span class="n">c</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">words</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">all</span><span class="p">(</span><span class="n">word</span><span class="p">[:</span><span class="n">k</span><span class="p">]</span> <span class="ow">in</span> <span class="n">wordset</span> <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">))):</span>
                <span class="k">return</span> <span class="n">word</span>

        <span class="k">return</span> <span class="s2">""</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">String</span> <span class="nf">longestWord</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">String</span> <span class="n">ans</span> <span class="o">=</span> <span class="s">""</span><span class="o">;</span>
        <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">wordset</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashSet</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="n">wordset</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">word</span><span class="o">);</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&gt;</span> <span class="n">ans</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">||</span>
                    <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">==</span> <span class="n">ans</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&amp;&amp;</span> <span class="n">word</span><span class="o">.</span><span class="na">compareTo</span><span class="o">(</span><span class="n">ans</span><span class="o">)</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span>
                <span class="kt">boolean</span> <span class="n">good</span> <span class="o">=</span> <span class="kc">true</span><span class="o">;</span>
                <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">k</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">k</span> <span class="o">&lt;</span> <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="o">++</span><span class="n">k</span><span class="o">)</span> <span class="o">{</span>
                    <span class="k">if</span> <span class="o">(!</span><span class="n">wordset</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">substring</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">k</span><span class="o">)))</span> <span class="o">{</span>
                        <span class="n">good</span> <span class="o">=</span> <span class="kc">false</span><span class="o">;</span>
                        <span class="k">break</span><span class="o">;</span>
                    <span class="o">}</span>
                <span class="o">}</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">good</span><span class="o">)</span> <span class="n">ans</span> <span class="o">=</span> <span class="n">word</span><span class="o">;</span>
            <span class="o">}</span>    
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><em>Alternate Implementation</em></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">String</span> <span class="nf">longestWord</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">wordset</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashSet</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="n">wordset</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">word</span><span class="o">);</span>
        <span class="n">Arrays</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">words</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="o">-&gt;</span> <span class="n">a</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">==</span> <span class="n">b</span><span class="o">.</span><span class="na">length</span><span class="o">()</span>
                    <span class="o">?</span> <span class="n">a</span><span class="o">.</span><span class="na">compareTo</span><span class="o">(</span><span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">-</span> <span class="n">a</span><span class="o">.</span><span class="na">length</span><span class="o">());</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">boolean</span> <span class="n">good</span> <span class="o">=</span> <span class="kc">true</span><span class="o">;</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">k</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">k</span> <span class="o">&lt;</span> <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="o">++</span><span class="n">k</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(!</span><span class="n">wordset</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">substring</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">k</span><span class="o">)))</span> <span class="o">{</span>
                    <span class="n">good</span> <span class="o">=</span> <span class="kc">false</span><span class="o">;</span>
                    <span class="k">break</span><span class="o">;</span>
                <span class="o">}</span>
            <span class="o">}</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">good</span><span class="o">)</span> <span class="k">return</span> <span class="n">word</span><span class="o">;</span>
        <span class="o">}</span>

        <span class="k">return</span> <span class="s">""</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\sum w_i^2)</script>, where <script type="math/tex; mode=display">w_i</script> is the length of <code>words[i]</code>.  Checking whether all prefixes of <code>words[i]</code> are in the set is <script type="math/tex; mode=display">O(\sum w_i^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\sum w_i^2)</script> to create the substrings.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-trie-depth-first-search-accepted">Approach #2: Trie + Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As prefixes of strings are involved, this is usually a natural fit for a <em>trie</em> (a prefix tree.)</p>
<p><strong>Algorithm</strong></p>
<p>Put every word in a trie, then depth-first-search from the start of the trie, only searching nodes that ended a word.  Every node found (except the root, which is a special case) then represents a word with all it's prefixes present.  We take the best such word.</p>
<p>In Python, we showcase a method using defaultdict, while in Java, we stick to a more general object-oriented approach.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">longestWord</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">):</span>
        <span class="n">Trie</span> <span class="o">=</span> <span class="k">lambda</span><span class="p">:</span> <span class="n">collections</span><span class="o">.</span><span class="n">defaultdict</span><span class="p">(</span><span class="n">Trie</span><span class="p">)</span>
        <span class="n">trie</span> <span class="o">=</span> <span class="n">Trie</span><span class="p">()</span>
        <span class="n">END</span> <span class="o">=</span> <span class="bp">True</span>

        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">word</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">words</span><span class="p">):</span>
            <span class="nb">reduce</span><span class="p">(</span><span class="nb">dict</span><span class="o">.</span><span class="n">__getitem__</span><span class="p">,</span> <span class="n">word</span><span class="p">,</span> <span class="n">trie</span><span class="p">)[</span><span class="n">END</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span>

        <span class="n">stack</span> <span class="o">=</span> <span class="n">trie</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
        <span class="n">ans</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">while</span> <span class="n">stack</span><span class="p">:</span>
            <span class="n">cur</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">END</span> <span class="ow">in</span> <span class="n">cur</span><span class="p">:</span>
                <span class="n">word</span> <span class="o">=</span> <span class="n">words</span><span class="p">[</span><span class="n">cur</span><span class="p">[</span><span class="n">END</span><span class="p">]]</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">ans</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">ans</span><span class="p">)</span> <span class="ow">and</span> <span class="n">word</span> <span class="o">&lt;</span> <span class="n">ans</span><span class="p">:</span>
                    <span class="n">ans</span> <span class="o">=</span> <span class="n">word</span>
                <span class="n">stack</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">cur</span><span class="p">[</span><span class="n">letter</span><span class="p">]</span> <span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">cur</span> <span class="k">if</span> <span class="n">letter</span> <span class="o">!=</span> <span class="n">END</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">String</span> <span class="nf">longestWord</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Trie</span> <span class="n">trie</span> <span class="o">=</span> <span class="k">new</span> <span class="n">Trie</span><span class="o">();</span>
        <span class="kt">int</span> <span class="n">index</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">trie</span><span class="o">.</span><span class="na">insert</span><span class="o">(</span><span class="n">word</span><span class="o">,</span> <span class="o">++</span><span class="n">index</span><span class="o">);</span> <span class="c1">//indexed by 1</span>
        <span class="o">}</span>
        <span class="n">trie</span><span class="o">.</span><span class="na">words</span> <span class="o">=</span> <span class="n">words</span><span class="o">;</span>
        <span class="k">return</span> <span class="n">trie</span><span class="o">.</span><span class="na">dfs</span><span class="o">();</span>
    <span class="o">}</span>
<span class="o">}</span>
<span class="kd">class</span> <span class="nc">Node</span> <span class="o">{</span>
    <span class="kt">char</span> <span class="n">c</span><span class="o">;</span>
    <span class="n">HashMap</span><span class="o">&lt;</span><span class="n">Character</span><span class="o">,</span> <span class="n">Node</span><span class="o">&gt;</span> <span class="n">children</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
    <span class="kt">int</span> <span class="n">end</span><span class="o">;</span>
    <span class="kd">public</span> <span class="nf">Node</span><span class="o">(</span><span class="kt">char</span> <span class="n">c</span><span class="o">){</span>
        <span class="k">this</span><span class="o">.</span><span class="na">c</span> <span class="o">=</span> <span class="n">c</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>

<span class="kd">class</span> <span class="nc">Trie</span> <span class="o">{</span>
    <span class="n">Node</span> <span class="n">root</span><span class="o">;</span>
    <span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">;</span>
    <span class="kd">public</span> <span class="nf">Trie</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">root</span> <span class="o">=</span> <span class="k">new</span> <span class="n">Node</span><span class="o">(</span><span class="sc">'0'</span><span class="o">);</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">insert</span><span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">,</span> <span class="kt">int</span> <span class="n">index</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Node</span> <span class="n">cur</span> <span class="o">=</span> <span class="n">root</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">char</span> <span class="n">c</span><span class="o">:</span> <span class="n">word</span><span class="o">.</span><span class="na">toCharArray</span><span class="o">())</span> <span class="o">{</span>
            <span class="n">cur</span><span class="o">.</span><span class="na">children</span><span class="o">.</span><span class="na">putIfAbsent</span><span class="o">(</span><span class="n">c</span><span class="o">,</span> <span class="k">new</span> <span class="n">Node</span><span class="o">(</span><span class="n">c</span><span class="o">));</span>
            <span class="n">cur</span> <span class="o">=</span> <span class="n">cur</span><span class="o">.</span><span class="na">children</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">c</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="n">cur</span><span class="o">.</span><span class="na">end</span> <span class="o">=</span> <span class="n">index</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="n">String</span> <span class="nf">dfs</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">String</span> <span class="n">ans</span> <span class="o">=</span> <span class="s">""</span><span class="o">;</span>
        <span class="n">Stack</span><span class="o">&lt;</span><span class="n">Node</span><span class="o">&gt;</span> <span class="n">stack</span> <span class="o">=</span> <span class="k">new</span> <span class="n">Stack</span><span class="o">();</span>
        <span class="n">stack</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">root</span><span class="o">);</span>
        <span class="k">while</span> <span class="o">(!</span><span class="n">stack</span><span class="o">.</span><span class="na">empty</span><span class="o">())</span> <span class="o">{</span>
            <span class="n">Node</span> <span class="n">node</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="na">pop</span><span class="o">();</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">node</span><span class="o">.</span><span class="na">end</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="o">||</span> <span class="n">node</span> <span class="o">==</span> <span class="n">root</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">node</span> <span class="o">!=</span> <span class="n">root</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">String</span> <span class="n">word</span> <span class="o">=</span> <span class="n">words</span><span class="o">[</span><span class="n">node</span><span class="o">.</span><span class="na">end</span> <span class="o">-</span> <span class="mi">1</span><span class="o">];</span>
                    <span class="k">if</span> <span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&gt;</span> <span class="n">ans</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">||</span>
                            <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">==</span> <span class="n">ans</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&amp;&amp;</span> <span class="n">word</span><span class="o">.</span><span class="na">compareTo</span><span class="o">(</span><span class="n">ans</span><span class="o">)</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span>
                        <span class="n">ans</span> <span class="o">=</span> <span class="n">word</span><span class="o">;</span>
                    <span class="o">}</span>
                <span class="o">}</span>
                <span class="k">for</span> <span class="o">(</span><span class="n">Node</span> <span class="n">nei</span><span class="o">:</span> <span class="n">node</span><span class="o">.</span><span class="na">children</span><span class="o">.</span><span class="na">values</span><span class="o">())</span> <span class="o">{</span>
                    <span class="n">stack</span><span class="o">.</span><span class="na">push</span><span class="o">(</span><span class="n">nei</span><span class="o">);</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(\sum w_i)</script>, where <script type="math/tex; mode=display">w_i</script> is the length of <code>words[i]</code>.  This is the complexity to build the trie and to search it.</li>
</ul>
<p>If we used a BFS instead of a DFS, and ordered the children in an array, we could drop the need to check whether the candidate word at each node is better than the answer, by forcing that the last node visited will be the best answer.</p>
<ul>
<li>Space Complexity: <script type="math/tex; mode=display">O(\sum w_i)</script>, the space used by our trie.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>