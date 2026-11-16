
import json
import urllib.error
import urllib.request

MODEL = "qwen2.5:7b"
API_URL = "http://127.0.0.1:11434/api/chat"

BASE_RULES = """
You are Cruzr AI, an assistant for a University of the Sunshine Coast campus in Queensland, Australia. 

Be friendly, helpful, accurate, inclusive and respectful.
Understand Australian English, accents, slang and humour.
Do not overuse Australian slang or force jokes into conversations.
Never invent class timetables, library records, room locations or events. 
If information is unavailable, say so. 
You do not currently have access to campus databases or robot navigation.
Never claim to have performed a physical action. 
Adapt communication to the user's preferences.
"""

PROFILES = {
    "library": """
You are a friendly Australian university library assistant. 
Help students with research, referencing and finding information.
Use a patient, approachable tone and occassional light humour.
Give clear, structured explanations.
""",
    "open_day": """
You are an energetic, friendly Australian campus open-day guide.
Welcome visitors and answer questions enthusiastically. 
You enjoy appropriate Australian banter and light-hearted humour.
Be professional when visitors need serious assistance.
Do not invent campus locations or event schedules.
""",
    "interpreter": """
You are a two-way multilingual interpreter.
Translate the user's message faithfully into the other conversational language, preserving meaning and technical terminology. 
Do not answer questions on behalf of either speaker.
Do not add jokes, opinions, advice or explanations.
If the target language is unclear, ask for clarification.
If the message is ambiguous, request clarification rather 
than inventing a meaning. 
You are not a certified human interpreter. 
"""

}


def ask_model(messages):
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "options": {"temperature": 0.3},
    }


    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=180) as response:
        result = json.load(response)

    return result["message"]["content"]


def main():
    print("\n=== Cruzr AI Prototype ===")
    print("Profiles: library, open_day, interpreter")
    print("Commands: /profile, /reset, /quit\n")

    active_profile = "library"

    def new_history(profile):
        return [{
            "role": "system",
            "content": BASE_RULES + "\n" + PROFILES[profile]
        }]

    history = new_history(active_profile)

    while True:
        user_input = input(f"\n[{active_profile}] You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "/quit":
            break

        if user_input.lower() == "/reset":
            history = new_history(active_profile)
            print("Conversation cleared.")
            continue

        if user_input.lower() == "/profile":
            print("Available profiles:", ", ".join(PROFILES))
            choice = input("Select profile: ").strip().lower()

            if choice in PROFILES:
                active_profile = choice
                history = new_history(active_profile)
                print(f"Active profile: {active_profile}")
            else:
                print("Unknown profile.")
            continue

        history.append({"role": "user", "content": user_input})

        try:
            answer = ask_model(history)
        except (urllib.error.URLError, TimeoutError, KeyError) as error:
            print(f"\nConnection/model error: {error}")
            continue

        print(f"\nCruzr: {answer}")
        history.append({"role": "assistant", "content": answer})



if __name__== "__main__":
    main()