from pathlib import Path


def find_preferences_file():
    possible_names = [
        "job_preferences.txt",
        "job_preferences.tx"
    ]

    # Search the whole repository
    for name in possible_names:
        matches = list(Path(".").rglob(name))

        if matches:
            return matches[0]

    return None


def load_preferences():
    preferences_file = find_preferences_file()

    if preferences_file is None:
        print("\nERROR: Job preferences file was not found.")
        print("\nFiles available in the repository:")

        for file in Path(".").rglob("*"):
            if file.is_file():
                print(" -", file)

        raise FileNotFoundError(
            "Could not find job_preferences.txt anywhere in the repository."
        )

    print(f"\nPreferences file found: {preferences_file}")

    return preferences_file.read_text(encoding="utf-8")


def find_cv():
    cv_extensions = [
        ".pdf",
        ".docx",
        ".doc",
        ".txt"
    ]

    for file in Path(".").rglob("*"):
        if file.is_file() and file.suffix.lower() in cv_extensions:
            # Don't accidentally treat the preferences file as the CV
            if "job_preferences" not in file.name.lower():
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
    cv_file = find_cv()

    if cv_file:
        print(f"\nCV found: {cv_file}")
    else:
        print("\nWARNING: CV file was not found.")

    print("\nAgent setup is working!")
    print("Next step: connect the AI model and job-search system.")


if __name__ == "__main__":
    main()
