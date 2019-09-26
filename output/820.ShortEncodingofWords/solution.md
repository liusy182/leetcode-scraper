<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-store-prefixes-accepted">Approach #1: Store Prefixes [Accepted]</a></li>
<li><a href="#approach-2-trie-accepted">Approach #2: Trie [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-store-prefixes-accepted">Approach #1: Store Prefixes [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If a word <code>X</code> is a suffix of <code>Y</code>, then it does not need to be considered, as the encoding of <code>Y</code> in the reference string will also encode <code>X</code>.  For example, if <code>"me"</code> and <code>"time"</code> is in <code>words</code>, we can throw out <code>"me"</code> without changing the answer.</p>
<p>If a word <code>Y</code> does not have any other word <code>X</code> (in the list of <code>words</code>) that is a suffix of <code>Y</code>, then <code>Y</code> must be part of the reference string.</p>
<p>Thus, the goal is to remove words from the list such that no word is a suffix of another.  The final answer would be <code>sum(word.length + 1 for word in words)</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Since a word only has up to 7 suffixes (as <code>words[i].length &lt;= 7</code>), let's iterate over all of them.  For each suffix, we'll try to remove it from our <code>words</code> list.  For efficiency, we'll make <code>words</code> a set.</p>
<iframe src="https://leetcode.com/playground/gV8UXxb3/shared" frameborder="0" width="100%" height="293" name="gV8UXxb3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\sum w_i^2)</script>, where <script type="math/tex; mode=display">w_i</script> is the length of <code>words[i]</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(\sum w_i)</script>, the space used in storing suffixes.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-trie-accepted">Approach #2: Trie [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, the goal is to remove words that are suffixes of another word in the list.</p>
<p><strong>Algorithm</strong></p>
<p>To find whether different words have the same suffix, let's put them backwards into a trie (prefix tree).  For example, if we have <code>"time"</code> and <code>"me"</code>, we will put <code>"emit"</code> and <code>"em"</code> into our trie.</p>
<p>After, the leaves of this trie (nodes with no children) represent words that have no suffix, and we will count <code>sum(word.length + 1 for word in words)</code>.</p>
<iframe src="https://leetcode.com/playground/whsBS94T/shared" frameborder="0" width="100%" height="500" name="whsBS94T"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\sum w_i)</script>, where <script type="math/tex; mode=display">w_i</script> is the length of <code>words[i]</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(\sum w_i)</script>, the space used by the trie.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>