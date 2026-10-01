# Club Esperanza: panel y automatización de WhatsApp

Actualización técnica: 30 de septiembre de 2026.

El proyecto combina campañas de Meta Ads, un panel Next.js con MongoDB y el asistente Clara en n8n. El panel incorpora un control administrativo para activar o pausar las respuestas sin desconectar WhatsApp.

La configuración revisada contiene deduplicación por identificador de mensaje, consulta del estado antes de la IA, hasta tres intentos en el nodo de Gemini y un filtro de origen publicitario antes de registrar leads. La deduplicación conserva un historial limitado; no se presenta como garantía absoluta de entrega única.

La pausa afecta a mensajes que aún no han superado la consulta de estado. Las ejecuciones que ya la superaron pueden terminar. El filtro publicitario está en n8n, no en el endpoint de registro; los mensajes manuales no deben crear leads siguiendo ese recorrido.

La guía operativa completa se mantiene en `docs/clara-n8n.md` del repositorio del panel. Incluye configuración, límites y pruebas pendientes. No publicar credenciales, direcciones privadas del editor, teléfonos, conversaciones ni exportaciones de ejecuciones.

Esta revisión no añade métricas de campaña ni certifica una prueba de entrega real. Las cifras del caso de estudio conservan su corte histórico del 22 de septiembre de 2026.
