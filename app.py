import streamlit as st
from openai import OpenAI
import time
import random  # Import correcto al principio

st.set_page_config(page_title="Primeros $1K con IA", layout="centered")
st.title("💰 Primeros $1K con IA")
st.markdown("### Generador de ideas para monetizar tus habilidades en IA")
st.markdown("Selecciona tus habilidades actuales y obtén 5 ideas reales de servicios o productos digitales que puedes vender YA en Fiverr, Upwork o Gumroad, con precios sugeridos.")

# Sidebar con apoyo
with st.sidebar:
    st.header("🚀 Apóyame")
    st.markdown("Si esta app te ayuda a ganar dinero, ¡apóyame!")
    st.markdown("- **Substack**: [Suscríbete](https://esospanas.substack.com/)")
    st.markdown("- **Ko-fi**: [Café ☕](https://ko-fi.com/esospanas)")
    st.markdown("- **Crypto ETH**: ")
    st.code("0xc50639FC0EA4B154AbE83Bf3006c745Cbeb0bEBd", language="text")

# Grok API opcional
api_key = st.text_input("🔑 Grok API Key (opcional para ideas ultra-personalizadas)", type="password")
client = None
if api_key:
    client = OpenAI(base_url="https://api.x.ai/v1", api_key=api_key)
    st.success("Grok conectado → ideas personalizadas en tiempo real")

# Habilidades
habilidades = [
    "Python básico",
    "Prompt engineering",
    "Fine-tuning de modelos",
    "Generación de imágenes (Stable Diffusion, Midjourney)",
    "Visión por computadora",
    "Creación de datasets",
    "Automatización con scripts IA",
    "Chatbots simples",
    "Análisis de datos con IA",
    "Creación de contenido con IA (textos, videos)"
]

selected = st.multiselect("Selecciona tus habilidades actuales (puedes varias)", habilidades)

if st.button("Generar 5 ideas 💡") and selected:
    with st.spinner("Generando ideas monetizables..."):
        skills_text = ", ".join(selected)
        
        if client:
            try:
                response = client.chat.completions.create(
                    model="grok-beta",
                    messages=[{
                        "role": "user",
                        "content": f"Genera exactamente 5 ideas concretas y accionables de servicios freelance o productos digitales que una persona con estas habilidades puede vender YA para ganar sus primeros $1K: {skills_text}. "
                                   "Formato para cada idea: **Idea #X: Título** - Descripción corta - Plataforma recomendada - Precio sugerido (rango realista) - Por qué es viable ahora."
                    }],
                    max_tokens=800
                )
                ideas = response.choices[0].message.content.strip()
            except Exception as e:
                ideas = f"Error con Grok API: {e}. Usando ideas predefinidas sólidas."
        else:
            # Ideas predefinidas curadas (alta calidad, variadas y realistas 2026)
            ideas_db = {
                "Python básico": [
                    "**Idea 1: Automatización Excel/Google Sheets** - Scripts personalizados para empresas - Fiverr/Upwork - $50-200/gig - Demanda alta en oficinas.",
                    "**Idea 2: Bots simples Telegram/Discord** - Bots para comunidades - Gumroad - $20-80/producto - Venta pasiva fácil.",
                    "**Idea 3: Limpieza y análisis básico de datos** - Procesar CSV/Excel - Upwork - $100-300/proyecto - Clientes constantes."
                ],
                "Prompt engineering": [
                    "**Idea 1: Paquete de prompts optimizados** - 100 prompts por nicho (marketing, arte) - Gumroad - $19-49 - Producto digital pasivo.",
                    "**Idea 2: Consultoría prompts 1:1** - Sesiones Zoom para optimizar - Fiverr - $50-150/hora - Boom actual.",
                    "**Idea 3: Prompts personalizados para negocios** - Para ChatGPT/Gemini - Upwork - $100-400/proyecto - Alta conversión."
                ],
                "Fine-tuning de modelos": [
                    "**Idea 1: Modelos custom para chatbots** - Fine-tune Llama/Gemma para empresas - Upwork - $300-1000/proyecto - Demanda creciente.",
                    "**Idea 2: Datasets + fine-tune pack** - Para nichos específicos - Gumroad - $99-299 - Venta repetida."
                ],
                "Generación de imágenes (Stable Diffusion, Midjourney)": [
                    "**Idea 1: Arte custom / NFTs** - Imágenes personalizadas - Fiverr - $20-100/imagen - Mercado eterno.",
                    "**Idea 2: Pack de prompts + imágenes** - Para marketing/social - Gumroad - $29-79 - Pasivo total."
                ],
                # Más habilidades pueden añadirse fácil
            }
            
            # Generar 5 ideas mezclando las seleccionadas
            all_ideas = []
            for skill in selected:
                if skill in ideas_db:
                    all_ideas.extend(ideas_db[skill])
            # Complementar con genéricas si menos de 5
            generic = [
                "**Idea extra: Curso mini en video** - Sobre tus habilidades - Gumroad - $29-99 - Ingreso pasivo.",
                "**Idea extra: Plantillas reutilizables** - Scripts/prompts listos - Etsy/Gumroad - $15-50."
            ]
            all_ideas.extend(generic)
            
            ideas = "\n\n".join(random.sample(all_ideas, min(5, len(all_ideas))))

        st.markdown("### Tus 5 ideas para ganar $1K:")
        st.markdown(ideas)

