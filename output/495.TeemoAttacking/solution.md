<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-one-pass">Approach 1: One pass</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-one-pass">Approach 1: One pass</h4>
<p><strong>Intuition</strong></p>
<p>The problem is an example of merge interval questions which are now <a href="https://leetcode.com/discuss/interview-question/280433/Google-or-Phone-screen-or-Program-scheduling">quite popular
in Google</a>.</p>
<p>Typically such problems could be solved in a linear time in the case
of sorted input, like <a href="https://leetcode.com/articles/insert-interval/">here</a>, 
and in <script type="math/tex; mode=display">\mathcal{O}(N \log N)</script> time otherwise,
<a href="https://leetcode.com/articles/merge-intervals/">here is an example</a>.</p>
<p>Here one deals with a sorted input, and the problem could be solved in one pass
with a constant space. 
The idea is straightforward: consider only the interval between two attacks. 
Ashe spends in a poisoned condition the whole time interval
if this interval is shorter than the poisoning time duration <code>duration</code>, 
and <code>duration</code> otherwise. </p>
<p><strong>Algorithm</strong></p>
<ul>
<li>
<p>Initiate total time in poisoned condition <code>total = 0</code>.</p>
</li>
<li>
<p>Iterate over <code>timeSeries</code> list. At each step add to the total time
the minimum between interval length and the poisoning time duration <code>duration</code>. </p>
</li>
<li>
<p>Return <code>total + duration</code> to take the last attack into account.  </p>
</li>
</ul>
<p><strong>Implementation</strong></p>
<p><img alt="pic" src="../Figures/495/ashe.png"></p>
<iframe src="https://leetcode.com/playground/gz6gYdPv/shared" frameborder="0" width="100%" height="242" name="gz6gYdPv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script>, where N is the length of the input list,
since we iterate the entire list.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(1)</script>, it's a constant space solution.</p>
</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>