<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-pointer-approach">Approach 1: Two Pointer Approach</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>The problem wants us to reform the linked list structure, such that the
elements lesser that a certain value <code>x</code>, come before the elements greater or
equal to <code>x</code>. This essentially means in this reformed list, there would be a
point in the linked list <code>before</code> which all the elements would be smaller than
<code>x</code> and <code>after</code> which all the elements would be greater or equal to <code>x</code>.
Let's call this point as the <code>JOINT</code>.</p>
<p></p><center>
<img src="../Figures/86/86_Partition_List_1.png" width="700">
</center>
<p>Reverse engineering the question tells us that if we break the reformed list
at the <code>JOINT</code>, we will get two smaller linked lists, one with lesser elements
and the other with elements greater or equal to <code>x</code>. In the solution, our main aim
is to create these two linked lists and join them.</p>
<h4 id="approach-1-two-pointer-approach">Approach 1: Two Pointer Approach</h4>
<p><strong>Intuition</strong></p>
<p>We can take two pointers <code>before</code> and <code>after</code> to keep track of the two linked
lists as described above. These two pointers could be
used two create two separate lists and then these lists could be combined to
form the desired reformed list.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>
<p>Initialize two pointers <code>before</code> and <code>after</code>. In the implementation we have
initialized these two with a dummy <code>ListNode</code>. This helps to reduce the number
of conditional checks we would need otherwise. You can try an implementation
where you don't initialize with a dummy node and see it yourself!</p>
<p></p><center>
<img src="../Figures/86/86_Partition_List_2.png" width="400">
</center>
<center>Dummy Node Initialization</center><br>
</li>
<li>
<p>Iterate the original linked list, using the <code>head</code> pointer.</p>
</li>
<li>
<p>If the node's value pointed by <code>head</code> is <em>lesser</em> than <code>x</code>, the node should
be part of the <code>before</code> list. So we move it to <code>before</code> list.</p>
<p></p><center>
<img src="../Figures/86/86_Partition_List_3.png" width="700">
</center>
</li>
<li>
<p>Else, the node should be part of <code>after</code> list. So we move it to <code>after</code> list.</p>
<p></p><center>
<img src="../Figures/86/86_Partition_List_4.png" width="700">
</center>
</li>
<li>
<p>Once we are done with all the nodes in the original linked list, we would
have two list <code>before</code> and <code>after</code>. The original list nodes are either part of
<code>before</code> list or <code>after</code> list, depending on its value.</p>
<p></p><center>
<img src="../Figures/86/86_Partition_List_5.png" width="700">
</center>
<p><em><code>Note:</code> Since we traverse the original linked list from left to right,
at no point would the order of nodes change relatively in the two lists. Another important thing to note here is that we show the original linked list intact in the above diagrams. However, in the implementation, we remove the nodes from the original linked list and attach them in the before or after list. We don't utilize any additional space. We simply move the nodes from the original list around.</em></p>
</li>
<li>
<p>Now, these two lists <code>before</code> and <code>after</code> can be combined to form the reformed list.</p>
<p></p><center>
<img src="../Figures/86/86_Partition_List_6.png" width="700">
</center>
</li>
</ol>
<p>We did a dummy node initialization at the start to make implementation
easier, you don't want that to be part of the returned list, hence just
move ahead one node in both the lists while combining the two list. Since both
before and after have an extra node at the front.</p>
<iframe src="https://leetcode.com/playground/EjKysw9Z/shared" frameborder="0" width="100%" height="500" name="EjKysw9Z"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the original
linked list and we iterate the original list.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, we have not utilized any extra space, the point to
note is that we are reforming the original list, by moving the original nodes, we
have not used any extra space as such.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>