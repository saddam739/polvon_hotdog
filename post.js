const url = "https://script.google.com/macros/s/AKfycbznLh5nT1spgrmgKwLUiWquVV2oY0f61yLbfK8MLIPnHDkeOcxeZATHkLxjT-5zOvG-/exec";
const data = {
  inventory: [{id: 1, name: "Test Item", qty: 5}],
  recipes: [],
  sales: [],
  expenses: []
};

fetch(url, {
  method: "POST",
  body: JSON.stringify(data)
})
.then(res => res.text())
.then(text => console.log("Result:", text))
.catch(err => console.error("Error:", err));

