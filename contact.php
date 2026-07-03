<?php
header('Content-Type: application/json; charset=UTF-8');

// ---------- Helpers ----------
function respond($code, $ok, $ui_message, $extra = []) {
  http_response_code($code);
  echo json_encode(array_merge([
    'ok' => $ok,
    'ui_message' => $ui_message
  ], $extra));
  exit;
}

function clean_header_value($value) {
  // Previene header injection
  return trim(str_replace(["\r", "\n"], ' ', $value));
}

function get_client_ip() {
  // Hostgator normalmente usa REMOTE_ADDR
  return $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0';
}

// ---------- Allow GET (healthcheck) ----------
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
  respond(200, true, 'OK');
}

// ---------- Only POST ----------
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
  respond(405, false, 'Método no permitido');
}

// ---------- Honeypot ----------
if (!empty($_POST['company'])) {
  respond(403, false, 'Acceso denegado');
}

// ---------- Inputs ----------
$ip       = get_client_ip();
$nombre   = trim($_POST['full-name'] ?? '');
$email    = trim($_POST['email'] ?? '');
$telefono = trim($_POST['phone'] ?? '');
$asunto   = trim($_POST['topic'] ?? '');
$mensaje  = trim($_POST['msg'] ?? '');

if ($nombre === '' || $email === '' || $mensaje === '') {
  respond(400, false, 'Completa los campos obligatorios.');
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  respond(400, false, 'Email inválido.');
}

// ---------- Rate limit (por IP + email, no bloquea a otras personas en la misma red) ----------
$rateDir = __DIR__ . '/leads';
if (!is_dir($rateDir)) {
  // Intenta crearla (o créala tú desde cPanel)
  @mkdir($rateDir, 0755, true);
}

$rateKey = $ip . '|' . mb_strtolower($email);
$rateFile = $rateDir . '/rate_' . preg_replace('/[^a-zA-Z0-9_\-\.]/', '_', md5($rateKey)) . '.txt';
$now = time();
$cooldownSeconds = 20; // 1 envío cada 20s por IP+email

if (file_exists($rateFile)) {
  $last = (int) @file_get_contents($rateFile);
  if ($last && ($now - $last) < $cooldownSeconds) {
    respond(429, false, 'Demasiados intentos. Intenta en unos segundos.');
  }
}
@file_put_contents($rateFile, (string)$now, LOCK_EX);

// Limpieza anti header injection
$nombre_safe = clean_header_value($nombre);
$email_safe  = clean_header_value($email);
$tel_safe    = clean_header_value($telefono);
$asunto_safe = clean_header_value($asunto);

// ---------- Clasificación (tags) ----------
$topicLower = mb_strtolower($asunto_safe);
$tag = 'GENERAL';

if (str_contains($topicLower, 'web') || str_contains($topicLower, 'landing')) $tag = 'WEB';
if (str_contains($topicLower, 'tienda') || str_contains($topicLower, 'ecommerce') || str_contains($topicLower, 'shop')) $tag = 'ECOM';
if (str_contains($topicLower, 'seo') || str_contains($topicLower, 'marketing')) $tag = 'MKT';
if (str_contains($topicLower, 'soporte') || str_contains($topicLower, 'error')) $tag = 'SOPORTE';

$subjectFinal = "[$tag] Formulario Web: " . ($asunto_safe !== '' ? $asunto_safe : 'Sin asunto');

// ---------- Guardar lead a CSV (backup CRM) ----------
$csvPath = $rateDir . '/leads.csv';
$csvRow = [
  date('Y-m-d H:i:s'),
  $ip,
  $tag,
  $nombre_safe,
  $email_safe,
  $tel_safe,
  $asunto_safe,
  $mensaje
];

$fp = @fopen($csvPath, 'a');
if ($fp) {
  // Si está vacío, escribe headers
  if (filesize($csvPath) === 0) {
    fputcsv($fp, ['fecha', 'ip', 'tag', 'nombre', 'email', 'telefono', 'asunto', 'mensaje']);
  }
  fputcsv($fp, $csvRow);
  fclose($fp);
}

// ---------- Email HTML (bonito) ----------
$to = 'soporte@andyrosado.com';
$from = 'soporte@andyrosado.com';
$fromName = 'Andy Rosado Web';

