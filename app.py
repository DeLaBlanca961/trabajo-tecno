import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="REBAJAS PRODUCTOS", page_icon="🏥")

# Título y Descripción
st.title("Calculadora de Rebajas")
st.markdown(
    "Bienvenido. Introduce el precio original y el porcentaje de rebaja para que se lo pueda calcular"
)
st.write("---")

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio = st.sidebar.number_input(
    "Tu precio (euros)", min_value=0.0, max_value=300000.0, value=60.0
)
rebaja = st.sidebar.slider("Tu rebaja (%)", 0, 100)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora") and precio > 0:
    
    # Cálculos
    ahorro = precio * (rebaja / 100)
    precio_final = precio - ahorro

    # 4. Mostrar Resultado
    st.metric(label="Precio original (€)", value=f"{precio:.2f} €")
    st.metric(label="Porcentaje de rebaja", value=f"{rebaja}%")

    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="💸 Ahorro (€)", value=f"{ahorro:.2f}")
    
    with col2:
        st.metric(label="💰 Precio a pagar (€)", value=f"{precio_final:.2f}")

    # 5. Animación y mensaje especial
    if rebaja > 50:
        st.balloons()
        st.success("🔥 MENUDO CHOLLO 🔥")
