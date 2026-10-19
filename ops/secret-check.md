# Secret check result

- Checked at (UTC): 2026-10-19T08:53:58Z
- ElevenLabs `GET /v1/user/subscription` (no auth header): HTTP 401 — "Neither authorization header nor xi-api-key received, please provide one."
- Upload-Post `GET /api/uploadposts/users` (no auth header): HTTP 401 — "Authorization header required"

Conclusion: the proxy did not inject credentials for either host.
