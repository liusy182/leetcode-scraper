<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-reduce-search-space-accepted">Approach #1: Reduce Search Space [Accepted]</a></li>
<li><a href="#approach-2-mathematical-accepted">Approach #2: Mathematical [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-reduce-search-space-accepted">Approach #1: Reduce Search Space [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As the search space is very large (<script type="math/tex; mode=display">2^N</script> states of lights, naively <script type="math/tex; mode=display">4^M</script> operation sequences), let us try to reduce it.</p>
<p>The first 6 lights uniquely determine the rest of the lights.  This is because every operation that modifies the <script type="math/tex; mode=display">x</script>-th light also modifies the <script type="math/tex; mode=display">(x+6)</script>-th light.</p>
<p>Also, operations commute: doing operation A followed by B is the same as doing operation B followed by A.  So we can assume we do all the operations in order.</p>
<p>Finally, doing the same operation twice in a row is the same as doing nothing.  So we only need to consider whether each operation was done 0 or 1 times.</p>
<p><strong>Algorithm</strong></p>
<p>Say we do the <script type="math/tex; mode=display">i</script>-th operation <script type="math/tex; mode=display">f_i</script> times.  Let's first figure out what sets of residues are possible: that is, what sets <script type="math/tex; mode=display">c_i = f_i</script> (<script type="math/tex; mode=display">\mod 2</script> ) are possible.</p>
<p>Because <script type="math/tex; mode=display">c_i \equiv f_i</script> and <script type="math/tex; mode=display">c_i \leq f_i</script>, if <script type="math/tex; mode=display">\sum f_i \not\equiv \sum c_i</script>, or if <script type="math/tex; mode=display">\sum f_i < \sum c_i</script>, it isn't possible.  Otherwise, it is possible by a simple construction: do the operations specified by <script type="math/tex; mode=display">c_i</script>, then do operation number 1 with the even number of operations you have left.</p>
<p>For each possible set of residues, let's simulate and remember what the first 6 lights will look like, storing it in a <em>Set</em> structure <code>seen</code>.  At the end, we'll return the size of this set.</p>
<p>In Java, we make use of bit manipulations to manage the state of lights, where in Python we simulate it directly.</p>
<iframe src="https://leetcode.com/playground/pHeNoQ3Q/shared" frameborder="0" width="100%" height="378" name="pHeNoQ3Q"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(1)</script>.  Our checks are bounded by a constant.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the size of the data structures used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-mathematical-accepted">Approach #2: Mathematical [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As before, the first 6 lights uniquely determine the rest of the lights.  This is because every operation that modifies the <script type="math/tex; mode=display">x</script>-th light also modifies the <script type="math/tex; mode=display">(x+6)</script>-th light, so the <script type="math/tex; mode=display">x</script>-th light is always equal to the <script type="math/tex; mode=display">(x+6)</script>-th light.</p>
<p>Actually, the first 3 lights uniquely determine the rest of the sequence, as shown by the table below for performing the operations a, b, c, d:</p>
<ul>
<li>Light 1 = 1 + a + c + d</li>
<li>Light 2 = 1 + a + b</li>
<li>Light 3 = 1 + a + c</li>
<li>Light 4 = 1 + a + b + d</li>
<li>Light 5 = 1 + a + c</li>
<li>Light 6 = 1 + a + b</li>
</ul>
<p>So that (modulo 2):</p>
<ul>
<li>Light 4 = (Light 1) + (Light 2) + (Light 3)</li>
<li>Light 5 = Light 3</li>
<li>Light 6 = Light 2</li>
</ul>
<p>The above justifies taking <script type="math/tex; mode=display">n = min(n, 3)</script> without loss of generality.  The rest is now casework.</p>
<p>Let's denote the state of lights by the tuple <script type="math/tex; mode=display">(a, b, c)</script>.  The transitions are to XOR by <script type="math/tex; mode=display">(1, 1, 1), (0, 1, 0), (1, 0, 1),</script> or <script type="math/tex; mode=display">(1, 0, 0)</script>.</p>
<p>When <script type="math/tex; mode=display">m = 0</script>, all the lights are on, and there is only one state <script type="math/tex; mode=display">(1, 1, 1)</script>.  The answer in this case is always 1.</p>
<p>When <script type="math/tex; mode=display">m = 1</script>, we could get states <script type="math/tex; mode=display">(0, 0, 0)</script>, <script type="math/tex; mode=display">(1, 0, 1)</script>, <script type="math/tex; mode=display">(0, 1, 0)</script>, or <script type="math/tex; mode=display">(0, 1, 1)</script>.  The answer in this case is either <script type="math/tex; mode=display">2, 3, 4</script> for <script type="math/tex; mode=display">n = 1, 2, 3</script> respectively.</p>
<p>When <script type="math/tex; mode=display">m = 2</script>, we can manually check that we can get 7 states: all of them except for <script type="math/tex; mode=display">(0, 1, 1)</script>.  The answer in this case is either <script type="math/tex; mode=display">2, 4, 7</script> for <script type="math/tex; mode=display">n = 1, 2, 3</script> respectively.</p>
<p>When <script type="math/tex; mode=display">m = 3</script>, we can get all 8 states.  The answer in this case is either <script type="math/tex; mode=display">2, 4, 8</script> for <script type="math/tex; mode=display">n = 1, 2, 3</script> respectively.</p>
<iframe src="https://leetcode.com/playground/yn2rvFzw/shared" frameborder="0" width="100%" height="208" name="yn2rvFzw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity: <script type="math/tex; mode=display">O(1)</script>.  The entire program uses constants.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>