# Signed, Sealed, Delivered — Concepts & Vocabulary Brief

## Purpose of This Document

This is a design and vocabulary brief for the **Signed, Sealed, Delivered** app and its broader ecosystem. It covers the core cryptographic concepts, the vocabulary to communicate them to different user audiences, and the wider vision the app sits within. Feed this into any development or design session to ensure consistent language and intent.

---

## The Core Application

A document signing and encryption app. Users create key pairs to:

- **Sign** documents they create, proving authorship and integrity
- **Seal** documents for specific recipients, encrypted so only they can open it
- **Deliver** documents with provable receipt confirmation

The app is called **Signed, Sealed, Delivered** — and those three words map directly onto the three core actions.

---

## The Cryptographic Reality (for developers)

- Each user generates a **key pair** — a private key (never shared) and a public key (shared freely)
- **Signing** uses the sender's private key — anyone with their public key can verify the signature
- **Sealing** uses an **ephemeral key** to encrypt the document, then encrypts that ephemeral key with the recipient's public key — only the recipient can unlock the ephemeral key and therefore the document
- A sealed document for multiple recipients means **one sealed copy per recipient** — each sealed individually with their own public key
- Double signing is expected: an **outer signature** (proves who sent this package) and an **inner signature** (proves the content is intact and unmodified)
- There is a planned **key request mode**: the encrypted document arrives, but the ephemeral key is held back until the recipient actively requests it — making the request itself a cryptographic proof of receipt

---

## Core Vocabulary

### The Three Actions

| Term | Meaning | Notes |
|---|---|---|
| **Sign** | I validate this content — it came from me and hasn't changed | Applies to both authored and vouched content |
| **Seal** | Encrypted individually for a specific recipient — only they can open it | One seal per recipient, even for the same document |
| **Deliver** | Confirmed receipt — document arrived, unsealed, and verified | The full circle is closed |

### Document States

A document moves through clear states:

- **Draft** — not yet signed
- **Signed** — provably from the signer, anyone can verify, not encrypted
- **Sealed** — signed and encrypted for named recipient(s)
- **Delivered** — received, unsealed, and content verified by recipient
- **Held** — sealed and arrived, but key withheld pending recipient's request (key request mode)

### Signed But Not Sealed

An important distinct state — a document can be **signed but not sealed**. This means:
- Publicly readable by anyone
- But provably from the signer — unforgeable
- Useful for public publishing with attribution

Call this: **Open & Signed**

---

## Keys — What They Are and What They Aren't

### The Key Principle

> **A key is a tool you hold, not a flag you plant.**

A key does not inherently claim identity. It proves:
- **Consistency** — the same key signed these things
- **Integrity** — the content hasn't changed since signing

It does **not** prove who holds the key in the physical world. That link to a human is a choice, not a requirement.

### The Key as Address, Not Identity

Preferred framing: *"Here is a key you can use to send content to me"* — not *"Here is my key, it represents me."*

The key is more like a **PO Box** than a passport. It tells you where to send things and that someone consistent collects from there. Who lives there is their own business.

### Multiple Keys Are Normal

One person may legitimately hold many keys for different contexts:

- A professional key — fully attributed, used for work
- A community key — pseudonymous, known in certain circles
- A private key — anonymous, for sensitive contexts

None of these are fake. Compartmentalisation is a legitimate human need.

### Shared Keys

Multiple trusted people can share a single key — creating a **collective identity**. This is:
- Technically legitimate — the key is the identity, full stop
- Historically precedented — collective pseudonyms (Luther Blissett, Bourbaki, Wu Ming)
- A genuine plausible deniability mechanism — if several people hold a key, attribution is honestly impossible
- Suitable for editorial boards, activist groups, journalist collectives

The system should **never assume one key = one person**.

---

## The Identity Spectrum

Users fall into two broad bases with the same underlying infrastructure:

| Base | Approach | Key represents |
|---|---|---|
| **Identity users** | Want to be known, choose when to reveal | A person, by their choice |
| **Privacy users** | Don't need or want attribution | A handle, full stop |

