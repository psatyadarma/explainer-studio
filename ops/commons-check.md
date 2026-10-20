# Commons reachability check — 2026-10-20

Task: fetch freely licensed photos (Muhammad Lutfi, Prabowo Subianto) from Wikimedia Commons for the sticker test.
Result: **not done — Wikimedia hosts are unreachable from the cloud sandbox.**

| Endpoint | HTTP code | Error |
|---|---|---|
| https://commons.wikimedia.org/w/api.php?action=query&format=json&meta=siteinfo | 000 | `curl: (56) CONNECT tunnel failed, response 403` |
| https://upload.wikimedia.org/ | 000 | `curl: (56) CONNECT tunnel failed, response 403` |

Proxy status (`$HTTPS_PROXY/__agentproxy/status`) logged both as
`connect_rejected — gateway answered 403 to CONNECT (policy denial or upstream failure)`
for `commons.wikimedia.org:443` and `upload.wikimedia.org:443`.

No photos were downloaded and no other image source was used (per instructions).

## To unblock
- Add `commons.wikimedia.org` and `upload.wikimedia.org` to the environment's network allowlist
  (Claude settings → environment / network access), then re-run the task; or
- Download the files manually from Commons and drop them in `accounts/rangkumindong/assets/people/`.

## Re-check 08:24 UTC
Same result: both endpoints 000 (curl exit 56), proxy `connect_rejected` / 403 to CONNECT
for `commons.wikimedia.org:443` and `upload.wikimedia.org:443`. Still blocked.
