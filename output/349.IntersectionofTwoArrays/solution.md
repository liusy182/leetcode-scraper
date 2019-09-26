<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-sets">Approach 1: Two Sets</a></li>
<li><a href="#approach-2-built-in-set-intersection">Approach 2: Built-in Set Intersection</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-sets">Approach 1: Two Sets</h4>
<p><strong>Intuition</strong></p>
<p>The naive approach would be to iterate along the first array <code>nums1</code>
and to check for each value if this value in <code>nums2</code> or not. 
If yes - add the value to output. Such an approach would result 
in a pretty bad
<script type="math/tex; mode=display">\mathcal{O}(n \times m)</script> time complexity, where <code>n</code> and <code>m</code> are 
arrays' lengths.</p>
<blockquote>
<p>To solve the problem in linear time, let's use the structure <code>set</code>,
which provides <code>in/contains</code> operation in <script type="math/tex; mode=display">\mathcal{O}(1)</script> time in
average case.</p>
</blockquote>
<p>The idea is to convert both arrays into sets, and then iterate over 
the smallest set checking the presence of each element in the larger set.
Time complexity of this approach is <script type="math/tex; mode=display">\mathcal{O}(n + m)</script> in the average case.</p>
<p>!?!../Documents/349_LIS.json:1000,352!?!</p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/i5eLapjz/shared" frameborder="0" width="100%" height="395" name="i5eLapjz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(n + m)</script>, where <code>n</code> and <code>m</code> are 
arrays' lengths. <script type="math/tex; mode=display">\mathcal{O}(n)</script> time is used to convert <code>nums1</code>
into set, <script type="math/tex; mode=display">\mathcal{O}(m)</script> time is used to convert <code>nums2</code>, and
<code>contains/in</code> operations are <script type="math/tex; mode=display">\mathcal{O}(1)</script> in the average case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(m + n)</script> in the worst case when
all elements in the arrays are different.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-built-in-set-intersection">Approach 2: Built-in Set Intersection</h4>
<p><strong>Intuition</strong></p>
<p>There are built-in intersection facilities,
which provide <script type="math/tex; mode=display">\mathcal{O}(n + m)</script> time complexity in the 
average case and <script type="math/tex; mode=display">\mathcal{O}(n \times m)</script> time complexity in the 
worst case. </p>
<blockquote>
<p>In Python it's <a href="https://wiki.python.org/moin/TimeComplexity#set">intersection operator</a>, 
in Java - <a href="https://docs.oracle.com/javase/8/docs/api/java/util/AbstractCollection.html#retainAll-java.util.Collection-">retainAll() function</a>.</p>
</blockquote>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/fYrF2xVt/shared" frameborder="0" width="100%" height="310" name="fYrF2xVt"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(n + m)</script> in the average case 
 and <script type="math/tex; mode=display">\mathcal{O}(n \times m)</script>
<a href="https://wiki.python.org/moin/TimeComplexity#set">in the worst case
 when load factor is high enough</a>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(n + m)</script> in the worst case when
all elements in the arrays are different.</p>
</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>