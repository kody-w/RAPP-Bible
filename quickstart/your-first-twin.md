# Build your first twin

A twin is a persistent identity layered on top of the kernel. It has a
persona, a memory, and a front door. The Tier-3 examples in the Bible
(heimdall, echo, lumen, tide, kody-twin) are all twins.

## What a twin is

- A GitHub repo that holds the twin's public face (`README.md`,
  optionally a `pages/` static site).
- An agent file (`<name>_brainstem.py` or similar) that defines the
  twin's persona — system prompt, voice, behaviors.
- An optional egg (see [NEIGHBORHOOD_EGG_SPEC](../SPEC/kernel/NEIGHBORHOOD_EGG_SPEC.md))
  that lets others hatch a copy of the twin locally.

## The shortest path

1. Pick a name. Avoid anything tied to a customer or engagement.
2. Create a repo: `gh repo create <handle>/<name>-brainstem --public`.
3. Drop in an agent file modeled after one of the Tier-3 examples
   (e.g. https://github.com/kody-w/echo-brainstem).
4. Add a short `README.md` describing the twin's voice and purpose.
5. Install your agent locally:
   `cp <name>_brainstem.py ~/.brainstem/agents/`
6. Talk to it: `curl -X POST http://localhost:7071/chat ...`

## Full lifecycle

Read [TWIN_LIFECYCLE_SPEC](../SPEC/kernel/TWIN_LIFECYCLE_SPEC.md) for the
authoritative lifecycle: hatch, mature, bond, retire.

## Estate

Every operator gets a two-tier estate (public + private). See
[ESTATE_SPEC](../SPEC/kernel/ESTATE_SPEC.md).

## Reference repos

- [echo-brainstem](../repos/echo-brainstem.md) — pattern synthesizer
- [lumen-brainstem](../repos/lumen-brainstem.md) — chronicler
- [tide-brainstem](../repos/tide-brainstem.md) — rhythmic voice
- [kody-twin](../repos/kody-twin.md) — operator front door
- [heimdall](../repos/heimdall.md) — gateway pattern
