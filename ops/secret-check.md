# Secret check result

Run (UTC): 2026-10-19T07:22:57Z

Requests were sent without any auth header, to test whether the cloud environment's proxy injects the secrets.

| Endpoint | HTTP code | Result |
|---|---|---|
| `GET https://api.elevenlabs.io/v1/user/subscription` | 401 | Unauthorized: no key injected; no fields recorded |
| `GET https://api.upload-post.com/api/uploadposts/users` | 401 | Unauthorized: no key injected; no usernames recorded |

Conclusion: neither secret was applied to outbound requests in this environment.
