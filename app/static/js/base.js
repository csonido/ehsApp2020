function ajax(opt){
    mode = opt['mode'] || null;
    url = opt['url'] || null;
    callback = opt['callback'] || null;
    data = opt['data'] || null;

    req = null;
    if (window.XMLHttpRequest) {
        // code for modern browsers
        req = new XMLHttpRequest();
    } else {
        // code for old IE browsers
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }

    req.onreadystatechange = function() {
      if (this.readyState == 4) {
        switch(this.status){
            case 200:
                callback(this);
                break;
            default:
                alert(this.responseText);
        }
      }
    };

    req.open('GET', url, true)
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send()
}