

// async function plotGraph() {
//   const container = document.querySelector("#g_box_1");
//   console.log("Graph script loaded; container:", container);

//   const dataUrl = new URL("../../Data/info.json", import.meta.url);
//   console.log("Loading data from:", dataUrl.href);

//   const response = await fetch(dataUrl);
//   if (!response.ok) {
//     throw new Error(`JSON request failed: ${response.status}`);
//   }

//   const countryData = await response.json();

//   const rows = Object.entries(countryData).flatMap(([country, observations]) =>
//     observations.map(d => ({ ...d, country }))
//   );

//   const chart = Plot.plot({
//     width: container.clientWidth - 40,
//     height: 420,
//     marginLeft: 65,
//     marginBottom: 50,
//     x: {
//       label: "Year",
//       tickFormat: year => String(year)
//     },
//     y: {
//       label: "Debt (% of GDP)",
//       grid: true
//     },
//     color: { legend: true },
//     marks: [
//       Plot.lineY(rows, {
//         x: "year",
//         y: "debt_gdp",
//         stroke: "country"
//       })
//     ]
//   });

//   container.replaceChildren(chart);
// }

// plotGraph().catch(error => console.error("Graph failed:", error));

let sayHi = function() {
  console.log("hello")
}
sayHi()