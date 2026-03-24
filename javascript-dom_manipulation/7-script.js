const list = document.querySelector("ul#list_movies");
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {

        const items = data.results;

        list.innerHTML = "";
        items.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item.title;
            list.append(li);
        });
    });
