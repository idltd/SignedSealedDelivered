# Signed, Sealed, Delivered (SSD)

A cryptographic document signing and verification tool that runs entirely in the browser. No server, no accounts, no cloud.

## Current State

v39 — core workflow complete, sync machinery removed in favour of the sealed-document transfer model.

## How It Works

### Identities and devices

Each browser instance is an independent identity. A user sets up each device separately — passkey registration, then a named signing keypair. There is no cross-device sync; instead, private material travels as sealed documents.

**Recipient hierarchy when sealing a document:**
1. **Self** — your own encryption key (keep a private copy)
2. **Own devices** — other devices you own, added as contacts by scanning their key card QR
3. **Contacts** — other people whose key cards you have imported

### Key exchange

You share your public key card as a QR code or exported JSON. Anyone who scans it can verify your signatures and seal documents addressed to you. There is no trust authority — you decide whose keys to import.

### Cross-device key transfer

To copy a signing key to another device:
1. On the receiving device, go to Keyring → Show QR and add it as a contact on the sending device
2. On the sending device, create a document containing the private key, seal it addressed to the receiving device, and deliver it
3. On the receiving device, open the sealed document and import the key

This uses the same sealed-document format as everything else. No special sync protocol.

### Backup

Seal a copy of your private key addressed to yourself. Store the `.sealed` file somewhere safe. To restore on a new device, set up a fresh instance, add the backed-up key card as a contact, then open the sealed backup.

## Features

- **Passkey registration** — WebAuthn with PRF extension for keyring encryption
- **Ed25519 keypairs** — named signing identities, stored encrypted in IndexedDB
- **Key card** — self-signed JSON exportable as QR or file; verifiable without the app
- **Drafts** — compose and save documents before signing
- **Sign** — compose → canonical render → biometric confirmation → `.sealed` artifact
- **Seal / Reseal** — encrypt artifacts to one or more recipients by public key
- **Deliver** — send sealed artifacts from the Documents list
- **Verify** — drag-and-drop `.sealed` files; checks hashes and Ed25519 signature
- **Contacts** — import key cards via QR scan or paste; quarantine management
- **Device name** — shown in your key card QR so contacts can identify which device a key came from
- **Identicons** — deterministic 5×5 pixel grid from SHA-256 of public key
- **PWA** — installs offline, service worker caches shell

## Running

Served from GitHub Pages. To run locally — no build step, just serve over HTTP/HTTPS:

```
py -m http.server 8080
```

Open `http://localhost:8080`. **WebAuthn requires localhost or HTTPS** — `file://` URLs will not work.

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
- `manifest.json`  — metadata, render spec, SHA-256 hashes of source and render
- `source.txt`     — canonical wrapped document text
- `render.txt`     — source + signature attestation block
- `signature.json` — Ed25519 signature over `manifest.json` bytes

Encrypted artifacts add an outer envelope with per-recipient X25519 key encapsulation.

## Architecture

All JavaScript lives in `index.html` as named const objects:
`db` · `opfsStore` · `cryptoOps` · `passkey` · `keyring` · `signer` · `artifact` · `identicon` · `ui` · `app`

All cryptography uses the native WebCrypto API. Storage is IndexedDB (metadata) + OPFS (artifact blobs). Nothing sensitive is stored unencrypted or in localStorage.

## Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| 1 | Core loop — sign, verify, key management | ✅ Complete |
| 2 | Key exchange — QR codes, paste import, contact keyring | ✅ Complete |
| 3 | Encryption — per-recipient encrypted artifacts | ✅ Complete |
| 4 | Backup/restore — sealed document format for private key transfer | Planned |
| 5 | New document types — contacts export, key bundles | Planned |

## Browser Requirements

- Chrome 113+ / Edge 113+
- Firefox 130+
- Safari 17+

Ed25519 and WebAuthn PRF are required for full functionality.
