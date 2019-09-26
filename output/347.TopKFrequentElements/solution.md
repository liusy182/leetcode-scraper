<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#intuition">Intuition</a></li>
<li><a href="#approach-1-heap">Approach 1: Heap</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="intuition">Intuition</h4>
<p>If <code>k = 1</code> the linear-time solution is quite simple. One could keep 
the frequency of elements appearance in a hash map and update the maximum
element at each step. </p>
<p>When <code>k &gt; 1</code> we need a data structure that 
has a fast access to the elements
ordered by their frequencies. 
The idea here is to use the heap which is also known as priority queue.
<br>
<br></p>
<hr>
<h4 id="approach-1-heap">Approach 1: Heap</h4>
<p>The first step is to build a hash map <code>element -&gt; its frequency</code>.
In Java we could use data structure <code>HashMap</code> but have to fill it manually.
Python provides us both a dictionary structure for the hash map and
a method <code>Counter</code> in the <code>collections</code> library 
to build the hash map we need. <br>
This step takes <script type="math/tex; mode=display">\mathcal{O}(N)</script> time where <code>N</code> is number of elements 
in the list.</p>
<p>The second step is to build a heap. 
The time complexity of adding an element in a heap
is <script type="math/tex; mode=display">\mathcal{O}(\log(k))</script> and we do it <code>N</code> times that means
<script type="math/tex; mode=display">\mathcal{O}(N \log(k))</script> time complexity for this step.</p>
<p>The last step to build an output list has<br>
<script type="math/tex; mode=display">\mathcal{O}(k \log(k))</script> time complexity.</p>
<p>In Python there is a method <code>nlargest</code> in <code>heapq</code> library 
(<a href="https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l203">check here the source code</a>)
which has the same <script type="math/tex; mode=display">\mathcal{O}(k \log(k))</script> time complexity
and combines two last steps in one line.</p>
<!--![LIS](../Figures/347/347_tr.gif)-->

<p>!?!../Documents/347_LIS.json:1000,498!?!</p>
<iframe src="https://leetcode.com/playground/nMWGBTcf/shared" frameborder="0" width="100%" height="500" name="nMWGBTcf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N \log(k))</script>. 
The complexity of <code>Counter</code> method is <script type="math/tex; mode=display">\mathcal{O}(N)</script>. 
To build a heap and output list takes <script type="math/tex; mode=display">\mathcal{O}(N \log(k))</script>.
Hence the overall complexity of the algorithm is 
<script type="math/tex; mode=display">\mathcal{O}(N + N \log(k)) = \mathcal{O}(N \log(k))</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> to store the hash map.</p>
</li>
</ul>
<p><strong>Side Notes</strong></p>
<p>Following the complexity analysis, the approach is
optimal for small <code>k</code>. In the case of large <code>k</code>, one could
revert the procedure by excluding the less frequent elements from
the output.</p>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>