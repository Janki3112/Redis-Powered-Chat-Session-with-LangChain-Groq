import redis
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_redis import RedisChatMessageHistory

# Step 1: Setup Redis Client
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    password=None
)

# Step 2: Ask for User ID before anything else
user_id = input("👤 Please enter your User ID: ").strip()

# Step 3: Function to retrieve Redis chat history for a user
def get_redis_history(session_id: str) -> BaseChatMessageHistory:
    return RedisChatMessageHistory(
        session_id=session_id,
        redis_client=redis_client
    )

# Step 4: Define your OpenAI model
model = ChatGroq(model="llama3-8b-8192")

# Step 5: Define Prompt Template with History Placeholder
human_template = "{question}"

prompt_template = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="history"),
    ("human", human_template),
])

# Step 6: Create the Chain
chain = prompt_template | model

# Step 7: Wrap with History Support
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history=get_redis_history,
    input_messages_key="question",
    history_messages_key="history",
)

# Step 8: Start Chat Session
print(f"\n💬 Chat session started for user: {user_id}\n(Type 'exit' to end)\n")

while True:
    user_question = input(">>>> ").strip()
    if user_question.lower() in ['exit', 'quit']:
        print("👋 Ending chat. Your session has been saved.")
        break

    result = chain_with_history.invoke(
        {"question": user_question},
        config={"configurable": {"session_id": user_id}},
    )

    print(result.content)
