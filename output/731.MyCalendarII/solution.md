<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
<li><a href="#approach-2-boundary-count-accepted">Approach #2: Boundary Count [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Maintain a list of bookings and a list of double bookings.  When booking a new event <code>[start, end)</code>, if it conflicts with a double booking, it will have a triple booking and be invalid.  Otherwise, parts that overlap the calendar will be a double booking.</p>
<p><strong>Algorithm</strong></p>
<p>Evidently, two events <code>[s1, e1)</code> and <code>[s2, e2)</code> do <em>not</em> conflict if and only if one of them starts after the other one ends: either <code>e1 &lt;= s2</code> OR <code>e2 &lt;= s1</code>.  By De Morgan's laws, this means the events conflict when <code>s1 &lt; e2</code> AND <code>s2 &lt; e1</code>.</p>
<p>If our event conflicts with a double booking, it's invalid.  Otherwise, we add conflicts with the calendar to our double bookings, and add the event to our calendar.</p>
<iframe src="https://leetcode.com/playground/joRUVwzm/shared" frameborder="0" width="100%" height="395" name="joRUVwzm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of events booked.  For each new event, we process every previous event to decide whether the new event can be booked.  This leads to <script type="math/tex; mode=display">\sum_k^N O(k) = O(N^2)</script> complexity.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of the <code>calendar</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-boundary-count-accepted">Approach #2: Boundary Count [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>When booking a new event <code>[start, end)</code>, count <code>delta[start]++</code> and <code>delta[end]--</code>.  When processing the values of <code>delta</code> in sorted order of their keys, the running sum <code>active</code> is the number of events open at that time.  If the sum is 3 or more, that time is (at least) triple booked.</p>
<p>A Python implementation was not included for this approach because there is no analog to <em>TreeMap</em> available.</p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">MyCalendarTwo</span> <span class="o">{</span>
    <span class="n">TreeMap</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">delta</span><span class="o">;</span>

    <span class="kd">public</span> <span class="nf">MyCalendarTwo</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">delta</span> <span class="o">=</span> <span class="k">new</span> <span class="n">TreeMap</span><span class="o">();</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">book</span><span class="o">(</span><span class="kt">int</span> <span class="n">start</span><span class="o">,</span> <span class="kt">int</span> <span class="n">end</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">delta</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">start</span><span class="o">,</span> <span class="n">delta</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">start</span><span class="o">,</span> <span class="mi">0</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
        <span class="n">delta</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">end</span><span class="o">,</span> <span class="n">delta</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">end</span><span class="o">,</span> <span class="mi">0</span><span class="o">)</span> <span class="o">-</span> <span class="mi">1</span><span class="o">);</span>

        <span class="kt">int</span> <span class="n">active</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">d</span><span class="o">:</span> <span class="n">delta</span><span class="o">.</span><span class="na">values</span><span class="o">())</span> <span class="o">{</span>
            <span class="n">active</span> <span class="o">+=</span> <span class="n">d</span><span class="o">;</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">active</span> <span class="o">&gt;=</span> <span class="mi">3</span><span class="o">)</span> <span class="o">{</span>
                <span class="n">delta</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">start</span><span class="o">,</span> <span class="n">delta</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">start</span><span class="o">)</span> <span class="o">-</span> <span class="mi">1</span><span class="o">);</span>
                <span class="n">delta</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">end</span><span class="o">,</span> <span class="n">delta</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">end</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">delta</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">start</span><span class="o">)</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span>
                    <span class="n">delta</span><span class="o">.</span><span class="na">remove</span><span class="o">(</span><span class="n">start</span><span class="o">);</span>
                <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of events booked.  For each new event, we traverse <code>delta</code> in <script type="math/tex; mode=display">O(N)</script> time.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>delta</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Solution in Approach #2 inspired by <a href="https://discuss.leetcode.com/topic/111276/simplified-winner-s-solution">@cchao</a>.</p>
          </div>
        
      </div>