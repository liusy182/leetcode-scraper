<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-linear-scan-time-limit-exceeded">Approach #1 (Linear Scan) [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-binary-search-accepted">Approach #2 (Binary Search) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This is a very simple problem. There is a subtle trap that you may fall into if you are not careful. Other than that, it is a direct application of a very famous algorithm.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-linear-scan-time-limit-exceeded">Approach #1 (Linear Scan) [Time Limit Exceeded]</h4>
<p>The straight forward way is to brute force it by doing a linear scan.</p>
<iframe src="https://leetcode.com/playground/Ezb8JYsL/shared" frameborder="0" name="Ezb8JYsL" width="100%" height="190"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
Assume that <script type="math/tex; mode=display">isBadVersion(version)</script> takes constant time to check if a <em>version</em> is bad. It takes at most <script type="math/tex; mode=display">n - 1</script> checks, therefore the overall time complexity is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-binary-search-accepted">Approach #2 (Binary Search) [Accepted]</h4>
<p>It is not difficult to see that this could be solved using a classic algorithm - Binary search. Let us see how the search space could be halved each time below.</p>
<div class="codehilite"><pre><span></span>Scenario #1: isBadVersion(mid) =&gt; false

 1 2 3 4 5 6 7 8 9
 G G G G G G B B B       G = Good, B = Bad
 |       |       |
left    mid    right
</pre></div>


<p>Let us look at the first scenario above where <script type="math/tex; mode=display">isBadVersion(mid) \Rightarrow  false</script>. We know that all versions preceding and including <script type="math/tex; mode=display">mid</script> are all good. So we set <script type="math/tex; mode=display">left = mid + 1</script> to indicate that the new search space is the interval <script type="math/tex; mode=display">[mid + 1, right]</script> (inclusive).</p>
<div class="codehilite"><pre><span></span>Scenario #2: isBadVersion(mid) =&gt; true

 1 2 3 4 5 6 7 8 9
 G G G B B B B B B       G = Good, B = Bad
 |       |       |
left    mid    right
</pre></div>


<p>The only scenario left is where <script type="math/tex; mode=display">isBadVersion(mid) \Rightarrow true</script>. This tells us that <script type="math/tex; mode=display">mid</script> may or may not be the first bad version, but we can tell for sure that all versions after <script type="math/tex; mode=display">mid</script> can be discarded. Therefore we set <script type="math/tex; mode=display">right = mid</script> as the new search space of interval <script type="math/tex; mode=display">[left,mid]</script> (inclusive).</p>
<p>In our case, we indicate <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> as the boundary of our search space (both inclusive). This is why we initialize <script type="math/tex; mode=display">left = 1</script> and <script type="math/tex; mode=display">right = n </script>. How about the terminating condition? We could guess that <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> eventually both meet and it must be the first bad version, but how could you tell for sure?</p>
<p>The formal way is to <a href="http://www.cs.cornell.edu/courses/cs211/2006sp/Lectures/L06-Induction/binary_search.html">prove by induction</a>, which you can read up yourself if you are interested. Here is a helpful tip to quickly prove the correctness of your binary search algorithm
during an interview. We just need to test an input of size 2. Check if it reduces the search space to a single element (which must be the answer) for both of the scenarios above. If not, your algorithm will never terminate.</p>
<p>If you are setting <script type="math/tex; mode=display">mid = \frac{left + right}{2}</script>, you have to be very careful. Unless you are using a language that does not overflow such as <a href="https://www.reddit.com/r/Python/comments/36xu5z/can_integer_operations_overflow_in_python/">Python</a>, <script type="math/tex; mode=display">left + right</script> could overflow. One way to fix this is to use <script type="math/tex; mode=display">left + \frac{right - left}{2}</script> instead.</p>
<p>If you fall into this subtle overflow bug, you are not alone. Even Jon Bentley's own implementation of binary search had this <a href="https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues">overflow bug</a> and remained undetected for over twenty years.</p>
<iframe src="https://leetcode.com/playground/VQBrosDg/shared" frameborder="0" name="VQBrosDg" width="100%" height="275"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log n)</script>.
The search space is halved each time, so the time complexity is <script type="math/tex; mode=display">O(\log n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>