import boto3

# Set up the Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "amazon.nova-lite-v1:0"

# Define the chatbot's personality
system_prompt = [{"text": "You are a friendly cloud computing tutor. Explain concepts simply and use analogies."}]

# Track conversation history
messages = []

print("Chatbot ready! Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    # Add the user's message to history
    messages.append({"role": "user", "content": [{"text": user_input}]})

    # Call the Converse API with the full conversation history
    response = client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompt,
        inferenceConfig={
            "temperature": 0.1,
            "topP": 0.9,
            "maxTokens": 512
        }
    )

    # Extract and store the assistant's response
    assistant_message = response["output"]["message"]
    messages.append(assistant_message)
    print(f"Bot: {assistant_message['content'][0]['text']}")
