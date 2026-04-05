// Configuration
const API_BASE = 'http://localhost:8000';
const STATS_URL = `${API_BASE}/stats`;
const UPDATE_INTERVAL = 1000; // 1 second

// UI Elements
const personCountEl = document.getElementById('personCount');
const logEntriesEl = document.getElementById('logEntries');

let lastCount = -1;

/**
 * Fetch stats from the backend
 */
async function fetchStats() {
    try {
        const response = await fetch(STATS_URL);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        const count = data.person_count;
        console.log(`Stats fetched: count=${count}`);

        if (count !== lastCount) {
            updateUI(count);
            addLogEntry(count);
            lastCount = count;
        }
    } catch (error) {
        console.error('Error fetching stats:', error);
    }
}

/**
 * Update UI elements
 */
function updateUI(count) {
    personCountEl.innerText = count;
    
    // Add a quick animation effect
    personCountEl.style.transform = 'scale(1.1)';
    setTimeout(() => {
        personCountEl.style.transform = 'scale(1)';
    }, 200);
}

/**
 * Add an entry to the system log
 */
function addLogEntry(count) {
    const now = new Date();
    const timeStr = now.toTimeString().split(' ')[0];
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    
    const countText = count === 1 ? '1 person' : `${count} people`;
    entry.innerText = `[${timeStr}] Detection changed: ${countText} detected.`;
    
    // Insert at top
    logEntriesEl.insertBefore(entry, logEntriesEl.firstChild);
    
    // Limit log entries
    if (logEntriesEl.children.length > 5) {
        logEntriesEl.removeChild(logEntriesEl.lastChild);
    }
}

// Start polling
setInterval(fetchStats, UPDATE_INTERVAL);

// Initial call
fetchStats();

console.log('Human Detection Dashboard Logic Initialized');
