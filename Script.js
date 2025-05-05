document.getElementById("studentForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const name = document.getElementById("name").value.trim();
  const age = document.getElementById("age").value.trim();
  const grade = document.getElementById("grade").value.trim();

  if (!name || !age || !grade) return alert("Please fill in all fields.");

  const newStudent = { name, age, grade };
  const students = JSON.parse(localStorage.getItem("students")) || [];
  students.push(newStudent);
  localStorage.setItem("students", JSON.stringify(students));
  alert("Student added!");
  this.reset();
});
