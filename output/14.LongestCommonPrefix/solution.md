<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-horizontal-scanning">Approach 1: Horizontal scanning</a></li>
<li><a href="#approach-2-vertical-scanning">Approach 2: Vertical scanning</a></li>
<li><a href="#approach-3-divide-and-conquer">Approach 3: Divide and conquer</a></li>
<li><a href="#approach-4-binary-search">Approach 4: Binary search</a></li>
<li><a href="#further-thoughts-follow-up">Further Thoughts / Follow up</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-horizontal-scanning">Approach 1: Horizontal scanning</h4>
<p><strong>Intuition</strong></p>
<p>For a start we will describe a simple way of finding the longest prefix shared by a set of strings <script type="math/tex; mode=display">LCP(S_1  \ldots  S_n)</script>.
We will use the observation that :</p>
<p>
<script type="math/tex; mode=display">LCP(S_1 \ldots S_n) = LCP(LCP(LCP(S_1, S_2),S_3),\ldots S_n)</script>
</p>
<p><strong>Algorithm</strong></p>
<p>To employ this idea, the algorithm iterates through the strings <script type="math/tex; mode=display">[S_1  \ldots  S_n]</script>, finding at each iteration <script type="math/tex; mode=display">i</script> the longest common prefix of strings <script type="math/tex; mode=display">LCP(S_1  \ldots  S_i)</script> When <script type="math/tex; mode=display">LCP(S_1  \ldots  S_i)</script> is an empty string, the algorithm ends. Otherwise after <script type="math/tex; mode=display">n</script> iterations, the algorithm returns <script type="math/tex; mode=display">LCP(S_1  \ldots  S_n)</script>.</p>
<p align="center"><img alt="Finding the longest common prefix" src="https://leetcode.com/media/original_images/14_basic.png" width="539px"></p>
<p align="center"><em>Figure 1. Finding the longest common prefix (Horizontal scanning)</em></p>
<p><iframe src="https://leetcode.com/playground/qSriZsc7/shared" frameborder="0" width="100%" height="225" name="qSriZsc7"></iframe></p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(S)</script> , where S is the sum of all characters in all strings.</p>
<p>In the worst case all <script type="math/tex; mode=display">n</script> strings are the same. The algorithm compares the string <script type="math/tex; mode=display">S1</script> with the other strings <script type="math/tex; mode=display">[S_2 \ldots S_n]</script> There are <script type="math/tex; mode=display">S</script> character comparisons, where <script type="math/tex; mode=display">S</script> is the sum of all characters in the input array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. We only used constant extra space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-vertical-scanning">Approach 2: Vertical scanning</h4>
<p><strong>Algorithm</strong></p>
<p>Imagine a very short string is at the end of the array. The above approach will still do <script type="math/tex; mode=display">S</script> comparisons. One way to optimize this case is to do vertical scanning. We compare characters from top to bottom on the same column (same character index of  the strings) before moving on to the next column.</p>
<iframe src="https://leetcode.com/playground/XBkP9paR/shared" frameborder="0" width="100%" height="242" name="XBkP9paR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(S)</script> , where S is the sum of all characters in all strings.
In the worst case there will be <script type="math/tex; mode=display">n</script> equal strings with length <script type="math/tex; mode=display">m</script> and the algorithm performs  <script type="math/tex; mode=display">S = m \cdot n</script> character comparisons.
Even though the worst case is still the same as <a href="#approach-1-horizontal-scanning">Approach 1</a>, in the best case there are at most <script type="math/tex; mode=display">n \cdot minLen</script> comparisons where <script type="math/tex; mode=display">minLen</script> is the length of the shortest string in the array.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. We only used constant extra space.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-3-divide-and-conquer">Approach 3: Divide and conquer</h4>
<p><strong>Intuition</strong></p>
<p>The idea of the algorithm comes from the associative property of LCP operation. We notice that :
<script type="math/tex; mode=display">LCP(S_1 \ldots S_n) = LCP(LCP(S_1 \ldots S_k), LCP (S_{k+1} \ldots S_n))</script>
, where <script type="math/tex; mode=display">LCP(S_1 \ldots S_n)</script> is the longest common prefix in set of strings <script type="math/tex; mode=display">[S_1 \ldots S_n]</script> , <script type="math/tex; mode=display">1 < k < n</script>
</p>
<p><strong>Algorithm</strong></p>
<p>To apply the observation above, we use divide and conquer technique, where we split the <script type="math/tex; mode=display">LCP(S_i \ldots S_j)</script> problem into two subproblems <script type="math/tex; mode=display">LCP(S_i \ldots S_{mid})</script>   and <script type="math/tex; mode=display">LCP(S_{mid+1} \ldots S_j)</script>, where <code>mid</code> is <script type="math/tex; mode=display">\frac{i + j}{2}</script>. We use their solutions <code>lcpLeft</code> and <code>lcpRight</code> to construct the solution of the main problem <script type="math/tex; mode=display">LCP(S_i \ldots S_j)</script>. To accomplish this we compare one by one the characters of <code>lcpLeft</code> and <code>lcpRight</code> till there is no character match. The found common prefix of <code>lcpLeft</code> and <code>lcpRight</code> is the solution of the  <script type="math/tex; mode=display">LCP(S_i \ldots S_j)</script>.</p>
<p align="center"><img alt="Finding the longest common prefix" src="https://leetcode.com/media/original_images/14_lcp_diviso_et_lmpera.png" width="539px"></p>
<p align="center"><em>Figure 2. Finding the longest common prefix of strings using divide and conquer technique</em></p>
<iframe src="https://leetcode.com/playground/z4RPaUv2/shared" frameborder="0" width="100%" height="480" name="z4RPaUv2"></iframe>

