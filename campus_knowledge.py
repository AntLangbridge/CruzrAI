
import json
import re
from pathlib import Path

DATA_FILE = Path(__file__).with_name("campus_data.json")

with DATA_FILE.open("r", encoding="utf-8") as file:
    CAMPUS_DATA = json.load(file)


def campus_answer(question):
    """
    Return:
      None   = not identified as a campus-specific lookup
      string = verified answer or safe fallback
    """
    q = question.lower()

    location_request = bool(re.search(
        r"\b(where|find|located|location|directions|"
        r"get to|take me|show me|which building|which room)\b",
        q
    ))

    if location_request:
        locations = CAMPUS_DATA["locations"]

        if re.search(r"\b(library)\b", q):
            item = locations["library"]
            return (
                f"The Moreton Bay library is in "
                f"Building {item['building']}. "
                "I don't have verified step-by-step directions yet."
            )

        if re.search(r"\b(student services|student central|service centre)\b", q):
            item = locations["student_services"]
            return (
                f"The Student Service Centre is on the "
                f"{item['floor']} of Building {item['building']}."
            )

        if re.search(r"\b(engineering lab|engineering labs|robotics lab)\b", q):
            return (
                "The engineering laboratories have been reported "
                "in A1 on Level 2, but their exact location "
                "still needs confirmation for this system."
            )

        return (
            "I'm not sure where that is at Moreton Bay yet. "
            "I don't want to send you to the wrong place."
        )

    campus_context = re.search(
        r"\b(unisc|sunshine coast university|moreton bay|"
        r"on campus|this campus|our campus|"
        r"here at uni|here at university)\b",
        q
    )

    campus_details = re.search(
        r"\b(course|program|facility|facilities|event|"
        r"timetable|schedule|opening hours|"
        r"demonstration|workshop|building|room)\b",
        q
    )

    if campus_context and campus_details:
        return (
            "I don't have verified information about that "
            "at UniSC Moreton Bay yet."
        )

    return None
