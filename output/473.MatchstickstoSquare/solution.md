<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth First Search</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<p><br>
<strong>Intuition</strong></p>
<p>Suppose we have <code>1,1,1,1,2,2,2,2,3,3,3,3</code> as our set of matchsticks. In this case a square of side <script type="math/tex; mode=display">6</script> can be formed and we have 4 matchsticks each of 1, 2 and 3 and so we can have each square side formed by <code>3 + 2 + 1 = 6</code>.</p>
<p></p><center>
<img src="../Figures/473/473_Matchsticks-In-Square-Diag-1.png" height="400"></center>
<p>We can clearly see in the diagram above that the 3 matchsticks of sizes <code>1</code>, <code>2</code> and <code>3</code> combine to give one side of our resulting square.</p>
<p>This problem boils down to splitting an array of integers into <script type="math/tex; mode=display">4</script> subsets where all of these subsets are:
<em> mutually exclusive i.e. no specific element of the array is shared by any two of these subsets, and
</em> have the same sum which is equal to the side of our square.</p>
<p>We know that we will have <script type="math/tex; mode=display">4</script> different subsets. The sum of elements of these subsets would be <script type="math/tex; mode=display">\frac{1}{4}\sum_{}^{} arr</script>. If the sum if not divisible by <script type="math/tex; mode=display">4</script>, that implies that <script type="math/tex; mode=display">4</script> subsets of equal value are not possible and we don't need to do any further processing on this.</p>
<p>The only question that remains now for us to solve is:</p>
<blockquote>
<p>what subset a particular element belongs to?</p>
</blockquote>
<p>If we are able to figure that out, then there's nothing else left to do. But, since we can't say which of the <script type="math/tex; mode=display">4</script> subsets would contain a particular element, we try out all the options.
<br>
<br></p>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth First Search</h4>
<p>It is possible that a matchstick <strong><em>can</em></strong> be a part of any of the 4 sides of the resulting square, but which one of these choices leads to an actual square is something we don't know.</p>
<p>This means that for every matchstick in our given array, we have <script type="math/tex; mode=display">4</script> different options each representing the side of the square or subset that this matchstick can be a part of.</p>
<p>We try out all of them and keep on doing this recursively until we exhaust all of the possibilities or until we find an arrangement of our matchsticks such that they form the square.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>
<p>As discussed previously, we will follow a recursive, depth first approach to solve this problem. So, we have a function that takes the current matchstick index we are to process and also the number of sides of the square that are completely formed till now.</p>
</li>
<li>
<p>If all of the matchsticks have been used up and 4 sides have been completely formed, that implies our square is completely formed. This is the base case for the recursion.</p>
</li>
<li>
<p>For the current matchstick we have 4 different options. This matchstick at <script type="math/tex; mode=display">index</script> can be a part of any of the sides of the square. We try out the 4 options by recursing on them.</p>
<ul>
<li>If any of these recursive calls returns <script type="math/tex; mode=display">True</script>, then we return from there, else we return <script type="math/tex; mode=display">False</script>
</li>
</ul>
</li>
</ol>
<iframe src="https://leetcode.com/playground/PcFBb5tW/shared" frameborder="0" width="100%" height="500" name="PcFBb5tW"></iframe>

<p><strong>Implementation Details</strong></p>
<p>This solution is very slow as is. However, we can speed it up considerably by a small trick and that is to <code>sort our matchsticks sizes in reverse order before processing them recursively</code>.</p>
<p>The reason for this is that if there is no solution, trying a longer matchstick first will get to negative conclusion earlier.</p>
<p>e.g. <script type="math/tex; mode=display">[8,4,4,4]</script>. In this case we can have a square of size 5 but the largest side 8 doesn't fit in anywhere i.e. cannot be a part of any of the sides (because we can't break matchsticks according to the question) and hence we can simply return <script type="math/tex; mode=display">False</script> without even considering the remaining matchsticks.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity : <script type="math/tex; mode=display">O(4^N)</script> because we have a total of <script type="math/tex; mode=display">N</script> sticks and for each one of those matchsticks, we have <script type="math/tex; mode=display">4</script> different possibilities for the subsets they might belong to or the side of the square they might be a part of.</p>
</li>
<li>
<p>Space Complexity : <script type="math/tex; mode=display">O(N)</script>. For recursive solutions, the space complexity is the stack space occupied by all the recursive calls. The deepest recursive call here would be of size <script type="math/tex; mode=display">N</script> and hence the space complexity is <script type="math/tex; mode=display">O(N)</script>. There is no additional space other than the recursion stack in this solution.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p>In any dynamic programming problem, what's important is that our problem must be breakable into smaller subproblems and also, these subproblems show some sort of overlap which we can save upon by caching or memoization.</p>
<p>Suppose we have <code>3,3,4,4,5,5</code> as our matchsticks that have been used already to construct some of the sides of our square (<strong>Note:</strong> not all the sides may be completely constructed at all times.)</p>
<p>If the square side is <script type="math/tex; mode=display">8</script>, then there are many possibilities for how the sides can be constructed using the matchsticks above. We can have</p>
<pre>
  (4, 4), (3, 5), (3, 5) -----------&gt; 3 sides fully constructed.
  (3, 4), (3, 5), (4), (5) ---------&gt; 0 sides completely constructed.
  (3, 3), (4, 4), (5), (5) ---------&gt; 1 side completely constructed.
