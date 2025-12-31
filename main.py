from crew import SEACrew
from utils.resume_parser import extract_resume_text

def main():
    print("\n🎓 Students Employability Accelerator (SEA)")
    print("Ask about jobs, resume analysis, rewriting, or interviews")
    print("Commands:")
    print("  upload <path_to_resume>")
    print("  exit\n")

    crew = SEACrew()
    resume_text = None

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("🚀 All the best!")
            break

        if user_input.lower().startswith("upload"):
            try:
                path = user_input.split(" ", 1)[1]
                resume_text = extract_resume_text(path)
                print("✅ Resume uploaded and parsed successfully")
            except Exception as e:
                print(f"❌ Error: {e}")
            continue

        if resume_text:
            user_input = f"""
            Resume:
            {resume_text}

            User Question:
            {user_input}
            """

        response = crew.run(user_input)
        print("\nSEA Copilot:\n")
        print(response)
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
