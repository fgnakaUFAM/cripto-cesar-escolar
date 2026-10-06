import streamlit as st

st.title("🔐 Cifra de César")
st.write("Escolha uma opção e teste a criptografia no seu celular!")

# Substitui o input() de opção por botões de seleção (radio)
modo = st.radio(
    "Escolha a operação:",
    ["1 - Criptografar", "2 - Descriptografar", "3 - Força Bruta (Testar todas as chaves)"]
)

# --- OPÇÃO 1: CRIPTOGRAFAR ---
if modo.startswith("1"):
    original = st.text_input("Digite o texto original (letras minúsculas):")
    chave = st.number_input("Digite a chave (deslocamento):", min_value=1)

    if st.button("🔒 Criptografar"):
        cifrada = ""
        chave_efetiva = chave % 26 if chave > 26 else chave

        for letra in original:
            if 'a' <= letra <= 'z':
                asciiLetra = ord(letra)
                deslocamenteChave = asciiLetra + chave_efetiva
                if deslocamenteChave > 122:
                    deslocamenteChave = deslocamenteChave - 123 + 97
                cifrada += chr(deslocamenteChave)
            else:
                cifrada += letra  # Mantém espaços ou pontuações sem quebrar

        st.success(f"**Resultado Cifrado:** {cifrada}")

# --- OPÇÃO 2: DESCRIPTOGRAFAR ---
elif modo.startswith("2"):
    cifrada = st.text_input("Digite o texto cifrado:")
    chave = st.number_input("Digite a chave (deslocamento):", min_value=1)

    if st.button("🔓 Descriptografar"):
        original = ""
        chave_efetiva = chave % 26 if chave > 26 else chave

        for letra in cifrada:
            if 'a' <= letra <= 'z':
                asciiLetra = ord(letra)
                deslocamenteChave = asciiLetra - chave_efetiva
                if deslocamenteChave < 97:
                    deslocamenteChave = deslocamenteChave + 123 - 97
                original += chr(deslocamenteChave)
            else:
                original += letra

        st.success(f"**Texto Original:** {original}")

# --- OPÇÃO 3: FORÇA BRUTA ---
elif modo.startswith("3"):
    cifrada = st.text_input("Digite o texto cifrado para testar todas as chaves:", "khoor")

    if st.button("🔎 Testar Todas as Chaves"):
        st.subheader("Tentativas de Descriptografia:")
        for chave in range(1, 26):
            original = ""
            for letra in cifrada:
                if 'a' <= letra <= 'z':
                    asciiLetra = ord(letra)
                    deslocamenteChave = asciiLetra - chave
                    if deslocamenteChave < 97:
                        deslocamenteChave = deslocamenteChave + 123 - 97
                    original += chr(deslocamenteChave)
                else:
                    original += letra

            st.write(f"**Chave {chave:02d}:** `{original}`")
            
