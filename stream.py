import streamlit as st

# Dados simulados de ganhos mensais por pacote
ganhos = {
    "Horas Extras": {
        "Janeiro": 30000, "Fevereiro": 1200, "Março": 1100, "Abril": 950,
        "Maio": 1300, "Junho": 1250, "Julho": 1400, "Agosto": 1350,
        "Setembro": 1200, "Outubro": 1500, "Novembro": 1450, "Dezembro": 1600
    },
    "Água": {
        "Janeiro": 800, "Fevereiro": 850, "Março": 780, "Abril": 820,
        "Maio": 900, "Junho": 890, "Julho": 950, "Agosto": 910,
        "Setembro": 870, "Outubro": 940, "Novembro": 920, "Dezembro": 980
    },
    "GLP": {
        "Janeiro": 1500, "Fevereiro": 1400, "Março": 1600, "Abril": 1550,
        "Maio": 1650, "Junho": 1700, "Julho": 1750, "Agosto": 1800,
        "Setembro": 1780, "Outubro": 1900, "Novembro": 1850, "Dezembro": 2000
    },
    "Energia Elétrica": {
        "Janeiro": 2200, "Fevereiro": 2100, "Março": 2300, "Abril": 2250,
        "Maio": 2400, "Junho": 2350, "Julho": 2500, "Agosto": 2550,
        "Setembro": 2600, "Outubro": 2700, "Novembro": 2650, "Dezembro": 2800
    },
    "Preços de Materiais": {
        "Janeiro": 1100, "Fevereiro": 1150, "Março": 1120, "Abril": 1170,
        "Maio": 1190, "Junho": 1220, "Julho": 1240, "Agosto": 1260,
        "Setembro": 1280, "Outubro": 1300, "Novembro": 1320, "Dezembro": 1350
    },
    "Combustível Salinor": {
        "Janeiro": 1700, "Fevereiro": 1600, "Março": 1650, "Abril": 1680,
        "Maio": 1750, "Junho": 1720, "Julho": 1800, "Agosto": 1820,
        "Setembro": 1850, "Outubro": 1900, "Novembro": 1880, "Dezembro": 1950
    },
    "Combustível Navenor": {
        "Janeiro": 1550, "Fevereiro": 1500, "Março": 1580, "Abril": 1600,
        "Maio": 1620, "Junho": 1650, "Julho": 1700, "Agosto": 1720,
        "Setembro": 1740, "Outubro": 1780, "Novembro": 1800, "Dezembro": 1850
    },
    "Materiais Salinor": {
        "Janeiro": 1300, "Fevereiro": 1350, "Março": 1320, "Abril": 1380,
        "Maio": 1400, "Junho": 1450, "Julho": 1500, "Agosto": 1520,
        "Setembro": 1550, "Outubro": 1580, "Novembro": 1600, "Dezembro": 1650
    },
    "Materiais Navenor": {
        "Janeiro": 1250, "Fevereiro": 1200, "Março": 1230, "Abril": 1270,
        "Maio": 1290, "Junho": 1320, "Julho": 1350, "Agosto": 1380,
        "Setembro": 1400, "Outubro": 1420, "Novembro": 1450, "Dezembro": 1480
    }
}

# Interface com Streamlit
st.title("🤖 Assistente Virtual de Planejamento")

menu = st.selectbox("O que você deseja fazer?", [
    "Consultar data das reuniões",
    "Consultar ganho por pacote e mês",
    "Consultar ganho total por pacote",
    "Ver ganhos totais de todos os pacotes"
])

# Opção 1: Datas das reuniões
if menu == "Consultar data das reuniões":
    st.subheader("📅 Datas das próximas reuniões")
    st.write("- Reunião N1: 30/04/2025")
    st.write("- Reunião N2: 12/04/2025")

# Opção 2: Ganho por pacote e mês
elif menu == "Consultar ganho por pacote e mês":
    pacote = st.selectbox("Escolha o pacote:", list(ganhos.keys()))
    mes = st.selectbox("Escolha o mês:", list(ganhos[pacote].keys()))
    valor = ganhos[pacote][mes]
    st.success(f"💰 O ganho do pacote **{pacote}** em **{mes}** foi: R$ {valor:,.2f}")

# Opção 3: Ganho total de um pacote
elif menu == "Consultar ganho total por pacote":
    pacote = st.selectbox("Selecione o pacote:", list(ganhos.keys()))
    total = sum(ganhos[pacote].values())
    st.success(f"📈 O ganho total do pacote **{pacote}** no ano foi: R$ {total:,.2f}")

# Opção 4: Todos os pacotes
elif menu == "Ver ganhos totais de todos os pacotes":
    st.subheader("📊 Ganhos totais por pacote:")
    for pacote, valores in ganhos.items():
        total = sum(valores.values())
        st.write(f"✅ {pacote}: R$ {total:,.2f}")
