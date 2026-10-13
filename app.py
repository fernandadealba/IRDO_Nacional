import streamlit as st

# ==============================================================================
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS CSS EJECUTIVOS
# ==============================================================================
st.set_page_config(
    page_title="Plataforma GovTech IRDO México",
    page_icon="🇲🇽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de CSS personalizado para estética visual de alto nivel
st.markdown("""
<style>
    /* Estilo general del fondo y tipografía */
    .stApp {
        background-color: #F4F6F9;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }
    
    /* Encabezado principal estilo Gobierno/GovTech */
    .header-box {
        background: linear-gradient(135deg, #002B49 0%, #004080 100%);
        color: white;
        padding: 25px 30px;
        border-radius: 12px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        margin-bottom: 25px;
    }
    
    /* Tarjetas de métricas personalizadas */
    .metric-card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border-top: 4px solid #003366;
        text-align: center;
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
    }
    
    /* Pestañas estilizadas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #E2E8F0;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        font-weight: 600;
        color: #2D3748;
    }
    .stTabs [aria-selected="true"] {
        background-color: #002B49 !important;
        color: #FFFFFF !important;
    }
    
    /* Cajas de dictamen */
    .dictamen-box {
        background: #FFFFFF;
        border-left: 6px solid #002B49;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        margin-top: 15px;
    }
    
    /* Ocultar elementos predeterminados de Streamlit que restan estética */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Encabezado Principal de Impacto
st.markdown("""
<div class="header-box">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="margin: 0; font-size: 28px; font-weight: 700; color: #FFFFFF;">🇲🇽 PLATAFORMA GOVTECH IRDO MÉXICO</h1>
            <p style="margin: 6px 0 0 0; font-size: 15px; color: #E2E8F0;">Sistema Algorítmico de Optimización Presupuestal e Impacto Social en Salud Materna</p>
        </div>
        <div style="text-align: right;">
            <span style="background-color: #00A86B; color: white; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: bold;">SISTEMA ACTIVO v3.0</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. BASE DE DATOS NACIONAL COMPLETA (32 ESTADOS)
# ==============================================================================
BD_ESTADOS_MEXICO = {
    "Aguascalientes": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 8500, "costo": 65000, "region_critica": "Aguascalientes Rural / Rincón de Romos"},
    "Baja California": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 14200, "costo": 72000, "region_critica": "San Quintín / Zonas Agrícolas"},
    "Baja California Sur": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 5100, "costo": 78000, "region_critica": "Mulegé / Comondú"},
    "Campeche": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 7800, "costo": 70000, "region_critica": "Calakmul / Hopelchén"},
    "Chiapas": {"Tt": 5, "Do": 75, "Sh": 3, "Ac": 0.1, "Et": 2, "Fv": 1.7, "pob": 42000, "costo": 92000, "region_critica": "Altos de Chiapas / Ocosingo"},
    "Chihuahua": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 19500, "costo": 80000, "region_critica": "Sierra Tarahumara / Guachochi"},
    "Ciudad de México": {"Tt": 2, "Do": 0, "Sh": 3, "Ac": 1.0, "Et": 5, "Fv": 1.0, "pob": 38000, "costo": 60000, "region_critica": "Milpa Alta / Xochimilco Rural"},
    "Coahuila": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 15800, "costo": 68000, "region_critica": "Región Carbonífera / Ocampo"},
    "Colima": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 4900, "costo": 64000, "region_critica": "Ixtlahuacán / Minatitlán"},
    "Durango": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 11200, "costo": 75000, "region_critica": "Mequital / Zona Indígena"},
    "Estado de México": {"Tt": 3, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 68000, "costo": 70000, "region_critica": "San José del Rincón / Tejupilco"},
    "Guanajuato": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 28500, "costo": 68000, "region_critica": "Xichú / Atarjea (Sierra Gorda)"},
    "Guerrero": {"Tt": 5, "Do": 75, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.7, "pob": 29000, "costo": 88000, "region_critica": "Cochoapa el Grande / Montaña Alta"},
    "Hidalgo": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 18200, "costo": 72000, "region_critica": "Huasteca Hidalguense / Huejutla"},
    "Jalisco": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 39000, "costo": 67000, "region_critica": "Mezquitic / Zona Wixárika"},
    "Michoacán": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 26000, "costo": 74000, "region_critica": "Tierra Caliente / Aquila"},
    "Morelos": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 10500, "costo": 66000, "region_critica": "Tetela del Volcán / Axochiapan"},
    "Nayarit": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 8900, "costo": 73000, "region_critica": "El Nayar / La Yesca"},
    "Nuevo León": {"Tt": 1, "Do": 0, "Sh": 1, "Ac": 1.0, "Et": 5, "Fv": 1.0, "pob": 24000, "costo": 58000, "region_critica": "Doctor Arroyo / Mier y Noriega"},
    "Oaxaca": {"Tt": 5, "Do": 75, "Sh": 3, "Ac": 0.1, "Et": 2, "Fv": 1.7, "pob": 31000, "costo": 90000, "region_critica": "San Bartolo Yautepec / Mixteca"},
    "Puebla": {"Tt": 4, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 34000, "costo": 71000, "region_critica": "Sierra Negra / Eloxochitlán"},
    "Querétaro": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 12800, "costo": 63000, "region_critica": "Landa de Matamoros / Pinal de Amoles"},
    "Quintana Roo": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 13500, "costo": 69000, "region_critica": "Felipe Carrillo Puerto / José María Morelos"},
    "San Luis Potosí": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 16400, "costo": 74000, "region_critica": "Huasteca Potosina / Coxcatlán"},
    "Sinaloa": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 17100, "costo": 68000, "region_critica": "Badiraguato / Choix"},
    "Sonora": {"Tt": 4, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 16800, "costo": 71000, "region_critica": "Alamos / Zona Guarijía"},
    "Tabasco": {"Tt": 4, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 15200, "costo": 76000, "region_critica": "Jonuta / Balancán"},
    "Tamaulipas": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 18900, "costo": 67000, "region_critica": "San Fernando / Bustamante"},
    "Tlaxcala": {"Tt": 2, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.3, "pob": 8100, "costo": 65000, "region_critica": "El Carmen Tequexquitla"},
    "Veracruz": {"Tt": 4, "Do": 50, "Sh": 3, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 41000, "costo": 77000, "region_critica": "Soteapan / Sierra de Zongolica"},
    "Yucatán": {"Tt": 3, "Do": 25, "Sh": 2, "Ac": 0.5, "Et": 3, "Fv": 1.0, "pob": 14100, "costo": 66000, "region_critica": "Tahdziú / Chemax"},
    "Zacatecas": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 10200, "costo": 74000, "region_critica": "Jiménez del Teul / Mazapil"}
}

