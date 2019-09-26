<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-counting-accepted">Approach #1: Counting [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-counting-accepted">Approach #1: Counting [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>This problem is about the implementation, as the question tells us how to solve the problem. We'll count each word separately, ignoring punctuation and converting each word to lowercase. The word with the highest frequency that isn't in the banned list is the answer.</p>
<p><strong>Algorithm</strong></p>
<p>We'll need some <code>count</code> of words (converted to lowercase) that we have seen in the paragraph. As we iterate through the paragraph, we will collect these words (with punctuation removed and converted to lowercase).</p>
<p>There are two ways we could try to collect these words: we could try to split the paragraph (delimited by spaces) and then clean up the fragment like <code>"Bob!"</code> to be <code>"bob"</code>. Or, we could add characters one by one to build the next word, stopping when we reach a character that isn't a letter.</p>
<p>For each word (lowercase, and free of punctuation), we'll update our count and update the answer if the count of that word is highest (and the word is not banned.)</p>
<iframe src="https://leetcode.com/playground/vAHSEpAf/shared" frameborder="0" width="100%" height="500" name="vAHSEpAf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(P + B)</script>, where <script type="math/tex; mode=display">P</script> is the size of <code>paragraph</code> and <script type="math/tex; mode=display">B</script> is the size of <code>banned</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(P + B)</script>, to store the <code>count</code> and the banned set.</p>
</li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/awice">@awice</a> and editted by <a href="https://leetcode.com/khaled-ali">@Khaled</a>.</p>
          </div>
        
      </div>