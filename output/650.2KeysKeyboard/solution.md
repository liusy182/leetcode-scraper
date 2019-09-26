<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-prime-factorization-accepted">Approach #1: Prime Factorization [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-prime-factorization-accepted">Approach #1: Prime Factorization [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can break our moves into groups of <code>(copy, paste, ..., paste)</code>.  Let <code>C</code> denote copying and <code>P</code> denote pasting.  Then for example, in the sequence of moves <code>CPPCPPPPCP</code>, the groups would be <code>[CPP][CPPPP][CP]</code>.</p>
<p>Say these groups have lengths <code>g_1, g_2, ...</code>.  After parsing the first group, there are <code>g_1</code> <code>'A'</code>s.  After parsing the second group, there are <code>g_1 * g_2</code> <code>'A'</code>s, and so on.  At the end, there are <code>g_1 * g_2 * ... * g_n</code> <code>'A'</code>s.</p>
<p>We want exactly <code>N = g_1 * g_2 * ... * g_n</code>.  If any of the <code>g_i</code> are composite, say <code>g_i = p * q</code>, then we can split this group into two groups (the first of which has one copy followed by <code>p-1</code> pastes, while the second group having one copy and <code>q-1</code> pastes).</p>
<p>Such a split never uses more moves: we use <code>p+q</code> moves when splitting, and <code>pq</code> moves previously.  As <code>p+q &lt;= pq</code> is equivalent to <code>1 &lt;= (p-1)(q-1)</code>, which is true as long as <code>p &gt;= 2</code> and <code>q &gt;= 2</code>.</p>
<p><strong>Algorithm</strong>
By the above argument, we can suppose <code>g_1, g_2, ...</code> is the prime factorization of <code>N</code>, and the answer is therefore the sum of these prime factors.</p>
<iframe src="https://leetcode.com/playground/U88jzmPG/shared" frameborder="0" width="100%" height="276" name="U88jzmPG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(\sqrt{N})</script>.  When <code>N</code> is the square of a prime, our loop does <script type="math/tex; mode=display">O(\sqrt{N})</script> steps.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>ans</code> and <code>d</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>