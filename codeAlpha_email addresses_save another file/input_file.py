def extract_and_validate_emails():
    # Dynamically import modules inside the function
    import re
    import os
    import socket

    input_file = input("Enter input .txt file name: ")
    output_file = input("Enter output file name: ")

    # Step 1: Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found.")
        return

    # Step 2: Read the input file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Step 3: Use regex to find all email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

    # Step 4: Remove duplicates and sort alphabetically
    unique_emails = sorted(set(emails))

    valid_emails = []
    invalid_emails = []

    # Step 5: Validate domains
    for email in unique_emails:
        domain = email.split("@")[-1]
        try:
            socket.gethostbyname(domain)  # Check if domain resolves
            valid_emails.append(email)
        except socket.gaierror:
            invalid_emails.append(email)

    # Step 6: Save valid emails to output file
    with open(output_file, "w", encoding="utf-8") as f:
        for email in valid_emails:
            f.write(email + "\n")

    # Step 7: Print summary
    print("✅ Email extraction and validation complete!")
    print(f"Total emails found: {len(unique_emails)}")
    print(f"Valid emails: {len(valid_emails)}")
    print(f"Invalid emails: {len(invalid_emails)}")
    print(f"Valid emails saved to '{output_file}'")
    print("Sample valid emails:")
    for email in valid_emails[:5]:  # Show first 5 valid emails
        print(" -", email)

# Run function
extract_and_validate_emails()
