# Install the RAPP brainstem

The brainstem is the local-first server that hosts your agents. One
process, one port, drop-in `*_agent.py` files.

## One-liner

```bash
curl -fsSL https://raw.githubusercontent.com/kody-w/rapp-installer/main/install.sh | bash
```

This clones the kernel into `~/.brainstem/`, sets up the agent directory,
and prints the start command.

## Manual

```bash
git clone https://github.com/kody-w/RAPP.git ~/.brainstem
cd ~/.brainstem
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m rapp_brainstem
```

The brainstem listens on `http://localhost:7071` by default.

## Verify

```bash
curl -X POST http://localhost:7071/chat \
  -H "Content-Type: application/json" \
  -d '{"user_input": "hello", "user_guid": "test"}'
```

If you get a JSON response, you're up.

## Next

- [Drop in an agent](drop-in-an-agent.md)
- [Build your first twin](your-first-twin.md)
- [Build your first rapplication](your-first-rapplication.md)

## Reference

- Installer source: https://github.com/kody-w/rapp-installer
- Kernel source: https://github.com/kody-w/RAPP
- Constitution (read this): [../SPEC/kernel/CONSTITUTION.md](../SPEC/kernel/CONSTITUTION.md)
