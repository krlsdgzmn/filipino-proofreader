import json
import re
import unidecode


def process_data(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    standardized_data = {}

    for word, word_info in data.items():
        # Remove pattern like "2-3", "1-1", etc. from the end of the word
        processed_word = process_word(word)
        processed_definitions = process_definitions(word_info.get("definitions", []))

        # Store standardized data for the word in the dictionary
        standardized_data[processed_word] = {"definitions": processed_definitions}

    return standardized_data


def process_word(word):
    # Remove pattern like "2-3", "1-1", etc. from the end of the word
    processed_word = re.sub(r"\d+-\d+$", "", word)
    # Remove trailing hyphens without affecting hyphens within the word
    return processed_word.rstrip("-").lower()


def process_definitions(definitions):
    # Decode the definitions using unidecode to remove accents and diacritics
    decoded_definitions = [
        unidecode.unidecode(definition) for definition in definitions
    ]

    # Remove numbers and trailing hyphens from definitions
    cleaned_definitions = [
        re.sub(r"(\d+[-]\d+|\d+)", "", definition).replace("*", "").strip()
        for definition in decoded_definitions
    ]

    # Implement your standardization logic here
    # For example, clean up definitions, remove any unwanted characters, etc.

    return cleaned_definitions


if __name__ == "__main__":
    json_file = "../data/interim/tagalog-words-decoded.json"
    standardized_data = process_data(json_file)

    # Export the standardized data to a new JSON file
    with open(
        "../data/processed/processed_data.json", "w", encoding="utf-8"
    ) as output_file:
        json.dump(standardized_data, output_file, ensure_ascii=False, indent=4)

    print("Processing complete. Standardized data exported to 'processed_data.json'.")
