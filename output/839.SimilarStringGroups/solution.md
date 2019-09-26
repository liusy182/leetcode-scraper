<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-piecewise-accepted">Approach #1: Piecewise [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-piecewise-accepted">Approach #1: Piecewise [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let <code>W = A[0].length</code>.  It is clear that we can determine in <script type="math/tex; mode=display">O(W)</script> time, whether two words from <code>A</code> are similar.</p>
<p>One attempt is a standard kind of brute force: for each pair of words, let's draw an edge between these words if they are similar.  We can do this in <script type="math/tex; mode=display">O(N^2 W)</script> time.  After, finding the connected components can be done in <script type="math/tex; mode=display">O(N^2)</script> time naively (each node may have up to <script type="math/tex; mode=display">N-1</script> edges), (or <script type="math/tex; mode=display">O(N)</script> with a union-find structure.)  The total complexity is <script type="math/tex; mode=display">O(N^2 W)</script>.</p>
<p>Another attempt is to enumerate all neighbors of a word.  A <code>word</code> has up to <script type="math/tex; mode=display">\binom{W}{2}</script> neighbors, and if that <code>neighbor</code> is itself a given word, we know that <code>word</code> and <code>neighbor</code> are connected by an edge.  In this way, we can build the graph in <script type="math/tex; mode=display">O(N W^3)</script> time, and again take <script type="math/tex; mode=display">O(N^2)</script> or <script type="math/tex; mode=display">O(N)</script> time to analyze the number of connected components.</p>
<p>One insight is that between these two approaches, we can choose which approach works better.  If we have very few words, we want to use the first approach; if we have very short words, we want to use the second approach.  We'll piecewise add these two approaches (with complexity <script type="math/tex; mode=display">O(N^2 W)</script> and <script type="math/tex; mode=display">O(N W^3)</script>), to create an approach with <script type="math/tex; mode=display">O(NW\min(N, W^2))</script> complexity.</p>
<p><strong>Algorithm</strong></p>
<p>We will build some underlying graph with <code>N</code> nodes, where nodes <code>i</code> and <code>j</code> are connected if and only if <code>A[i]</code> is similar to <code>A[j]</code>, then look at the number of connected components.</p>
<p>There are a few challenges involved in this problem, but each challenge is relatively straightforward.  </p>
<ul>
<li>
<p>Use a helper function <code>similar(word1, word2)</code> that is <code>true</code> if and only if two given words are similar.</p>
</li>
<li>
<p>Enumerate all neighbors of a word, and discover when it is equal to a given word.</p>
</li>
<li>
<p>Use either a union-find structure or a depth-first search, to calculate the number of connected components of the underlying graph.  We've showcased a union-find structure in this solution, with notes of a depth-first search in the comments.</p>
</li>
</ul>
<p>For more details, see the implementations below.</p>
<iframe src="https://leetcode.com/playground/B2BjbwA7/shared" frameborder="0" width="100%" height="500" name="B2BjbwA7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NW \min(N, W^2))</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">W</script> is the length of each given word.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(NW^3)</script>.  If <script type="math/tex; mode=display">N < W^2</script>, the space complexity is <script type="math/tex; mode=display">O(N)</script>.  Otherwise, the space complexity is <script type="math/tex; mode=display">O(NW^3)</script>: for each of <script type="math/tex; mode=display">NW^2</script> neighbors we store a word of length <script type="math/tex; mode=display">W</script>.  (Plus, we store <script type="math/tex; mode=display">O(NW^2)</script> node indices ("buckets") which is dominated by the <script type="math/tex; mode=display">O(NW^3)</script> term.)  Because <script type="math/tex; mode=display">W^2 <= N</script> in this case, we could also write the space complexity as <script type="math/tex; mode=display">O(N^2 W)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>