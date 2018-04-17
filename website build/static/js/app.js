// var button = document.getElementById("button");

// button.onclick = function () {
//     // listen for user input
//     console.log("Clicked!!!")
//     // FUNCTION PLACEHOLDER
//     var userInput = document.getElementById("userInput").value;
    
//     // Send input to APIs
//     // fraudAnalysis(userInput)
//     sentimentAnalysis(userInput)
// };

// function fraudAnalysis(userInput) {
//     // Send user input to fraudAnalysis API
//     console.log(userInput)
//     data = String(userInput)
//     console.log(data)
//     // FUNCTION PLACEHOLDER

//     // Visualize Output
//     displayFraud(data)
// }

function handleClear() {
    var canvas = document.getElementById("userInput");
    var context = canvas.getContext("2d");
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.rect(0, 0, canvasWidth, canvasHeight);
    context.fillStyle = 'white';
    context.fill();
}
function handleSubmit() {
    var canvas = document.getElementById("userInput");
    var dataURL = canvas.toDataURL("userInput");
    document.getElementById('userInput').value = dataURL;
    document.forms["form1"].submit();
};

// function sentimentAnalysis(userInput) {
//     // Send user input to sentimentAnalysis API
//     console.log(userInput)
//     user_input = String(userInput)
//     console.log(user_input)
//     // FUNCTION PLACEHOLDER
//     function handleSubmit() {
//         var canvas = document.getElementById("canvas");
//         var dataURL = canvas.toDataURL("image/png");
//         document.getElementById('digit').value = dataURL;
//         document.forms["form1"].submit();
//     };
//     // Visualize Output
//     displaySentiment(data)
// }

// // function displayFraud(data) {
// //     // Reset DIV
// //     d3.select("#fraudDisplay").remove();
// //     d3.select("#fraudContainer").html('<div id="fraudDisplay" class="span" style="width: 100%; height: 800px; border: 3px solid #AAA;"></div>');
// //     console.log(userInput.value)
// //     // Visualize analysis

// // }

// function displaySentiment(data) {
//     // Reset DIV
//     d3.select("#sentimentDisplay").remove();
//     d3.select("#fraudContainer").html('<div id="sentimentDisplay" class="span" style="width: 100%; height: 800px; border: 3px solid #AAA;"></div>');
//     console.log(userInput.value)
//     // Visualize analysis

// }