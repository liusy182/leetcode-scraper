<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-stack">Approach 1: Stack</a></li>
<li><a href="#approach-2-regex">Approach 2: Regex</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-stack">Approach 1: Stack</h4>
<p>Summarizing the given problem, we can say that we need to determine whether a tag is valid or not, by checking the following properties.</p>
<ol>
<li>
<p>The code should be wrapped in valid closed tag.</p>
</li>
<li>
<p>The <code>TAG_NAME</code> should be valid.</p>
</li>
<li>
<p>The <code>TAG_CONTENT</code> should be valid.</p>
</li>
<li>
<p>The <strong>cdata</strong> should be valid.</p>
</li>
<li>
<p>All the tags should be closed. i.e. each start-tag should have a corresponding end-tag and vice-versa and the order of the tags should be correct as well.</p>
</li>
</ol>
<p>In order to check the validity of all these, firstly, we need to identify which parts of the given <script type="math/tex; mode=display">code</script> string act as which part from the above mentioned categories. To understand how it's done, we'll go through the implementation and the reasoning behind it step by step.</p>
<p>We iterate over the given <script type="math/tex; mode=display">code</script> string. Whenever a <code>&lt;</code> is encountered(unless we are currently inside <code>&lt;![CDATA[...]]&gt;</code>), it indicates the beginning of either a <code>TAG_NAME</code>(start tag or end tag) or the beginning of cdata as per the conditions given in the problem statement. </p>
<p>If the character immediately following this <code>&lt;</code> is an <code>!</code>, the characters following this <code>&lt;</code> can't be a part of a valid <code>TAG_NAME</code>, since only upper-case letters(in case of a start tag) or <code>/</code> followed by upper-case letters(in the case of an end tag). Thus, the choice now narrows down to only <strong>cdata</strong>. Thus, we need to check if the current bunch of characters following <code>&lt;!</code>(including it) constitute a valid <strong>cdata</strong>. For doing this, firstly we find out the first matching <code>]]&gt;</code> following the current <code>&lt;!</code> to mark the ending of <strong>cdata</strong>. If no such matching <code>]]&gt;</code> exists, the <script type="math/tex; mode=display">code</script> string is considered as invalid. Apart from this, the <code>&lt;!</code> should also be immediately followed by <code>CDATA[</code> for the <strong>cdata</strong> to be valid. The characters lying inside the  <code>&lt;![CDATA[</code> and <code>]]&gt;</code> do not have any constraints on them.</p>
<p>If the character immediately following the <code>&lt;</code> encountered isn't an <code>!</code>, this <code>&lt;</code> can only mark the beginnning of <code>TAG_NAME</code>. Now, since a valid start tag can't contain anything except upper-case letters, if a <code>/</code> is found after <code>&lt;</code>, the <code>&lt;/</code> pair indicates the beginning of an end tag. Now, when a <code>&lt;</code> refers to the beginning of a <code>TAG_NAME</code>(either start-tag or end-tag), we find out the first closing <code>&gt;</code> following the <code>&lt;</code> to find out the substring(say <script type="math/tex; mode=display">s</script>), that constitutes the <code>TAG_NAME</code>. This <script type="math/tex; mode=display">s</script> should satisfy all the criterion to constitute a valid <code>TAG_NAME</code>. Thus, for every such <script type="math/tex; mode=display">s</script>, we check if it contains all upper-case letters and also check its length(It should be between 1 to 9). If any of the criteria isn't fulfilled, <script type="math/tex; mode=display">s</script> doesn't constitue a valid <code>TAG_NAME</code>. Hence, the <script type="math/tex; mode=display">code</script> string turns out to be invalid as well.</p>
<p>Apart from checking the validity of the <code>TAG_NAME</code>, we also need to ensure that the tags always exist in pairs. i.e. for every start-tag, a corresponding end-tag should always exist. Further, we can note that in case of multiple <code>TAG_NAME</code>'s, the <code>TAG_NAME</code> whose start-tag comes later than the other ones, should have its end-tag appearing before the end-tags of those other <code>TAG_NAME</code>'s. i.e. the tag which starts later should end first. </p>
<p>From this, we get the intuition that we can make use of a <script type="math/tex; mode=display">stack</script> to check the existence of matching start and end-tags. Thus, whenever we find out a valid start-tag, as mentioned above, we push its <code>TAG_NAME</code> string onto a <script type="math/tex; mode=display">stack</script>. Now, whenever an end-tag is found, we compare its <code>TAG_NAME</code> with the <code>TAG_NAME</code> at the top the <script type="math/tex; mode=display">stack</script> and remove this element from the <script type="math/tex; mode=display">stack</script>. If the two don't match, this implies that either the current end-tag has no corresponding start-tag or there is a problem with the ordering of the tags. The two need to match for the tag-pair to be valid, since there can't exist an end-tag without a corresponding start-tag and vice-versa. Thus, if a match isn't found, we can conclude that the given <script type="math/tex; mode=display">code</script> string is invalid.</p>
<p>Now, after the complete <script type="math/tex; mode=display">code</script> string has been traversed, the <script type="math/tex; mode=display">stack</script> should be empty if all the start-tags have their corresponding end-tags as well. If the <script type="math/tex; mode=display">stack</script> isn't empty, this implies that some start-tag doesn't have the corresponding end-tag, violating the closed-tag's validity condition.</p>
<p>Further, we also need to ensure that the given <script type="math/tex; mode=display">code</script> is completely enclosed within closed tags. For this, we need to ensure that the first <strong>cdata</strong> found is also inside the closed tags. Thus, when we find a possibility of the presence of <strong>cdata</strong>, we proceed further only if we've already found a start tag, indicated by a non-empty stack. Further, to ensure that no data lies after the last end-tag, we need to ensure that the <script type="math/tex; mode=display">stack</script> doesn't become empty before we reach the end of the given <script type="math/tex; mode=display">code</script> string, since an empty <script type="math/tex; mode=display">stack</script> indicates that the last end-tag has been encountered.</p>
<p>The following animation depicts the process.</p>
<p>!?!../Documents/Tag_Validator_Stack.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/jBPTd4xA/shared" frameborder="0" width="100%" height="500" name="jBPTd4xA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We traverse over the given <script type="math/tex; mode=display">code</script> string of length <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The stack can grow upto a size of <script type="math/tex; mode=display">n/3</script> in the worst case. e.g. In case of <code>&lt;A&gt;&lt;B&gt;&lt;C&gt;&lt;D&gt;</code>, <script type="math/tex; mode=display">n</script>=12 and number of tags = 12/3 = 4.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-regex">Approach 2: Regex</h4>
<p>Instead of manually checking the given <script type="math/tex; mode=display">code</script> string for checking the validity of <code>TAG_NAME</code>, <code>TAG_CONTENT</code> and <strong>cdata</strong>, we can make use of an inbuilt java fuunctionality known as regular expressions.</p>
<p>A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. They can be used to search, edit, or manipulate text and data. The most common quantifiers used in regular expressions are listed below. A quantifier after a token (such as a character) or group specifies how often that preceding element is allowed to occur.</p>
<p><code>?</code> The question mark indicates zero or one occurrences of the preceding element. For example, colou?r matches both "color" and "colour".</p>
<p><code>*</code> The asterisk indicates zero or more occurrences of the preceding element. For example, ab*c matches "ac", "abc", "abbc", "abbbc", and so on.</p>
<p><code>+</code> The plus sign indicates one or more occurrences of the preceding element. For example, ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".</p>
<p><code>{n}</code> The preceding item is matched exactly <strong>n</strong> times.</p>
<p><code>{min,}</code> The preceding item is matched <strong>min</strong> or more times.</p>
<p><code>{min,max}</code> The preceding item is matched at least <strong>min</strong> times, but not more than <strong>max</strong> times.</p>
<p><code>|</code> A vertical bar separates alternatives. For example, gray|grey can match "gray" or "grey".</p>
<p><code>()</code> Parentheses are used to define the scope and precedence of the operators (among other uses). For example, gray|grey and gr(a|e)y are equivalent patterns which both describe the set of "gray" or "grey".</p>
<p><code>[...]</code> Matches any single character in brackets.</p>
<p><code>[^...]</code>    Matches any single character not in brackets.</p>
<p>Thus, by making use of regex, we can directly check the validity of the <script type="math/tex; mode=display">code</script> string directly(except the nesting of the inner tags) by using the regex expression below:</p>
<p><code>&lt;([A-Z]{1,9})&gt;([^&lt;]*((&lt;\/?[A-Z]{1,9}&gt;)|(&lt;!\[CDATA\[(.*?)]]&gt;))?[^&lt;]*)*&lt;\/\1&gt;</code></p>
<p>The image below shows the portion of the string that each part of the expression helps to match:</p>
<p align="center"><img alt="Regex" src="../Figures/591/591_Tag_Validator.PNG"></p>
<p>But, if we make use of back-referencing as mentioned above, the matching process takes a very large amount of CPU time. Thus, we use the regex only to check the validity of the <code>TAG_CONTENT</code>, <code>TAG_NAME</code> and the <strong>cdata</strong>. We check the presence of the outermost closed tags by making use of a <script type="math/tex; mode=display">stack</script> as done in the last approach.</p>
<p>The rest of the process remains the same as in the last approach, except that we need not manually check the validity of <code>TAG_CONTENT</code>, <code>TAG_NAME</code> and the <strong>cdata</strong>, since it is already done by the regex expression. We only need to check the presence of inner closed tags.</p>
<p>Check <a href="https://regexr.com/">this</a> link for testing any regular expression on a sample text.</p>
<iframe src="https://leetcode.com/playground/wacVss6K/shared" frameborder="0" width="100%" height="500" name="wacVss6K"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : Regular Expressions are/can be implemented in the form of Finite State Machines. Thus, the time complexity is dependent on the internal representation. In case of any suggestions, please comment below.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The stack can grow upto a size of <script type="math/tex; mode=display">n/3</script> in the worst case. e.g. In case of <code>&lt;A&gt;&lt;B&gt;&lt;C&gt;&lt;D&gt;</code>, <script type="math/tex; mode=display">n</script>=12 and number of tags = 12/3 = 4.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>