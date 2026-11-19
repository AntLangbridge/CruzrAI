
from robot_config import ROBOT_CONFIG
from campus_knowledge import campus_answer
from profiles import BASE_RULES, PROFILES
import json
import urllib.error
import urllib.request

MODEL = "qwen2.5:7b"
API_URL = "http://127.0.0.1:11434/api/chat"

def ask_model(messages):
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.65,
            "num_predict": 180
        }
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
        identity = (
            f"\nYOUR IDENTITY:\n"
            f"Your name is {ROBOT_CONFIG['name']}.\n"
            f"You are a {ROBOT_CONFIG['model']} robot.\n"
            f"You belong to {ROBOT_CONFIG['institution']}.\n"
            f"You operate at the {ROBOT_CONFIG['campus']} campus.\n"
            f"When someone addresses you by name, recognise that "
            f"they are speaking to you.\n"
            f"Never address the user using your own name unless "
            f"they explicitly identify themselves that way.\n"
        )

        return [{
            "role": "system",
            "content": BASE_RULES + "\n" + identity + "\n" + PROFILES[profile]
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

        if active_profile != "interpreter":
            verified_response = campus_answer(user_input)

            if verified_response is not None:
                print(f"\n{ROBOT_CONFIG['name']}: {verified_response}")
                continue
        
        history.append({"role": "user", "content": user_input})

        try:
            answer = ask_model(history)
        except (urllib.error.URLError, TimeoutError, KeyError) as error:
            print(f"\nConnection/model error: {error}")
            continue

        print(f"\n{ROBOT_CONFIG['name']}: {answer}")
        history.append({"role": "assistant", "content": answer})



if __name__== "__main__":
    main()