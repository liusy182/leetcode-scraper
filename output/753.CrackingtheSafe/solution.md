<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-hierholzers-algorithm-accepted">Approach #1: Hierholzer's Algorithm [Accepted]</a></li>
<li><a href="#approach-2-inverse-burrows-wheeler-transform-accepted">Approach #2: Inverse Burrows-Wheeler Transform [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-hierholzers-algorithm-accepted">Approach #1: Hierholzer's Algorithm [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can think of this problem as the problem of finding an Euler path (a path visiting every edge exactly once) on the following graph: there are <script type="math/tex; mode=display">k^{n-1}</script> nodes with each node having <script type="math/tex; mode=display">k</script> edges.</p>
<p>For example, when <code>k = 4, n = 3</code>, the nodes are <code>'00', '01', '02', ..., '32', '33'</code> and each node has 4 edges <code>'0', '1', '2', '3'</code>.  A node plus edge represents a <em>complete edge</em> and viewing that substring in our answer.</p>
<p>Any connected directed graph where all nodes have equal in-degree and out-degree has an Euler circuit (an Euler path ending where it started.)  Because our graph is highly connected and symmetric, we should expect intuitively that taking any path greedily in some order will probably result in an Euler path.  </p>
<p>This intuition is called Hierholzer's algorithm: whenever there is an Euler cycle, we can construct it greedily.  The algorithm goes as follows:</p>
<ul>
<li>
<p>Starting from a vertex <code>u</code>, we walk through (unwalked) edges until we get stuck.  Because the in-degrees and out-degrees of each node are equal, we can only get stuck at <code>u</code>, which forms a cycle.</p>
</li>
<li>
<p>Now, for any node <code>v</code> we had visited that has unwalked edges, we start a new cycle from <code>v</code> with the same procedure as above, and then merge the cycles together to form a new cycle <script type="math/tex; mode=display">u \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow u</script>.</p>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>We will modify our standard depth-first search: instead of keeping track of nodes, we keep track of (complete) edges: <code>seen</code> records if an edge has been visited.</p>
<p>Also, we'll need to visit in a sort of "post-order", recording the answer after visiting the edge.  This is to prevent getting stuck.  For example, with <code>k = 2, n = 2</code>, we have the nodes <code>'0', '1'</code>.  If we greedily visit complete edges <code>'00', '01', '10'</code>, we will be stuck at the node <code>'0'</code> prematurely.  However, if we visit in post-order, we'll end up visiting <code>'00', '01', '11', '10'</code> correctly.</p>
<p>In general, during our Hierholzer walk, we will record the results of other subcycles first, before recording the main cycle we started from, just as in our first description of the algorithm.  Technically, we are recording backwards, as we exit the nodes.</p>
<p>For example, we will walk (in the "original cycle") until we get stuck, then record the node as we exit.  (Every edge walked is always marked immediately so that it can no longer be used.)  Then in the penultimate node of our original cycle, we will do a Hierholzer walk and then record this node; then in the third-last node of our original cycle we will do a Hierholzer walk and then record this node, and so on.</p>
<iframe src="https://leetcode.com/playground/6FQhQc9V/shared" frameborder="0" width="100%" height="500" name="6FQhQc9V"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(n * k^n)</script>.  We visit every edge once in our depth-first search, and nodes take <script type="math/tex; mode=display">O(n)</script> space.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(n * k^n)</script>, the size of <code>seen</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-inverse-burrows-wheeler-transform-accepted">Approach #2: Inverse Burrows-Wheeler Transform [Accepted]</h4>
<p><strong>Explanation</strong></p>
<p>If we are familiar with the theory of combinatorics on words, recall that a <em>Lyndon Word</em> <code>L</code> is a word that is the unique minimum of it's rotations.</p>
<p>One important mathematical result (due to <a href="http://www-igm.univ-mlv.fr/~perrin/Recherche/Publications/Articles/debruijnRevised3.pdf">Fredericksen and Maiorana</a>), is that the concatenation in lexicographic order of Lyndon words with length dividing <code>n</code>, forms a <em>de Bruijin</em> sequence: a sequence where every every word (from the <script type="math/tex; mode=display">k^n</script> available) appears as a substring of length <code>n</code> (where we are allowed to wrap around.)</p>
<p>For example, when <code>n = 6, k = 2</code>, all the Lyndon words with length dividing <code>n</code> in lexicographic order are (spaces for convenience):
<code>0 000001 000011 000101 000111 001 001011 001101 001111 01
010111 011 011111 1</code>.  It turns out this is the smallest de Bruijin sequence.</p>
<p>We can use the <em>Inverse Burrows-Wheeler Transform</em> (IBWT) to generate these Lyndon words.  Consider two sequences: <code>S</code> is the alphabet repeated <script type="math/tex; mode=display">k^{n-1}</script> times: <code>S = 0123...0123...0123....</code>, and <code>S'</code> is the alphabet repeated <script type="math/tex; mode=display">k^{n-1}</script> times for each letter: <code>S' = 00...0011...1122....</code>  We can think of <code>S'</code> and <code>S</code> as defining a permutation, where the <code>j</code>-th occurrence of each letter of the alphabet in <code>S'</code> maps to the corresponding <code>j</code>-th occurrence in <code>S</code>.  The cycles of this permutation turn out to be the corresponding smallest de Bruijin sequence (<a href="http://www.macs.hw.ac.uk/~markl/Higgins.pdf">link</a>).</p>
<p>Under this view, the permutation <script type="math/tex; mode=display">S' \rightarrow S</script> [mapping permutation indices <script type="math/tex; mode=display">(i * k^{n-1} + q) \rightarrow (q * k + i)</script>] form the desired Lyndon words.</p>
<iframe src="https://leetcode.com/playground/Xcx7eTBD/shared" frameborder="0" width="100%" height="463" name="Xcx7eTBD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(k^n)</script>.  We loop through every possible substring.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(k^n)</script>, the size of <code>P</code> and <code>ans</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>