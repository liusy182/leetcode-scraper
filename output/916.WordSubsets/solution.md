<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-reduce-to-single-word-in-b">Approach 1: Reduce to Single Word in B</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-reduce-to-single-word-in-b">Approach 1: Reduce to Single Word in B</h4>
<p><strong>Intuition</strong></p>
<p>If <code>b</code> is a subset of <code>a</code>, then say <code>a</code> is a superset of <code>b</code>.  Also, say <script type="math/tex; mode=display">N_{\text{"a"}}(\text{word})</script> is the count of the number of <script type="math/tex; mode=display">\text{"a"}</script>'s in the word.</p>
<p>When we check whether a word <code>wordA</code> in <code>A</code> is a superset of <code>wordB</code>, we are individually checking the counts of letters: that for each <script type="math/tex; mode=display">\text{letter}</script>, we have <script type="math/tex; mode=display">N_{\text{letter}}(\text{wordA}) \geq N_{\text{letter}}(\text{wordB})</script>.</p>
<p>Now, if we check whether a word <code>wordA</code> is a superset of all words <script type="math/tex; mode=display">\text{wordB}_i</script>, we will check for each letter and each <script type="math/tex; mode=display">i</script>, that <script type="math/tex; mode=display">N_{\text{letter}}(\text{wordA}) \geq N_{\text{letter}}(\text{wordB}_i)</script>.  This is the same as checking <script type="math/tex; mode=display">N_{\text{letter}}(\text{wordA}) \geq \max\limits_i(N_{\text{letter}}(\text{wordB}_i))</script>.</p>
<p>For example, when checking whether <code>"warrior"</code> is a superset of words <code>B = ["wrr", "wa", "or"]</code>,  we can combine these words in <code>B</code> to form a "maximum" word <code>"arrow"</code>, that has the maximum count of every letter in each word in <code>B</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Reduce <code>B</code> to a single word <code>bmax</code> as described above, then compare the counts of letters between words <code>a</code> in <code>A</code>, and <code>bmax</code>.</p>
<iframe src="https://leetcode.com/playground/arU2pN5v/shared" frameborder="0" width="100%" height="500" name="arU2pN5v"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\mathcal{A} + \mathcal{B})</script>, where <script type="math/tex; mode=display">\mathcal{A}</script> and <script type="math/tex; mode=display">\mathcal{B}</script> is the total amount of information in <code>A</code> and <code>B</code> respectively.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(A\text{.length} + B\text{.length})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>