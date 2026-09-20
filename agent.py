import os
import json
from pathlib import Path


def read_text_file(filename):
    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"Could not find {filename}")

    return path.read_text(encoding="utf-8")


def load_preferences():
    return read_text_file("job_preferences.txt")


def get_cv_file():
    files = list(Path(".").glob("*"))

    cv_extensions = [".pdf", ".docx", ".doc", ".txt"]

    for file in files:
        if file.suffix.lower() in cv_extensions:
            return file

    return None


def main():
    print("=" * 60)
    print("CV JOB SEARCH AGENT")
    print("=" * 60)

    # Load job preferences
    preferences = load_preferences()

    print("\nJob preferences loaded successfully.")
    print("-" * 60)
    print(preferences)
    print("-" * 60)

    # Find CV
    cv_file = get_cv_file()

    if cv_file:
        print(f"\nCV found: {cv_file.name}")
    else:
        print("\nWARNING: CV file was not found.")

    print("\nAgent setup is working.")
    print("Next step: connect an AI model and job-search source.")


if __name__ == "__main__":
    main()
