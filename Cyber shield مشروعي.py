# ============================================================
# CyberShield - Personal Password Security Analyzer
# ============================================================

import secrets
import string
import json


# ============================================================
# Welcome
# ============================================================

print("=" * 55)
print("🛡️ Welcome to CyberShield!")
print("🔐 Personal Password Security Analyzer")
print("=" * 55)

print()
username = input("👤 Enter your username: ")
password = input("🔑 Enter your password: ")

print()
print("🔎 Starting password analysis...")
print("-" * 55)


# ============================================================
# Basic Password Information
# ============================================================

password_length = len(password)

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)


print("📊 Basic Password Analysis")
print("📏 Password length:", password_length)
print("🔠 Uppercase letter:", "Yes" if has_upper else "No")
print("🔡 Lowercase letter:", "Yes" if has_lower else "No")
print("🔢 Number:", "Yes" if has_digit else "No")
print("🔣 Special character:", "Yes" if has_special else "No")

print("🛡️ Basic password analysis completed.")


# ============================================================
# Password Length Check
# ============================================================

print()
print("📏 Checking password length...")

if password_length < 8:
    print("🔴 Password is too short.")
elif password_length < 12:
    print("🟡 Good length, but 12+ characters is recommended.")
elif password_length < 16:
    print("🟢 Strong password length.")
else:
    print("🟢 Excellent password length.")

print("🛡️ Password length check completed.")


# ============================================================
# Uppercase Check
# ============================================================

print()
print("🔠 Checking uppercase letters...")

if has_upper:
    print("✅ Uppercase letter detected.")
else:
    print("⚠️ Add at least one uppercase letter.")

print("🛡️ Uppercase security check completed.")


# ============================================================
# Lowercase Check
# ============================================================

print()
print("🔡 Checking lowercase letters...")

if has_lower:
    print("✅ Lowercase letter detected.")
else:
    print("⚠️ Add at least one lowercase letter.")

print("🛡️ Lowercase security check completed.")


# ============================================================
# Number Check
# ============================================================

print()
print("🔢 Checking numbers...")

if has_digit:
    print("✅ Number detected.")
else:
    print("⚠️ Add at least one number.")

print("🛡️ Number security check completed.")


# ============================================================
# Special Character Check
# ============================================================

print()
print("🔣 Checking special characters...")

if has_special:
    print("✅ Special character detected.")
else:
    print("⚠️ Add at least one special character.")

print("🛡️ Special character security check completed.")


# ============================================================
# Common Password Check
# ============================================================

print()
print("🔍 Checking for common passwords...")

common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "iloveyou",
    "abc123",
    "123123"
]

if password.lower() in common_passwords:
    print("⚠️ Warning: Your password is commonly used.")
    print("🔒 Avoid common passwords.")
    common_password = True
else:
    print("✅ This password is not commonly used.")
    common_password = False

print("🛡️ Common password security check completed.")


# ============================================================
# Easy Pattern Check
# ============================================================

print()
print("🔎 Checking for easy-to-guess patterns...")

easy_patterns = [
    "1234",
    "2345",
    "3456",
    "4567",
    "5678",
    "6789",
    "abcd",
    "qwer",
    "asdf",
    "1111",
    "2222",
    "3333",
    "4444",
    "5555",
    "6666",
    "7777",
    "8888",
    "9999",
    "0000"
]

has_easy_pattern = False

for pattern in easy_patterns:
    if pattern in password.lower():
        has_easy_pattern = True
        break

if has_easy_pattern:
    print("⚠️ Warning: Your password contains an easy-to-guess pattern.")
    print("🔒 Avoid common sequences or repeated characters.")
else:
    print("✅ No common easy-to-guess pattern detected.")

print("🛡️ Pattern security check completed.")


# ============================================================
# Username Check
# ============================================================

print()
print("👤 Checking username security...")

