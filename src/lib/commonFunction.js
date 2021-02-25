export function injectCSS(href) {
    return new Promise((resolve, reject) => {
        const link = document.createElement('link')
        link.setAttribute("rel", "stylesheet")
        link.setAttribute("type", "text/css")
        link.onload = () => resolve()
        link.onerror = () => reject()
        link.setAttribute("href", href)
        document.head.appendChild(link)
    })
}

export function injectJS(href) {
    return new Promise((resolve, reject) => {
        const link = document.createElement('script')
        link.onload = () => resolve()
        link.onerror = () => reject()
        link.setAttribute("src", href)
        document.head.appendChild(link)
    })
}