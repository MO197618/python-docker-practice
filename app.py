KEYWORDS = ["error", "bug", "crash", "slow", "failure"]


def analyze_issue(issue):
    if not isinstance(issue, str):
        raise TypeError("Issue description must be a string")

    found = [
        word for word in KEYWORDS
        if word in issue.lower()
    ]

    return found


def main():
    print("\n=== Repository Issue Analyzer ===")

    issue = input("Enter GitHub issue description: ")

    found = analyze_issue(issue)

    print("\nIssue Description:")
    print(issue)

    print("\nIdentified Issues:")

    if found:
        for word in found:
            print(f"- Possible issue related to: {word}")
    else:
        print("- No common issue keywords found.")

    print("\nRecommended Checks:")
    print("- Review the affected code.")
    print("- Check expected behavior.")
    print("- Test possible edge cases.")
    print("- Verify the fix.")


if __name__ == "__main__":
    main()