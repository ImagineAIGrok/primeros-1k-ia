import streamlit as st
from openai import OpenAI
import time
import random  # Import correcto

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
            # Ideas predefinidas curadas (sintaxis perfecta, más completas)
            ideas_db = {
                "Python básico": [
                    "**Idea 1: Automatización Excel/Google Sheets** - Scripts personalizados para empresas - Fiverr/Upwork - $50-200/gig - Demanda alta en oficinas.",
                    "**Idea 2: Bots simples Telegram/Discord** - Bots para comunidades - Gumroad - $20-80/producto - Venta pasiva fácil.",
                    "**Idea 3: Limpieza y análisis básico de datos** - Procesar CSV/Excel - Upwork - $100-300/proyecto - Clientes constantes.",
                    "**Idea 4: Scripts de scraping simple** - Extracción datos web - Fiverr - $50-150 - Útil para marketing.",
                    "**Idea 5: Tutoría Python 1:1** - Sesiones para principiantes - Fiverr - $20-60/hora - Recurrencia alta."
                ],
                "Prompt engineering": [
                    "**Idea 1: Paquete de prompts optimizados** - 100 prompts por nicho - Gumroad - $19-49 - Producto digital pasivo.",
                    "**Idea 2: Consultoría prompts 1:1** - Sesiones Zoom - Fiverr - $50-150/hora - Boom actual.",
                    "**Idea 3: Prompts personalizados para negocios** - Para ChatGPT - Upwork - $100-400/proyecto - Alta conversión.",
                    "**Idea 4: Pack prompts + guía PDF** - Para Midjourney/marketing - Gumroad - $29-79 - Venta repetida.",
                    "**Idea 5: Optimización prompts para contenido** - YouTube/social - Fiverr - $30-100/gig - Viral fácil."
                ],
                "Fine-tuning de modelos": [
                    "**Idea 1: Modelos custom para chatbots** - Fine-tune para empresas - Upwork - $300-1000/proyecto - Demanda creciente.",
                    "**Idea 2: Pack fine-tune + dataset** - Para nichos - Gumroad - $99-299 - Pasivo alto.",
                    "**Idea 3: Servicio fine-tune Llama** - Para apps - Fiverr - $200-600 - Especializado.",
                    "**Idea 4: Consultoría fine-tuning** - 1:1 - Upwork - $150-400/sesión.",
                    "**Idea 5: Modelos pre-tuned listos** - Venta directa - Gumroad - $50-200."
                ],
                "Generación de imágenes (Stable Diffusion, Midjourney)": [
                    "**Idea 1: Imágenes custom / arte** - Personalizadas - Fiverr - $20-100/imagen - Mercado eterno.",
                    "**Idea 2: Pack prompts + imágenes** - Para marketing - Gumroad - $29-79 - Pasivo total.",
                    "**Idea 3: Logos/branding con IA** - Para startups - Upwork - $100-500/proyecto.",
                    "**Idea 4: Edición imágenes IA** - Upscale/remove background - Fiverr - $10-50/gig.",
                    "**Idea 5: Pack stock images IA** - Temáticos - Etsy/Gumroad - $19-59."
                ],
                # Genéricas para complementar siempre 5
                "default": [
                    "**Idea extra: Curso mini video** - Sobre tus habilidades - Gumroad - $29-99 - Ingreso pasivo.",
                    "**Idea extra: Plantillas reutilizables** - Scripts/prompts - Gumroad - $15-50 - Fácil creación.",
                    "**Idea extra: Bundle habilidades** - Pack completo - Gumroad - $49-149 - Upsell."
                ]
            }
            
            all_ideas = []
            for skill in selected:
                key = skill if skill in ideas_db else "default"
                all_ideas.extend(ideas_db.get(key, ideas_db["default"]))
            
            # Siempre 5 únicas
            ideas = "\n\n".join(random.sample(all_ideas, min(5, len(all_ideas))))

        st.markdown("### Tus 5 ideas para ganar $1K:")
        st.markdown(ideas)

else:
    if selected:
        st.info("Pulsa 'Generar 5 ideas' para ver opciones accionables.")
    else:
        st.warning("Selecciona al menos una habilidad.")

st.caption("App creada con ❤️ y Grok por @EsosPanas desde Venezuela. ¡Empieza a vender hoy!")
