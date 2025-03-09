import random
import component_words as words


def generate_prompt():
    component_lists = {
        "Subject": words.subject,
        "Composition": words.composition,
        "Landscape": words.landscape,
        "Lighting": words.lighting,
        "Mood": words.mood,
        "Style": words.style,
    }

    components = []

    for label in component_lists.keys():
        if random.choice([True, False]):
            choice = random.choice(component_lists[label])
            components.append(choice)

    return ", ".join(components) if components else "No components selected."


if __name__ == "__main__":
    for c, i in enumerate(range(10), start=1):
        print(c, generate_prompt())
