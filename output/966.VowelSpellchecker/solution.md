<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-hashmap">Approach 1: HashMap</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-hashmap">Approach 1: HashMap</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We analyze the 3 cases that the algorithm needs to consider: when the query is an exact match, when the query is a match up to capitalization, and when the query is a match up to vowel errors.</p>
<p>In all 3 cases, we can use a hash table to query the answer.</p>
<ul>
<li>For the first case (exact match), we hold a set of words to efficiently test whether our query is in the set.</li>
<li>For the second case (capitalization), we hold a hash table that converts the word from its lowercase version to the original word (with correct capitalization).</li>
<li>For the third case (vowel replacement), we hold a hash table that converts the word from its lowercase version with the vowels masked out, to the original word.</li>
</ul>
<p>The rest of the algorithm is careful planning and reading the problem carefully.</p>
<iframe src="https://leetcode.com/playground/LKWt6sVP/shared" frameborder="0" width="100%" height="500" name="LKWt6sVP"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\mathcal{C})</script>, where <script type="math/tex; mode=display">\mathcal{C}</script> is the total <em>content</em> of <code>wordlist</code> and <code>queries</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\mathcal{C})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>