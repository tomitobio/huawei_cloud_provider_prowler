# Installation Guide — Prowler Huawei Cloud Provider

This guide covers installing Prowler with the Huawei Cloud provider, authenticating to Huawei Cloud, running security checks, and running the test suite.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Clone the Repository](#2-clone-the-repository)
3. [Install Prowler + Huawei Cloud Provider](#3-install-prowler--huawei-cloud-provider)
4. [Install Huawei Cloud SDK Dependencies](#4-install-huawei-cloud-sdk-dependencies)
5. [Huawei Cloud Credentials](#5-huawei-cloud-credentials)
6. [Running Security Checks](#6-running-security-checks)
7. [CIS Compliance Benchmark](#7-cis-compliance-benchmark)
8. [Running Tests](#8-running-tests)
9. [Docker Deployment](#9-docker-deployment)
10. [Troubleshooting](#10-troubleshooting)
11. [Prowler Server Web UI Dashboard](#11-prowler-server-web-ui-dashboard)

---

## 1. Prerequisites

### Summary

| Requirement | Version |
|-------------|---------|
| Python | 3.12+ |
| pip | latest (bundled with Python) |
| Git | any recent version |
| Huawei Cloud SDK | 28 packages (installed in Section 4) |
| Prowler | 5.31.0 (installed in Section 3) |
| Huawei Cloud account | with Access Key ID + Secret Access Key (see Section 5) |

### Step-by-Step Installation

#### 1.1 — Install Python 3.12+

**Ubuntu / Debian:**

```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3.12-dev
```

Verify:

```bash
python3.12 --version
# Python 3.12.x
```

**CentOS / RHEL / Fedora:**

```bash
sudo dnf install -y python3.12 python3.12-devel
```

Verify:

```bash
python3.12 --version
```

**macOS (Homebrew):**

```bash
brew install python@3.12
```

Verify:

```bash
python3.12 --version
```

**From source (any Linux):**

```bash
curl -O https://www.python.org/ftp/python/3.12.7/Python-3.12.7.tgz
tar -xzf Python-3.12.7.tgz
cd Python-3.12.7
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
cd ..
python3.12 --version
```

#### 1.2 — Create a Virtual Environment

Using `venv` (recommended):

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Verify:

```bash
python --version
# Python 3.12.x
pip --version
# pip xx.x from ... (python 3.12)
```

> You must activate the virtual environment (`source .venv/bin/activate`) in every new terminal session before running Prowler or tests.

Alternatively, using `uv` (faster):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 .venv
source .venv/bin/activate
```

#### 1.3 — Upgrade pip

```bash
pip install --upgrade pip
```

#### 1.4 — Install Git

**Ubuntu / Debian:**

```bash
sudo apt install -y git
```

**CentOS / RHEL / Fedora:**

```bash
sudo dnf install -y git
```

**macOS:**

```bash
brew install git
```

Verify:

```bash
git --version
# git version 2.x.x
```

#### 1.5 — Huawei Cloud Account

You need a Huawei Cloud account with an **Access Key ID** and **Secret Access Key**. If you don't have one:

1. Sign up at [https://www.huaweicloud.com/](https://www.huaweicloud.com/)
2. Create access keys in the console under **My Credentials** → **Access Keys** → **Create Access Key**
3. Note down your **Project ID** (found under **My Credentials** → **Projects**)

See [Section 5](#5-huawei-cloud-credentials) for full details.

---

## 2. Clone the Repository

```bash
git clone https://github.com/tomitobio/huawei_cloud_provider_prowler.git
cd huawei_cloud_provider_prowler
```

The repository contains:

```
prowler/providers/huaweicloud/     # Provider code (27 services, 67 checks)
prowler/compliance/huaweicloud/     # CIS 1.0 compliance benchmark
tests/providers/huaweicloud/        # 228 tests across 116 test files
patches/                            # Patches to Prowler core files
scripts/setup-prowler.sh            # Setup script
api/prowler_patches/                # API compliance patches
docs/                               # User and developer documentation
```

---

## 3. Install Prowler + Huawei Cloud Provider

The provider is not a standalone package — it plugs into the official Prowler installation. The `scripts/setup-prowler.sh` script handles this:

### Step 1 — Install Prowler

```bash
pip install prowler==5.31.0
```

> **Important:** Prowler 5.31.0 is the exact version this provider is built against. Using a different version may cause incompatibilities.

### Step 2 — Run the Setup Script

```bash
bash scripts/setup-prowler.sh python
```

This script:
1. Locates the installed Prowler package
2. Copies the `huaweicloud` provider into `prowler/providers/`
3. Copies the CIS compliance benchmark into `prowler/compliance/huaweicloud/`
4. Applies patches to 5 Prowler core files:

| Patched File | Modification |
|-------------|-------------|
| `lib/check/check.py` | Add `_huaweicloud_checks` property |
| `lib/check/models.py` | Add `CheckReportHuaweiCloud` model |
| `lib/outputs/finding.py` | Add Huawei Cloud finding mapping |
| `lib/outputs/outputs.py` | Add Huawei Cloud output support |
| `providers/common/provider.py` | Add Huawei Cloud to provider registry |

### Step 3 — Verify Installation

```bash
prowler huaweicloud --help
```

You should see the Huawei Cloud provider help with `--access-key-id`, `--secret-access-key`, and other options.

---

## 4. Install Huawei Cloud SDK Dependencies

The provider uses 28 Huawei Cloud SDK packages. Install them all:

```bash
pip install huaweicloudsdkcore huaweicloudsdkbms huaweicloudsdkcbr huaweicloudsdkcce \
    huaweicloudsdkces huaweicloudsdkcfw huaweicloudsdkcts huaweicloudsdkdcs \
    huaweicloudsdkdns huaweicloudsdkecs huaweicloudsdkeip huaweicloudsdkelb \
    huaweicloudsdkevs huaweicloudsdkfunctiongraph huaweicloudsdkiam \
    huaweicloudsdkidentitycenter huaweicloudsdkkms huaweicloudsdklts \
    huaweicloudsdknat huaweicloudsdkobs huaweicloudsdkrds huaweicloudsdkrms \
    huaweicloudsdksfsturbo huaweicloudsdksmn huaweicloudsdktms \
    huaweicloudsdkvpc huaweicloudsdkvpn huaweicloudsdkwaf
```

### SDK-to-Service Mapping

| SDK Package | Service |
|-------------|---------|
| `huaweicloudsdkcore` | Core SDK (required) |
| `huaweicloudsdkbms` | Bare Metal Server (BMS) |
| `huaweicloudsdkcbr` | Cloud Backup and Recovery (CBR) |
| `huaweicloudsdkcce` | Cloud Container Engine (CCE) |
| `huaweicloudsdkces` | Cloud Eye Service (CES) |
| `huaweicloudsdkcfw` | Cloud Firewall (CFW) |
| `huaweicloudsdkcts` | Cloud Trace Service (CTS) |
| `huaweicloudsdkdcs` | Distributed Cache Service (DCS) |
| `huaweicloudsdkdns` | Domain Name Service (DNS) |
| `huaweicloudsdkecs` | Elastic Cloud Server (ECS) |
| `huaweicloudsdkeip` | Elastic IP (EIP) |
| `huaweicloudsdkelb` | Elastic Load Balancing (ELB) |
| `huaweicloudsdkevs` | Elastic Volume Service (EVS) |
| `huaweicloudsdkfunctiongraph` | FunctionGraph |
| `huaweicloudsdkiam` | Identity and Access Management (IAM) |
| `huaweicloudsdkidentitycenter` | Identity Center |
| `huaweicloudsdkkms` | Key Management Service (KMS) |
| `huaweicloudsdklts` | Log Tank Service (LTS) |
| `huaweicloudsdknat` | NAT Gateway (NAT) |
| `huaweicloudsdkobs` | Object Storage Service (OBS) |
| `huaweicloudsdkrds` | Relational Database Service (RDS) |
| `huaweicloudsdkrms` | Resource Management Service (Config) |
| `huaweicloudsdksfsturbo` | Scalable File Service (SFS) |
| `huaweicloudsdksmn` | Simple Message Notification (SMN) |
| `huaweicloudsdktms` | Tag Management Service (TMS) |
| `huaweicloudsdkvpc` | Virtual Private Cloud (VPC) |
| `huaweicloudsdkvpn` | Virtual Private Network (VPN) |
| `huaweicloudsdkwaf` | Web Application Firewall (WAF) |

---

## 5. Huawei Cloud Credentials

### Creating Access Keys

1. Log in to the [Huawei Cloud Console](https://console.huaweicloud.com/)
2. Go to **My Credentials** → **Access Keys**
3. Click **Create Access Key**
4. Save the **Access Key ID** (AK) and **Secret Access Key** (SK) — the SK is only shown once

### Using Environment Variables (Recommended)

Only AK/SK are required — the SDK auto-derives Project ID and Domain ID from your credentials via IAM:

```bash
export HUAWEICLOUD_ACCESS_KEY_ID="your-access-key-id"
export HUAWEICLOUD_SECRET_ACCESS_KEY="your-secret-access-key"
```

Alternative shorter variable names also work:

```bash
export HW_ACCESS_KEY="your-access-key-id"
export HW_SECRET_KEY="your-secret-access-key"
```

### Using CLI Arguments

Pass credentials directly on the command line (not recommended for production — keys will appear in shell history):

```bash
prowler huaweicloud \
    --access-key-id "your-access-key-id" \
    --secret-access-key "your-secret-access-key"
```

### Optional Arguments

| Argument | Env Variable | Description |
|----------|-------------|-------------|
| `--region` | — | Region ID(s) (default: `cn-north-4`; pass multiple for multi-region) |
| `--project-id` | `HUAWEICLOUD_PROJECT_ID` / `HW_PROJECT_ID` | Project ID (auto-derived if not set) |
| `--domain-id` | `HUAWEICLOUD_DOMAIN_ID` / `HW_DOMAIN_ID` | Domain ID (auto-derived if not set) |
| `--security-token` | `HUAWEICLOUD_SECURITY_TOKEN` | Security token for temporary credentials (STS) |
| `--agency-name` | — | Agency name for cross-account access |
| `--delegation-domain-id` | — | Domain ID of the delegating account |

---

## 6. Running Security Checks

### Basic Scan

```bash
prowler huaweicloud
```

(Credentials read from environment variables. Defaults to region `cn-north-4`.)

### Multi-Region Scan

```bash
prowler huaweicloud --region cn-north-4 cn-east-3 ap-southeast-2
```

### List Available Checks

```bash
prowler huaweicloud --list-checks
```

### Run Specific Checks

```bash
prowler huaweicloud --checks iam_user_mfa_enabled,ecs_instance_public_ip
```

### Run by Severity

```bash
prowler huaweicloud --severity critical,high
```

### Run by Service

```bash
prowler huaweicloud --services iam,ecs,obs
```

### Output Formats

```bash
# JSON
prowler huaweicloud -M json

# CSV
prowler huaweicloud -M csv

# HTML
prowler huaweicloud -M html

# Multiple formats
prowler huaweicloud -M json csv html
```

### Supported Regions

The provider supports all Huawei Cloud regions. Common ones:

| Region ID | Location |
|-----------|----------|
| `cn-north-4` | China (Beijing-4) — **default** |
| `cn-east-3` | China (Shanghai-1) |
| `cn-south-1` | China (Guangzhou) |
| `ap-southeast-2` | Singapore |
| `ap-southeast-1` | Hong Kong |
| `eu-west-0` | Ireland |
| `la-south-2` | Chile (Santiago) |
| `sa-brazil-1` | Brazil |
| `na-mexico-1` | Mexico |

See `prowler/providers/huaweicloud/config.py` for the full list.

### Available Checks (67 total)

| Severity | Count |
|----------|-------|
| Critical | 6 |
| High | 16 |
| Medium | 33 |
| Low | 12 |

### Available Services (27 total)

`bms`, `cbr`, `cce`, `ces`, `cfw`, `config`, `cts`, `dcs`, `dns`, `ecs`, `eip`, `elb`, `evs`, `functiongraph`, `iam`, `identitycenter`, `kms`, `lts`, `nat`, `obs`, `rds`, `sfs`, `smn`, `tms`, `vpc`, `vpn`, `waf`

---

## 7. CIS Compliance Benchmark

The provider includes a **CIS Huawei Cloud 1.0** compliance benchmark mapping 21 checks to 21 requirements across 8 sections:

| Section | Description | Checks |
|---------|-------------|--------|
| 1 | Identity and Access Management (IAM) | 8 |
| 2 | Storage (OBS) | 2 |
| 3 | Network Security (VPC) | 2 |
| 4 | Compute (ECS) | 1 |
| 5 | Database (RDS) | 2 |
| 6 | Load Balancing (ELB) | 1 |
| 7 | Logging and Monitoring (CTS) | 1 |
| 8 | Key Management (KMS) | 2 |

### Run a Compliance Scan

```bash
prowler huaweicloud \
    --compliance cis_1.0_huaweicloud
```

### List Compliance Checks

```bash
prowler huaweicloud --compliance cis_1.0_huaweicloud --list-checks
```

---

## 8. Running Tests

### Install Test Dependencies

```bash
pip install -r requirements-test.txt
```

This installs `prowler==5.31.0` and `pytest>=8.0`.

### Set Up Prowler with Provider

```bash
bash scripts/setup-prowler.sh python
```

### Run All Tests

```bash
pytest tests/providers/huaweicloud/ -v
```

Expected: **228 tests** across **116 test files**, all passing.

### Run Tests for a Single Service

```bash
pytest tests/providers/huaweicloud/services/iam/ -v
```

### Run a Single Check's Tests

```bash
pytest tests/providers/huaweicloud/services/iam/iam_user_mfa_enabled/ -v
```

### Quick Smoke Test (No Real Credentials Needed)

Tests use mock authentication — no real Huawei Cloud credentials are required:

```bash
export HUAWEICLOUD_MOCK_AUTH=true
pytest tests/providers/huaweicloud/ -v --tb=short
```

---

## 9. Docker Deployment

The provider can be deployed as part of a Prowler Docker stack.

### Using Prowler's Docker Image

```bash
# Pull the official Prowler image
docker pull prowlercloud/prowler:5.31.0

# Run with the provider mounted as a volume
docker run --rm \
    -v "$(pwd)/prowler/providers/huaweicloud:/prowler/prowler/providers/huaweicloud" \
    -v "$(pwd)/prowler/compliance/huaweicloud:/prowler/prowler/compliance/huaweicloud" \
    -e HUAWEICLOUD_ACCESS_KEY_ID \
    -e HUAWEICLOUD_SECRET_ACCESS_KEY \
    prowlercloud/prowler:5.31.0 \
    huaweicloud
```

> **Note:** When using Docker, you still need to apply the core patches. Build a custom image with a Dockerfile that runs `scripts/setup-prowler.sh` after installing Prowler.

### Custom Dockerfile

```dockerfile
FROM prowlercloud/prowler:5.31.0
COPY prowler/providers/huaweicloud /prowler/prowler/providers/huaweicloud
COPY prowler/compliance/huaweicloud /prowler/prowler/compliance/huaweicloud
COPY patches/ /tmp/patches/
COPY scripts/setup-prowler.sh /tmp/setup-prowler.sh
RUN bash /tmp/setup-prowler.sh python
```

```bash
docker build -t prowler-huaweicloud .
docker run --rm \
    -e HUAWEICLOUD_ACCESS_KEY_ID \
    -e HUAWEICLOUD_SECRET_ACCESS_KEY \
    prowler-huaweicloud \
    huaweicloud
```

---

## 10. Troubleshooting

### `prowler huaweicloud: error: unrecognized arguments`

The setup script did not run or failed. Re-run:

```bash
bash scripts/setup-prowler.sh python
```

Verify the provider was copied:

```bash
python -c "import prowler; import os; print(os.path.join(os.path.dirname(prowler.__file__), 'providers/huaweicloud'))"
```

### `ModuleNotFoundError: No module named 'huaweicloudsdk...'`

You are missing one or more Huawei Cloud SDK packages. Re-run the SDK install command from [Section 4](#4-install-huawei-cloud-sdk-dependencies).

### `HuaweiCloudNoCredentialsError`

No credentials were found. Set the environment variables or pass `--access-key-id` and `--secret-access-key`:

```bash
export HUAWEICLOUD_ACCESS_KEY_ID="your-ak"
export HUAWEICLOUD_SECRET_ACCESS_KEY="your-sk"
```

### `HuaweiCloudInvalidCredentialsError`

The credentials are invalid or expired. Verify your AK/SK in the Huawei Cloud console under **My Credentials** → **Access Keys**.

### Tests Fail with Import Errors

Ensure the setup script ran successfully and you're using Python 3.12:

```bash
python --version  # should be 3.12+
bash scripts/setup-prowler.sh python
pytest tests/providers/huaweicloud/ -v
```

### Prowler Version Mismatch

This provider requires Prowler **5.31.0** exactly. Check your version:

```bash
prowler --version
```

If different, reinstall:

```bash
pip install prowler==5.31.0
bash scripts/setup-prowler.sh python
```

---

## Quick Start (One-Liner)

```bash
git clone https://github.com/tomitobio/huawei_cloud_provider_prowler.git && \
cd huawei_cloud_provider_prowler && \
pip install prowler==5.31.0 && \
pip install huaweicloudsdkcore huaweicloudsdkbms huaweicloudsdkcbr huaweicloudsdkcce \
    huaweicloudsdkces huaweicloudsdkcfw huaweicloudsdkcts huaweicloudsdkdcs \
    huaweicloudsdkdns huaweicloudsdkecs huaweicloudsdkeip huaweicloudsdkelb \
    huaweicloudsdkevs huaweicloudsdkfunctiongraph huaweicloudsdkiam \
    huaweicloudsdkidentitycenter huaweicloudsdkkms huaweicloudsdklts \
    huaweicloudsdknat huaweicloudsdkobs huaweicloudsdkrds huaweicloudsdkrms \
    huaweicloudsdksfsturbo huaweicloudsdksmn huaweicloudsdktms \
    huaweicloudsdkvpc huaweicloudsdkvpn huaweicloudsdkwaf && \
bash scripts/setup-prowler.sh python && \
export HUAWEICLOUD_ACCESS_KEY_ID="YOUR_AK" && \
export HUAWEICLOUD_SECRET_ACCESS_KEY="YOUR_SK" && \
prowler huaweicloud
```

---

## 11. Prowler Server Web UI Dashboard

Prowler includes a built-in web server with a dashboard UI for viewing and managing scan results visually. This is useful for teams who want a centralized view of security findings without parsing JSON/CSV files.

### Step 1 — Install Prowler API/Server Dependencies

```bash
pip install prowler==5.31.0
```

The Prowler server is included in the standard package — no extra installation is needed.

### Step 2 — Apply the Provider Patches

Ensure the Huawei Cloud provider is installed and patched:

```bash
bash scripts/setup-prowler.sh python
```

### Step 3 — Start the Prowler Server

```bash
prowler server
```

By default the server starts on `http://localhost:8000`.

To run on a different host/port:

```bash
prowler server --host 0.0.0.0 --port 8080
```

### Step 4 — Open the Dashboard

Open your browser and navigate to:

```
http://localhost:8000
```

You will see the Prowler dashboard with options to:

- **View findings** — browse all scan results with filters by provider, service, severity, and status
- **Run scans** — trigger new scans directly from the UI (requires credentials configured)
- **Compare scans** — diff findings between two scan runs to track changes over time
- **Export reports** — download results as JSON, CSV, or HTML from the UI
- **View compliance** — see CIS benchmark compliance status at a glance

### Step 5 — Run a Scan via the API

You can also trigger scans programmatically via the REST API:

```bash
# Start the server first
prowler server &

# Trigger a Huawei Cloud scan via API
curl -X POST http://localhost:8000/api/scan \
    -H "Content-Type: application/json" \
    -d '{
        "provider": "huaweicloud",
        "access_key_id": "'"$HUAWEICLOUD_ACCESS_KEY_ID"'",
        "secret_access_key": "'"$HUAWEICLOUD_SECRET_ACCESS_KEY"'"
    }'
```

### Step 6 — Docker Compose with Dashboard

For a production deployment with a persistent database and dashboard:

```bash
# docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: "3.8"
services:
  prowler-server:
    image: prowlercloud/prowler:5.31.0
    command: server --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    environment:
      - HUAWEICLOUD_ACCESS_KEY_ID=${HUAWEICLOUD_ACCESS_KEY_ID}
      - HUAWEICLOUD_SECRET_ACCESS_KEY=${HUAWEICLOUD_SECRET_ACCESS_KEY}
    volumes:
      - prowler-data:/prowler/data
      - ./prowler/providers/huaweicloud:/prowler/prowler/providers/huaweicloud
      - ./prowler/compliance/huaweicloud:/prowler/prowler/compliance/huaweicloud

volumes:
  prowler-data:
EOF

docker compose up -d
```

Then open `http://localhost:8000`.

> **Note:** When using Docker, you still need to apply the core patches. Build a custom image with a Dockerfile that runs `scripts/setup-prowler.sh` after installing Prowler (see [Section 9](#9-docker-deployment)).

### Dashboard Tips

| Tip | Description |
|-----|-------------|
| **Persistent storage** | Mount a volume to `/prowler/data` so scan results survive container restarts |
| **Authentication** | Prowler server supports API key authentication — configure it for production deployments |
| **Reverse proxy** | Put nginx or Apache in front for TLS termination and access control |
| **Multi-provider** | The dashboard shows all providers — filter by `huaweicloud` to see only Huawei Cloud findings |
| **Compliance view** | Navigate to the Compliance tab and select `cis_1.0_huaweicloud` to see benchmark results |