else:
    if selected:
        st.info("Pulsa 'Generar 5 ideas' para ver opciones accionables.")
    else:
        st.warning("Selecciona al menos una habilidad.")

st.caption("App creada con ❤️ y Grok por @EsosPanas desde Venezuela. ¡Empieza a vender hoy!")    "Creación de contenido con IA (textos, videos)"
]

selected = st.multiselect("Selecciona tus habilidades actuales (múltiples OK)", habilidades)

if st.button("Generar 5 ideas 💡") and selected:
    with st.spinner("Generando ideas monetizables..."):
        skills_text = ", ".join(selected)
        
        if client:
            # Usar Grok API para ideas personalizadas
            try:
                response = client.chat.completions.create(
                    model="grok-beta",
                    messages=[{
                        "role": "user",
                        "content": f"Genera 5 ideas concretas y realistas de servicios freelance o productos digitales que una persona con estas habilidades puede vender YA para ganar sus primeros $1K: {skills_text}. "
                                   "Para cada idea incluye: nombre del gig/producto, descripción corta, plataforma recomendada (Fiverr, Upwork, Gumroad, Etsy), precio sugerido (rango realista) y por qué es viable."
                    }],
                    max_tokens=800
                )
                ideas = response.choices[0].message.content.strip()
                time.sleep(1)
            except:
                ideas = "Error con API. Usando ideas predefinidas."
        else:
            # Ideas predefinidas de alta calidad (curadas por mí)
            ideas_db = {
                "Python básico": [
                    "Automatización de tareas en Excel/Google Sheets con Python → Fiverr → $20-100/gig → Muy demandado por empresas.",
                    "Scripts simples para limpieza de datos → Upwork → $50-200 → Clientes constantes.",
                    "Bots de Telegram/Discord básicos → Gumroad → $10-50/producto → Venta pasiva.",
                    "Plantillas de código reutilizables → Gumroad → $15-40 → Bajo esfuerzo.",
                    "Tutoría Python para principiantes (1 hora) → Fiverr → $15-50/sesión."
                ],
                "Prompt engineering": [
                    "Creación de prompts personalizados para ChatGPT/Midjourney → Fiverr → $15-80/gig → Boom actual.",
                    "Paquete de 100 prompts optimizados por nicho → Gumroad → $19-49 → Venta pasiva.",
                    "Optimización de prompts para negocios → Upwork → $100-300/proyecto.",
                    "Curso mini de prompt engineering → Gumroad → $29-79.",
                    "Consultoría 1:1 de prompts → Fiverr → $50-150/sesión."
                ],
                # ... (puedo añadir más combinaciones, pero para simplicidad, el código combina aleatoriamente)
            }
            # Lógica simple: selecciona ideas de las habilidades + mezcla
            ideas = ""
            import random
            for skill in selected:
                if skill in ideas_db:
                    ideas += f"### Por {skill}:\n"
                    ideas += "\n".join(random.sample(ideas_db[skill], min(2, len(ideas_db[skill])))) + "\n\n"
            ideas += "### Ideas combinadas:\n- Servicio completo de chatbot con prompts + Python → Upwork → $300-1000\n- Pack de prompts + scripts → Gumroad → $49-99"

        st.markdown("### Tus 5 ideas para ganar $1K:")
        st.markdown(ideas if client else ideas)

else:
    if selected:
        st.info("Pulsa 'Generar 5 ideas' para ver opciones reales.")
    else:
        st.warning("Selecciona al menos una habilidad para generar ideas.")

st.caption("App creada con ❤️ y Grok por @EsosPanas desde Venezuela. ¡Tu primer $1K empieza aquí!")
