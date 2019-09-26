<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-stack-of-stacks">Approach 1: Stack of Stacks</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-stack-of-stacks">Approach 1: Stack of Stacks</h4>
<p><strong>Intuition</strong></p>
<p>Evidently, we care about the frequency of an element.  Let <code>freq</code> be a <code>Map</code> from <script type="math/tex; mode=display">x</script> to the number of occurrences of <script type="math/tex; mode=display">x</script>.</p>
<p>Also, we (probably) care about <code>maxfreq</code>, the current maximum frequency of any element in the stack.  This is clear because we must pop the element with the maximum frequency.</p>
<p>The main question then becomes: among elements with the same (maximum) frequency, how do we know which element is most recent?  We can use a stack to query this information: the top of the stack is the most recent.</p>
<p>To this end, let <code>group</code> be a map from frequency to a stack of elements with that frequency.  We now have all the required components to implement <code>FreqStack</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Actually, as an implementation level detail, if <code>x</code> has frequency <code>f</code>, then we'll have <code>x</code> in all <code>group[i] (i &lt;= f)</code>, not just the top.  This is because each <code>group[i]</code> will store information related to the <code>i</code>th copy of <code>x</code>.</p>
<p>Afterwards, our goal is just to maintain <code>freq</code>, <code>group</code>, and <code>maxfreq</code> as described above.</p>
<iframe src="https://leetcode.com/playground/jD2jBGjF/shared" frameborder="0" width="100%" height="500" name="jD2jBGjF"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(1)</script> for both <code>push</code> and <code>pop</code> operations.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <code>N</code> is the number of elements in the <code>FreqStack</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>