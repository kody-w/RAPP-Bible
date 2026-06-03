# RAPP Bible

**One repo. Every RAPP spec. Every entry point. Every link.**

The RAPP Bible is the canonical aggregation point for the entire
[RAPP](https://github.com/kody-w/RAPP) (Rapid Agent Prototyping Platform)
ecosystem. It mirrors the specs from each canonical repo, indexes every
front door, and gives anyone landing here a complete map of what exists and
where to go next.

**Two sources of truth.** Each canonical repo stays authoritative. The
Bible aggregates and surfaces drift via a nightly sync. If you want to
change a spec, open a PR upstream.

- Site: https://kody-w.github.io/RAPP-Bible/
- Repo: https://github.com/kody-w/RAPP-Bible
- License: BSD-3-Clause

## What is RAPP?

RAPP is a portable, shareable, vibe-swarm building tool. Single-file Python
agents. Local-first. Powered by GitHub Copilot. The kernel is small; the
ecosystem around it is large.

This Bible exists because the ecosystem has grown past the point where any
one README can hold it all. Land here, find what you need, follow the link
to the canonical source.

## Quickstart

```bash
# Install the brainstem (one-liner from rapp-installer)
curl -fsSL https://raw.githubusercontent.com/kody-w/rapp-installer/main/install.sh | bash

# Drop an agent into ~/.brainstem/agents/ — it just runs
# Browse agents at https://kody-w.github.io/RAR/
```

See [quickstart/install.md](quickstart/install.md) for the full path.

## Ecosystem map

```
                          [ kody-w/RAPP ]
                         (kernel + spec)
                                |
        +-----------------------+-----------------------+
        |                       |                       |
   [ RAPP-Network ]        [ RAPP_Store ]          [ RAR ]
   (neighborhoods)       (rapplications)     (single-file agents)
        |                       |                       |
        +-----------+-----------+-----------+-----------+
                    |                       |
            [ rapp-installer ]      [ RAPP_Sense_Store ]
              (install path)            (senses catalog)

                On-ramps / transport
                   [ rapp-mcp ]
            (MCP host -> /chat, Layer 2)

                Distribution & UX wrappers
        +------------------+------------------+
        |                  |                  |
   [ rappterbook ]   [ rappter-distro ]   [ ez-rapp ]
   (social net)     (organism distro)    (Electron UX)
                    [ rappterbox ]      [ openrappter ]
                    (console)           (Copilot SDK agent)

           Federation surfaces
   [ rapp-commons ]   [ rapp-leviathan-hub ]   [ rapp-estate ]
   (signed events)    (egg distribution)       (operator inventory)

       Front doors (link only — don't mirror)
   [ heimdall ] [ kody-twin ] [ kody-w-twin ]
   [ echo-brainstem ] [ lumen-brainstem ] [ tide-brainstem ]
```

## Three tiers

**Tier 1 — Core specs and kernel.** What you read to understand the system.
- [RAPP](repos/RAPP.md) — kernel + constitution
- [RAPP-Network](repos/RAPP-Network.md) — neighborhood layer
- [RAPP_Store](repos/RAPP_Store.md) — rapplication catalog
- [RAR](repos/RAR.md) — agent registry
- [RAPP_Sense_Store](repos/RAPP_Sense_Store.md) — sense catalog
- [rapp-installer](repos/rapp-installer.md) — install path
- [rapp-mcp](repos/rapp-mcp.md) — MCP gateway: serve agents + a brainstem to any MCP host

**Tier 2 — Distribution and ecosystem.** What ships RAPP to humans.
See [repos/_index.md](repos/_index.md).

**Tier 3 — Front doors.** Example twins built on top of the kernel.
Link-only — the Bible does not mirror their content.

## What's in here

- [SPEC/](SPEC/_index.md) — every mirrored spec, with provenance headers
- [repos/](repos/_index.md) — one-pager per repo with metadata and links
- [quickstart/](quickstart/install.md) — paste-able getting-started flows
- [scripts/](scripts/) — `mirror_sync.py` (re-sync from upstream),
  `validate.py` (run cross-validators), `build_repo_pages.py`
- [tests/](tests/) — link checks, freshness checks, PII guards
- [CONTRIBUTING.md](CONTRIBUTING.md) — how the two-sources-of-truth model works

## How to contribute

You almost certainly don't want to edit files in this repo directly. See
[CONTRIBUTING.md](CONTRIBUTING.md) for where to actually make changes.

## Excluded by design

Some RAPP-ecosystem repos are private and intentionally not surfaced here.
The Bible never references private repos as content sources. See
`tests/test_no_private.py` for the enforced exclusion list.

The Bible also never includes customer or engagement names. See
`tests/test_no_pii.py` for the enforced banned-name list. If you spot a
leak, open an issue.

## License

BSD-3-Clause. See [LICENSE](LICENSE).
