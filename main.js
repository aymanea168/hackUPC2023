function loadProc() {
    urlparams = new URLSearchParams(window.location.search);
    query = urlparams.get('query');
    document.getElementById('inputSearch').value = query;

    $.getJSON('http://localhost:5000/query/' + query, function(data) {
        console.log(data);
        dres = data;
        for (var i = 0; i < dres.length; i++) {
            val = dres[i];
            document.getElementById('results').innerHTML +=
            `<tr>
                <td>${val["id"]}</td>
                <td>${val["name"]}</td>
                <td>${val["description"]}</td>
                <td>${val["professors"]}</td>
                <td>${val["contents"]}</td>
                <td>${val["objectives"]}</td>
            </tr>`;
        }
    });
}

function querySearch() {
    text = document.getElementById('inputSearch').value;
    console.log('Text: ' + text);
    window.location.href = "./items.html?query=" + text;
}