// Escapes para HTML
$h = fn($v) => htmlspecialchars($v ?? '', ENT_QUOTES, 'UTF-8');

$htmlBody = '
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Nuevo contacto</title>
  </head>
  <body style="margin:0;padding:0;background:#0b1220;font-family:Arial,Helvetica,sans-serif;">
    <div style="max-width:680px;margin:0 auto;padding:24px;">
      <div style="background:#0f172a;border:1px solid rgba(255,255,255,.08);border-radius:14px;overflow:hidden;">
        <div style="padding:18px 20px;background:linear-gradient(90deg,#0ea5e9,#22c55e);color:#02131a;">
          <div style="font-size:14px;opacity:.9;">Nuevo mensaje desde andyrosado.com</div>
          <div style="font-size:22px;font-weight:700;">' . $h($subjectFinal) . '</div>
        </div>

        <div style="padding:18px 20px;color:#e5e7eb;">
          <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);width:140px;color:#93c5fd;">Nombre</td>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);">' . $h($nombre_safe) . '</td>
            </tr>
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);color:#93c5fd;">Email</td>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);">
                <a href="mailto:' . $h($email_safe) . '" style="color:#7dd3fc;text-decoration:none;">' . $h($email_safe) . '</a>
              </td>
            </tr>
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);color:#93c5fd;">Teléfono</td>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);">' . $h($tel_safe) . '</td>
            </tr>
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);color:#93c5fd;">Etiqueta</td>
              <td style="padding:10px 0;border-bottom:1px solid rgba(255,255,255,.08);">' . $h($tag) . '</td>
            </tr>
          </table>

          <div style="margin-top:16px;padding:14px;border-radius:12px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);">
            <div style="font-size:13px;color:#93c5fd;margin-bottom:8px;">Mensaje</div>
            <div style="white-space:pre-wrap;line-height:1.5;color:#f1f5f9;">' . $h($mensaje) . '</div>
          </div>

          <div style="margin-top:16px;font-size:12px;color:#94a3b8;">
            IP: ' . $h($ip) . ' • ' . $h(date('Y-m-d H:i:s')) . '
          </div>
        </div>
      </div>

      <div style="text-align:center;color:#64748b;font-size:12px;margin-top:16px;">
        Andy Rosado Web • Formulario de contacto
      </div>
    </div>
  </body>
</html>';

$textBody =
"Nuevo mensaje desde andyrosado.com\n\n" .
"Asunto: $subjectFinal\n" .
"Nombre: $nombre_safe\n" .
"Email: $email_safe\n" .
"Teléfono: $tel_safe\n" .
"Etiqueta: $tag\n" .
"IP: $ip\n\n" .
"Mensaje:\n$mensaje\n";

// Headers HTML
$headers  = "From: " . clean_header_value($fromName) . " <" . clean_header_value($from) . ">\r\n";
$headers .= "Reply-To: " . $email_safe . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

// ---------- Enviar a ti ----------
$sentToOwner = @mail($to, $subjectFinal, $htmlBody, $headers);

// ---------- Auto-respuesta al usuario (texto simple) ----------
$autoSubject = "Recibimos tu mensaje ✅ (Andy Rosado Web)";
$autoBody =
"Hola $nombre_safe,\n\n" .
"¡Gracias por escribirme! Recibí tu mensaje y te responderé lo antes posible.\n\n" .
"Resumen:\n" .
"Asunto: " . ($asunto_safe !== '' ? $asunto_safe : 'Sin asunto') . "\n" .
"Mensaje: " . $mensaje . "\n\n" .
"— Andy Rosado\n" .
"andyrosado.com\n";

$autoHeaders  = "From: Andy Rosado Web <" . clean_header_value($from) . ">\r\n";
$autoHeaders .= "Reply-To: " . clean_header_value($from) . "\r\n";
$autoHeaders .= "Content-Type: text/plain; charset=UTF-8\r\n";
$autoHeaders .= "X-Mailer: PHP/" . phpversion() . "\r\n";

$sentToUser = @mail($email_safe, $autoSubject, $autoBody, $autoHeaders);

if ($sentToOwner) {
  respond(200, true, 'Mensaje enviado correctamente 🚀', [
    'tag' => $tag,
    'sent_autoresponse' => $sentToUser ? true : false
  ]);
}

respond(500, false, 'No se pudo enviar el mensaje ❌');
