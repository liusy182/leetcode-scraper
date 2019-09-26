<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-simple-solutionaccepted">Approach #2 Simple Solution[Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p>In the brute force approach we will generate all the possible <script type="math/tex; mode=display">2^n</script> subsequences of both the strings and store their number of occurences in a hashmap.
Longest subsequence whose frequency is equal to <script type="math/tex; mode=display">1</script> will be the required subsequence.
And, if it is not found we will return <script type="math/tex; mode=display">-1</script>.</p>
<iframe src="https://leetcode.com/playground/tSXGPoqU/shared" frameborder="0" name="tSXGPoqU" width="100%" height="479"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(2^x+2^y)</script>. where <script type="math/tex; mode=display">x</script> and <script type="math/tex; mode=display">y</script> are the lengths of strings <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> respectively . Number of subsequences will be <script type="math/tex; mode=display">2^x+2^y</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(2^x+2^y)</script>. <script type="math/tex; mode=display">2^x+2^y</script> subsequences will be generated.</li>
</ul>
<hr>
<h4 id="approach-2-simple-solutionaccepted">Approach #2 Simple Solution[Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Simple analysis of this problem can lead to an easy solution.</p>
<p>These three cases are possible with string <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script>:-</p>
<ul>
<li>
<p>
<script type="math/tex; mode=display">a=b</script>. If both the strings are identical, it is obvious that no subsequence will be uncommon. Hence, return -1.</p>
</li>
<li>
<p>
<script type="math/tex; mode=display">length(a)=length(b)</script> and <script type="math/tex; mode=display">a \ne b</script>. Example: <script type="math/tex; mode=display">abc</script> and <script type="math/tex; mode=display">abd</script>. In this case we can consider any string i.e. <script type="math/tex; mode=display">abc</script> or <script type="math/tex; mode=display">abd</script> as a required subsequence, as out of these two strings one string will never be a subsequence of other string. Hence, return <script type="math/tex; mode=display">length(a)</script> or <script type="math/tex; mode=display">length(b)</script>.</p>
</li>
<li>
<p>
<script type="math/tex; mode=display">length(a) \ne length(b)</script>. Example <script type="math/tex; mode=display">abcd</script> and <script type="math/tex; mode=display">abc</script>. In this case we can consider bigger string as a required subsequence because bigger string can't be a subsequence of smaller string. Hence, return <script type="math/tex; mode=display">max(length(a),length(b))</script>.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/YdNcPgTE/shared" frameborder="0" name="YdNcPgTE" width="100%" height="173"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(min(x,y))</script>. where <script type="math/tex; mode=display">x</script> and <script type="math/tex; mode=display">y</script> are the lengths of strings <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> respectively. Here equals method will take <script type="math/tex; mode=display">min(x,y)</script> time .</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space required.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>