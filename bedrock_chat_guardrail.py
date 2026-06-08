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

    # Call the Converse API with the full history, routed through a Bedrock Guardrail.
    # The guardrail screens both the input and the model's output against the
    # content-safety policies configured for this guardrail in the Bedrock console.
    response = client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompt,
        inferenceConfig={
            "temperature": 0.7,
            "topP": 0.9,
            "maxTokens": 512
        },
        guardrailConfig={
            "guardrailIdentifier": "ulbz6jwxa9hf",  # account-specific; see README
            "guardrailVersion": "DRAFT",
            "trace": "enabled"
        }
    )

    # Extract and store the assistant's response
    assistant_text = response["output"]["message"]["content"][0]["text"]
    print(f"Bot: {assistant_text}")
    messages.append({"role": "assistant", "content": [{"text": assistant_text}]})
