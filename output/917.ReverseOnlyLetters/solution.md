<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-stack-of-letters">Approach 1: Stack of Letters</a></li>
<li><a href="#approach-2-reverse-pointer">Approach 2: Reverse Pointer</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-stack-of-letters">Approach 1: Stack of Letters</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Collect the letters of <code>S</code> separately into a stack, so that popping the stack reverses the letters.  (Alternatively, we could have collected the letters into an array and reversed the array.)</p>
<p>Then, when writing the characters of <code>S</code>, any time we need a letter, we use the one we have prepared instead.</p>
<iframe src="https://leetcode.com/playground/2S2yvnpZ/shared" frameborder="0" width="100%" height="361" name="2S2yvnpZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-reverse-pointer">Approach 2: Reverse Pointer</h4>
<p><strong>Intuition</strong></p>
<p>Write the characters of <code>S</code> one by one.  When we encounter a letter, we want to write the next letter that occurs if we iterated through the string backwards.</p>
<p>So we do just that: keep track of a pointer <code>j</code> that iterates through the string backwards.  When we need to write a letter, we use it.</p>
<iframe src="https://leetcode.com/playground/2RFgNCou/shared" frameborder="0" width="100%" height="344" name="2RFgNCou"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>