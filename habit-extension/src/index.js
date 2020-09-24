import axios from "axios";
const api = "https://habit-tracking-sid.herokuapp.com/addData";
const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const status = document.querySelector(".api-status");
const results = document.querySelector(".result-container");
results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";
// grab the form
const form = document.querySelector(".form-data");
// grab the country name
const activity = document.querySelector(".activity-name");
const start = document.querySelector(".start-time");
const time = document.querySelector(".time-amount");
const category = document.querySelector(".category-name");

// declare a method to search by country name
const processQuery = async (activity, start, time, category) => {
  loading.style.display = "block";
  errors.textContent = "";
  try {
    const response = await axios.get(`${api}?name=Sid&activity=${activity}&category=${category}&start=${start}&duration=${time}`);
    loading.style.display = "none";
    status.textContent = response.data.Message;
    results.style.display = "block";
  } catch (error) {
    loading.style.display = "none";
    results.style.display = "none";
    errors.textContent = "We could not process that request.";
  }
};

// declare a function to handle form submission
const handleSubmit = async e => {
  e.preventDefault();
  processQuery(activity.value, start.value, time.value, category.value);
  console.log(activity.value);
};

form.addEventListener("submit", e => handleSubmit(e));