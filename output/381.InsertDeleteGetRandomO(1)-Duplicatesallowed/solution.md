<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#intuition">Intuition</a></li>
<li><a href="#approach-1-arraylist-hashmap">Approach 1: ArrayList + HashMap</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="intuition">Intuition</h4>
<p>We must support three operations with duplicates:</p>
<ol>
<li><code>insert</code></li>
<li><code>remove</code></li>
<li><code>getRandom</code></li>
</ol>
<p>To <code>getRandom</code> in <script type="math/tex; mode=display">O(1)</script> and have it scale linearly with the number of copies of a value. The simplest solution is to store all values in a list. Once all values are stored, all we have to do is pick a random index.</p>
<p>We don't care about the order of our elements, so <code>insert</code> can be done in <script type="math/tex; mode=display">O(1)</script> using a dynamic array (<code>ArrayList</code> in Java or <code>list</code> in Python).</p>
<p>The issue we run into is how to go about an <code>O(1)</code> remove. Generally we learn that removing an element from an array takes a place in <script type="math/tex; mode=display">O(N)</script>, unless it is the last element in which case it is <script type="math/tex; mode=display">O(1)</script>.</p>
<p>The key here is that <em>we don't care about order</em>. For the purposes of this problem, if we want to remove the element at the <code>i</code>th index, we can simply swap the <code>i</code>th element and the last element, and perform an <script type="math/tex; mode=display">O(1)</script> pop (<em>technically</em> we don't have to swap, we just have to copy the last element into index <code>i</code> because it's popped anyway).</p>
<p>With this in mind, the most difficult part of the problem becomes <em>finding</em> the index of the element we have to remove. All we have to do is have an accompanying data structure that maps the element values to their index.</p>
<hr>
<h4 id="approach-1-arraylist-hashmap">Approach 1: ArrayList + HashMap</h4>
<p><strong>Algorithm</strong></p>
<p>We will keep a <code>list</code> to store all our elements. In order to make finding the index of elements we want to remove <script type="math/tex; mode=display">O(1)</script>, we will use a <code>HashMap</code> or dictionary to map values to all indices that have those values. To make this work each value will be mapped to a set of indices. The tricky part is properly updating the <code>HashMap</code> as we modify the <code>list</code>.</p>
<ul>
<li><code>insert</code>: Append the element to the <code>list</code> and add the index to <code>HashMap[element]</code>.</li>
<li><code>remove</code>: This is the tricky part. We find the index of the element using the <code>HashMap</code>.  We use the trick discussed in the intuition to remove the element from the <code>list</code> in <script type="math/tex; mode=display">O(1)</script>. Since the last element in the list gets moved around, we have to update its value in the <code>HashMap</code>. We also have to get rid of the index of the element we removed from the <code>HashMap</code>.</li>
<li><code>getRandom</code>: Sample a random element from the list.</li>
</ul>
<p><strong>Implementation</strong>
<iframe src="https://leetcode.com/playground/meFMwZ4g/shared" frameborder="0" width="100%" height="500" name="meFMwZ4g"></iframe></p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(N)</script>, with <script type="math/tex; mode=display">N</script> being the number of operations. All of our operations are <script type="math/tex; mode=display">O(1)</script>, giving <script type="math/tex; mode=display">N * O(1) = O(N)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(N)</script>, with <script type="math/tex; mode=display">N</script> being the number of operations. The worst case scenario is if we get <script type="math/tex; mode=display">N</script>
<code>add</code> operations, in which case our <code>ArrayList</code> and our <code>HashMap</code> grow to size <script type="math/tex; mode=display">N</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by @<a href="https://leetcode.com/alwinpeng/">alwinpeng</a></p>
          </div>
        
      </div>