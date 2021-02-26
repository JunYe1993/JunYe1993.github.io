import '../../node_modules/jquery/dist/jquery.js'

jQuery(document).ready(function($){
    $( "#root" ).load( "../../article/2021/01/6-express-2.html" , function () {
        $('pre > code').each(function() {
            hljs.highlightBlock(this);
        });
    });
});