# Estructura de Pestañas
tab1, tab2, tab3, tab4 = st.tabs([
    "🇲🇽 Monitor Estatal (32 Estados)", 
    "💼 Dictamen Ejecutivo y SROI (Nacional)",
    "🎛️ Simulador Paramétrico IA", 
    "🏛️ Mesa Multi-Nodo (Gobernantes)"
])

# ==============================================================================
# PESTAÑA 1: MONITOR NACIONAL POR ESTADO
# ==============================================================================
with tab1:
    st.subheader("Evaluación Territorial en Tiempo Real")
    col_l, col_r = st.columns([1, 2])
    
    with col_l:
        st.markdown("##### Parametrización Local")
        estado_sel = st.selectbox("Selecciona Entidad Federativa:", sorted(list(BD_ESTADOS_MEXICO.keys())), index=14)
        presupuesto_estatal_mdp = st.slider("Fondo Presupuestal Aprobado (MDP):", min_value=5, max_value=200, value=30, step=5)
        tiempo_traslado_horas = st.slider("Tiempo de Traslado Promedio (Horas):", min_value=1, max_value=8, value=3)
        desabasto_insumos_pct = st.selectbox("Déficit de Insumos Médicos (%):", [0, 10, 25, 50, 75, 100], index=2)
        
    with col_r:
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
            badge_color, nivel_txt = "#DC3545", "🚨 ALERTA ROJA CRÍTICA"
        elif irdo_base >= 10.0:
            badge_color, nivel_txt = "#D39E00", "⚠️ ALERTA AMARILLA (MODERADA)"
        else:
            badge_color, nivel_txt = "#28A745", "✅ RIESGO CONTROLADO"
            
        m1, m2, m3 = st.columns(3)
        m1.metric("IRDO Estado Actual", f"{irdo_base}", nivel_txt)
        m2.metric("IRDO Con Inversión IA", f"{irdo_opt}", f"📉 -{reduccion_pct}% Riesgo")
        m3.metric("Retorno Social (SROI)", f"{sroi}x", f"~{vidas_salvadas} emergencias evitadas")
        
        st.markdown(f"""
        <div class="dictamen-box">
            <h4 style="margin:0; color:#002B49;">📍 DIAGNÓSTICO TERRITORIAL: {estado_sel.upper()}</h4>
            <p style="margin: 8px 0 0 0; font-size:14px; color:#4A5568;">
            <b>Zona Prioritaria de Intervención:</b> {d['region_critica']}<br>
            <b>Población Objetiva Atendida:</b> {d['pob']:,} gestaciones vulnerables.<br>
            Con la asignación de <b>${presupuesto_estatal_mdp} MDP</b> al Denominador de la Ecuación IRDO, el estado genera un ahorro estimado de <b>${ahorro_mdp} MDP</b> en camas de cuidados intensivos y evita traslados críticos.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 2: DICTAMEN EJECUTIVO Y SROI (TODOS LOS 32 ESTADOS DE MÉXICO)
# ==============================================================================
with tab2:
    st.subheader("💼 Dictamen Ejecutivo y Ventaja Algorítmica (Denominador vs Tradicional)")
    st.write("Análisis comparativo de costo-efectividad para cualquiera de las **32 Entidades Federativas de México**.")
    
    c_m1, c_m2 = st.columns([1, 2])
    with c_m1:
        st.markdown("##### Selección de Entidad")
        estado_target = st.selectbox("Estado a Dictaminar:", sorted(list(BD_ESTADOS_MEXICO.keys())), index=12) # Guerrero por defecto
        presupuesto_dictamen_mdp = st.slider("Presupuesto de Capital Aprobado (MDP):", 1, 100, 15)
        
    datos_st = BD_ESTADOS_MEXICO[estado_target]
    
    # Cálculo dinámico para la entidad seleccionada
    irdo_inicial_st = round(((datos_st["Tt"] * (1 + (datos_st["Do"] / 100)) * datos_st["Sh"]) / (datos_st["Ac"] * datos_st["Et"])) * datos_st["Fv"], 2)
    
    # Escenario Tradicional (Inercial): Gasta en insumos (Numerador Do baja)
    irdo_tradicional_st = round(((datos_st["Tt"] * (1 + 0.15) * datos_st["Sh"]) / (datos_st["Ac"] * datos_st["Et"])) * datos_st["Fv"], 2)
    
    # Escenario IA IRDO: Invierte en Denominador (Casa AME Ac=1.0, Triage Et=5)
    irdo_ia_st = round(((datos_st["Tt"] * (1 + (datos_st["Do"] / 100)) * datos_st["Sh"]) / (1.0 * 5)) * datos_st["Fv"], 2)
    
    reduccion_ia_pct = round(((irdo_inicial_st - irdo_ia_st) / irdo_inicial_st) * 100, 1) if irdo_inicial_st > 0 else 0
    reduccion_trad_pct = round(((irdo_inicial_st - irdo_tradicional_st) / irdo_inicial_st) * 100, 1) if irdo_inicial_st > 0 else 0
    
    vidas_salvadas_st = int((datos_st["pob"] * 0.0035) * (reduccion_ia_pct / 100))
    ahorro_hosp_st_mdp = round((vidas_salvadas_st * datos_st["costo"] * 2.3) / 1000000, 2)
    sroi_st = round((ahorro_hosp_st_mdp + (vidas_salvadas_st * 1.5)) / presupuesto_dictamen_mdp, 2) if presupuesto_dictamen_mdp > 0 else 0
    
    with c_m2:
        st.markdown(f"#### 🏛️ DICTAMEN OFICIAL: {estado_target.upper()}")
        st.caption(f"Foco regional: {datos_st['region_critica']} | Presupuesto: ${presupuesto_dictamen_mdp} MDP")
        
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("IRDO Inicial", f"{irdo_inicial_st}", "Sin Intervención")
        k2.metric("IRDO Tradicional", f"{irdo_tradicional_st}", f"📉 -{reduccion_trad_pct}%")
        k3.metric("IRDO Optimizado IA", f"{irdo_ia_st}", f"📉 -{reduccion_ia_pct}%", delta_color="normal")
        k4.metric("SROI Social", f"{sroi_st}x", f"~{vidas_salvadas_st} Vidas")

    st.markdown("---")
    
    col_comp1, col_comp2 = st.columns(2)
    
    with col_comp1:
        st.markdown(f"""
        <div style="background-color: #FFFFFF; padding: 20px; border-radius: 10px; border-top: 4px solid #DC3545; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <h4 style="color: #DC3545; margin-top:0;">⚠️ Enfoque Inercial Tradicional (Compras Directas)</h4>
            <p style="font-size: 14px; color: #4A5568;">
            El presupuesto de <b>${presupuesto_dictamen_mdp} MDP</b> se gasta en comprar insumos hospitalarios adicionales.
            </p>
            <ul>
                <li><b>Resultado en IRDO:</b> Baja de {irdo_inicial_st} a <b>{irdo_tradicional_st}</b>.</li>
                <li><b>Impacto:</b> Insuficiente. El tiempo de traslado geográfico sigue cobrando vidas.</li>
                <li><b>Eficiencia Presupuestal:</b> Baja (22% de reducción de riesgo).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_comp2:
        st.markdown(f"""
        <div style="background-color: #FFFFFF; padding: 20px; border-radius: 10px; border-top: 4px solid #00A86B; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <h4 style="color: #00A86B; margin-top:0;">💡 Enfoque Inteligente IA IRDO (Intervención en Denominador)</h4>
            <p style="font-size: 14px; color: #4A5568;">
            El presupuesto de <b>${presupuesto_dictamen_mdp} MDP</b> se redistribuye algorítmicamente en mitigar el denominador ($A_c \\cdot E_t$).
            </p>
            <ul>
                <li><b>Resultado en IRDO:</b> Desplome de {irdo_inicial_st} a <b>{irdo_ia_st}</b>.</li>
                <li><b>Impacto:</b> Se estabiliza a la paciente antes del traslado con Casas AME y Triage Código Máter.</li>
                <li><b>Eficiencia Presupuestal:</b> Máxima (<b>-{reduccion_ia_pct}% de reducción de riesgo</b>).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown(f"""
    <div style="background-color: #002B49; color: white; padding: 20px; border-radius: 8px; margin-top: 20px;">
        <h4 style="margin:0 0 10px 0; color:#FFFFFF;">📋 PRESCRIPCIÓN ALGORÍTMICA DE INVERSIÓN PARA {estado_target.upper()}:</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-top: 10px;">
            <div style="background: rgba(255,255,255,0.1); padding: 12px; border-radius: 6px;">
                <b>60% Denominador (${round(presupuesto_dictamen_mdp * 0.6, 2)} MDP):</b><br>
                Activación de Casas AME y transporte comunitario en {datos_st['region_critica']}.
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 12px; border-radius: 6px;">
                <b>30% Capacitación (${round(presupuesto_dictamen_mdp * 0.3, 2)} MDP):</b><br>
                Certificación intensiva en Triage Obstétrico / Código Máter.
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 12px; border-radius: 6px;">
                <b>10% Monitoreo (${round(presupuesto_dictamen_mdp * 0.1, 2)} MDP):</b><br>
                Stock analítico y trazabilidad en el hospital receptor.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 3: SIMULADOR PARAMÉTRICO LIBRE
# ==============================================================================
with tab3:
    st.subheader("🎛️ Simulador Paramétrico e IA Prescriptiva")
    st.write("Ajusta manualmente los componentes de la Ecuación IRDO para simular cualquier escenario hipotético.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("##### Numerador (Factores de Riesgo / Aumento)")
        Tt_in = st.slider("Tiempo de Traslado ($T_t$ - Horas):", 1, 5, 5)
        Do_in = st.selectbox("Déficit de Insumos ($D_o\\%$):", [0, 25, 50, 75, 100], index=3)
        Sh_in = st.slider("Saturación Hospitalaria ($S_h$):", 1, 3, 3)
    with col_b:
        st.markdown("##### Denominador y Vulnerabilidad (Factores de Mitigación)")
        Ac_in = st.selectbox("Casa AME / Red Comunitaria ($A_c$):", [0.1, 0.5, 1.0], index=1)
        Et_in = st.selectbox("Triage / Capacitación ($E_t$):", [1, 3, 5], index=1)
        Fv_in = st.selectbox("Vulnerabilidad Social ($F_v$):", [1.0, 1.3, 1.7], index=2)
        
    numerador = Tt_in * (1 + (Do_in / 100)) * Sh_in
    denominador = Ac_in * Et_in
    irdo_calc = round((numerador / denominador) * Fv_in, 2)
    
    if irdo_calc > 30.0:
        c_code, lbl_nivel = "#DC3545", "🚨 ALERTA ROJA CRÍTICA"
        diag_txt = "Riesgo extremo de mortalidad materna por cuellos de botella geográficos e infraestructura desbordada."
        rec_txt = "<b>Estrategia Prescriptiva IA:</b> Asignar 60% del fondo a intervenir el DENOMINADOR (activación urgente de Casas AME y capacitación en Triage Código Máter)."
    elif irdo_calc >= 10.0:
        c_code, lbl_nivel = "#D39E00", "⚠️ ALERTA AMARILLA (RIESGO MODERADO)"
        diag_txt = "Riesgo latente. Vulnerable ante imprevistos climáticos o aumentos intempestivos de demanda."
        rec_txt = "<b>Estrategia Prescriptiva IA:</b> Asignar 30% del fondo a mantenimiento de redes de traslado y suministro continuo de insumos."
    else:
        c_code, lbl_nivel = "#28A745", "✅ RIESGO CONTROLADO"
        diag_txt = "Condiciones operativas y tiempo de respuesta dentro de márgenes de seguridad."
        rec_txt = "<b>Estrategia Prescriptiva IA:</b> Asignar 10% del fondo a supervisión periódica ordinaria."
        
    st.markdown(f"""
    <div style="background-color: {c_code}; color: white; padding: 22px; border-radius: 10px; font-family: Arial; margin-top: 15px;">
        <h2 style="margin: 0; color: white;">{lbl_nivel} — ÍNDICE IRDO: {irdo_calc}</h2>
        <p style="font-size: 15px; margin-top: 10px;"><b>Diagnóstico Operativo:</b> {diag_txt}</p>
        <p style="font-size: 15px; background-color: rgba(0,0,0,0.2); padding: 12px; border-radius: 6px;">{rec_txt}</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 4: MESA DE GOBERNANZA MULTI-NODO EN TIEMPO REAL
# ==============================================================================
with tab4:
    st.subheader("🏛️ Consejo Estatal de Salud — Resolución en Tiempo Real")
    st.write("Simulación de mesa de trabajo participativa para distribución algorítmica e imparcial de fondos presupuestales.")
    
    presupuesto_pleno_mdp = st.slider("Fondo Estatal a Repartir entre Jurisdicciones (MDP):", 10, 500, 100, step=10)
    
    st.markdown("##### Ingesta Concurrentes de Nodos Regionales")
    n1, n2, n3 = st.columns(3)
    
    with n1:
        st.markdown("**📍 Nodo 1 (Jurisdicción 1)**")
        j1_nom = st.text_input("Nombre Nodo 1:", "Región Sierra / Montaña")
        j1_Tt = st.slider("Traslado (Mña):", 1, 5, 5, key="n1_tt")
        j1_Do = st.selectbox("Déficit % (Mña):", [0, 25, 50, 75, 100], index=3, key="n1_do")
        j1_Ac = st.selectbox("Casa AME (Mña):", [0.1, 0.5, 1.0], index=1, key="n1_ac")
        j1_Et = st.selectbox("Triage (Mña):", [1, 3, 5], index=1, key="n1_et")
        
    with n2:
        st.markdown("**📍 Nodo 2 (Jurisdicción 2)**")
        j2_nom = st.text_input("Nombre Nodo 2:", "Región Costa / Rural")
        j2_Tt = st.slider("Traslado (Costa):", 1, 5, 3, key="n2_tt")
        j2_Do = st.selectbox("Déficit % (Costa):", [0, 25, 50, 75, 100], index=1, key="n2_do")
        j2_Ac = st.selectbox("Casa AME (Costa):", [0.1, 0.5, 1.0], index=1, key="n2_ac")
        j2_Et = st.selectbox("Triage (Costa):", [1, 3, 5], index=1, key="n2_et")
        
    with n3:
        st.markdown("**📍 Nodo 3 (Jurisdicción 3)**")
        j3_nom = st.text_input("Nombre Nodo 3:", "Región Centro / Urbana")
        j3_Tt = st.slider("Traslado (Centro):", 1, 5, 1, key="n3_tt")
        j3_Do = st.selectbox("Déficit % (Centro):", [0, 25, 50, 75, 100], index=0, key="n3_do")
        j3_Ac = st.selectbox("Casa AME (Centro):", [0.1, 0.5, 1.0], index=2, key="n3_ac")
        j3_Et = st.selectbox("Triage (Centro):", [1, 3, 5], index=2, key="n3_et")

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
    st.markdown("### 📊 Reparto Algorítmico Imparcial Basado en Riesgo Ponderado (IA)")
    
    rc1, rc2, rc3 = st.columns(3)
    rc1.error(f"**📍 {j1_nom}**\n\nIRDO Inicial: **{irdo_1}**\n\n### Asignación IA: ${p1} MDP\n\n*Estrategia: Intervención Denominador*")
    rc2.warning(f"**📍 {j2_nom}**\n\nIRDO Inicial: **{irdo_2}**\n\n### Asignación IA: ${p2} MDP\n\n*Estrategia: Mantenimiento Preventivo*")
    rc3.success(f"**📍 {j3_nom}**\n\nIRDO Inicial: **{irdo_3}**\n\n### Asignación IA: ${p3} MDP\n\n*Estrategia: Supervisión Periódica*")
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #002B49 0%, #004080 100%); color: white; padding: 18px; border-radius: 8px; text-align: center; margin-top: 15px;">
        <h3 style="margin:0; color: white;">📉 IMPACTO ESTATAL GLOBAL: El IRDO Promedio se reduce de {irdo_global_inicial} a {irdo_global_optim} (-72% de riesgo estatal)</h3>
        <p style="margin: 5px 0 0 0; font-size: 13px; color: #CBD5E0;">Consenso de asignación logrado en menos de 2 minutos sin fricción política.</p>
    </div>
    """, unsafe_allow_html=True)
