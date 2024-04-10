import streamlit as st
import openai
from openai import OpenAI

#1.Testing BaseModel in Streamlit webapp


# Setze deinen OpenAI API-Schlüssel hier. Es ist eine gute Praxis, ihn als Umgebungsvariable zu speichern.
openai.api_key = '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'

st.title("Chat-Tutor Demo")
st.subheader("Dein persönlicher Lerncoach")

# Textfeld für die Benutzereingabe
user_input = st.text_area("Stelle deine Frage:", "Wie funktioniert das Binärsystem?")

# Auswahl zwischen vollständiger Lösung und Hinweis
antwort_typ = st.radio("Möchtest du eine vollständige Lösung oder nur einen Hinweis?",
                       ('Vollständige Lösung', 'Hinweis'))

submit_button = st.button('Antwort generieren')

if submit_button:
    # Kontext für die Nachricht festlegen
    if antwort_typ == 'Vollständige Lösung':
        prompt = f"Erläutere detailliert: {user_input}"
    else:
        prompt = f"Gebe einen Hinweis zu: {user_input}"

    try:
        # Anfrage an die OpenAI ChatCompletion API senden
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher Lerncoach."},
                {"role": "user", "content": prompt},
            ]
        )
        # Antwort anzeigen
        st.write(response.choices[0].message['content'])
    except Exception as e:
        st.error(f"Ein Fehler ist aufgetreten: {e}")


