<div class="separator" style="clear: both;text-align: center;">
 <div class="separator" style="clear: both;text-align: center;">
  <div class="separator" style="clear: both;text-align: center;">
   <div class="separator" style="clear: both;text-align: center;">
    <div class="separator" style="clear: both;text-align: center;">
     <a style="margin-left: 1em;margin-right: 1em;">
      <img alt="'Tree.jpg'" border="0" data-original-height="1365" data-original-width="2048" height="424" src="https://junye1993.github.io/image/Development.jpg" width="640"/>
     </a>
    </div>
   </div>
  </div>
 </div>
</div>
<h2 style="background-color: #e6edeb;border-left: 5px solid rgb(2, 180, 206);box-sizing: border-box;font-size: large;letter-spacing: 1.44px;line-height: 1.6em;margin: 16px 0px 24px;padding: 10px 10px 10px 18px;text-align: justify;">
 使用 vscode 自動刪除空格的原因
</h2>
<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;"><font face="helvetica" size="4">當你上 code 時，有 reviewer 看你的程式碼時，通常會用 meld 等軟體 review。當你的程式碼加了多餘的空格時，都會被這些程式碼 highlight，使得 reviewer 在查看你的程式碼時有一定的不便。</font></pre>
<h2 style="background-color: #e6edeb;border-left: 5px solid rgb(2, 180, 206);box-sizing: border-box;font-size: large;letter-spacing: 1.44px;line-height: 1.6em;margin: 36px 0px 24px;padding: 10px 10px 10px 18px;text-align: justify;">
 vscode 刪除空格
</h2>
<ul>
 <li>
  <pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;"><font face="helvetica" size="4" style="background-color: #fff7e9;"><b><u>手動刪除空格 (Remove trailing spaces manually)</u></b></font></pre>
  <pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;"><font face="helvetica" size="4"><kbd>ctrl + alt + p</kbd>，輸入 trail 你應該就可以看到相關快捷鍵。</font></pre>
 </li>
 <li>
  <pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;"><font face="helvetica" size="4" style="background-color: #fff7e9;"><b><u>自動刪除空格 (Remove trailing spaces automatically)</u></b></font></pre>
  <pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;"><font face="helvetica" size="4"><kbd>setting</kbd> &gt; <kbd>右上角的 open setting (JSON)</kbd> &gt; 加入以下這行。</font></pre>
  <pre><code class="language-JSON" style="width: 95%;">    "files.trimTrailingWhitespace": true
</code></pre>
 </li>
</ul>