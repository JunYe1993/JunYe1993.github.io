// import {injectCSS, injectJS} from '../src/lib/commonFunction.js'

var css = '../../article/header/blogger.css'
var highlight = '//cdn.jsdelivr.net/gh/highlightjs/cdn-release@10.1.2/build/highlight.min.js'
var file = '../../article/2021/01/6-express-2.html'
var htmlContent = require('../../article/2021/01/6-express-2.html');
var commonFunc = require('../lib/commonFunction.js');
// var article = { htmlContent: htmlContent };

commonFunc.injectCSS(css)
commonFunc.injectJS(highlight)

// class Article extends React.Component {
//     render() {
//         return <div id="articleContainer">123</div>
//     }
// }
// 
// ReactDOM.render(<Article />, document.querySelector('#root'))
// includeHTML('root2', file)

