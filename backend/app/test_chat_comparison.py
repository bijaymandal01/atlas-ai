from app.services.chat_service import chat

TEST_USER_ID = 9999999997

print("=" * 70)
print("LOCAL TELEGRAM CHAT — COMPARISON TEST")
print("=" * 70)

message = "Compare Apple vs Microsoft"

print("\nUSER:")
print(message)

try:

    response = chat(
        TEST_USER_ID,
        message
    )

    print("\nATLAS:")
    print(response["reply"])

    print("\nSTATUS: PASS")

except Exception as e:

    print("\nSTATUS: FAIL")
    print("ERROR:")
    print(e)