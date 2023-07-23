import json
import unidecode


if __name__ == "__main__":
    with open("../data/raw/scraped_data.json", "r", encoding="utf-8") as f:
        words = json.load(f)

        new_words = {}

        for word, details in words.items():
            new_definitions = []

            for definition in details["definitions"][:]:
                new_definitions.append(unidecode.unidecode(definition))

            details["definitions"] = new_definitions
            new_words[unidecode.unidecode(word)] = details

        with open("../data/interim/unidecoded_data.json", "w+", encoding="utf-8") as g:
            json.dump(new_words, g, ensure_ascii=False)
