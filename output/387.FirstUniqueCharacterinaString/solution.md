<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-linear-time-solution">Approach 1: Linear time solution</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-linear-time-solution">Approach 1: Linear time solution</h4>
<p>The best possible solution here could be of a linear time 
because to ensure 
that the character is unique 
you have to check the whole string anyway. </p>
<p>The idea is to go through the string and 
save in a hash map the number of times 
each character appears in the string. 
That would take <script type="math/tex; mode=display">\mathcal{O}(N)</script> time, 
where <code>N</code> is a number of characters in the string.</p>
<p>And then we go through the string the second time, this time 
we use the hash map as a reference to check if a character 
is unique or not. <br>
If the character is unique, one could just return its index. 
The complexity of the second iteration is <script type="math/tex; mode=display">\mathcal{O}(N)</script> as well.</p>
<!--![LIS](../Figures/387/387_tr.gif)-->

<p>!?!../Documents/387_LIS.json:1000,621!?!</p>
<iframe src="https://leetcode.com/playground/Joed7Ar7/shared" frameborder="0" width="100%" height="361" name="Joed7Ar7"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> since we go 
through the string of length <code>N</code> two times. </li>
<li>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> since we have to keep a hash map 
with <code>N</code> elements.</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>