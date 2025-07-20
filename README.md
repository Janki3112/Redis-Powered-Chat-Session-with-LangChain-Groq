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
1) Activate Virtual Environment
2) Check redis docker container is up
3) Install all requirements
```
pip install -r requirements.py
```
4) Run the script:  
```
python redis_chat_with_history.py
```  
5) When prompted, enter your User id. For example: 
```
👤 Please enter your User ID: user_123
```  
6) You can now ask questions: 
```
>>>> What is the capital of Japan?
```  
7) At any moment in your session, you can exit with: 
```
>>>> exit
```
## Outputs
### On VS Code
1) For user 1
   
<img width="911" height="645" alt="{DCEFA555-0B30-4BD0-9F77-9600AAEFBBC9}" src="https://github.com/user-attachments/assets/b93762b3-85ac-4f03-9dd1-c75bc339a1fb" />

3) For user 2

<img width="897" height="615" alt="{F224E521-A25F-48D1-98C9-086F2B7EA711}" src="https://github.com/user-attachments/assets/20ec23ea-0c16-45dd-9841-69cc7330b152" />

### On Redis Server
<img width="956" height="1019" alt="{594DBF9B-255A-42A6-ACBD-01937EA744E3}" src="https://github.com/user-attachments/assets/f1059e02-b753-48b0-b27e-eabc4d0768c3" />

1) Human Query
   
<img width="908" height="597" alt="{8BC5154D-96E8-49CF-87D6-56DE6AA39F18}" src="https://github.com/user-attachments/assets/67ec3f20-2810-4ded-a51e-3bfe23e297f7" />

3) Ai Response
   
<img width="940" height="635" alt="{7EF9614B-DA9F-4247-82DE-F38A1618A73D}" src="https://github.com/user-attachments/assets/0afab342-fc32-44a8-b854-721e5505ca81" />

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
