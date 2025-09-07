"use strict";

// --- CONFIGURATION ---
const API_ENDPOINT = "https://xmxoux78g7.execute-api.ap-northeast-1.amazonaws.com/";

// --- DOM ELEMENTS ---
const totalCountElement = document.getElementById('total-count');
const rankingTableBody = document.getElementById('ranking-table');
const clickButton = document.getElementById('click-button');

// --- HELPER FUNCTION ---
/**
 * Takes the ranking data and updates the HTML page.
 * @param {Array<Object>} rankings - A list of country objects, e.g., [{country: 'Japan', click_count: 100}]
 */
function updateDisplay(rankings) {
  // Clear the existing table rows before adding new ones
  rankingTableBody.innerHTML = '';
  let totalClicks = 0;

  // Loop through the rankings to calculate the total and build the table
  rankings.forEach((ranking, i) => {
    totalClicks += ranking.click_count;

    const tableRow = document.createElement('tr');
    tableRow.innerHTML = `
      <th scope="row">${i + 1}</th>
      <td>${ranking.country}</td>
      <td>${ranking.click_count.toLocaleString()}</td>
    `;
    rankingTableBody.appendChild(tableRow);
  });

  // Update the big number at the top
  totalCountElement.textContent = totalClicks.toLocaleString();
}

// --- CORE FUNCTIONS ---

/**
 * 1. Fetches the initial rankings when the page loads.
 */
async function getInitialRankings() {
  try {
    // A GET request is the default for fetch()
    const response = await fetch(API_ENDPOINT);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    updateDisplay(data);
  } catch (error) {
    console.error("Could not fetch initial rankings:", error);
    totalCountElement.textContent = "Error";
  }
}

/**
 * 2. Handles the button click event.
 */
async function handleButtonClick() {
  try {
    // Send an empty POST request
    const response = await fetch(API_ENDPOINT, {
      method: 'POST'
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const updatedData = await response.json();
    updateDisplay(updatedData);
  } catch (error) {
    console.error("Could not process click:", error);
  }
}

// --- EVENT LISTENERS ---

// Runs the getInitialRankings function once the HTML page is fully loaded
document.addEventListener('DOMContentLoaded', getInitialRankings);

// Attaches the handleButtonClick function to the button's 'click' event
clickButton.addEventListener('click', handleButtonClick);