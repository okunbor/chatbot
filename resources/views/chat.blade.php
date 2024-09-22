<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPT Custom Assistant</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script type="importmap">
        {
          "imports": {
            "@google/generative-ai": "https://esm.run/@google/generative-ai"
          }
        }
      </script>
    <style>
        /* Caret blinking effect */
        .typing::after {
            content: '|';
            animation: blink 1s step-end infinite;
        }

        @keyframes blink {
            50% {
                opacity: 0;
            }
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    {{$data["p"]}}
    <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <h1 class="text-2xl font-bold mb-4">Moses Assistant</h1>
        <div id="chat-box" class="bg-gray-200 p-4 h-64 rounded-lg overflow-y-scroll mb-4"></div>
        <input id="user-input" type="text" class="border border-gray-300 p-2 w-full rounded-lg mb-2" placeholder="Ask me anything...">
        <button id="send-btn" class="bg-blue-500 text-white p-2 rounded-lg w-full">Send</button>
    </div>

    <script type="module">
       import { GoogleGenerativeAI } from "@google/generative-ai";

       // Fetch your API_KEY
       const API_KEY = " AIzaSyD4TH-krIOeeLETxodJHP1ANP6FIf6mfLU ";

       // Access your API key (see "Set up your API key" above)
       const genAI = new GoogleGenerativeAI(API_KEY);

       const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});

       async function run(query) {
           const prompt = query;
           const result = await model.generateContent(prompt);
           const response = await result.response;
           const text = response.text();
           return text;
       }

       document.getElementById('send-btn').addEventListener('click', async () => {
           const userInput = document.getElementById('user-input').value;
           if (userInput.trim() === '') return;

           addMessageToChatBox('User', userInput);
           document.getElementById('user-input').value = '';

           const response = await run(userInput);
           typeMessage('Assistant', response);
       });

       function addMessageToChatBox(sender, message) {
           const chatBox = document.getElementById('chat-box');
           const messageElement = document.createElement('div');
           messageElement.classList.add('mb-2', 'p-2', 'rounded-lg', 'break-words');
           if (sender === 'User') {
               messageElement.classList.add('bg-blue-100', 'self-end');
               messageElement.textContent = `Moses: ${message}`;
           } else {
               messageElement.classList.add('bg-green-100');
               messageElement.textContent = `Assistant: ${message}`;
           }
           chatBox.appendChild(messageElement);
           chatBox.scrollTop = chatBox.scrollHeight;
       }

       function typeMessage(sender, message) {
           const chatBox = document.getElementById('chat-box');
           const messageElement = document.createElement('div');
           messageElement.classList.add('mb-2', 'p-2', 'rounded-lg', 'break-words', 'typing');
           messageElement.classList.add(sender === 'User' ? 'bg-blue-100' : 'bg-green-100');
           chatBox.appendChild(messageElement);

           let index = 0;
           function typeWriter() {
               if (index < message.length) {
                   messageElement.textContent = `${sender === 'User' ? 'Moses: ' : 'Assistant: '}${message.slice(0, index + 1)}`;
                   index++;
                   setTimeout(typeWriter, 50); // Adjust speed here
               } else {
                   messageElement.classList.remove('typing'); // Remove blinking cursor after typing
               }
               chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll as message types
           }

           typeWriter();
       }

    </script>
</body>
</html>
