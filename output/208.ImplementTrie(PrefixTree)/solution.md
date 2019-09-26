<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#applications">Applications</a><ul>
<li><a href="#1-autocomplete">1. Autocomplete</a></li>
<li><a href="#2-spell-checker">2. Spell checker</a></li>
<li><a href="#3-ip-routing-longest-prefix-matching">3. IP routing (Longest prefix matching)</a></li>
<li><a href="#4-t9-predictive-text">4. T9 predictive text</a></li>
<li><a href="#5-solving-word-games">5. Solving word games</a></li>
</ul>
</li>
<li><a href="#trie-node-structure">Trie node structure</a></li>
<li><a href="#insertion-of-a-key-to-a-trie">Insertion of a key to a trie</a></li>
<li><a href="#search-for-a-key-in-a-trie">Search for a key in a trie</a></li>
<li><a href="#search-for-a-key-prefix-in-a-trie">Search for a key prefix in a trie</a></li>
</ul>
</li>
<li><a href="#practice-problems">Practice Problems</a></li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for intermediate level users. It introduces the following ideas:
The data structure Trie (Prefix tree) and most common operations with it.</p>
<h2 id="solution">Solution</h2>
<h4 id="applications">Applications</h4>
<p>Trie (we pronounce "try") or prefix tree is a tree data structure, which is used for retrieval of a key in a dataset of strings.
There are various applications of this very efficient data structure such as :</p>
<h5 id="1-autocomplete">1. <a href="https://en.wikipedia.org/wiki/Autocomplete">Autocomplete</a></h5>
<p align="center"><img alt="Google Suggest" src="https://leetcode.com/media/original_images/208_GoogleSuggest.png" width="539px"></p>
<p align="center"><em>Figure 1. Google Suggest in action.</em></p>
<h5 id="2-spell-checker">2. <a href="https://en.wikipedia.org/wiki/Spell_checker">Spell checker</a></h5>
<p align="center"><img alt="Spell Checker" src="https://leetcode.com/media/original_images/208_SpellCheck.png" width="400px"></p>
<p align="center"><em>Figure 2. A spell checker used in word processor.</em></p>
<h5 id="3-ip-routing-longest-prefix-matching">3. <a href="https://en.wikipedia.org/wiki/Longest_prefix_match">IP routing (Longest prefix matching)</a></h5>
<p align="center"><img alt="IP Routing" src="https://leetcode.com/media/original_images/208_IPRouting.gif" width="539px"></p>
<p align="center"><em>Figure 3. Longest prefix matching algorithm uses Tries in Internet Protocol (IP) routing to select an entry from a forwarding table.</em></p>
<h5 id="4-t9-predictive-text">4. <a href="https://en.wikipedia.org/wiki/T9_(predictive_text)">T9 predictive text</a></h5>
<p align="center"><img alt="T9 Predictive Text" src="https://leetcode.com/media/original_images/208_T9.jpg"></p>
<p align="center"><em>Figure 4. T9 which stands for Text on 9 keys, was used on phones to input texts during the late 1990s.</em></p>
<h5 id="5-solving-word-games">5. <a href="https://en.wikipedia.org/wiki/Boggle">Solving word games</a></h5>
<p align="center"><img alt="Boggle" src="https://leetcode.com/media/original_images/208_Boggle.png" width="350px"></p>
<p align="center"><em>Figure 5. Tries is used to solve Boggle efficiently by pruning the search space.</em></p>
<p>There are several other data structures, like balanced trees and hash tables, which give us the possibility to search for a word in a dataset of strings. Then why do we need trie?
Although hash table has <script type="math/tex; mode=display">O(1)</script> time complexity for looking for a key, it is not efficient in the following operations :</p>
<ul>
<li>Finding all keys with a common prefix.</li>
<li>Enumerating a dataset of strings in lexicographical order.</li>
</ul>
<p>Another reason why trie outperforms hash table, is that as hash table increases in size, there are lots of hash collisions and the search time complexity could deteriorate to <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n</script> is the number of keys inserted.
Trie could use less space compared to Hash Table when storing many keys with the same prefix.
In this case using trie has only <script type="math/tex; mode=display">O(m)</script> time complexity, where <script type="math/tex; mode=display">m</script> is the key length.
Searching for a key in a balanced tree costs  <script type="math/tex; mode=display">O(m \log n)</script> time complexity.</p>
<h4 id="trie-node-structure">Trie node structure</h4>
<p>Trie is a rooted tree. Its nodes have the following fields:</p>
<ul>
<li>Maximum of <script type="math/tex; mode=display">R</script> links to its children, where each link corresponds to one of <script type="math/tex; mode=display">R</script> character values from dataset alphabet.
In this article we assume that <script type="math/tex; mode=display">R</script> is 26, the number of lowercase latin letters.</li>
<li>Boolean field which specifies whether the node corresponds to the end of the key, or is just a key prefix.</li>
</ul>
<p align="center"><img alt="Representation of a key in trie" src="https://leetcode.com/media/original_images/208_Node.png" width="539px"></p>
<p align="center"><em>Figure 6. Representation of a key "leet" in trie.</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">TrieNode</span> <span class="o">{</span>

    <span class="c1">// R links to node children</span>
    <span class="kd">private</span> <span class="n">TrieNode</span><span class="o">[]</span> <span class="n">links</span><span class="o">;</span>

    <span class="kd">private</span> <span class="kd">final</span> <span class="kt">int</span> <span class="n">R</span> <span class="o">=</span> <span class="mi">26</span><span class="o">;</span>

    <span class="kd">private</span> <span class="kt">boolean</span> <span class="n">isEnd</span><span class="o">;</span>

    <span class="kd">public</span> <span class="nf">TrieNode</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">links</span> <span class="o">=</span> <span class="k">new</span> <span class="n">TrieNode</span><span class="o">[</span><span class="n">R</span><span class="o">];</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">containsKey</span><span class="o">(</span><span class="kt">char</span> <span class="n">ch</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">return</span> <span class="n">links</span><span class="o">[</span><span class="n">ch</span> <span class="o">-</span><span class="sc">'a'</span><span class="o">]</span> <span class="o">!=</span> <span class="kc">null</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="n">TrieNode</span> <span class="nf">get</span><span class="o">(</span><span class="kt">char</span> <span class="n">ch</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">return</span> <span class="n">links</span><span class="o">[</span><span class="n">ch</span> <span class="o">-</span><span class="sc">'a'</span><span class="o">];</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">put</span><span class="o">(</span><span class="kt">char</span> <span class="n">ch</span><span class="o">,</span> <span class="n">TrieNode</span> <span class="n">node</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">links</span><span class="o">[</span><span class="n">ch</span> <span class="o">-</span><span class="sc">'a'</span><span class="o">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">setEnd</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">isEnd</span> <span class="o">=</span> <span class="kc">true</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">isEnd</span><span class="o">()</span> <span class="o">{</span>
        <span class="k">return</span> <span class="n">isEnd</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p>Two of the most common operations in a trie are insertion of a key and search for a key.</p>
<h4 id="insertion-of-a-key-to-a-trie">Insertion of a key to a trie</h4>
<p>We insert a key by searching into the trie. We start from the root and search a link, which corresponds to the first key character. There are two cases :</p>
<ul>
<li>A link exists. Then we move down the tree following the link to the next child level. The algorithm continues with searching for the next key character.</li>
<li>A link does not exist. Then we create a new node and link it with the parent's link matching the current key character.
We repeat this step until we encounter the last character of the key, then we mark the current node as an end node and the algorithm finishes.</li>
</ul>
<p align="center"><img alt="Insertion of keys into a trie" src="https://leetcode.com/media/original_images/208_TrieInsert.png" width="539px"></p>
<p align="center"><em>Figure 7. Insertion of keys into a trie.</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Trie</span> <span class="o">{</span>
    <span class="kd">private</span> <span class="n">TrieNode</span> <span class="n">root</span><span class="o">;</span>

    <span class="kd">public</span> <span class="nf">Trie</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">root</span> <span class="o">=</span> <span class="k">new</span> <span class="n">TrieNode</span><span class="o">();</span>
    <span class="o">}</span>

    <span class="c1">// Inserts a word into the trie.</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">insert</span><span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">TrieNode</span> <span class="n">node</span> <span class="o">=</span> <span class="n">root</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="kt">char</span> <span class="n">currentChar</span> <span class="o">=</span> <span class="n">word</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">);</span>
            <span class="k">if</span> <span class="o">(!</span><span class="n">node</span><span class="o">.</span><span class="na">containsKey</span><span class="o">(</span><span class="n">currentChar</span><span class="o">))</span> <span class="o">{</span>
                <span class="n">node</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">currentChar</span><span class="o">,</span> <span class="k">new</span> <span class="n">TrieNode</span><span class="o">());</span>
            <span class="o">}</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">currentChar</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="n">node</span><span class="o">.</span><span class="na">setEnd</span><span class="o">();</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(m)</script>, where m is the key length.</li>
</ul>
<p>In each iteration of the algorithm, we either examine or create a node in the trie till we reach the end of the key. This takes only <script type="math/tex; mode=display">m</script> operations.</p>
<ul>
<li>Space complexity : <script type="math/tex; mode=display">O(m)</script>.</li>
</ul>
<p>In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add <script type="math/tex; mode=display">m</script>
new nodes, which takes us  <script type="math/tex; mode=display">O(m)</script> space.</p>
<h4 id="search-for-a-key-in-a-trie">Search for a key in a trie</h4>
<p>Each key is represented in the trie as a path from the root to the internal node or leaf.
We start from the root with the first key character. We examine the current node for a link corresponding to the key character. There are two cases :</p>
<ul>
<li>A link exist. We move to the next node in the path following this link, and proceed searching for the next key character.</li>
<li>
<p>A link does not exist. If there are no available key characters and current node is marked as <code>isEnd</code> we return true. Otherwise there are possible two cases in each of them we return false :</p>
<ul>
<li>There are key characters left, but it is impossible to follow the key path in the trie, and the key is missing.</li>
<li>No key characters left, but current node is not marked as <code>isEnd</code>. Therefore the search key is only a prefix of another key in the trie.</li>
</ul>
</li>
</ul>
<p align="center"><img alt="Search of a key in a trie" src="https://leetcode.com/media/original_images/208_TrieSearchKey.png" width="539px"></p>
<p align="center"><em>Figure 8. Search for a key in a trie.</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Trie</span> <span class="o">{</span>
    <span class="o">...</span>

    <span class="c1">// search a prefix or whole key in trie and</span>
    <span class="c1">// returns the node where search ends</span>
    <span class="kd">private</span> <span class="n">TrieNode</span> <span class="nf">searchPrefix</span><span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">TrieNode</span> <span class="n">node</span> <span class="o">=</span> <span class="n">root</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">word</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
           <span class="kt">char</span> <span class="n">curLetter</span> <span class="o">=</span> <span class="n">word</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">);</span>
           <span class="k">if</span> <span class="o">(</span><span class="n">node</span><span class="o">.</span><span class="na">containsKey</span><span class="o">(</span><span class="n">curLetter</span><span class="o">))</span> <span class="o">{</span>
               <span class="n">node</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">curLetter</span><span class="o">);</span>
           <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
               <span class="k">return</span> <span class="kc">null</span><span class="o">;</span>
           <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">node</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="c1">// Returns if the word is in the trie.</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">search</span><span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">)</span> <span class="o">{</span>
       <span class="n">TrieNode</span> <span class="n">node</span> <span class="o">=</span> <span class="n">searchPrefix</span><span class="o">(</span><span class="n">word</span><span class="o">);</span>
       <span class="k">return</span> <span class="n">node</span> <span class="o">!=</span> <span class="kc">null</span> <span class="o">&amp;&amp;</span> <span class="n">node</span><span class="o">.</span><span class="na">isEnd</span><span class="o">();</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m)</script>
In each step of the algorithm we search for the next key character. In the worst case the algorithm performs <script type="math/tex; mode=display">m</script> operations.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>
</p>
</li>
</ul>
<h4 id="search-for-a-key-prefix-in-a-trie">Search for a key prefix in a trie</h4>
<p>The approach is very similar to the one we used for searching a key in a trie. We traverse the trie from the root, till there are no characters left in key prefix or it is impossible to continue the path in the trie with the current key character. The only difference with the mentioned above <code>search for a key</code> algorithm is that when we come to an end of the key prefix, we always return true. We don't need to consider the <code>isEnd</code> mark of the current trie node, because we are searching for a prefix of a key, not for a whole key.</p>
<p align="center"><img alt="Search of a key prefix in a trie" src="https://leetcode.com/media/original_images/208_TrieSearchPrefix.png" width="539px"></p>
<p align="center"><em>Figure 9. Search for a key prefix in a trie.</em></p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Trie</span> <span class="o">{</span>
    <span class="o">...</span>

    <span class="c1">// Returns if there is any word in the trie</span>
    <span class="c1">// that starts with the given prefix.</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">startsWith</span><span class="o">(</span><span class="n">String</span> <span class="n">prefix</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">TrieNode</span> <span class="n">node</span> <span class="o">=</span> <span class="n">searchPrefix</span><span class="o">(</span><span class="n">prefix</span><span class="o">);</span>
        <span class="k">return</span> <span class="n">node</span> <span class="o">!=</span> <span class="kc">null</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m)</script>
</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>
</p>
</li>
</ul>
<h2 id="practice-problems">Practice Problems</h2>
<p>Here are some wonderful problems for you to practice which uses the Trie data structure.</p>
<ol>
<li><a href="https://leetcode.com/problems/add-and-search-word-data-structure-design/">Add and Search Word - Data structure design</a> - Pretty much a direct application of Trie.</li>
<li><a href="https://leetcode.com/problems/word-search-ii/">Word Search II</a> - Similar to Boggle.</li>
</ol>
<p>Analysis written by: @elmirap.</p>
          </div>
        
      </div>