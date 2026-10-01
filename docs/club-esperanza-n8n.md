# Club Esperanza: panel y automatización de WhatsApp

Actualización técnica: 30 de septiembre de 2026.

El proyecto combina campañas de Meta Ads, un panel Next.js con MongoDB y el asistente Clara en n8n. El panel incorpora un control administrativo para activar o pausar las respuestas sin desconectar WhatsApp.

La configuración revisada contiene deduplicación por identificador de mensaje, consulta del estado antes de la IA, hasta tres intentos en el nodo de Gemini y un filtro de origen publicitario antes de registrar leads. La deduplicación conserva un historial limitado; no se presenta como garantía absoluta de entrega única.

La pausa afecta a mensajes que aún no han superado la consulta de estado. Las ejecuciones que ya la superaron pueden terminar. El filtro publicitario está en n8n, no en el endpoint de registro; los mensajes manuales no deben crear leads siguiendo ese recorrido.

La guía operativa completa se mantiene en `docs/clara-n8n.md` del repositorio del panel. Incluye configuración, límites y pruebas pendientes. No publicar credenciales, direcciones privadas del editor, teléfonos, conversaciones ni exportaciones de ejecuciones.

Esta revisión no añade métricas de campaña ni certifica una prueba de entrega real. Las cifras del caso de estudio conservan su corte histórico del 22 de septiembre de 2026.

## Registro consolidado de entregables

1. Gestión de campaña de Meta Ads: creativos, segmentación, pruebas y optimización.
2. Meta Pixel, Conversions API y atribución por referencia publicitaria.
3. Panel Next.js/MongoDB con métricas, leads y sincronización de Ads Insights.
4. Activos comerciales y app de mensajería de Meta; app publicada y permisos aprobados.
5. Embedded Signup y coexistencia de WhatsApp Business con Cloud API para el cliente.
6. Workflow de Clara en n8n con webhook, memoria, IA, deduplicación y reintentos.
7. Envío corregido para conservar el teléfono desde el mensaje original.
8. Filtro de leads provenientes de anuncios y prevención de registros manuales malformados.
9. Control administrativo para activar o pausar a Clara sin desactivar el workflow.
10. Documentación operativa y definición del servicio para implementaciones futuras.

Este inventario distingue entregables técnicos de resultados comerciales. El caso público solo usa métricas históricas verificadas y no publica credenciales, datos de contactos ni exportaciones privadas del workflow.

## Visualización pública

El caso de estudio incrusta `image/club-esperanza-n8n-flow.svg`, un diagrama derivado de la configuración activa revisada. Representa el flujo principal, las bifurcaciones, el modelo, la memoria y la rama de verificación de Meta. Es deliberadamente una versión saneada: no debe sustituirse por una exportación de n8n ni por una captura que muestre credenciales, URLs privadas, números o datos de ejecuciones.

## Evidencias de revisión de Meta

Se revisaron cuatro grabaciones WebM suministradas por el propietario:

- Dos demostraciones de `whatsapp_business_messaging`, con workflow, envío de prueba y ejecución de n8n.
- Una demostración de `whatsapp_business_management`, con selección del activo, descripción del uso y llamada de prueba.
- Una grabación de la prueba de coexistencia y mensajería en WhatsApp Web.

Los originales no se publican porque muestran números, contactos y conversaciones. El caso usa cuatro evidencias públicas saneadas: `club-esperanza-proof-meta-app.png`, `club-esperanza-proof-n8n.webp`, `club-esperanza-proof-whatsapp.webp` y `club-esperanza-proof-permission.webp`. La captura de la App conserva su nombre y la estructura general de Meta Business, pero oculta el identificador, propietario y cuentas asignadas. Esta selección demuestra la configuración de la App, la ejecución, el envío y la preparación de la revisión sin divulgar datos de terceros. La aprobación final se verificó por separado en Meta for Developers el 30 de septiembre de 2026.
