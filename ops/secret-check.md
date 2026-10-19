# Secret check result

Run at: 2026-10-19T07:22:35Z (UTC), one-off scheduled task in the cloud environment.

| Check | HTTP code | Result |
|---|---|---|
| ElevenLabs `GET /v1/user/subscription` (no auth header) | 401 | `needs_authorization`, so no key was injected by the proxy |
| Upload-Post `GET /api/uploadposts/users` (no auth header) | 401 | "Authorization header required", so no key was injected by the proxy |

Conclusion: the network proxy did not attach credentials for either API on this run.