if username.strip() != "":
    if username.lower() in password.lower():
        print("⚠️ Warning: Your password contains your username.")
        print("🔒 Avoid using your username inside your password.")
        username_found = True
    else:
        print("✅ Your password does not contain your username.")
        username_found = False
else:
    print("ℹ️ Username was not provided.")
    username_found = False

print("🛡️ Username security check completed.")


# ============================================================
# Sensitive Word Check
# ============================================================

print()
print("🔍 Checking for sensitive common words...")

sensitive_words = [
    "password",
    "admin",
    "administrator",
    "qwerty",
    "welcome",
    "login",
    "user",
    "root",
    "secret",
    "security",
    "cyber",
    "letmein"
]

found_sensitive_word = False

for word in sensitive_words:
    if word in password.lower():
        found_sensitive_word = True
        break

if found_sensitive_word:
    print("⚠️ Warning: Your password contains a sensitive or common word.")
    print("🔒 Avoid words like password, admin, or qwerty.")
else:
    print("✅ No sensitive common words detected.")

print("🛡️ Sensitive word security check completed.")


# ============================================================
# Security Score Calculation
# ============================================================

print()
print("📊 Calculating security score...")

score = 0

if password_length >= 8:
    score += 15

if password_length >= 12:
    score += 15

if password_length >= 16:
    score += 10

if has_upper:
    score += 10

if has_lower:
    score += 10

if has_digit:
    score += 10

if has_special:
    score += 15

if not common_password:
    score += 5

if not has_easy_pattern:
    score += 5

if not username_found:
    score += 5

if not found_sensitive_word:
    score += 5


if score > 100:
    score = 100


print("🛡️ Security Score:", score, "/ 100")

if score >= 90:
    print("🟢 Excellent security level.")
elif score >= 75:
    print("🟢 Strong security level.")
elif score >= 60:
    print("🟡 Good security level.")
else:
    print("🔴 Your password needs improvement.")

print("🛡️ Security score calculation completed.")


# ============================================================
# Final Security Assessment
# ============================================================

print()
print("=" * 55)
print("🔐 Final Security Assessment")

if score >= 90:
    level = "Excellent"
    message = "Your password has excellent security."
elif score >= 75:
    level = "Strong"
    message = "Your password has strong security."
elif score >= 60:
    level = "Good"
    message = "Your password has good security features."
else:
    level = "Weak"
    message = "Your password needs significant improvement."

print("🔐 Security Level:", level)
print("💡 Assessment:", message)
print("🛡️ CyberShield assessment completed.")


# ============================================================
# Improvement Suggestions
# ============================================================

print()
print("💡 Improvement Suggestions")

suggestions_found = False

if password_length < 12:
    print("🔹 Use at least 12 characters.")
    suggestions_found = True

if not has_upper:
    print("🔹 Add at least one uppercase letter.")
    suggestions_found = True

if not has_lower:
    print("🔹 Add at least one lowercase letter.")
    suggestions_found = True

if not has_digit:
    print("🔹 Add at least one number.")
    suggestions_found = True

if not has_special:
    print("🔹 Add at least one special character.")
    suggestions_found = True

if common_password:
    print("🔹 Avoid commonly used passwords.")
    suggestions_found = True

if has_easy_pattern:
    print("🔹 Avoid easy sequences and repeated characters.")
    suggestions_found = True

if username_found:
    print("🔹 Do not use your username in your password.")
    suggestions_found = True

if found_sensitive_word:
    print("🔹 Avoid sensitive or common words.")
    suggestions_found = True

if score >= 90:
    print("✅ No major improvements needed.")

print("🛡️ Improvement suggestions completed.")


# ============================================================
# Strong Password Generator
# ============================================================

print()
print("=" * 55)
print("🔐 Strong Password Generator")


def generate_strong_password(length=16):

    if length < 12:
        length = 12

    uppercase = secrets.choice(string.ascii_uppercase)
    lowercase = secrets.choice(string.ascii_lowercase)
    number = secrets.choice(string.digits)
    special = secrets.choice("!@#$%^&*")

    all_characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )

    remaining_characters = [
        secrets.choice(all_characters)
        for _ in range(length - 4)
    ]

    password_characters = [
        uppercase,
        lowercase,
        number,
        special
    ] + remaining_characters

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