<p><strong>Complexity Analysis</strong></p>
<p>In the worst case we have <script type="math/tex; mode=display">n</script> equal strings with length <script type="math/tex; mode=display">m</script>
</p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(S)</script>, where <script type="math/tex; mode=display">S</script> is the number of all characters in the array, <script type="math/tex; mode=display">S = m \cdot n</script>
 Time complexity is <script type="math/tex; mode=display">2 \cdot T\left ( \frac{n}{2} \right ) + O(m)</script>. Therefore time complexity is <script type="math/tex; mode=display">O(S)</script>.
  In the best case this algorithm performs  <script type="math/tex; mode=display">O(minLen \cdot n)</script> comparisons, where  <script type="math/tex; mode=display">minLen</script> is the shortest string of the array</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m \cdot \log n)</script>
</p>
<p>There is a memory overhead since we store recursive calls in the execution stack. There are <script type="math/tex; mode=display">\log n</script> recursive calls, each store need <script type="math/tex; mode=display">m</script> space to store the result,  so space complexity is <script type="math/tex; mode=display">O(m \cdot \log n)</script>
</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-4-binary-search">Approach 4: Binary search</h4>
<p>The idea is to apply binary search method to find the string with maximum value <code>L</code>, which is common prefix of all of the strings. The algorithm searches space is the interval <script type="math/tex; mode=display">(0 \ldots minLen)</script>, where <code>minLen</code> is minimum string length and the maximum possible common prefix. Each time search space is divided in two equal parts, one of them is discarded, because it is sure that it doesn't contain the solution. There are two possible cases:
<em> <code>S[1...mid]</code> is not a common string. This means that for each <code>j &gt; i S[1..j]</code> is not a common string and we discard the second half of the  search space.
</em> <code>S[1...mid]</code> is common string. This means that for for each <code>i &lt; j S[1..i]</code> is a common string and we discard the first half of the search space, because we try to find longer common prefix.</p>
<p align="center"><img alt="Finding the longest common prefix" src="https://leetcode.com/media/original_images/14_lcp_binary_search.png" width="539px"></p>
<p align="center"><em>Figure 3. Finding the longest common prefix of strings using binary search technique</em></p>
<iframe src="https://leetcode.com/playground/CoEPcWJA/shared" frameborder="0" width="100%" height="480" name="CoEPcWJA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<p>In the worst case we have <script type="math/tex; mode=display">n</script> equal strings with length <script type="math/tex; mode=display">m</script>
</p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(S \cdot \log n)</script>, where <script type="math/tex; mode=display">S</script> is the sum of all characters in all strings.</p>
<p>The algorithm makes <script type="math/tex; mode=display">\log n</script> iterations, for each of them there are <script type="math/tex; mode=display">S = m \cdot n</script> comparisons, which gives in total <script type="math/tex; mode=display">O(S \cdot \log n)</script> time complexity.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. We only used constant extra space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="further-thoughts-follow-up">Further Thoughts / Follow up</h4>
<p>Let's take a look at a slightly different problem:</p>
<blockquote>
<p>Given a set of keys S = <script type="math/tex; mode=display">[S_1,S_2 \ldots S_n]</script>, find the longest common prefix among a string <code>q</code> and S. This LCP query will be called frequently.</p>
</blockquote>
<p>We could optimize LCP queries by storing the set of keys S in a Trie. For more information about Trie, please see this article <a href="https://leetcode.com/articles/implement-trie-prefix-tree/">Implement a trie (Prefix trie)</a>. In a Trie, each node descending from the root represents a common prefix of some keys. But we need to find the longest common prefix of a string <code>q</code> and all key strings. This means that we have to find the deepest path from the root, which satisfies the following conditions:
<em> it is prefix of query string <code>q</code>
</em> each node along the path must contain only one child element. Otherwise the found path will not be a common prefix among all strings.
* the path doesn't comprise of nodes which are marked as end of key. Otherwise the path couldn't be a prefix a of key which is shorter than itself.</p>
<p><strong>Algorithm</strong></p>
<p>The only question left, is how to find the deepest path in the Trie, that fulfills the requirements above. The most effective way is to build a trie from <script type="math/tex; mode=display">[S_1 \ldots   S_n]</script> strings. Then find the prefix of query string <code>q</code> in the Trie. We traverse the Trie from the root, till it is impossible to continue the path in the Trie because one of the conditions above is not satisfied.</p>
<p align="center"><img alt="Finding the longest common prefix using Trie" src="https://leetcode.com/media/original_images/14_lcp_trie.png" width="539px"></p>
<p align="center"><em>Figure 4. Finding the longest common prefix of strings using Trie</em></p>
<iframe src="https://leetcode.com/playground/MuyVN8wa/shared" frameborder="0" width="100%" height="500" name="MuyVN8wa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<p>In the worst case query <script type="math/tex; mode=display">q</script> has length <script type="math/tex; mode=display">m</script> and it is equal to all <script type="math/tex; mode=display">n</script> strings of the array.</p>
<ul>
<li>
<p>Time complexity : preprocessing <script type="math/tex; mode=display">O(S)</script>, where <script type="math/tex; mode=display">S</script> is the number of all characters in the array, LCP query <script type="math/tex; mode=display">O(m)</script>.</p>
<p>Trie build has <script type="math/tex; mode=display">O(S)</script> time complexity. To find the common prefix of <script type="math/tex; mode=display">q</script> in the Trie takes in the worst case <script type="math/tex; mode=display">O(m)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(S)</script>. We only used additional  <script type="math/tex; mode=display">S</script> extra space for the Trie.</p>
</li>
</ul>
          </div>
        
      </div>