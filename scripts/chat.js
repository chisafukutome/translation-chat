const chatArea = document.querySelector(".chat-area");

//Action: when clicking the "Send" button
function sendMessage() {
  var message = document.getElementById("textbox").value;
  chatArea.classList.remove(".hidden");
  alert("The message you sent is " + message);
}
