<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-insert-each-character-accepted">Approach #1: Insert Each Character [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-insert-each-character-accepted">Approach #1: Insert Each Character [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can write out each character in the string <code>S</code> one by one.</p>
<p>As we write characters, we can update <code>(lines, width)</code> that keeps track of how many lines we have used, and what is the length of the used space in the last line.</p>
<p><strong>Algorithm</strong></p>
<p>If the space <code>w</code> of the next character in <code>S</code> fits our current line, we will add it.  Otherwise, we will start a new line, and use <code>w</code> space to put that character on the next line.</p>
<iframe src="https://leetcode.com/playground/QNF9BsvY/shared" frameborder="0" width="100%" height="310" name="QNF9BsvY"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(S\text{.length})</script>, as we iterate through <code>S</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script> additional space, as we only use <code>lines</code> and <code>width</code>.  (In Java, our <code>toCharArray</code> method makes this <script type="math/tex; mode=display">O(S\text{.length})</script>, but we could use <code>.charAt</code> instead).</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>