generated_password = generate_strong_password()

print()
print("🔐 Generated Strong Password:")
print(generated_password)
print("🛡️ Password generation completed.")


# ============================================================
# Generated Password Security Verification
# ============================================================

print()
print("🔎 Checking generated password security...")

generated_has_upper = any(
    c.isupper() for c in generated_password
)

generated_has_lower = any(
    c.islower() for c in generated_password
)

generated_has_digit = any(
    c.isdigit() for c in generated_password
)

generated_has_special = any(
    not c.isalnum() for c in generated_password
)


print(
    "🔠 Uppercase letter:",
    "Yes" if generated_has_upper else "No"
)

print(
    "🔡 Lowercase letter:",
    "Yes" if generated_has_lower else "No"
)

print(
    "🔢 Number:",
    "Yes" if generated_has_digit else "No"
)

print(
    "🔣 Special character:",
    "Yes" if generated_has_special else "No"
)

print(
    "📏 Password length:",
    len(generated_password)
)


if (
    len(generated_password) >= 12
    and generated_has_upper
    and generated_has_lower
    and generated_has_digit
    and generated_has_special
):
    print("🟢 Generated password passed all security checks.")
else:
    print("🟠 Generated password needs improvement.")

print("🛡️ Generated password security check completed.")


# ============================================================
# Final Message
# ============================================================

print()
print("=" * 55)
print("🛡️ CyberShield protects your digital security.")
print("✅ Password analysis completed successfully.")
print("🔐 Strong password generation completed.")
print("=" * 55)

print()
print("👋 Thank you for using CyberShield!")


# ============================================================
# Security Report Export
# ============================================================

def clean_filename(value):
    """Create a safe filename from the username."""

    allowed_characters = (
        string.ascii_letters
        + string.digits
        + "_-"
    )

    cleaned = "".join(
        c if c in allowed_characters else "_"
        for c in value.strip()
    )

    if not cleaned:
        cleaned = "user"

    return cleaned


def save_security_report(username, password_length, score, level):
    """Save the password security analysis as a text report."""

    safe_username = clean_filename(username)
    filename = f"cybershield_report_{safe_username}.txt"

    try:
        with open(filename, "w", encoding="utf-8") as report_file:
            report_file.write("=" * 55 + "\n")
            report_file.write(
                "       CYBERSHIELD - PASSWORD SECURITY REPORT\n"
            )
            report_file.write("=" * 55 + "\n")
            report_file.write(
                f"Target Username: {username}\n"
            )
            report_file.write(
                f"Password Length: {password_length}\n"
            )
            report_file.write(
                f"Strength Score: {score} / 100\n"
            )
            report_file.write(
                f"Security Level: {level}\n"
            )
            report_file.write("-" * 55 + "\n")
            report_file.write(
                "Generated by CyberShield Security Tool\n"
            )

        print(
            f"📄 Security report saved successfully: {filename}"
        )

    except Exception as e:
        print(f"❌ Error saving security report: {e}")


save_security_report(
    username,
    password_length,
    score,
    level
)


# ============================================================
# JSON Security Report Export
# ============================================================

def save_json_report(username, password_length, score, level):
    """Save the password security analysis as a JSON report."""

    safe_username = clean_filename(username)
    filename = f"cybershield_report_{safe_username}.json"

    report_data = {
        "tool": "CyberShield",
        "target_username": username,
        "password_length": password_length,
        "strength_score": score,
        "security_level": level
    }

    try:
        with open(filename, "w", encoding="utf-8") as report_file:
            json.dump(
                report_data,
                report_file,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"📊 JSON security report saved successfully: {filename}"
        )

    except Exception as e:
        print(f"❌ Error saving JSON report: {e}")


save_json_report(
    username,
    password_length,
    score,
    level
)