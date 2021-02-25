// Include highlight CDN
var highlight = document.createElement('script');  
highlight.setAttribute('src','//cdn.jsdelivr.net/gh/highlightjs/cdn-release@10.1.2/build/highlight.min.js');
document.head.appendChild(highlight);

// Active highlight
hljs.initHighlightingOnLoad();