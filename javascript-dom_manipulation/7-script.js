const list = document.querySelector("ul#list_movies");
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(response => response.json())
.then(data => {
    // Extraire la liste depuis JSON
    const items = data.results;  // ou data.liste, data.items...
    
    // Vider + remplir
    list.innerHTML = "";
    items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item.title;
        list.append(li);
	});
});
