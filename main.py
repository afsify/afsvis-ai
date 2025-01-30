import sys
import pyttsx3
from ollama import chat

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the properties of the engine for a more natural voice
engine.setProperty('rate', 175)  # Moderate speed for clarity
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Start the streaming process
stream = chat(
    model='deepseek-r1:1.5b',
    messages=[{'role': 'user', 'content': "define multiverse ?"}],
    stream=True,
)

reasoning_content = ""
content = ""

# Collect all the content first, print it, then speak it
final_content = ""

for chunk in stream:
    if chunk and 'message' in chunk and chunk['message'].content:
        # Get the content from the chunk
        chunk_content = chunk['message'].content
        
        # Collect all content into one string
        final_content += chunk_content

        # Print the content immediately
        sys.stdout.write(chunk_content)
        sys.stdout.flush()

# Now speak the entire content after printing
engine.say(final_content)
engine.runAndWait()

# Final result
reasoning_content = "The reasoning behind this is explained..."
content = "The final answer is here."

# Speak reasoning and final answer separately
engine.say("\n\nReasoning: " + reasoning_content)
engine.say("\nFinal Answer: " + content)
engine.runAndWait()

# Final output to console
print("\n\nReasoning:", reasoning_content)
print("\nFinal Answer:", content)
