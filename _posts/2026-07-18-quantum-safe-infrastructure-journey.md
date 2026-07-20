---
layout: post
title: "Quantum-Safe Infrastructure Journey"
date: 2026-07-18 12:00:00 +0000
categories: [quantum]
excerpt: "A draft post structure for a practical discussion of quantum-safe infrastructure planning, adoption, and migration."
---

Quantum-safe infrastructure is becoming an increasingly important topic for organizations that want to protect data, infrastructure and communications against future cryptographic disruption - 'Q-day'

Q-Day is the hypothetical milestone (estimated by NIST) that refers to the point in time when quantum computers will be capable of breaking widely used encryption and authentication methods (RSA, ECC etc)

The conversation often begins with inventory, risk assessment, and a phased approach to modernisation rather than a single large migration.

![The Four-Phase Quantum-safe Journey](/assets/images/qpqc0.png)


A sensible approach to this journey usually starts with understanding which systems depend on vulnerable cryptographic methods and which business functions would be most affected by a transition. From there, teams can align policy, architecture, and operations around a manageable roadmap.

## PQC - Comparative Global Timeline
![Comparative Global Timeline](/assets/images/qtimeline.png)

## Key considerations
The transition to quantum-safe infrastructure is not only a technical exercise, but a strategic necessity. It also requires governance, training, vendor coordination, and clear communication with stakeholders. A phased approach often works better than trying to replace everything at once.

## UK Timeline
The UK NCSC Timeline (Transition to 2035),  published in March 2025. It represents a structured, ten-year risk-managed transition. [NCSC PQC Migration Guidance](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines){:target="_blank" rel="noopener noreferrer"}

- Phase 1 (to 2028): 
Dedicated to asset discovery, scoping out what cryptographic services need upgrades, and establishing robust organisational plans
- Phase 2 (2028–2031): 
Focused on executing upgrades for high-priority systems, Critical national infrastructure, must start migrating core systems during this window
- Phase 3 & 4 (2031–2035): 
Full remediation across all remaining networks, devices, and products to meet the 2035 quantum deadline

## Why PQC?
Post-quantum cryptography (PQC) is specifically designed to mitigate vulnerabilities in asymmetric (public-key) cryptography, which is threatened by Shor’s algorithm running on a cryptographically relevant quantum computer (CRQC).

The primary vulnerable elements and systems being mitigated include:
1. Vulnerable Mathematical Primitives
- Rivest-Shamir-Adleman (RSA): Relying on the computational hardness of factorising large prime numbers
- Elliptic Curve Cryptography (ECC, ECDH, ECDSA): Relying on the difficulty of solving discrete logarithms over elliptic curves
- Note: Symmetric ciphers (like AES) are not fundamentally broken by quantum computers; Grover's algorithm only provides a quadratic speedup, which is mitigated by doubling key sizes (such as using AES-256)
2. Core Cryptographic Capabilities
- Key Exchange & Confidentiality (HNDL): Classical asymmetric key exchanges (like Diffie-Hellman) are entirely vulnerable.
Threat actors can harvest encrypted network traffic today and store it to decrypt in the future once a CRQC becomes available—known as "Harvest Now, Decrypt Later" (HNDL) attacks
- Digital Signatures & Authentication: Digital signatures are vulnerable to forgery because an adversary with a CRQC can derive private keys from harvested public keys
3. Impacted Systems & Protocols
- Network Transport Protocols: Secure communication channels such as TLS (especially TLS 1.2, which cannot support PQC), SSH, IPsec/VPNs, and QUIC that depend on vulnerable asymmetric handshakes to establish secure sessions
- Public Key Infrastructure (PKI): X.509 digital certificates, certificate authorities, and the "roots of trust" used to verify identities and secure online connections
- Device & Code Integrity (Secure Boot): RSA and ECC signatures used to verify operating systems, firmware updates, and bootloaders
If these signatures are compromised, attackers can sign maliciously modified software images with backdoors to gain remote control of devices or shut down entire networks
- Long-Term Encrypted Data: Stored databases, backups, and long-lived contracts (e.g., mortgages or health records) that require multi-decade confidentiality or authenticity

NIST - first set of finalized [NIST PQC Standards](https://csrc.nist.gov/projects/post-quantum-cryptography){:target="_blank" rel="noopener noreferrer"}
 are FIPS 203 -> ML KEM , FIPS 204 -> ML-DSA and FIPS 205 -> SLH-DSA

## Building a quantum-safe infrastructure - a Network perspective

![Quantum-safe infrastructure journey infographic](/assets/images/qpqc1.png)



<div style="font-size: 0.95rem; color: var(--muted-text); margin-top: 2rem; padding: 1rem; border: 1px solid var(--border-color); border-radius: 0.75rem; background-color: var(--card-alt-bg);">
  <h2 style="font-size: 1.25rem; margin-bottom: 0.75rem; color: var(--heading-color); font-weight: 700;">Knowledge sources & Further Reading</h2>
  <ul style="margin: 0; padding-left: 1.25rem; line-height: 1.8;">
    <li>
      <a href="https://datatracker.ietf.org/doc/html/rfc8784" target="_blank" rel="noopener noreferrer">
        RFC 8784 – Mixing Preshared Keys in IKEv2 for Post-quantum Security
      </a>
    </li>
    <li>
      <a href="https://www.bis.org/publ/bppdf/bispap158.pdf" target="_blank" rel="noopener noreferrer">
        BIS Paper 158 – Quantum-readiness for the financial system
      </a>
    </li>
    <li>
      <a href="https://www.ncsc.gov.uk/guidance/pqc-migration-timelines" target="_blank" rel="noopener noreferrer">
        NCSC PQC Migration Guidance
      </a>
    </li>
    <li>
      <a href="https://www.enisa.europa.eu/sites/default/files/publications/Post%20Quantum%20Cryptography-%20Integration%20Publication.pdf" target="_blank" rel="noopener noreferrer">
        ENISA PQC Integration Study
      </a>
    </li>
    <li>
      <a href="https://www.enisa.europa.eu/publications/post-quantum-cryptography-current-state-and-quantum-mitigation" target="_blank" rel="noopener noreferrer">
        ENISA PQC Quantum Mitigation
      </a>
    </li>
    <li>
      <a href="https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Crypto/Migration_to_Post_Quantum_Cryptography.pdf?__blob=publicationFile&v=2" target="_blank" rel="noopener noreferrer">
        BSI Migration to PQC
      </a>
    </li>
    <li>
      <a href="https://www.nccoe.nist.gov/sites/default/files/2023-12/pqc-migration-nist-sp-1800-38b-preliminary-draft.pdf" target="_blank" rel="noopener noreferrer">
        NIST PQC Migration Guidance
      </a>
    </li>
  </ul>
</div>
---
*Knowledge credit to various information sources and augmented by AI