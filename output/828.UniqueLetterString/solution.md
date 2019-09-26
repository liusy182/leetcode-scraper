<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-maintain-answer-of-suffix-accepted">Approach #1: Maintain Answer of Suffix [Accepted]</a></li>
<li><a href="#approach-2-split-by-character-accepted">Approach #2: Split by Character [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-maintain-answer-of-suffix-accepted">Approach #1: Maintain Answer of Suffix [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can think of substrings as two for-loops, for the left and right boundary of the substring.  To get a handle on this problem, let's try to answer the question: what is the answer over all substrings that start at index <code>i</code>?  Let's call this <script type="math/tex; mode=display">F(i)</script>.  If we can compute this faster than linear (brute force), we have an approach.</p>
<p>Now let <script type="math/tex; mode=display">U</script> be the unique letters function, eg. <script type="math/tex; mode=display">U(\text{"LETTER"}) = 2</script>.</p>
<p>The key idea is we can write <script type="math/tex; mode=display">U</script> as a sum of disjoint functions over each character.  Let <script type="math/tex; mode=display">U_{\text{"A"}}(x)</script> be <script type="math/tex; mode=display">1</script> if <script type="math/tex; mode=display">\text{"A"}</script> occurs exactly once in <script type="math/tex; mode=display">x</script>, otherwise <script type="math/tex; mode=display">0</script>, and so on with every letter.  Then <script type="math/tex; mode=display">U(x) = \sum_{c \in \mathcal{A}} U_c(x)</script>, where <script type="math/tex; mode=display">\mathcal{A} = \{ \text{"A"}, \text{"B"}, \dots \}</script> is the alphabet.</p>
<p><strong>Algorithm</strong></p>
<p>This means we only need to answer the following question (26 times, one for each character): how many substrings have exactly one <script type="math/tex; mode=display">\text{"A"}</script>?  If we knew that <code>S[10] = S[14] = S[20] = "A"</code> (and only those indexes have an <code>"A"</code>), then when <code>i = 8</code>, the answer is <code>4</code> (<code>j = 10, 11, 12, 13</code>); when <code>i = 12</code> the answer is <code>6</code> (<code>j = 14, 15, 16, 17, 18, 19</code>), and so on.</p>
<p>In total, <script type="math/tex; mode=display">F(0) = \sum_{c \in \mathcal{A}} \text{index}[c][1] - \text{index}[c][0]</script>, where <code>index[c]</code> are the indices <code>i</code> (in order) where <code>S[i] == c</code> (and padded with <code>S.length</code> if out of bounds).  In the above example, <code>index["A"] = [10, 14, 20]</code>.</p>
<p>Now, we want the final answer of <script type="math/tex; mode=display">\sum_{i \geq 0} F(i)</script>.  There is a two pointer approach: how does <script type="math/tex; mode=display">F(1)</script> differ from <script type="math/tex; mode=display">F(0)</script>?  If for example <code>S[0] == "B"</code>, then most of the sum remains unchanged (specifically, <script type="math/tex; mode=display">\sum_{c \in \mathcal{A}, c \neq \text{"B"}} \text{index}[c][1] - \text{index}[c][0]</script>), and only the <script type="math/tex; mode=display">c = \text{"B"}</script> part changes, from <script type="math/tex; mode=display">\text{index}[\text{"B"}][1] - \text{index}[\text{"B"}][0]</script> to <script type="math/tex; mode=display">\text{index}[\text{"B"}][2] - \text{index}[\text{"B"}][1]</script>.</p>
<p>We can manage this in general by keeping track of <code>peek[c]</code>, which tells us the correct index <code>i = peek[c]</code> such that our current contribution by character <code>c</code> of <script type="math/tex; mode=display">F(i)</script> is <code>index[c][peek[c] + 1] - index[c][peek[c]]</code>.</p>
<iframe src="https://leetcode.com/playground/fkvb227q/shared" frameborder="0" width="100%" height="500" name="fkvb227q"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-split-by-character-accepted">Approach #2: Split by Character [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, we have <script type="math/tex; mode=display">U(x) = \sum_{c \in \mathcal{A}} U_c(x)</script>, where <script type="math/tex; mode=display">\mathcal{A} = \{ \text{"A"}, \text{"B"}, \dots \}</script> is the alphabet, and we only need to answer the following question (26 times, one for each character): how many substrings have exactly one <script type="math/tex; mode=display">\text{"A"}</script>?</p>
<p><strong>Algorithm</strong></p>
<p>Consider how many substrings have a specific <script type="math/tex; mode=display">\text{"A"}</script>.  For example, let's say <code>S</code> only has three <code>"A"</code>'s, at '<code>S[10] = S[14] = S[20] = "A"</code>; and we want to know the number of substrings that contain <code>S[14]</code>.  The answer is that there are 4 choices for the left boundary of the substring <code>(11, 12, 13, 14)</code>, and 6 choices for the right boundary <code>(14, 15, 16, 17, 18, 19)</code>.  So in total, there are 24 substrings that have <code>S[14]</code> as their unique <code>"A"</code>.</p>
<p>Continuing our example, if we wanted to count the number of substrings that have <code>S[10]</code>, this would be <code>10 * 4</code> - note that when there is no more <code>"A"</code> characters to the left of <code>S[10]</code>, we have to count up to the left edge of the string.</p>
<p>We can add up all these possibilities to get our final answer.</p>
<iframe src="https://leetcode.com/playground/qiRvovcd/shared" frameborder="0" width="100%" height="395" name="qiRvovcd"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.  We could reduce this to <script type="math/tex; mode=display">O(\mathcal{A})</script> if we do not store all the indices, but compute the answer on the fly.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approach #2 inspired by <a href="https://leetcode.com/lee215">@lee215</a>.</p>
          </div>
        
      </div>