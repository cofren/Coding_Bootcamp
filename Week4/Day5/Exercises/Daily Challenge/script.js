// Daily Challenge Planets

const planets = ["Earth", "Mars", "Jupiter"];
console.log(planets);

for (i=0; i<planets.length; i++) {
        let newElement = document.createElement("div");
        newElement.className = "planet";
        newElement.innerHTML = planets[i];
        document.body.appendChild(newElement);
}

let planet1 = document.querySelectorAll("div")[0];
planet1.style.backgroundColor = "red";

let planet2 = document.querySelectorAll("div")[1];
planet2.style.backgroundColor = "blue";

let planet3 = document.querySelectorAll("div")[2];
planet3.style.backgroundColor = "green";

