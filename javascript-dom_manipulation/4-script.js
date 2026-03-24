const maVariable = document.querySelector("#add_item");
const header = document.querySelector("ul.my_list");
maVariable.addEventListener("click", function () {
	const nouveauLi = document.createElement("li");
	nouveauLi.textContent = "Item";
	header.append(nouveauLi);  	
});