</pre>

<p>As we can see above, there are multiple ways to use the same set of matchsticks and land up in completely different recursion states.</p>
<p>This means that if we just keep track of what all matchsticks have been used and which all are remaining, it won't properly define the state of recursion we are in or what subproblem we are solving.</p>
<p>A single set of used matchsticks can represent multiple different unrelated subproblems and that is just not right.</p>
<p>We also need to keep track of number of sides of the square that have been <strong>completely</strong> formed till now.</p>
<p>Also, an important thing to note in the example we just considered was that if the matchsticks being used are <script type="math/tex; mode=display">[3,3,4,4,5,5]</script> and the side of the square is <code>8</code>, then we will always consider that arrangement that forms the most number of complete sides over that arrangement that leads to incomplete sides. Hence, the optimal arrangement here is <script type="math/tex; mode=display">(4, 4), (3, 5), (3, 5)</script> with 3 complete sides of the square.</p>
<p>Let us take a look at the following recursion tree to see if in-fact we can get overlapping subproblems.</p>
<p></p><center>
<img src="../Figures/473/473_Matchsticks-In-Square-Diag-2.png" width="500"></center>
<p><strong>Note:</strong> Not all subproblems have been shown in this figure. The thing we wanted to point out was overlapping subproblems.</p>
<p>We know that the overall sum of these matchsticks can be split equally into 4 halves. The only thing we don't know is if 4 <strong>equal</strong> halves can be carved out of the given set of matchsticks. For that also we need to keep track of the number of sides completely formed at any point in time. <strong><em>If we end up forming 4 equal sides successfully then naturally we would have used up all of the matchsticks each being used exactly once and we would have formed a square</em></strong>.</p>
<p>Let us first look at the pseudo-code for this problem before looking at the exact implementation details for the same.</p>
<pre>
let square_side = sum(matchsticks) / 4
func recurse(matchsticks_used, sides_formed) {
    if sides_formed == 4, then {
        Square Formed!!
    }
    for match in matchsticks available, do {
          add match to matchsticks_used
          let result = recurse(matchsticks_used, sides_formed)
          if result == True, then {
              return True
          }
          remove match from matchsticks_used
    }
    return False
}
</pre>

<p>This is the overall structure of our dynamic programming solution. Of-course, a lot of implementation details are missing here that we will address now.</p>
<p><br></p>
<p><strong>Implementation Details</strong></p>
<p>It is very clear from the pseudo-code above that the state of a recursion is defined by two variables <code>matchsticks_used</code> and <code>sides_formed</code>. Hence, these are the two variables that will be used to <strong>memoize</strong> or cache the results for that specific subproblem.</p>
<p>The question however is how do we actually store all the matchsticks that have been used? We want a memory efficient solution for this.</p>
<p>If we look at the question's constraints, we find that the max number of matchsticks we can have are <script type="math/tex; mode=display">15</script>. That's a pretty small number and we can make use of this constraint.</p>
<p>All we need to store is which of the matchsticks from the original list have been used. <code>We can use a Bit-Map for this</code></p>
<p>We will use <script type="math/tex; mode=display">N</script> number of bits, one for each of the matchsticks (<script type="math/tex; mode=display">N</script> is at max 15 according to the question's constraints). Initially we will start with a bit mask of <code>all 1s</code> and then as we keep on using the matchsticks, we will keep on setting their corresponding bits to <code>0</code>.</p>
<p>This way, we just have to hash an integer value which represents our bit-map and the max value for this mask would be <script type="math/tex; mode=display">2^{15}</script>.</p>
<p><br></p>
<p><strong>Do we really need to see if all 4 sides have been completely formed ?</strong></p>
<p>Another implementation trick that helps optimize this solution is that we don't really need to see if 4 sides have been completely formed.</p>
<p>This is because, we already know that the sum of all the matchsticks is divisible by 4. So, <em>if 3 equal sides have been formed by using some of the matchsticks, then the remaining matchsticks would definitely form the remaining side of our square.</em></p>
<p>Hence, we only need to check if 3 sides of our square can be formed or not.</p>
<iframe src="https://leetcode.com/playground/yNytHY5x/shared" frameborder="0" width="100%" height="500" name="yNytHY5x"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity : <script type="math/tex; mode=display">O(N \times 2^N)</script>. At max <script type="math/tex; mode=display">2^N</script> unique bit masks are possible and during every recursive call, we iterate our original matchsticks array to sum up the values of matchsticks used to update the <code>sides_formed</code> variable.</p>
</li>
<li>
<p>Space Complexity : <script type="math/tex; mode=display">O(N + 2^N)</script> because <script type="math/tex; mode=display">N</script> is the stack space taken up by recursion and <script type="math/tex; mode=display">4 \times 2^N</script> = <script type="math/tex; mode=display">O(2^N)</script> is the max possible size of our cache for memoization.</p>
<ul>
<li>The size of the cache is defined by the two variables <code>sides_formed</code> and <code>mask</code>. The number of different values that <code>sides_formed</code> can take = 4 and number of unique values of <code>mask</code> = <script type="math/tex; mode=display">2^N</script>.</li>
</ul>
</li>
</ul>
<p><br>
  <br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>