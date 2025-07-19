# Chat Session with LangChain & Groq Using Redis 
This Python application provides a persistent, personalized chatbot session with Redis saving chat history, and LangChain controlling interaction with the language model. The experience is entirely managed by Redis, thus when User 'x' starts a session, it can be accessed by the 'x' User and the chat history would be pulled from Redis. Therefore, personalized conversations are possible, even after stopping the app and restarting it.  

📦 Features  
- Chat History saved to Redis by User id  
- Stateful conversation using RunnableWithMessageHistory  
-  Connects to Groq's llama3-8b-8192 with LangChain  
- Command line interface  
- Can resume previous session  
- Easy to modify and can support other Users orbacks

# A. How to Setup Virtual Environment
## a. Using pipenv

1. Install Pipenv (if not already installed):
```
pip install pipenv
```
2. Install Dependencies with Pipenv:
```
pipenv install
```
3. Activate the Virtual Environment:
```
pipenv shell
```

## b. Using pip and venv

1. Create Virtual Environment
```
python-m venv venv
```
2. Activate the Virtual Environment on:

   i. Windows Operating System
      ```
      venv\Scripts\activate
      ```

   ii. MacOS or Linux Operating System
      ```
      source venv/bin/activate
      ```
## c. Using conda

1. Create Conda Environment
```
conda create-name myenv python=3.11
```

2. Activate the Virtual Environment
```
conda activate myenv
```

# B. How to Setup Redis with Docker
1) Pull Redis Docker Image
```
docker pull redis/redis-stack:latest
```
2) Run the Redis Stack Server
Note: Make sure Redis is running locally on localhost:6379  
You can get docker image for redis allot default port (6379) to it and for Redis UI allot port (8001)

```
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```
3) Verify Installation
```
docker ps
```
4) Visit the UI
Open your browser and go to:
```
http://localhost:8001
```


Make sure you have an API key for Groq (saved as GROQ_API_KEY in the environment (in .env file))  

# 🚀 How to Run
Run the script:  
```
python redis_chat_with_history.py
```  
When prompted, enter your User id. For example: 
```
👤 Please enter your User ID: user_123
```  
You can now ask questions: 
```
>>>> What is the capital of Japan?
```  
At any moment in your session, you can exit with: 
```
>>>> exit
```  
In Redis, your entire conversation regarding the UserID will have been saved. When the app is run again for the same User id, the conversational history could be resumed.  

# 🧩 Code Structure  

| Step      | Functionality                        |
|-----------|-------------------------------------|
| 1         | Connect to Redis                    |
| 2         | Prompt for User id                  |
| 3         | Create RunnableWithMessageHistory    |
|           | to be used in LangChain Conversation |
| 4         | Ask user for a question or command  |
| 5         | If user enters `exit`, exit session |
| 7         | If user enters a question, we pass it to RunnableWithMessageHistory |
