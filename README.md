# Signed, Sealed, Delivered (SSD)

A cryptographic document signing and verification tool that runs entirely in the browser. No server, no accounts, no cloud.

## Current State

All core phases complete (v36). The app covers the full Sign → Seal → Deliver workflow.

- **Passkey registration** — WebAuthn with PRF extension for keyring encryption
- **Ed25519 keypair generation** — keys stored in IndexedDB with AES-256-GCM-encrypted private keys
- **Identicon rendering** — deterministic 5×5 pixel grid (`ssd-identicon-1.0`) from SHA-256 of public key
- **Key card export** — self-signed JSON, verifiable without the app
- **Drafts** — compose and save documents before signing
- **Document signing** — compose → canonical render → explicit biometric confirmation → `.sealed` artifact
- **Seal / Reseal** — seal signed documents; re-seal encrypted documents after decryption
- **Deliver** — send sealed artifacts directly from the Documents list
- **Verification** — drag-and-drop `.sealed` files, checks hashes and Ed25519 signature
- **Contact keyring** — import contacts via QR or paste, quarantine management
- **Encryption** — encrypt artifacts to one or more recipients by public key
- **PWA** — installs offline, service worker caches shell

## Running

Served from GitHub Pages. To run locally — no build step, just serve over HTTP/HTTPS:

```
py -m http.server 8080
```

Then open `http://localhost:8080`. **WebAuthn requires localhost or HTTPS** — opening `index.html` as a `file://` URL will not work.

## File Structure

```
index.html          — entire application (HTML + CSS + JS)
manifest.json       — PWA manifest
service-worker.js   — cache-first shell, network-first CDN
favicon.ico
icon-192.png
icon-512.png
generate-icons.py   — run once to regenerate icons if needed
docs/               — specification
```

## Artifact Format (`.sealed`)

A ZIP containing:
- `manifest.json` — metadata, render spec, SHA-256 hashes of source and render
- `source.txt`    — canonical wrapped document text
- `render.txt`    — source + signature attestation block
- `signature.json` — Ed25519 signature over `manifest.json` bytes

## Architecture

All JavaScript lives in `index.html` as named const objects:
`db` · `opfsStore` · `cryptoOps` · `passkey` · `keyring` · `signer` · `artifact` · `identicon` · `ui` · `app`

All cryptography uses the native WebCrypto API. All storage is IndexedDB (metadata) + OPFS (artifact blobs). Nothing sensitive is stored unencrypted or in localStorage.

## Phase Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| 1 | Core loop — sign, verify, key management | ✅ Complete |
| 2 | Key exchange — QR codes, paste import, contact keyring | ✅ Complete |
| 3 | Encryption — per-recipient encrypted artifacts | ✅ Complete |
| 4 | Integration — contacts system links, countersignatures | Planned |

## Browser Requirements

- Chrome 113+ / Edge 113+
- Firefox 130+
- Safari 17+

Ed25519 and WebAuthn PRF are required for full functionality.
