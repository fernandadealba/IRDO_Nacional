import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Plataforma GovTech IRDO México",
    page_icon="🇲🇽",
    layout="wide"
)

st.title("🇲🇽 Plataforma GovTech — Ecuación e IA IRDO")
st.markdown("### Sistema de Optimización Presupuestal e Impacto Social para la Salud Materna")

# 2. Base de Datos Nacional de los 32 Estados
BD_ESTADOS_MEXICO = {
    "Aguascalientes": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 8500, "costo": 65000},
    "Baja California": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 14200, "costo": 72000},
    "Baja California Sur": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 5100, "costo": 78000},
    "Campeche": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 7800, "costo": 70000},
    "Chiapas": {"Tt": 5, "Do": 75, "Sh": 3, "Ac": 0.1, "Et": 2, "Fv": 1.7, "pob": 42000, "costo": 92000},
    "Chihuahua": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 19500, "costo": 80000},
    "Ciudad de México": {"Tt": 2, "Do": 0, "Sh": 3, "Ac": 1.0, "Et": 5, "Fv": 1.0, "pob": 38000, "costo": 60000},
    "Coahuila": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 15800, "costo": 68000},
    "Colima": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 4900, "costo": 64000},
    "Durango": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 11200, "costo": 75000},
    "Estado de México": {"Tt": 3, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 68000, "costo": 70000},
    "Guanajuato": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 28500, "costo": 68000},
    "Guerrero": {"Tt": 5, "Do": 75, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.7, "pob": 29000, "costo": 88000},
    "Hidalgo": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 18200, "costo": 72000},
    "Jalisco": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 39000, "costo": 67000},
    "Michoacán": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 26000, "costo": 74000},
    "Morelos": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 10500, "costo": 66000},
    "Nayarit": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 8900, "costo": 73000},
    "Nuevo León": {"Tt": 1, "Do": 0, "Sh": 1, "Ac": 1.0, "Et": 5, "Fv": 1.0, "pob": 24000, "costo": 58000},
    "Oaxaca": {"Tt": 5, "Do": 75, "Sh": 3, "Ac": 0.1, "Et": 2, "Fv": 1.7, "pob": 31000, "costo": 90000},
    "Puebla": {"Tt": 4, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 34000, "costo": 71000},
    "Querétaro": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 12800, "costo": 63000},
    "Quintana Roo": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 13500, "costo": 69000},
    "San Luis Potosí": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 16400, "costo": 74000},
    "Sinaloa": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 17100, "costo": 68000},
    "Sonora": {"Tt": 4, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 16800, "costo": 71000},
    "Tabasco": {"Tt": 4, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 15200, "costo": 76000},
    "Tamaulipas": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 18900, "costo": 67000},
    "Tlaxcala": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 8100, "costo": 65000},
    "Veracruz": {"Tt": 4, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 41000, "costo": 77000},
    "Yucatán": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 14100, "costo": 66000},
    "Zacatecas": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 10200, "costo": 74000}
}

# Base de Datos de Municipios Críticos
BD_MUNICIPIOS = {
    "Cochoapa el Grande (Guerrero)": {"irdo_actual": 44.62, "poblacion_objetivo": 15000, "costo_emergencia_prom": 85000},
    "Metlatónoc (Guerrero)": {"irdo_actual": 38.20, "poblacion_objetivo": 12000, "costo_emergencia_prom": 78000},
    "San Bartolo Yautepec (Oaxaca)": {"irdo_actual": 32.10, "poblacion_objetivo": 9500, "costo_emergencia_prom": 72000},
    "Mezquitic (Jalisco)": {"irdo_actual": 29.50, "poblacion_objetivo": 18000, "costo_emergencia_prom": 65000}
}

# Estructura de Pestañas Principales
tab1, tab2, tab3, tab4 = st.tabs([
    "🇲🇽 Monitor Estatal (32 Estados)", 
    "🎛️ Simulador Paramétrico IA", 
    "💼 Dictamen Municipal y SROI",
    "🏛️ Mesa Multi-Nodo (Gobernantes)"
])

