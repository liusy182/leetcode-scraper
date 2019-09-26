<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-trie-set-intersection-time-limit-exceeded">Approach #1: Trie + Set Intersection [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-paired-trie-accepted">Approach #2: Paired Trie [Accepted]</a></li>
<li><a href="#approach-3-trie-of-suffix-wrapped-words-accepted">Approach #3: Trie of Suffix Wrapped Words [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-trie-set-intersection-time-limit-exceeded">Approach #1: Trie + Set Intersection [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We use two tries to separately find all words that match the prefix, plus all words that match the suffix.  Then, we try to find the highest weight element in the intersection of these sets.</p>
<p>Of course, these sets could still be large, so we might TLE if we aren't careful.</p>
<iframe src="https://leetcode.com/playground/ihA9cm57/shared" frameborder="0" width="100%" height="500" name="ihA9cm57"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(NK + Q(N+K))</script> where <script type="math/tex; mode=display">N</script> is the number of words, <script type="math/tex; mode=display">K</script> is the maximum length of a word, and <script type="math/tex; mode=display">Q</script> is the number of queries.  If we use memoization in our solution, we could produce tighter bounds for this complexity, as the complex queries are somewhat disjoint.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(NK)</script>, the size of the tries.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-paired-trie-accepted">Approach #2: Paired Trie [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Say we are inserting the word <code>apple</code>.  We could insert <code>('a', 'e'), ('p', 'l'), ('p', 'p'), ('l', 'p'), ('e', 'a')</code> into our trie.  Then, if we had equal length queries like <code>prefix = "ap", suffix = "le"</code>, we could find the node <code>trie['a', 'e']['p', 'l']</code> in our trie.  This seems promising.</p>
<p>What about queries that aren't equal?  We should just insert them like normal.  For example, to capture a case like <code>prefix = "app", suffix = "e"</code>, we could create nodes <code>trie['a', 'e']['p', None]['p', None]</code>.</p>
<p>After inserting these pairs into our trie, our searches are straightforward.</p>
<iframe src="https://leetcode.com/playground/rphE5ncp/shared" frameborder="0" width="100%" height="500" name="rphE5ncp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(NK^2 + QK)</script> where <script type="math/tex; mode=display">N</script> is the number of words, <script type="math/tex; mode=display">K</script> is the maximum length of a word, and <script type="math/tex; mode=display">Q</script> is the number of queries.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(NK^2)</script>, the size of the trie.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-trie-of-suffix-wrapped-words-accepted">Approach #3: Trie of Suffix Wrapped Words [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Consider the word <code>'apple'</code>.  For each suffix of the word, we could insert that suffix, followed by <code>'#'</code>, followed by the word, all into the trie.</p>
<p>For example, we will insert <code>'#apple', 'e#apple', 'le#apple', 'ple#apple', 'pple#apple', 'apple#apple'</code> into the trie.  Then for a query like <code>prefix = "ap", suffix = "le"</code>, we can find it by querying our trie for <code>le#ap</code>.</p>
<iframe src="https://leetcode.com/playground/hSdRfBf4/shared" frameborder="0" width="100%" height="500" name="hSdRfBf4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(NK^2 + QK)</script> where <script type="math/tex; mode=display">N</script> is the number of words, <script type="math/tex; mode=display">K</script> is the maximum length of a word, and <script type="math/tex; mode=display">Q</script> is the number of queries.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(NK^2)</script>, the size of the trie.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>