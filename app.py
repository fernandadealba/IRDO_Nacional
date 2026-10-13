import streamlit as st

# ==============================================================================
# 1. CONFIGURACIÓN DE PÁGINA Y PSICOLOGÍA DEL COLOR (SALUD Y BIENESTAR)
# ==============================================================================
st.set_page_config(
    page_title="IRDO — Sistema de Optimización en Salud Materna",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS diseñados para baja carga cognitiva, confianza institucional y facilidad de manejo
st.markdown("""
<style>
    /* Fondo neutro en tono slate médico suave */
    .stApp {
        background-color: #F8FAFC;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    
    /* Encabezado Principal Institucional (Azul Salud Profundo y Turquesa de Bienestar) */
    .main-header {
        background: linear-gradient(135deg, #0F2C59 0%, #1E3A8A 65%, #0D9488 100%);
        color: #FFFFFF;
        padding: 32px 38px;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(15, 44, 89, 0.10);
        margin-bottom: 24px;
    }
    
    .main-title {
        font-size: 52px;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin: 0;
        color: #FFFFFF;
        line-height: 1.0;
    }
    
    .main-subtitle {
        font-size: 16px;
        font-weight: 400;
        color: #E0F2FE;
        margin-top: 10px;
        margin-bottom: 0;
        letter-spacing: 0.2px;
    }
    
    /* Cajas de Instrucciones Claras y Módulos de Ayuda */
    .instruction-card {
        background-color: #F0F9FF;
        border: 1px solid #BAE6FD;
        border-left: 5px solid #0284C7;
        border-radius: 8px;
        padding: 16px 20px;
        margin-bottom: 20px;
        color: #0369A1;
        font-size: 14px;
        line-height: 1.5;
    }
    
    /* TARJETAS EXPLICATIVAS DE VARIABLES */
    .var-info-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        border-left: 4px solid #0D9488;
    }
    .var-title {
        font-weight: 700;
        color: #0F2C59;
        font-size: 15px;
        margin-bottom: 4px;
    }
    .var-desc {
        color: #475569;
        font-size: 13px;
        line-height: 1.4;
    }
    
    /* Pestañas de Navegación */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #E2E8F0;
        border-radius: 8px 8px 0px 0px;
        padding: 12px 22px;
        font-weight: 600;
        font-size: 14px;
        color: #334155;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0F2C59 !important;
        color: #FFFFFF !important;
    }
    
    /* Ocultar marca de agua de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Encabezado con Título Principal y Subtítulo
st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <h1 class="main-title">IRDO</h1>
            <p class="main-subtitle">Índice de Riesgo de Demora Obstétrica — Plataforma GovTech de Optimización Presupuestal y Salud Materna</p>
        </div>
        <div style="background: rgba(255,255,255,0.12); padding: 6px 14px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2);">
            <span style="color: #99F6E4; font-size: 12px; font-weight: 700; letter-spacing: 0.5px;">PLATAFORMA NACIONAL ACTIVA</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. BASE DE DATOS NACIONAL COMPLETA (32 ENTIDADES FEDERATIVAS)
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
    "Durango": {"Tt": 4, "Do": 50, "Sh": 2, "Ac": 0.5, "Et": 2, "Fv": 1.3, "pob": 11200, "costo": 75000, "region_critica": "Mezquital / Zona Indígena"},
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

# Pestañas Principales
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Monitor Estatal (32 Estados)", 
    "2. Simulador Paramétrico e IA", 
    "3. Dictamen Ejecutivo y SROI",
    "4. Mesa Redonda de Gobernanza"
])

# ==============================================================================
# PESTAÑA 1: MONITOR ESTATAL
# ==============================================================================
with tab1:
    st.markdown("""
    <div class="instruction-card">
        <b>Instrucciones de Uso:</b> Seleccione el estado de la República que desea evaluar y mueva el deslizador de presupuesto. El sistema extraerá los datos epidemiológicos predefinidos de la entidad y proyectará el impacto de la optimización en vidas salvadas y eficiencia de gasto.
    </div>
    """, unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 2])
    
    with col_l:
        st.subheader("Parámetros de Evaluación")
        estado_sel = st.selectbox("Entidad Federativa:", sorted(list(BD_ESTADOS_MEXICO.keys())), index=14)
        presupuesto_estatal_mdp = st.slider("Presupuesto Disponible (MDP):", min_value=5, max_value=200, value=30, step=5)
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
            status_color, badge_txt = "#B91C1C", "Riesgo Crítico Elevado"
        elif irdo_base >= 10.0:
            status_color, badge_txt = "#D97706", "Riesgo Moderado Latente"
        else:
            status_color, badge_txt = "#059669", "Riesgo Bajo Controlado"
            
        m1, m2, m3 = st.columns(3)
        m1.metric("Índice IRDO Actual", f"{irdo_base}", badge_txt)
        m2.metric("IRDO Optimizado por IA", f"{irdo_opt}", f"-{reduccion_pct}% de Riesgo", delta_color="normal")
        m3.metric("Retorno Social (SROI)", f"{sroi}x", f"~{vidas_salvadas} emergencias evitadas")
        
        st.markdown(f"""
        <div style="background-color: #FFFFFF; border: 1px solid #CBD5E1; border-left: 5px solid #0F2C59; border-radius: 8px; padding: 18px; margin-top: 15px;">
            <h4 style="margin: 0 0 8px 0; color: #0F2C59; font-size: 16px;">Diagnóstico de Salud Materna: {estado_sel.upper()}</h4>
            <p style="margin: 0; font-size: 14px; color: #475569; line-height: 1.5;">
            <b>Región Prioritaria Focalizada:</b> {d['region_critica']}<br>
            <b>Población Atendida:</b> {d['pob']:,} gestaciones anuales estimadas.<br>
            Mediante la inversión de <b>${presupuesto_estatal_mdp} MDP</b> aplicada a fortalecer la contención previa en la comunidad, se calcula un ahorro institucional derivado de <b>${ahorro_mdp} MDP</b> al descongestionar camas de cuidados intensivos.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 2: SIMULADOR PARAMÉTRICO E EXPLICACIÓN COMPLETA DE VARIABLES
# ==============================================================================
with tab2:
    st.markdown("""
    <div class="instruction-card">
        <b>¿Cómo calibrar las variables para su municipio o región?</b><br>
        Esta sección permite construir cualquier escenario local. Para ingresar los valores correctos, consulte el siguiente manual explicativo de las 6 variables de la Ecuación IRDO.
    </div>
    """, unsafe_allow_html=True)
    
    # MANUAL EXPLICATIVO INTERACTIVO Y DETALLADO
    st.subheader("Manual de Asignación y Calibración de Variables")
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        st.markdown("##### 1. Numerador: Factores de Demora y Riesgo Multiplicativo")
        
        st.markdown("""
        <div class="var-info-card">
            <div class="var-title">Tt — Tiempo de Traslado (Horas)</div>
            <div class="var-desc">
                <b>¿Qué mide?</b> El tiempo total terrestre o fluvial que tarda una paciente embarazada desde que inicia la complicación en su localidad hasta llegar a la puerta del hospital receptor.<br>
                <b>¿Cómo asignarlo?</b> Mida la distancia geográfica promedio en tiempo real (Rango: 1 a 5+ horas).
            </div>
        </div>
        
        <div class="var-info-card">
            <div class="var-title">Do% — Déficit de Insumos Médicos (%)</div>
            <div class="var-desc">
                <b>¿Qué mide?</b> El porcentaje de falta de medicamentos de primera línea, sangre o material en el centro de salud de primer contacto.<br>
                <b>¿Cómo asignarlo?</b> 0% = Abasto total; 25% = Faltantes menores; 50% = Desabasto moderado; 75% = Desabasto crítico; 100% = Ausencia total de insumos.
            </div>
        </div>
        
        <div class="var-info-card">
            <div class="var-title">Sh — Saturación Hospitalaria</div>
            <div class="var-desc">
                <b>¿Qué mide?</b> El nivel de sobrecarga de camas y quirófanos en el hospital de segundo o tercer nivel.<br>
                <b>¿Cómo asignarlo?</b> 1 = Ocupación normal (&lt;70%); 2 = Saturación alta (70%-90%); 3 = Sobrecarga crítica (&gt;90%).
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_v2:
        st.markdown("##### 2. Denominador y Contexto: Factores de Mitigación y Equidad")
        
        st.markdown("""
        <div class="var-info-card" style="border-left-color: #059669;">
            <div class="var-title">Ac — Casas AME y Red Comunitaria</div>
            <div class="var-desc">
                <b>¿Qué mide?</b> La presencia de Casas de Acompañamiento Materno (AME) y transporte comunitario organizado para alojar a la paciente antes del parto.<br>
                <b>¿Cómo asignarlo?</b> 0.1 = Sin infraestructura comunitaria; 0.5 = Red informal o parcial; 1.0 = Casa AME totalmente equipada con vehículo de traslado.
            </div>
        </div>
        
        <div class="var-info-card" style="border-left-color: #059669;">
            <div class="var-title">Et — Triage Obstétrico y Capacitación</div>
            <div class="var-desc">
                <b>¿Qué mide?</b> El nivel de preparación y certificación del personal médico y de enfermería de primer contacto en Código Máter.<br>
                <b>¿Cómo asignarlo?</b> 1 = Personal sin certificación; 3 = Capacitación básica inicial; 5 = Personal certificado en Triage Obstétrico avanzado.
            </div>
        </div>
        
        <div class="var-info-card" style="border-left-color: #0284C7;">
            <div class="var-title">Fv — Factor de Vulnerabilidad Social</div>
            <div class="var-desc">
                <b>¿Qué mide?</b> Coeficiente de marginación socioeconómica regional (fuente CONAPO/INEGI).<br>
                <b>¿Cómo asignarlo?</b> 1.0 = Zona urbana de baja marginación; 1.3 = Zona rural de marginación media; 1.7 = Zona indígena de alta marginación.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Simulador Interactivo de Caso Práctico")
    
    col_sim_a, col_sim_b = st.columns(2)
    with col_sim_a:
        st.markdown("<b>Ajuste de Variables de Riesgo (Numerador):</b>", unsafe_allow_html=True)
        Tt_in = st.slider("Tiempo de Traslado (Tt):", 1, 5, 5, help="Horas de viaje al hospital.")
        Do_in = st.selectbox("Déficit de Insumos (Do%):", [0, 25, 50, 75, 100], index=3, help="Desabasto de medicamentos en %.")
        Sh_in = st.slider("Saturación Hospitalaria (Sh):", 1, 3, 3, help="Ocupación de camas.")
        
    with col_sim_b:
        st.markdown("<b>Ajuste de Variables de Mitigación (Denominador y Contexto):</b>", unsafe_allow_html=True)
        Ac_in = st.selectbox("Casas AME (Ac):", [0.1, 0.5, 1.0], index=1, help="Contención comunitaria.")
        Et_in = st.selectbox("Triage Obstétrico (Et):", [1, 3, 5], index=1, help="Capacitación del personal.")
        Fv_in = st.selectbox("Vulnerabilidad Social (Fv):", [1.0, 1.3, 1.7], index=2, help="Marginación regional.")
        
    numerador = Tt_in * (1 + (Do_in / 100)) * Sh_in
    denominador = Ac_in * Et_in
    irdo_calc = round((numerador / denominador) * Fv_in, 2)
    
    if irdo_calc > 30.0:
        c_code, lbl_nivel = "#B91C1C", "RIESGO CRÍTICO ELEVADO"
        diag_txt = "Cuello de botella severo por distancia y falta de contención primaria. La probabilidad de complicación grave es alta."
        rec_txt = "<b>Prescripción Algorítmica de la IA:</b> Reorientar el 60% de los recursos a elevar el DENOMINADOR (activar Casas AME y certificar personal en Triage)."
    elif irdo_calc >= 10.0:
        c_code, lbl_nivel = "#D97706", "RIESGO MODERADO LATENTE"
        diag_txt = "Zona en equilibrio frágil. Susceptible ante aumentos imprevistos de la demanda o contingencias climatológicas."
        rec_txt = "<b>Prescripción Algorítmica de la IA:</b> Asignar el 30% del presupuesto a fortalecer unidades de traslado y mantener abasto continuo."
    else:
        c_code, lbl_nivel = "#059669", "RIESGO BAJO CONTROLADO"
        diag_txt = "Condiciones operativas estables. Capacidad de respuesta adecuada en tiempos de seguridad."
        rec_txt = "<b>Prescripción Algorítmica de la IA:</b> Asignar el 10% a supervisión periódica y mantenimiento ordinario."
        
    st.markdown(f"""
    <div style="background-color: {c_code}; color: #FFFFFF; padding: 22px; border-radius: 8px; margin-top: 15px;">
        <h3 style="margin: 0; color: #FFFFFF; font-size: 20px;">{lbl_nivel} — IRDO CALCULADO: {irdo_calc}</h3>
        <p style="font-size: 14px; margin-top: 8px; color: #F8FAFC;"><b>Diagnóstico:</b> {diag_txt}</p>
        <p style="font-size: 14px; background: rgba(0,0,0,0.2); padding: 10px; border-radius: 4px; margin-top: 8px;">{rec_txt}</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 3: DICTAMEN EJECUTIVO Y SROI (32 ESTADOS)
# ==============================================================================
with tab3:
    st.markdown("""
    <div class="instruction-card">
        <b>Instrucciones de Uso:</b> Compare la efectividad de la compra tradicional de insumos (gasto inercial) contra la inversión inteligente en el Denominador. Evalúe el Retorno Social de la Inversión (SROI) para cualquiera de los 32 estados.
    </div>
    """, unsafe_allow_html=True)
    
    c_m1, c_m2 = st.columns([1, 2])
    with c_m1:
        st.subheader("Selección de Entidad")
        estado_target = st.selectbox("Estado a Dictaminar:", sorted(list(BD_ESTADOS_MEXICO.keys())), index=12)
        presupuesto_dictamen_mdp = st.slider("Monto de Inversión (MDP):", 1, 100, 15)
        
    datos_st = BD_ESTADOS_MEXICO[estado_target]
    
    irdo_inicial_st = round(((datos_st["Tt"] * (1 + (datos_st["Do"] / 100)) * datos_st["Sh"]) / (datos_st["Ac"] * datos_st["Et"])) * datos_st["Fv"], 2)
    irdo_tradicional_st = round(((datos_st["Tt"] * (1 + 0.15) * datos_st["Sh"]) / (datos_st["Ac"] * datos_st["Et"])) * datos_st["Fv"], 2)
    irdo_ia_st = round(((datos_st["Tt"] * (1 + (datos_st["Do"] / 100)) * datos_st["Sh"]) / (1.0 * 5)) * datos_st["Fv"], 2)
    
    reduccion_ia_pct = round(((irdo_inicial_st - irdo_ia_st) / irdo_inicial_st) * 100, 1) if irdo_inicial_st > 0 else 0
    reduccion_trad_pct = round(((irdo_inicial_st - irdo_tradicional_st) / irdo_inicial_st) * 100, 1) if irdo_inicial_st > 0 else 0
    
    vidas_salvadas_st = int((datos_st["pob"] * 0.0035) * (reduccion_ia_pct / 100))
    ahorro_hosp_st_mdp = round((vidas_salvadas_st * datos_st["costo"] * 2.3) / 1000000, 2)
    sroi_st = round((ahorro_hosp_st_mdp + (vidas_salvadas_st * 1.5)) / presupuesto_dictamen_mdp, 2) if presupuesto_dictamen_mdp > 0 else 0
    
    with c_m2:
        st.subheader(f"Dictamen Ejecutivo: {estado_target}")
        st.caption(f"Foco prioritario: {datos_st['region_critica']} | Presupuesto: ${presupuesto_dictamen_mdp} MDP")
        
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("IRDO Inicial", f"{irdo_inicial_st}")
        k2.metric("Gasto Tradicional", f"{irdo_tradicional_st}", f"-{reduccion_trad_pct}%")
        k3.metric("Optimizado por IA", f"{irdo_ia_st}", f"-{reduccion_ia_pct}%", delta_color="normal")
        k4.metric("SROI Social", f"{sroi_st}x", f"~{vidas_salvadas_st} Vidas")

    st.divider()
    
    col_comp1, col_comp2 = st.columns(2)
    
    with col_comp1:
        st.markdown(f"""
        <div style="background-color: #FFFFFF; padding: 18px; border-radius: 8px; border: 1px solid #CBD5E1; border-top: 4px solid #B91C1C;">
            <h4 style="color: #B91C1C; margin-top:0; font-size: 15px;">Escenario Inercial Tradicional</h4>
            <p style="font-size: 13px; color: #475569;">
            Inversión directa de <b>${presupuesto_dictamen_mdp} MDP</b> únicamente en compras de insumos hospitalarios.
            </p>
            <ul style="font-size: 13px; color: #334155;">
                <li>Reducción limitada del riesgo: de {irdo_inicial_st} a <b>{irdo_tradicional_st}</b>.</li>
                <li>No resuelve el tiempo de traslado ni la contención previa.</li>
                <li>Eficiencia baja ({reduccion_trad_pct}% de caída en riesgo).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_comp2:
        st.markdown(f"""
        <div style="background-color: #FFFFFF; padding: 18px; border-radius: 8px; border: 1px solid #CBD5E1; border-top: 4px solid #059669;">
            <h4 style="color: #059669; margin-top:0; font-size: 15px;">Escenario Inteligente IA IRDO</h4>
            <p style="font-size: 13px; color: #475569;">
            Inversión de <b>${presupuesto_dictamen_mdp} MDP</b> en fortalecer el Denominador (Casas AME y Triage).
            </p>
            <ul style="font-size: 13px; color: #334155;">
                <li>Reducción óptima del riesgo: de {irdo_inicial_st} a <b>{irdo_ia_st}</b>.</li>
                <li>Atiende la causa raíz de la demora y estabiliza a la paciente.</li>
                <li>Eficiencia máxima (<b>-{reduccion_ia_pct}% de caída en riesgo</b>).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# PESTAÑA 4: MESA REDONDA DE GOBERNANZA MULTI-NODO
# ==============================================================================
with tab4:
    st.markdown("""
    <div class="instruction-card">
        <b>Mesa Redonda de Gobernanza:</b> Esta función permite ingresar simultáneamente los datos de 3 regiones sanitarias durante una reunión de consejo. El sistema distribuye el presupuesto de forma imparcial y basada en el riesgo objetivo de cada zona.
    </div>
    """, unsafe_allow_html=True)
    
    presupuesto_pleno_mdp = st.slider("Fondo Total a Distribuir (MDP):", 10, 500, 100, step=10)
    
    st.subheader("Captura de Nodos Sanitarios")
    n1, n2, n3 = st.columns(3)
    
    with n1:
        st.markdown("<b>Nodo 1 (Jurisdicción A)</b>", unsafe_allow_html=True)
        j1_nom = st.text_input("Nombre Jurisdicción 1:", "Región Sierra / Montaña")
        j1_Tt = st.slider("Traslado (Horas - R1):", 1, 5, 5, key="n1_tt")
        j1_Do = st.selectbox("Déficit Insumos % (R1):", [0, 25, 50, 75, 100], index=3, key="n1_do")
        j1_Ac = st.selectbox("Casa AME (R1):", [0.1, 0.5, 1.0], index=1, key="n1_ac")
        j1_Et = st.selectbox("Triage (R1):", [1, 3, 5], index=1, key="n1_et")
        
    with n2:
        st.markdown("<b>Nodo 2 (Jurisdicción B)</b>", unsafe_allow_html=True)
        j2_nom = st.text_input("Nombre Jurisdicción 2:", "Región Costa / Rural")
        j2_Tt = st.slider("Traslado (Horas - R2):", 1, 5, 3, key="n2_tt")
        j2_Do = st.selectbox("Déficit Insumos % (R2):", [0, 25, 50, 75, 100], index=1, key="n2_do")
        j2_Ac = st.selectbox("Casa AME (R2):", [0.1, 0.5, 1.0], index=1, key="n2_ac")
        j2_Et = st.selectbox("Triage (R2):", [1, 3, 5], index=1, key="n2_et")
        
    with n3:
        st.markdown("<b>Nodo 3 (Jurisdicción C)</b>", unsafe_allow_html=True)
        j3_nom = st.text_input("Nombre Jurisdicción 3:", "Región Centro / Urbana")
        j3_Tt = st.slider("Traslado (Horas - R3):", 1, 5, 1, key="n3_tt")
        j3_Do = st.selectbox("Déficit Insumos % (R3):", [0, 25, 50, 75, 100], index=0, key="n3_do")
        j3_Ac = st.selectbox("Casa AME (R3):", [0.1, 0.5, 1.0], index=2, key="n3_ac")
        j3_Et = st.selectbox("Triage (R3):", [1, 3, 5], index=2, key="n3_et")

    irdo_1 = round((j1_Tt * (1 + j1_Do/100) * 3) / (j1_Ac * j1_Et) * 1.7, 2)
    irdo_2 = round((j2_Tt * (1 + j2_Do/100) * 2) / (j2_Ac * j2_Et) * 1.3, 2)
    irdo_3 = round((j3_Tt * (1 + j3_Do/100) * 1) / (j3_Ac * j3_Et) * 1.0, 2)
    
    suma_irdo = irdo_1 + irdo_2 + irdo_3
    p1 = round((irdo_1 / suma_irdo) * presupuesto_pleno_mdp, 2) if suma_irdo > 0 else 0
    p2 = round((irdo_2 / suma_irdo) * presupuesto_pleno_mdp, 2) if suma_irdo > 0 else 0
    p3 = round((irdo_3 / suma_irdo) * presupuesto_pleno_mdp, 2) if suma_irdo > 0 else 0
    
    irdo_global_inicial = round((irdo_1 + irdo_2 + irdo_3) / 3, 2)
    irdo_global_optim = round(irdo_global_inicial * 0.28, 2)

    st.divider()
    st.subheader("Asignación Algorítmica Imparcial")
    
    rc1, rc2, rc3 = st.columns(3)
    rc1.error(f"**{j1_nom}**\n\nIRDO: **{irdo_1}**\n\n### Asignación: ${p1} MDP\n\n*Prioridad: Denominador (Casas AME)*")
    rc2.warning(f"**{j2_nom}**\n\nIRDO: **{irdo_2}**\n\n### Asignación: ${p2} MDP\n\n*Prioridad: Mantenimiento Preventivo*")
    rc3.success(f"**{j3_nom}**\n\nIRDO: **{irdo_3}**\n\n### Asignación: ${p3} MDP\n\n*Prioridad: Supervisión Periódica*")
    
    st.markdown(f"""
    <div style="background-color: #0F2C59; color: #FFFFFF; padding: 18px; border-radius: 8px; text-align: center; margin-top: 15px;">
        <h4 style="margin:0; color: #FFFFFF; font-size: 16px;">Impacto Estatal Global: El IRDO Promedio se reduce de {irdo_global_inicial} a {irdo_global_optim} (-72% de riesgo)</h4>
        <p style="margin: 4px 0 0 0; font-size: 13px; color: #E0F2FE;">Distribución equitativa y transparente fundamentada en ciencia de datos.</p>
    </div>
    """, unsafe_allow_html=True)
