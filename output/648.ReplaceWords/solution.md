<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-prefix-hash-accepted">Approach #1: Prefix Hash [Accepted]</a></li>
<li><a href="#approach-2-trie-accepted">Approach #2: Trie [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-prefix-hash-accepted">Approach #1: Prefix Hash [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>For each word in the sentence, we'll look at successive prefixes and see if we saw them before.</p>
<p><strong>Algorithm</strong></p>
<p>Store all the <code>roots</code> in a <em>Set</em> structure.  Then for each word, look at successive prefixes of that word.  If you find a prefix that is a root, replace the word with that prefix.  Otherwise, the prefix will just be the word itself, and we should add that to the final sentence answer.</p>
<iframe src="https://leetcode.com/playground/tvjGGLzd/shared" frameborder="0" width="100%" height="361" name="tvjGGLzd"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(\sum w_i^2)</script> where <script type="math/tex; mode=display">w_i</script> is the length of the <script type="math/tex; mode=display">i</script>-th word.  We might check every prefix, the <script type="math/tex; mode=display">i</script>-th of which is <script type="math/tex; mode=display">O(w_i^2)</script> work.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the length of our sentence; the space used by <code>rootset</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-trie-accepted">Approach #2: Trie [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Put all the roots in a trie (prefix tree).  Then for any query word, we can find the smallest root that was a prefix in linear time.</p>
<iframe src="https://leetcode.com/playground/5Dt2dcFU/shared" frameborder="0" width="100%" height="500" name="5Dt2dcFU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the length of the <code>sentence</code>.  Every query of a word is in linear time.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of our trie.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>