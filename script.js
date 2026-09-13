const input = document.getElementById("userInput");
const chatContainer = document.querySelector(".chat-container");

async function sendMessage() {
    const question = input.value.trim();

    if (question === "") {
        return;
    }

    // Create user message
    const userMessage = document.createElement("div");
    userMessage.className = "message user";

    const userAvatar = document.createElement("div");
    userAvatar.className = "avatar";
    userAvatar.textContent = "👤";

    const userContent = document.createElement("div");
    userContent.className = "message-content";
    userContent.textContent = question;

    userMessage.appendChild(userAvatar);
    userMessage.appendChild(userContent);
    chatContainer.appendChild(userMessage);

    input.value = "";

    // Create loading message
    const aiMessage = document.createElement("div");
    aiMessage.className = "message";

    const aiAvatar = document.createElement("div");
    aiAvatar.className = "avatar";
    aiAvatar.textContent = "🤖";

    const aiContent = document.createElement("div");
    aiContent.className = "message-content";
    aiContent.textContent = "Thinking... 🧠";

    aiMessage.appendChild(aiAvatar);
    aiMessage.appendChild(aiContent);
    chatContainer.appendChild(aiMessage);

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        aiContent.textContent = data.answer;

    } catch (error) {
        aiContent.textContent =
            "❌ Could not connect to the SST AI server.";
        console.error(error);
    }

    document.querySelector(".chat").scrollTop =
        document.querySelector(".chat").scrollHeight;
}

input.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});
