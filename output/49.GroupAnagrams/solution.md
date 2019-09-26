<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-categorize-by-sorted-string">Approach 1: Categorize by Sorted String</a></li>
<li><a href="#approach-2-categorize-by-count">Approach 2: Categorize by Count</a></li>
</ul>
</div>
<h4 id="approach-1-categorize-by-sorted-string">Approach 1: Categorize by Sorted String</h4>
<p><strong>Intuition</strong></p>
<p>Two strings are anagrams if and only if their sorted strings are equal.</p>
<p><strong>Algorithm</strong></p>
<p>Maintain a map <code>ans : {String -&gt; List}</code> where each key <script type="math/tex; mode=display">\text{K}</script> is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to <script type="math/tex; mode=display">\text{K}</script>.</p>
<p>In Java, we will store the key as a string, eg. <code>code</code>.  In Python, we will store the key as a hashable tuple, eg. <code>('c', 'o', 'd', 'e')</code>.</p>
<p><img alt="Anagrams" src="../Figures/49_groupanagrams1.png"></p>
<iframe src="https://leetcode.com/playground/HwiBG7Pz/shared" frameborder="0" width="100%" height="293" name="HwiBG7Pz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NK \log K)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>strs</code>, and <script type="math/tex; mode=display">K</script> is the maximum length of a string in <code>strs</code>.  The outer loop has complexity <script type="math/tex; mode=display">O(N)</script> as we iterate through each string.  Then, we sort each string in <script type="math/tex; mode=display">O(K \log K)</script> time.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(NK)</script>, the total information content stored in <code>ans</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-categorize-by-count">Approach 2: Categorize by Count</h4>
<p><strong>Intuition</strong></p>
<p>Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.</p>
<p><strong>Algorithm</strong></p>
<p>We can transform each string <script type="math/tex; mode=display">\text{s}</script> into a character count, <script type="math/tex; mode=display">\text{count}</script>, consisting of 26 non-negative integers representing the number of <script type="math/tex; mode=display">\text{a}</script>'s, <script type="math/tex; mode=display">\text{b}</script>'s, <script type="math/tex; mode=display">\text{c}</script>'s, etc.  We use these counts as the basis for our hash map.</p>
<p>In Java, the hashable representation of our count will be a string delimited with '<strong>#</strong>' characters.  For example, <code>abbccc</code> will be <code>#1#2#3#0#0#0...#0</code> where there are 26 entries total.  In python, the representation will be a tuple of the counts.  For example, <code>abbccc</code> will be <code>(1, 2, 3, 0, 0, ..., 0)</code>, where again there are 26 entries total.</p>
<p><img alt="Anagrams" src="../Figures/49_groupanagrams2.png"></p>
<iframe src="https://leetcode.com/playground/DvDMzZTX/shared" frameborder="0" width="100%" height="412" name="DvDMzZTX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NK)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>strs</code>, and <script type="math/tex; mode=display">K</script> is the maximum length of a string in <code>strs</code>.  Counting each string is linear in the size of the string, and we count every string.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(NK)</script>, the total information content stored in <code>ans</code>.</p>
</li>
</ul>
          </div>
        
      </div>