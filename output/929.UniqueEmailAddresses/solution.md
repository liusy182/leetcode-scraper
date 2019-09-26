<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-canonical-form">Approach 1: Canonical Form</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-canonical-form">Approach 1: Canonical Form</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each email address, convert it to the <em>canonical</em> address that actually receives the mail.  This involves a few steps:</p>
<ul>
<li>
<p>Separate the email address into a <code>local</code> part and the <code>rest</code> of the address.</p>
</li>
<li>
<p>If the <code>local</code> part has a <code>'+'</code> character, remove it and everything beyond it from the <code>local</code> part.</p>
</li>
<li>
<p>Remove all the zeros from the <code>local</code> part.</p>
</li>
<li>
<p>The canonical address is <code>local + rest</code>.</p>
</li>
</ul>
<p>After, we can count the number of unique canonical addresses with a <code>Set</code> structure.</p>
<iframe src="https://leetcode.com/playground/z2pkvpLG/shared" frameborder="0" width="100%" height="344" name="z2pkvpLG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\mathcal{C})</script>, where <script type="math/tex; mode=display">\mathcal{C}</script> is the total content of <code>emails</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\mathcal{C})</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>