Both are valid. Both use identical infrastructure. The difference is what the user chooses to attach to their key — and that choice remains theirs, always, and can change.

### The Spectrum of Attribution

| Level | What it means |
|---|---|
| **Anonymous** | Key exists, nothing attached |
| **Pseudonymous** | Key has a name/handle, not traceable to a person |
| **Partially attributed** | Key linked to verifiable facts but not name (e.g. "a UK resident", "a doctor") |
| **Fully attributed** | Key publicly linked to real identity — user's explicit choice |

All levels can sign. All signatures are cryptographically equal. The trust weight given to them is the reader's decision.

### Pen Names and Bylines

For communicating the identity spectrum to users without technical language:

- **Byline** — authorship claim, reputation stake, transferable between publications, searchable history. Maps directly to a signing key.
- **Pen name** — consistent identity without personal revelation, legitimate and culturally accepted, a reputation in its own right. Maps directly to a pseudonymous key.

*"Your key is your byline. It can be your real name, a pen name, or just an address. That's your choice, always."*

---

## The Vouching System (Broader Ecosystem)

### What Vouching Is

Signing extends beyond authorship to **vouching** — signing content you didn't create, meaning:

> *"I don't think this will be a waste of your time."*

This is a deliberately low bar. Not endorsement, not agreement — just a signal that the content is legitimate and worth attention. By signing it, you create your own version — you own having put your name on it.

### Why It Works Against Spam and Bots

Bots can create infinite identities. They cannot get real people to vouch for them at scale without cost. The filter isn't *"is this from a real person"* but *"did someone I trust think this was worth passing on."* Much harder to game.

### The Trust Graph

Each user builds a personal trust graph:
- A small number of people trusted explicitly
- Their signed content rises in the feed
- Their vouches extend trust further
- Bad vouches cost reputation — the social cost is real

The trust graph is **your algorithm** — transparent, portable, auditable, and yours. Not the platform's.

### Curators

A **curator** is any key with a public record of what it has vouched for and a stated set of principles about what it will and won't pass. Curators are accountable in a way algorithms never are — they have a key, a signature, a track record.

Anyone can review a curator's history before trusting them. If they deliver content you don't want — they get one chance. Drop them silently and their content sinks back into the noise.

### The Filter Model

The trust filter should **prioritise, not block** by default:
- Vouched content rises
- Unvouched content doesn't disappear — it just loses
- Spam dies not because it's detected but because nobody will sign it
- New voices can still be discovered by those open to it

Blocking is available — shared block lists work on identical infrastructure to trust lists, opposite polarity.

### The Cold Start Problem

New keys have no history. Solutions:
- **Patron model** — an established key explicitly provisionally vouches for a new person. The patron's reputation is mildly on the line.
- **Unsigned space** — unvouched content doesn't disappear, just deprioritises naturally
- **Provisional marking** — new keys are marked as new, readers can choose to include them

---

## Vocabulary by Audience

The mechanism is identical for all users. The story changes.

### Tracy (casual user — just wants less spam)

No keys, no cryptography. Just:

- **Trusted** — from someone she knows or chose
- **Recommended** — passed through someone she trusts
- **New** — no history yet, could be interesting
- **Unknown** — nobody vouched, her judgement
- *Quiet* — unvouched content, still there, not shouting

Pitch: *"Only see messages from people you trust. Friends' recommendations first. No adverts."*

### Media Consumer (wants trustworthy content)

- **Byline** — follow the writer, not the masthead
- **Track record** — the key's history of vouches
- **Vouched** — someone with a track record passed this on
- **Curator** — a trusted filter for a specific topic or domain

Pitch: *"Follow the byline, not the masthead. A journalist's track record is theirs — it travels with them."*

### Journalist / Creator (wants audience ownership)

- **Your byline** — your key, your track record, permanently yours
- **Signed** — provably yours, unforgeable
- **Portable** — your audience trusts your key, not the platform
- **Back catalogue** — your signed history

