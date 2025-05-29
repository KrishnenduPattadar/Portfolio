// import FloatingCard from "@/components/ui/snappy-floating-card";
// Lines to be typed
const lines = [
    "a Backend Developer 🧑‍💻.....",
];

// Variables to track the current line and character
let currentLine = 0;
let currentChar = 0;

// Function to type each line character by character
function typeLine() {
    if (currentLine < lines.length) {
        const lineId = `line${currentLine + 1}`;
        const element = document.getElementById(lineId);

        if (element && currentChar < lines[currentLine].length) {
            element.innerHTML += lines[currentLine][currentChar];
            currentChar++;
            setTimeout(typeLine, 80); // Typing speed in milliseconds
        } else if (element) {
            currentLine++;
            currentChar = 0;
            setTimeout(typeLine, 500); // Delay before typing the next line
        }
    }
}

// Initialize typing effect on window load
window.onload = typeLine;

