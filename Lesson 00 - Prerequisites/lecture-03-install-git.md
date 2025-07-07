# Install Git
Git provides version control so changes can be tracked and shared. We'll install it before creating any files.


1. Download Git from <https://git-scm.com/downloads>.
2. Run the installer and accept the default options.
3. After the installation open a terminal and check:

```powershell
git --version
```

## Configure Git

Use the `setup-git.ps1` script in this folder to configure your name and email:

```powershell
./setup-git.ps1
```

## Why this lecture?

Git tracks changes to your code and lets you collaborate effectively. Running
the setup script configures your identity so commits can be attributed to you
in version history.
## Theory example
Git is a distributed version control system. Every clone contains the full history, enabling offline work and robust branching.