Pitch: *"Your reputation is yours. It doesn't belong to the platform that employs you."*

### Privacy-Conscious User

- **Pen name** — a legitimate pseudonymous identity with its own reputation
- **Handle** — where to reach you, nothing more
- **Compartment** — different keys for different contexts

Pitch: *"Your key is a pen name. Your identity is your business."*

### Technical User

Key pairs, asymmetric encryption, ephemeral symmetric keys, signed metadata, trust graphs — the full model. Available but never required reading for other audiences.

---

## The Gaming Vocabulary Layer (cross-audience, casual)

For the trust/vouch system specifically, gaming vocabulary maps cleanly and is widely understood:

| Technical concept | Gaming vocabulary |
|---|---|
| Positive vouch | **Buff** |
| Anti-vouch / flag | **Debuff** |
| Highly trusted, long track record | **Legendary** |
| Verified in person, physically exchanged keys | **Legend** |
| New key, no history | **No stats yet** |
| Removed from trust list | **Nerfed** |
| Confirmed spam / malicious | **Cursed** |

**Buff of a Friend** (BoaF) — content that reached you through a chain of trusted vouches.

This vocabulary is appropriate for casual user interfaces, notifications, and onboarding. It sits alongside the formal vocabulary, not replacing it.

---

## The Trust Hierarchy

| Level | Basis | Vocabulary |
|---|---|---|
| Verified in person — physical key exchange | Strongest possible signal | **Legend** |
| Known, long track record | Established trust | **Trusted** |
| Vouched by someone trusted | Indirect trust | **Buffed** |
| Unknown, no history | No signal | **Unknown** |
| Flagged by someone trusted | Indirect distrust | **Debuffed** |
| Confirmed spam / malicious | Clear record | **Cursed** |

---

## Publication and Authorship Model

Individual author keys interlink with publication keys through counter-signing. This means:

- A journalist's track record is **theirs**, not the publication's
- If they leave, they take their signed history with them
- The publication retains only the trust it independently earned
- Readers who trusted a byline can follow the key, not the masthead
- A group of journalists departing together bring their entire cross-vouching network

This is a significant shift in the power dynamic between institutions and individuals. Credibility becomes accurately portable.

---

## Key Design Principles

1. **Never ask for more than the question requires.** Verification should answer the actual question, not harvest maximally identifying data under cover of it.

2. **The key is a tool you hold, not a flag you plant.** Never assume one key = one person.

3. **Privacy by architecture, not policy.** Build so the system could be private. Don't build so it has to be identified.

4. **The filter is gravity, not a wall.** Unvouched content sinks. It doesn't get blocked.

5. **Every vouch is auditable.** The voucher's name is on it. That's the deal.

6. **Trust is earned continuously, not inherited.** A publication cannot borrow a journalist's credibility after they leave.

7. **Revocation is private by default.** Remove from your trust list silently. Public revocation is an option, not a requirement.

8. **One strike.** A curator who delivers content you don't trust gets dropped. No appeals.

9. **The platform is a dumb pipe.** Curation happens in the user's trust layer, not the platform's algorithm.

10. **No wrong door.** Whatever problem a user arrives with — spam, trust, privacy, authorship — the same infrastructure solves it. Just differently described.

---

## Launch Strategy Notes

Demonstrate the value at both poles simultaneously:

- **High end:** Credible creators sign their content from day one. Immediately demonstrates what a signature means and starts building track records.
- **Low end:** Known spam sources get anti-vouched / debuffed from day one. Immediately demonstrates the filter working visibly.

Together they show the spectrum. The vocabulary teaches itself through use — show don't tell.

---

## What This Is Not

- Not anti-expertise — experts with good track records will be widely trusted
- Not pro-misinformation — bad vouches cost reputation
- Not utopian — bubbles will form, trust will be abused, people will be wrong
- Not a platform — it is infrastructure that sits under platforms

It is honest about what trust actually is — personal, fallible, human. The system stops pretending otherwise.
