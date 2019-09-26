<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-two-pointer-approach">Approach 2: Two Pointer Approach</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>We have to maximize the Area that can be formed between the vertical lines using the shorter line as length and the distance between the lines as the width of the rectangle forming the area.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>In this case, we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.</p>
<iframe src="https://leetcode.com/playground/gL3JYnab/shared" frameborder="0" width="100%" height="208" name="gL3JYnab"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Calculating area for all <script type="math/tex; mode=display">\dfrac{n(n-1)}{2}</script> height pairs.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-two-pointer-approach">Approach 2: Two Pointer Approach</h4>
<p><strong>Algorithm</strong></p>
<p>The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.</p>
<p>We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a variable <script type="math/tex; mode=display">\text{maxarea}</script> to store the maximum area obtained till now. At every step, we find out the area formed between them, update <script type="math/tex; mode=display">\text{maxarea}</script> and move the pointer pointing to the shorter line towards the other end by one step.</p>
<p>The algorithm can be better understood by looking at the example below:</p>
<div class="codehilite"><pre><span></span>1 8 6 2 5 4 8 3 7
</pre></div>


<!--![Water_Continer](https://leetcode.com/media/original_images/11_Container_Water.gif)-->

<p>!?!../Documents/11_Container_Water.json:1000,563!?!</p>
<p>How this approach works?</p>
<p>Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.</p>
<p>For further clarification click <a href="https://leetcode.com/problems/container-with-most-water/discuss/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm">here</a> and for the proof click <a href="https://leetcode.com/problems/container-with-most-water/discuss/6089/Anyone-who-has-a-O(N)-algorithm/7268">here</a>.</p>
<iframe src="https://leetcode.com/playground/f9MCyxXg/shared" frameborder="0" width="100%" height="276" name="f9MCyxXg"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single pass.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
          </div>
        
      </div>