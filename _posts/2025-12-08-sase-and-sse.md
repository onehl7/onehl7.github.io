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

{% comment %} Data-driven SASE table - rendered from `_data/sase-table.yml` via `_includes/sase-table.html` {% endcomment %}

{% include sase-table.html %}

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
