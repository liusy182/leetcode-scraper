<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-with-bucket-by-length-accepted">Approach #1: Brute Force with Bucket-By-Length [Accepted]</a></li>
<li><a href="#approach-2-generalized-neighbors-accepted">Approach #2: Generalized Neighbors [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-with-bucket-by-length-accepted">Approach #1: Brute Force with Bucket-By-Length [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Call two strings neighbors if exactly one character can be changed in one to make the strings equal (ie. their hamming distance is 1.)</p>
<p>Strings can only be neighbors if their lengths are equal.  When <code>search</code>ing a new word, let's check only the words that are the same length.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">MagicDictionary</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">buckets</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">buildDict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">words</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">buckets</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">word</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">word</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="n">a</span><span class="o">!=</span><span class="n">b</span> <span class="k">for</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">word</span><span class="p">,</span> <span class="n">candidate</span><span class="p">))</span> <span class="o">==</span> <span class="mi">1</span>
                   <span class="k">for</span> <span class="n">candidate</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">buckets</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)])</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">MagicDictionary</span> <span class="o">{</span>
    <span class="n">Map</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="n">buckets</span><span class="o">;</span>
    <span class="kd">public</span> <span class="nf">MagicDictionary</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">buckets</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">buildDict</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">buckets</span><span class="o">.</span><span class="na">computeIfAbsent</span><span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">(),</span> <span class="n">x</span> <span class="o">-&gt;</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">()).</span><span class="na">add</span><span class="o">(</span><span class="n">word</span><span class="o">);</span>
        <span class="o">}</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">search</span><span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(!</span><span class="n">buckets</span><span class="o">.</span><span class="na">containsKey</span><span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">()))</span> <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">candidate</span><span class="o">:</span> <span class="n">buckets</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">()))</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">mismatch</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">word</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">!=</span> <span class="n">candidate</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">))</span> <span class="o">{</span>
                    <span class="k">if</span> <span class="o">(++</span><span class="n">mismatch</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="o">)</span> <span class="k">break</span><span class="o">;</span>
                <span class="o">}</span>
            <span class="o">}</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">mismatch</span> <span class="o">==</span> <span class="mi">1</span><span class="o">)</span> <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(S)</script> to build and <script type="math/tex; mode=display">O(NK)</script> to search, where <script type="math/tex; mode=display">N</script> is the number of <code>words</code> in our magic dictionary, <script type="math/tex; mode=display">S</script> is the total number of letters in it, and <script type="math/tex; mode=display">K</script> is the length of the search word.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(S)</script>, the space used by <code>buckets</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-generalized-neighbors-accepted">Approach #2: Generalized Neighbors [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Recall in <em>Approach #1</em> that two words are <em>neighbors</em> if exactly one character can be changed in one word to make the strings equal.</p>
<p>Let's say a word 'apple' has <em>generalized neighbors</em> '*pple', 'a*ple', 'ap*le', 'app*e', and 'appl*'. When searching for whether a word like 'apply' has a neighbor like 'apple', we only need to know whether they have a common <em>generalized neighbor</em>.</p>
<p><strong>Algorithm</strong></p>
<p>Continuing the above thinking, one issue is that 'apply' is not a neighbor with itself, yet it has the same generalized neighbor '*pply'.  To remedy this, we'll count how many sources generated '*pply'.  If there are 2 or more, then one of them won't be 'apply'.  If there is exactly one, we should check that it wasn't 'apply'.  In either case, we can be sure that there was some magic word generating '*pply' that <em>wasn't</em> 'apply'.</p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">MagicDictionary</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">_genneighbors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">word</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)):</span>
            <span class="k">yield</span> <span class="n">word</span><span class="p">[:</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="s1">'*'</span> <span class="o">+</span> <span class="n">word</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">:]</span>

    <span class="k">def</span> <span class="nf">buildDict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">words</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">words</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">count</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">Counter</span><span class="p">(</span><span class="n">nei</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">words</span>
                                        <span class="k">for</span> <span class="n">nei</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_genneighbors</span><span class="p">(</span><span class="n">word</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">word</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">count</span><span class="p">[</span><span class="n">nei</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="ow">or</span>
                   <span class="bp">self</span><span class="o">.</span><span class="n">count</span><span class="p">[</span><span class="n">nei</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">word</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">words</span>
                   <span class="k">for</span> <span class="n">nei</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_genneighbors</span><span class="p">(</span><span class="n">word</span><span class="p">))</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">MagicDictionary</span> <span class="o">{</span>
    <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">words</span><span class="o">;</span>
    <span class="n">Map</span><span class="o">&lt;</span><span class="n">String</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">count</span><span class="o">;</span>

    <span class="kd">public</span> <span class="nf">MagicDictionary</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">words</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashSet</span><span class="o">();</span>
        <span class="n">count</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
    <span class="o">}</span>

    <span class="kd">private</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="nf">generalizedNeighbors</span><span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">ans</span> <span class="o">=</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">();</span>
        <span class="kt">char</span><span class="o">[]</span> <span class="n">ca</span> <span class="o">=</span> <span class="n">word</span><span class="o">.</span><span class="na">toCharArray</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">char</span> <span class="n">letter</span> <span class="o">=</span> <span class="n">ca</span><span class="o">[</span><span class="n">i</span><span class="o">];</span>
            <span class="n">ca</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">=</span> <span class="sc">'*'</span><span class="o">;</span>
            <span class="n">String</span> <span class="n">magic</span> <span class="o">=</span> <span class="k">new</span> <span class="n">String</span><span class="o">(</span><span class="n">ca</span><span class="o">);</span>
            <span class="n">ans</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">magic</span><span class="o">);</span>
            <span class="n">ca</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">=</span> <span class="n">letter</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">buildDict</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">this</span><span class="o">.</span><span class="na">words</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">word</span><span class="o">);</span>
            <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">nei</span><span class="o">:</span> <span class="n">generalizedNeighbors</span><span class="o">(</span><span class="n">word</span><span class="o">))</span> <span class="o">{</span>
                <span class="n">count</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">nei</span><span class="o">,</span> <span class="n">count</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">nei</span><span class="o">,</span> <span class="mi">0</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
            <span class="o">}</span>
        <span class="o">}</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">search</span><span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">nei</span><span class="o">:</span> <span class="n">generalizedNeighbors</span><span class="o">(</span><span class="n">word</span><span class="o">))</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">c</span> <span class="o">=</span> <span class="n">count</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">nei</span><span class="o">,</span> <span class="mi">0</span><span class="o">);</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">c</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="o">||</span> <span class="n">c</span> <span class="o">==</span> <span class="mi">1</span> <span class="o">&amp;&amp;</span> <span class="o">!</span><span class="n">words</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">word</span><span class="o">))</span> <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(\sum w_i^2)</script> to build and <script type="math/tex; mode=display">O(K^2)</script> to search, where <script type="math/tex; mode=display">w_i</script> is the length of <code>words[i]</code>, and <script type="math/tex; mode=display">K</script> is the length of our search word.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(\sum w_i^2)</script>, the space used by <code>count</code>.  We also use <script type="math/tex; mode=display">O(K^2)</script> space when generating neighbors to search.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>