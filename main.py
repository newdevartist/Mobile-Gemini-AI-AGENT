#Pydroid run terminal
import os
from google import genai

print("=== ΕΚΚΙΝΗΣΗ AI AGENT ===")

# --- ΒΑΛΕ ΕΔΩ ΤΟ API KEY ΣΟΥ ΜΕΣΑ ΣΤΑ ΕΙΣΑΓΩΓΙΚΑ ---
GEMINI_API_KEY = ""

try:
    # Χρήση του νέου επίσημου Client της Google
    client = genai.Client(api_key=GEMINI_API_KEY)
    print("Η σύνδεση με το Gemini API πέτυχε!\n")
except Exception as e:
    print(f"Σφάλμα αρχικοποίησης: {e}")

print("Agent: Γεια σου! Είμαι ο AI Agent σου. Γράψε 'έξοδος' για να σταματήσεις.")
print("-" * 40)

while True:
    user_input = input("Εσείς: ")
    
    if user_input.strip().lower() == 'έξοδος':
        print("Agent: Αντίο!")
        break
        
    if not user_input.strip():
        continue
        
    try:
        # Κλήση με το νέο μοντέλο gemini-2.5-flash
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_input,
        )
        print(f"\nAgent: {response.text}\n")
    except Exception as e:
        print(f"\nΣφάλμα Agent: {str(e)}\n")
    print("-" * 40)
