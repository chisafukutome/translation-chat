var messages = []; //list of messages
//Action: when clicking the "Send" button
function sendMessage() {
  var chatArea = document.querySelector(".message");
  if (chatArea.style.display === "none") {
    chatArea.style.display = "block";
  }
  var message = document.getElementById("textbox").value;
  messages.push(message); //storing the messages in the list
  document.querySelector(".chat-text").textContent = message;
  for (index = 0; index < messages.length; index++) {
    console.log(messages[index]);
  }
  // messages
  //   // .map((item) => createMessage(item))
  //   .forEach((el) => document.getElementById("chat-area").appendChild(el));
  document
    .getElementById("chat-section")
    .appendChild(createMessage(messages[messages.length - 1]));
}

var text = document.getElementById("textbox").value;
const createMessage = (text) => {
  const el = document.createElement("div"); //add something like this.
  el.innerHTML = text;
  el.className = "chat-area me shadow-lg";
  return el;
};
