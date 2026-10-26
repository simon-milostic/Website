let grids = document.querySelectorAll("td")
let dir = {0:"X", 1:"O", 2:""}
let count = 0

grids.forEach(function(grid) {
    grid.addEventListener("click", function() {
        grid.textContent = dir[count % 3];
        count++;
    });
});
