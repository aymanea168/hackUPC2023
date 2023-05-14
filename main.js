function loadProc() {
    urlparams = new URLSearchParams(window.location.search);
    query = urlparams.get('query');
    document.getElementById('inputSearch').value = query;

    sres = '[{"name": "1", "id": 32, "description": "DESC", "professors": "rew", "contents": "321", "objectives": "14"}, {"name": "2", "id": 32, "description": "DESC", "professors": "rew", "contents": "321", "objectives": "14"}]';
    dres = JSON.parse(sres)

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

}

function querySearch() {
    text = document.getElementById('inputSearch').value;
    console.log('Text: ' + text);
    window.location.href = "./items.html?query=" + text;
}