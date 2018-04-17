var button = document.getElementById("button");

button.onclick = function () {
    // listen for user input
    console.log("Clicked!!!")
    // FUNCTION PLACEHOLDER
    var userInput = document.getElementById("userInput").value;
    
    // Send input to APIs
    fraudAnalysis(userInput)
    sentimentAnalysis(userInput)
};




function fraudAnalysis(userInput) {
    // Send user input to fraudAnalysis API
    console.log(userInput)
    data = userInput.value
    // FUNCTION PLACEHOLDER

    // Visualize Output
    displayFraud(data)
}

function sentimentAnalysis(userInput) {
    // Send user input to sentimentAnalysis API
    console.log(userInput)
    data = userInput
    // FUNCTION PLACEHOLDER

    // Visualize Output
    
    displaySentiment(data)
}

function displayFraud(data) {
    // Reset DIV
    d3.select("#fraudDisplay").remove();
    d3.select("#fraudContainer").html('<div id="fraudDisplay" class="span" style="width: 100%; height: 800px; border: 3px solid #AAA;"></div>');
    console.log(userInput.value)
    // Visualize analysis

}

function displaySentiment(data) {
    // Reset DIV
    d3.select("#sentimentDisplay").remove();
    d3.select("#fraudContainer").html('<div id="sentimentDisplay" class="span" style="width: 100%; height: 800px; border: 3px solid #AAA;"></div>');
    console.log(userInput.value)
    // Visualize analysis

}