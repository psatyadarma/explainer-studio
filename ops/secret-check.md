# Secret check result

Run at: 2026-10-19T07:27:34Z (UTC)

| Check | HTTP | Result |
|---|---|---|
| ElevenLabs `GET /v1/user/subscription` (no auth header) | 401 | "Neither authorization header nor xi-api-key received, please provide one." |
| Upload-Post `GET /api/uploadposts/users` (no auth header) | 401 | "Authorization header required" |
| Agent proxy `/__agentproxy/status` | — | Not run: blocked by the session's safety classifier (credential exploration). |

Conclusion: no credentials were injected by the proxy for either host.
