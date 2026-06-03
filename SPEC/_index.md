# SPEC Index

Canonical specs mirrored from their upstream repos. Every file in this tree
carries a provenance header pointing back to its upstream source. Edits
happen upstream; the Bible re-syncs and surfaces drift.

Run `python3 scripts/mirror_sync.py --check` to see which mirrored copies
have drifted from upstream HEAD.

## Kernel — `kody-w/RAPP`

| File | Description |
|------|-------------|
| [kernel/CONSTITUTION.md](kernel/CONSTITUTION.md) | The full RAPP constitution — every article, every clause. Authoritative. |
| [kernel/NEIGHBORHOOD_PROTOCOL.md](kernel/NEIGHBORHOOD_PROTOCOL.md) | Wire protocol for project-anchored twin neighborhoods. |
| [kernel/SPEC.md](kernel/SPEC.md) | Core kernel spec — brainstem, agents, organism. |
| [kernel/ESTATE_SPEC.md](kernel/ESTATE_SPEC.md) | Two-tier estate spec (public + private). |
| [kernel/TWIN_LIFECYCLE_SPEC.md](kernel/TWIN_LIFECYCLE_SPEC.md) | Twin lifecycle — hatch, mature, bond, retire. |
| [kernel/NEIGHBORHOOD_EGG_SPEC.md](kernel/NEIGHBORHOOD_EGG_SPEC.md) | Egg format for neighborhood distribution. |

## Network — `kody-w/RAPP-Network`

| File | Description |
|------|-------------|
| [network/SPEC.md](network/SPEC.md) | Project-twin neighborhood specification with cross-validation. |

## Catalog — `kody-w/RAPP_Store`

| File | Description |
|------|-------------|
| [catalog/SPEC.md](catalog/SPEC.md) | Rapplication catalog format and index.json schema. |

## Registry — `kody-w/RAR`

| File | Description |
|------|-------------|
| [registry/SPEC.md](registry/SPEC.md) | Single-file agent registry — browse, vote, share. |

## Senses — `kody-w/RAPP_Sense_Store`

| File | Description |
|------|-------------|
| [senses/SPEC.md](senses/SPEC.md) | Per-channel output overlay catalog. |

## MCP — `kody-w/rapp-mcp`

| File | Description |
|------|-------------|
| [mcp/SPEC.md](mcp/SPEC.md) | The MCP on-ramp — `rapp-mcp-spec/1.0`: serve agents + a brainstem to any MCP host. |

MCP is **transport, not a new taxonomy.** An MCP host is a Layer-2 caller of
`/chat` per [Constitution Article XXV — Chat Is The Only Wire](kernel/CONSTITUTION.md#article-xxv--chat-is-the-only-wire-time-travel-safe):
"an MCP client over stdio … hit the same endpoint." It is not a new unit, kind,
or taxonomy — there is no `mcp` kind.

---

_Mirrored content is read-only inside this repo. To change a spec, open a PR upstream._
