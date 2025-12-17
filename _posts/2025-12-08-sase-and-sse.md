---
layout: post
title: "SASE & SSE"
date: 2025-12-08
category: technology
---

## SASE & SSE - Vendor solution comparison

Architecture Insights that will help choose based on your requirements

Tip - Know and clearly outline your requirments

Requirements could be 
- Zero Trust
- Next Generation protocols i.e. MASQUE ( as on 10/12/2025), QUIC , tunneled UDP
- Identity aware proxy
- Micro-segmentation
- Synthetic addresses
- Native OS suppport
- Network isolation - full separation between user's network (access network) and the Enterprise networks where services are hosted - it could be private cloud/on-prem and/or public cloud(s)
- flexible cloud/app connectivity options
- TPM certificate protection
- Better user experiance - seamless , optimised latency /throughput
- Easy Operations - easy policy administration , Unified portal or OK with multiple product portals 
- Secured by design 
- fitting favaorite ecosystem
- Co-existing with other ecosystem
- Observability 


## Vendor comparison

<!--
	Transcribed vendor comparison table. Use <br> to create line breaks inside cells for readability and easy editing.
	Edit cells directly; keep the four column structure: Cisco | Microsoft | Netskope | Zscaler
-->

| Dimension | Cisco Secure Access | Microsoft Global Secure Access (GSA) | Netskope | Zscaler |
|-----------|---------------------|---------------------------------------|----------|---------|
| Core components | Cisco Secure Access cloud<br>- Secure Client<br>- Resource connectors<br>- Unified SSE console (login.sse.cisco.com)<br>Includes: SWG, CASB, DLP, ZTNA, FWaaS with IPS, VPNaaS, DNS security, AMP, Sandbox, DEM, RBI<br>For SASE: add-on SD‑WAN, XDR, DUO MFA/SSO, CSPM | Entra Internet Access<br>Entra Private Access<br>GSA client<br>Private access connectors / remote networks<br>Entra portal / Intune portal<br>Includes: SWG, CASB, DLP, ZTA, Cloud Firewall for branches (preview) | Netskope SSE on NewEdge PoPs<br>- Netskope Client<br>- Connectors<br>Includes: Next‑gen SWG, CASB, ZTNA, DLP, FWaaS | ZIA + ZPA on Zero Trust Exchange<br>- Zscaler Digital Experience (ZDX)<br>- Client Connector<br>- App connectors / private service edge |
| Tech insights | Advanced ZTA using MASQUE / QUIC; ZTA Module; Cisco KDF (Kernel Driver Framework); socket streaming | Traffic classification:<br>- Microsoft traffic (all M365, Teams, MS SaaS)<br>- Internet traffic<br>- Private Access for self‑hosted apps | Netskope Client inspects end‑device packets using OS packet filtering (traffic modes & exceptions vary by OS)<br>Client uses Forward Proxy Steering: SSL tunnel from device to Netskope forward proxy in cloud; tunnel carries steered traffic<br>Netskope IP ranges must bypass local SSL inspection; client‑cloud connections are certificate‑pinned to prevent MitM | Zscaler Client Connector creates a virtual network adapter and uses packet‑filter based forwarding; apps use OS routing to forward traffic via this interface to the Zscaler service |
| AI | AI & ML for threat detection, protection, detect specific AI app usage, apply DLP policies to safeguard sensitive data | AI Gateway (part of Microsoft SSE)<br>- safeguards generative AI applications, agents, language models<br>- Prompt Shield: real‑time protection against malicious prompt injection (preview) | Netskope Copilot / Cloud Confidence Index (CCI); MCP Server; NPA<br>Private access leverages built‑in AI/ML to audit configurations and recommend optimized application segments & ZTNA policies | (no major public AI feature listed in table) |
| Main console model | Secure Access cloud console for SSE (login.sse.cisco.com)<br>Also: SD‑WAN console (sd.swan.cisco.com), ISE, etc. when in full SASE | All inside Entra portal: GSA + Conditional Access/compliance as main policy brain<br>Intune for Autopilot / conditional access workflows | Single SSE console for SWG, CASB, DLP, ZTNA, FWaaS (centralized security console) | ZIA and ZPA modules/console — shared platform but distinct sections for Internet vs private; ZIA for Internet/SaaS, ZPA for Private Apps; separate admin portals |
| Policy | SSE policies unified in Secure Access, but NAC/SD‑WAN/security posture live in other Cisco tools | High policy unification for identity/device: Conditional Access and compliance apply across SaaS, private, and Internet; GSA‑specific traffic controls layered on; policies enforced by priority (100 highest, 65,000 lowest)<br>Baseline 'catch‑all' security profile; link security profile to Conditional Access if required; preview: filter network file content (DLP) | One policy framework for Web, SaaS, Private Apps and data controls<br>Steering Profile: steers which traffic to capture/send to Netskope vs bypass<br>Policies: first match, top‑to‑bottom | Strong SWG policies in ZIA and ZTNA policies in ZPA; handled in distinct views; centralized platform but separate policy UIs |
| Admin experience | SSE & SASE: Best if you already live in Cisco security/SD‑WAN consoles; more moving parts but good convergence story. Cisco‑heavy shops (SD‑WAN, ISE, Duo) will find alignment with Secure Access policies. | SSE focused; Best if you live in Entra/M365 already; almost everything is Entra policy‑first with GSA as an extension. GSA policies are specializations of Conditional Access you already use. | Very SSE‑focused, less tied to any single ecosystem; unified policies for Web, SaaS and private apps; single place for security, web & data policy. | SSE and SASE: Mature SWG/ZTNA controls; admins commonly work in terms of ZIA vs ZPA; richer but more segmented policy constructs and consoles. |
| User Client | Single Client (`Cisco Secure Access`); also supports clientless (browser‑based) access from unmanaged devices | Global Secure Access (GSA) client<br>Browser Access for Private Apps (web/http(s)) and Browser Access AnyApp feature for non‑web apps | Netskope Client: Internet security, Private Access, Endpoint posture, DLP, Digital Experience Management (DEM) | Zscaler Client Connector with ZIA/ZPA; ZDX as a lightweight module; Zscaler Endpoint DLP (optional) |
| Branch connectivity | VPNaaS for Branch or SD‑WAN; Branch‑to‑Branch and Branch‑to‑Internet options | IPsec tunnel between on‑prem device and the Global Secure Access endpoint | Netskope One SASE Branch — one gateway, one client, Zero Trust Engine, NewEdge, One Orchestrator | Zscaler Branch Connector; Zero Trust SD‑WAN for branches |
| On‑prem integration | (varies by deployment) app connectors, backhaul VPN or SD‑WAN integration for on‑prem apps | Entra Private Access uses app proxy/connector model to expose apps via GSA; access controlled by Conditional Access | Netskope Private Access with local broker for on‑prem; Universal ZTNA for remote apps | ZPA with public or private service edges; app connector model for private apps |
| Internet / SWG | Integrated SWG, FWaaS, CASB, DLP, DNS security via Secure Access | Entra Internet Access — still evolving; tightly linked to Entra/Defender signals | Strong NG‑SWG with deep DLP and app/SaaS controls; steering and inline modes available | Mature ZIA SWG with global PoPs, URL filtering, CASB, DLP, FWaaS |
| Private / ZTNA | Client‑based and clientless ZTNA, app‑level access; supports MASQUE/QUIC proxies | Entra Private Access (App Proxy / connector) + Conditional Access | Netskope Private Access / Local Broker / Universal ZTNA | ZPA with app connectors and private service edge options |
| Private access — how? | Cisco Secure Access cloud PoPs to on‑prem hosted apps via App Connector or backhaul VPN (or both) | GSA integrated with Entra/Conditional Access and device compliance; app connectors control access | Netskope Private Access uses connectors or local broker; configurable app segments and access policies | Zscaler uses App Connector / Z‑Tunnel to service edges; connectors for private apps |
| Auth / Identity integration | Supports IdPs via SAML/OIDC for Secure Access; can integrate with Duo/ISE; identity reused across Cisco stack; MFA and posture checks supported | Native to Entra ID: uses same users, groups, Conditional Access, and device compliance across GSA and M365; leverages Intune/Defender for device posture and device objects | External IdP (Entra/Okta/etc.) via SAML/OIDC and SCIM; integrate and sync users/groups; client can leverage IdP SSO and OS session identity (avoid separate user/password flow) | Integrate with IdP via SAML/OIDC; use SCIM/LDAP for provisioning; ZIA/ZPA share identity configuration, but some separate items per module |
| DNS / synthetic IPs | Domain‑based flow redirection using random non‑routable loopback/synthetic IPs; KDF handles domain rule matching, synthetic IP→FQDN mapping and local cache | (no specific synthetic IP mechanism noted) | Google DNS used for geolocation to determine closest Netskope data center; synthetic IPs / steering used for traffic capture | Browser isolation, CBI integrated with ZIA/ZPA; (Zscaler uses its own redirection and TCP/IP handling via client connector) |
| DX / monitoring | (Cisco DEM / telemetry where deployed) | (Entra/Intune and Defender provide telemetry; GSA surfaced in Entra portal) | Netskope Digital Experience Management (DEM) — real‑time visibility of managed device cloud/web access from any location | ZDX — monitor granular details for users, devices, applications; detect user experience and productivity issues |
| Coexistence | (Supports co‑existence with VPN and SD‑WAN; typical split‑tunnel guidance depends on deployment) | Very strong if you are Entra ID/M365/Intune/Defender heavy; everything driven from Entra portal and Conditional Access (coexistence typically identity‑first) | Netskope with VPN — split tunnel mode recommended; flexible steering modes for capture vs bypass | Vendor‑neutral but mature SASE/SSE; common coexistence patterns with SD‑WAN and branch connectors |
| Emergency Access | (break‑glass methods available; vendor/platform dependent) | If GSA is down, script‑based breakglass access defined by admins | (tenant specific; admins can define bypass and emergency access patterns) | Zscaler supports breakglass and alternate routing configurations in enterprise deployments |
| Ecosystem fit | Strong with Cisco SD‑WAN, ISE, AnyConnect migration, Duo, Umbrella heritage | Very strong if you are Entra ID/M365/Intune/Defender heavy; policy driven from Entra portal and Conditional Access | Vendor‑neutral, focus on SSE depth and DLP / SaaS controls; integrates with SD‑WANs and IdPs | Vendor‑neutral and very mature SSE; integrates widely with SD‑WAN / IdPs; large market adoption |
| Cloud Access Security Broker (CASB) & notes | Built‑in CASB features, DLP and sandboxing integrated with Secure Access | CASB features via Entra/Defender integration; policy driven through Entra | Full CASB functionality integrated into Netskope SSE; deep app discovery & controls | CASB functionality in ZIA; strong app controls and DLP |

## Key points

- Slowest to adopt full SASE: vendors focused on on‑prem networking that lack cloud-native SSE components.  
- Fastest to market: managed SASE providers offering packaged deployments and operational support.  
- Choose SSE when you primarily need cloud‑centric security (SWG/CASB/ZTNA) and SASE when you also require integrated SD‑WAN and network edge capabilities.

### What is SASE?
Secure Access Service Edge (SASE) = network connectivity (i.e.  SD-WAN) + security services (SSE)

### What is SSE?
Security Service Edge (SSE) = security services like cloud access security broker (CASB) + secure web gateway (SWG) + zero trust network access (ZTNA) + DLP + FWaaS

SSE solutions
- cloud-based security architecture
- provides secure access to Private Applications/services, SaaS Applications/services, Internet
- componenets includes- cloud access security broker (CASB) + secure web gateway (SWG) + zero trust network access (ZTNA) + DLP + Firewall-as-a-Service (FWaaS)
