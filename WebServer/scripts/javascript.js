function clk()  {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/test?text=" + document.getElementById("searchbar").value, true);
    xhr.responseType = "text";
    xhr.onload = function(e) {
        document.getElementById("blurbtext").innerHTML = xhr.response
    }
    xhr.send();
}

document.getElementById("searchbar").addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        console.log("enter hit")
        clk();
    }
});