# ==============================================================================
# PESTAÑA 1: MONITOR NACIONAL (32 ESTADOS)
# ==============================================================================
with tab1:
    st.header("Evaluación de Inteligencia de Datos por Entidad Federativa")
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        estado_sel = st.selectbox("Estado Evaluado:", sorted(list(BD_ESTADOS_MEXICO.keys())), index=14)
        presupuesto_estatal_mdp = st.slider("Fondo de Capital (MDP):", min_value=5, max_value=200, value=30, step=5)
        tiempo_traslado_horas = st.slider("Tiempo de Traslado (Horas):", min_value=1, max_value=8, value=3)
        desabasto_insumos_pct = st.selectbox("Déficit de Insumos Médicos (%):", [0, 10, 25, 50, 75, 100], index=2)
        
    with col_right:
        d = BD_ESTADOS_MEXICO[estado_sel]
        Sh, Ac, Et, Fv = d["Sh"], d["Ac"], d["Et"], d["Fv"]
        Tt, Do = tiempo_traslado_horas, desabasto_insumos_pct
        
        irdo_base = round(((Tt * (1 + (Do / 100)) * Sh) / (Ac * Et)) * Fv, 2)
        irdo_opt = round(((Tt * (1 + (Do / 100)) * Sh) / (1.0 * 5)) * Fv, 2)
        
        reduccion_pct = round(((irdo_base - irdo_opt) / irdo_base) * 100, 1) if irdo_base > 0 else 0
        vidas_salvadas = int((d["pob"] * 0.0035) * (reduccion_pct / 100))
        ahorro_mdp = round((vidas_salvadas * d["costo"] * 2.2) / 1000000, 2)
        sroi = round((ahorro_mdp + (vidas_salvadas * 1.5)) / presupuesto_estatal_mdp, 2) if presupuesto_estatal_mdp > 0 else 0
        
        if irdo_base > 30.0:
            color_box, nivel_txt = "#DC3545", "🚨 ALERTA ROJA CRÍTICA"
        elif irdo_base >= 10.0:
            color_box, nivel_txt = "#FFC107", "⚠️ ALERTA AMARILLA (MODERADA)"
        else:
            color_box, nivel_txt = "#28A745", "✅ RIESGO CONTROLADO"
            
        m1, m2, m3 = st.columns(3)
        m1.metric("IRDO Estado Actual", f"{irdo_base}", nivel_txt)
        m2.metric("IRDO Con Inversión IA", f"{irdo_opt}", f"📉 Reducción {reduccion_pct}%")
        m3.metric("Retorno Social (SROI)", f"{sroi}x", f"~{vidas_salvadas} emergencias evitadas")
        
        st.markdown(f"""
        <div style="background-color: #003366; color: white; padding: 18px; border-radius: 10px; margin-top: 15px;">
            <h3 style="margin:0; color:#FFF;">💡 DICTAMEN DE ASIGNACIÓN ESTATAL: {estado_sel.upper()}</h3>
            <p style="margin-top:10px; font-size:15px;">
            Para el estado de <b>{estado_sel}</b> con una población obstétrica vulnerable de <b>{d['pob']:,} gestaciones</b>, 
            la inversión de <b>${presupuesto_estatal_mdp} MDP</b> aplicada a mitigar factores estructurales y optimizar el triage 
            permite rescatar una proyección de hasta <b>${ahorro_mdp} MDP</b> en costos hospitalarios por derivaciones de emergencias críticas evitadas.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 2: SIMULADOR PARAMÉTRICO E IA PRESCRIPTIVA
# ==============================================================================
with tab2:
    st.header("🎛️ Controles Interactivos del Sistema de IA IRDO")
    
    col_a, col_b = st.columns(2)
    with col_a:
        Tt_in = st.slider("Traslado (Tt - Horas):", 1, 5, 5)
        Do_in = st.selectbox("Déficit de Insumos (Do%):", [0, 25, 50, 75, 100], index=3)
        Sh_in = st.slider("Saturación Hospitalaria (Sh):", 1, 3, 3)
    with col_b:
        Ac_in = st.selectbox("Casa AME / Red Comunitaria (Ac):", [0.1, 0.5, 1.0], index=1)
        Et_in = st.selectbox("Triage / Capacitación (Et):", [1, 3, 5], index=1)
        Fv_in = st.selectbox("Vulnerabilidad Social (Fv):", [1.0, 1.3, 1.7], index=2)
        
    numerador = Tt_in * (1 + (Do_in / 100)) * Sh_in
    denominador = Ac_in * Et_in
    irdo_calc = round((numerador / denominador) * Fv_in, 2)
    
    if irdo_calc > 30.0:
        c_code = "#DC3545"
        lbl_nivel = "🚨 ALERTA ROJA CRÍTICA"
        diag_txt = "Riesgo extremo de mortalidad materna por cuellos de botella geográficos e infraestructura desbordada."
        rec_txt = "<b>Estrategia Prescriptiva IA:</b> Asignar 60% del fondo a intervenir el DENOMINADOR (activación urgente de Casas AME y capacitación en Triage Código Máter)."
    elif irdo_calc >= 10.0:
        c_code = "#FFC107"
        lbl_nivel = "⚠️ ALERTA AMARILLA (RIESGO MODERADO)"
        diag_txt = "Riesgo latente. Vulnerable ante imprevistos climáticos o aumentos de demanda."
        rec_txt = "<b>Estrategia Prescriptiva IA:</b> Asignar 30% del fondo a mantenimiento de redes de traslado y suministro continuo de insumos."
    else:
        c_code = "#28A745"
        lbl_nivel = "✅ RIESGO CONTROLADO"
        diag_txt = "Condiciones operativas y tiempo de respuesta dentro de márgenes seguros."
        rec_txt = "<b>Estrategia Prescriptiva IA:</b> Asignar 10% del fondo a supervisión periódica ordinaria."
        
    st.markdown(f"""
    <div style="background-color: {c_code}; color: white; padding: 20px; border-radius: 12px; font-family: Arial; margin-top: 15px;">
        <h2 style="margin: 0; color: white;">{lbl_nivel} — ÍNDICE IRDO: {irdo_calc}</h2>
        <p style="font-size: 16px; margin-top: 10px;"><b>Diagnóstico:</b> {diag_txt}</p>
        <p style="font-size: 16px; background-color: rgba(0,0,0,0.25); padding: 12px; border-radius: 6px;">{rec_txt}</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 3: DICTAMEN MUNICIPAL Y RETORNO SOCIAL (SROI)
# ==============================================================================
with tab3:
    st.header("💼 Demo Ejecutivo y Ventaja Algorítmica (Denominador vs Tradicional)")
    
    c_m1, c_m2 = st.columns([1, 2])
    with c_m1:
        mun_target = st.selectbox("Municipio Objetivo:", list(BD_MUNICIPIOS.keys()))
        presupuesto_mun_mdp = st.slider("Presupuesto Aprobado (MDP):", 1, 50, 10)
        
    datos_mun = BD_MUNICIPIOS[mun_target]
    irdo_ini = datos_mun["irdo_actual"]
    
    irdo_inercial = round((5 * (1 + 0.25) * 3) / (0.5 * 2) * 1.7, 2)
    irdo_ia_den = round((5 * (1 + 0.75) * 3) / (1.0 * 5) * 1.7, 2)
    
    reduccion_riesgo_pct = round(((irdo_ini - irdo_ia_den) / irdo_ini) * 100, 1)
    vidas_salvadas_est = int((datos_mun["poblacion_objetivo"] * 0.003) * (reduccion_riesgo_pct / 100))
    ahorro_hosp_mdp = round((vidas_salvadas_est * datos_mun["costo_emergencia_prom"] * 2.5) / 1000000, 2)
    sroi_mun = round((ahorro_hosp_mdp + (vidas_salvadas_est * 1.2)) / presupuesto_mun_mdp, 2)
    
    st.markdown(f"#### 🏛️ Dictamen para {mun_target} | Presupuesto: ${presupuesto_mun_mdp} MDP")
    
    col_k1, col_k2, col_k3, col_k4 = st.columns(4)
    col_k1.error(f"IRDO INICIAL\n\n### {irdo_ini}\n\nAlerta Roja")
    col_k2.success(f"IRDO OPTIMIZADO IA\n\n### {irdo_ia_den}\n\n-{reduccion_riesgo_pct}% Riesgo")
    col_k3.info(f"VIDAS PREVENIDAS\n\n### ~{vidas_salvadas_est}\n\nEmergencias")
    col_k4.metric("SROI (RETORNO SOCIAL)", f"{sroi_mun}x", "Por cada $1 invertido")
    
    st.markdown(f"""
    <div style="background-color: #F8F9FA; border-left: 5px solid #003366; padding: 15px; border-radius: 6px; margin-top: 15px;">
        <h4 style="margin:0 0 8px 0; color:#003366;">📋 PRESCRIPCIÓN ALGORÍTMICA DE INVERSIÓN PÚBLICA:</h4>
        <ul>
            <li><b>Asignación Prioritaria (${round(presupuesto_mun_mdp * 0.6, 2)} MDP):</b> Fortalecimiento del Denominador mediante activación de Casas AME y transporte comunitario.</li>
            <li><b>Capacitación Operativa (${round(presupuesto_mun_mdp * 0.3, 2)} MDP):</b> Certificación intensiva en Triage Obstétrico / Código Máter.</li>
            <li><b>Monitoreo y Contingencia (${round(presupuesto_mun_mdp * 0.1, 2)} MDP):</b> Reserva analítica para insumos críticos en hospital de destino.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.subheader("🎯 Comparativa del Algoritmo: Tradicional vs. IA Denominador")
    st.write(f"Invertir **${presupuesto_mun_mdp} MDP** en el Denominador (Casas AME y Triage) reduce el IRDO a **{irdo_ia_den}** (caída del {round(((irdo_ini-irdo_ia_den)/irdo_ini)*100, 1)}%), mientras que el gasto inercial en insumos hospitalarios solo lo baja a **{irdo_inercial}**. **¡Intervenir el denominador es 4 veces más efectivo para salvar vidas!**")

# ==============================================================================
# PESTAÑA 4: MESA DE GOBERNANZA MULTI-NODO EN TIEMPO REAL
# ==============================================================================
with tab4:
    st.header("🏛️ Consejo Estatal de Salud — Resolución en Tiempo Real")
    presupuesto_pleno_mdp = st.slider("Presupuesto Total del Pleno a Repartir (MDP):", 10, 500, 100, step=10)
    
    st.markdown("### Configuración de Nodos de Gobernadores / Jurisdicciones")
    
    n1, n2, n3 = st.columns(3)
    
    with n1:
        st.subheader("📍 Nodo 1")
        j1_nom = st.text_input("Región 1:", "Región Montaña")
        j1_Tt = st.slider("Tt (Traslado Mña):", 1, 5, 5)
        j1_Do = st.selectbox("Do% (Déficit Mña):", [0, 25, 50, 75, 100], index=3)
        j1_Ac = st.selectbox("Ac (Casa AME Mña):", [0.1, 0.5, 1.0], index=1)
        j1_Et = st.selectbox("Et (Triage Mña):", [1, 3, 5], index=1)
        
    with n2:
        st.subheader("📍 Nodo 2")
        j2_nom = st.text_input("Región 2:", "Región Costa")
        j2_Tt = st.slider("Tt (Traslado Costa):", 1, 5, 3)
        j2_Do = st.selectbox("Do% (Déficit Costa):", [0, 25, 50, 75, 100], index=1)
        j2_Ac = st.selectbox("Ac (Casa AME Costa):", [0.1, 0.5, 1.0], index=1)
        j2_Et = st.selectbox("Et (Triage Costa):", [1, 3, 5], index=1)
        
    with n3:
        st.subheader("📍 Nodo 3")
        j3_nom = st.text_input("Región 3:", "Región Centro")
        j3_Tt = st.slider("Tt (Traslado Centro):", 1, 5, 1)
        j3_Do = st.selectbox("Do% (Déficit Centro):", [0, 25, 50, 75, 100], index=0)
        j3_Ac = st.selectbox("Ac (Casa AME Centro):", [0.1, 0.5, 1.0], index=2)
        j3_Et = st.selectbox("Et (Triage Centro):", [1, 3, 5], index=2)

    irdo_1 = round((j1_Tt * (1 + j1_Do/100) * 3) / (j1_Ac * j1_Et) * 1.7, 2)
    irdo_2 = round((j2_Tt * (1 + j2_Do/100) * 2) / (j2_Ac * j2_Et) * 1.3, 2)
    irdo_3 = round((j3_Tt * (1 + j3_Do/100) * 1) / (j3_Ac * j3_Et) * 1.0, 2)
    
    suma_irdo = irdo_1 + irdo_2 + irdo_3
    p1 = round((irdo_1 / suma_irdo) * presupuesto_pleno_mdp, 2)
    p2 = round((irdo_2 / suma_irdo) * presupuesto_pleno_mdp, 2)
    p3 = round((irdo_3 / suma_irdo) * presupuesto_pleno_mdp, 2)
    
    irdo_global_inicial = round((irdo_1 + irdo_2 + irdo_3) / 3, 2)
    irdo_global_optim = round(irdo_global_inicial * 0.28, 2)

    st.markdown("---")
    st.markdown("### 📊 Reparto Algorítmico Basado en Riesgo Ponderado (IA)")
    
    rc1, rc2, rc3 = st.columns(3)
    rc1.error(f"**📍 {j1_nom}**\n\nIRDO: **{irdo_1}**\n\n### Asignación IA: ${p1} MDP\n\n*Estrategia: Fortalecer Denominador*")
    rc2.warning(f"**📍 {j2_nom}**\n\nIRDO: **{irdo_2}**\n\n### Asignación IA: ${p2} MDP\n\n*Estrategia: Mantenimiento Preventivo*")
    rc3.success(f"**📍 {j3_nom}**\n\nIRDO: **{irdo_3}**\n\n### Asignación IA: ${p3} MDP\n\n*Estrategia: Supervisión Periódica*")
    
    st.markdown(f"""
    <div style="background-color: #003366; color: white; padding: 15px; border-radius: 8px; text-align: center; margin-top: 15px;">
        <h3 style="margin:0; color: white;">📉 IMPACTO ESTATAL GLOBAL: El IRDO Promedio se reduce de {irdo_global_inicial} a {irdo_global_optim} (-72% de riesgo estatal)</h3>
    </div>
    """, unsafe_allow_html=True)
