import { injectCSS } from '../src/lib/commonFunction.js'
import { hljs } from './js/hightlight.js'
import '../src/lib/jquery.js'
injectCSS('./css/highlight.css')

// jQuery(function ($){}) == jQuery(document).ready(function($){});
// Only run once the page Document Object Model (DOM) is ready for JavaScript code to execute.
jQuery (function ($) {
    $( "#article_container" ).load( "../../article/2021/01/6-express-2.html" , function () {
        $('pre > code').each(function() {
            hljs.highlightBlock(this);
        });
    });
})

class Test extends React.Component {
    render() {
        return (
            <div>
                <h1>Hello World!</h1>
                <div id="article_container"></div>
            </div>
        );
    }
}

ReactDOM.render(<Test />, document.getElementById('root'));