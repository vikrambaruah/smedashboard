const data = [
  { component: "Comp1", component_name: "CompName1", timestamp: "2023-07-25 12:00:00", name: "Name1", value: 10 },
  { component: "Comp2", component_name: "CompName2", timestamp: "2023-07-25 13:00:00", name: "Name2", value: 20 },
  { component: "Comp3", component_name: "CompName3", timestamp: "2023-07-25 14:00:00", name: "Name3", value: 30 },
];

const tableBody = document.getElementById("tableBody");

// Function to populate the table with data
function populateTable() {
  let html = "";
  data.forEach(item => {
    html += `
      <tr>
        <td>${item.component}</td>
        <td>${item.component_name}</td>
        <td>${item.timestamp}</td>
        <td>${item.name}</td>
        <td>${item.value}</td>
      </tr>
    `;
  });
  tableBody.innerHTML = html;
}

// Call the function to populate the table on page load
window.onload = populateTable;
