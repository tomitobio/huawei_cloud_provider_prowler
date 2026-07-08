# Huawei Cloud Provider for Prowler

A custom [Prowler](https://github.com/prowler-cloud/prowler) provider for **Huawei Cloud**, implementing 21 security best-practice checks across 10 services with a CIS compliance benchmark.

# Introduction

Hi, I am Tomas Tobio. As a student of Informatics Engineering and Huawei Cloud user, I saw the opportunity to use Prowler as I start to get into infrastructure cybersecurity. I hope this project (and repo) becomes the first of many in my professional journey.

## Services & Checks

| # | Service | Check | Severity | Description |
|---|---------|-------|----------|-------------|
| 1 | CTS | `cts_enabled` | Medium | Ensure CTS tracker is enabled to record all API calls |
| 2 | ECS | `ecs_instance_public_ip` | Medium | Ensure ECS instances do not have public IP addresses |
| 3 | ELB | `elb_public_exposure` | Medium | Ensure ELB load balancers are not publicly exposed |
| 4 | EVS | `evs_volume_encryption` | High | Ensure EVS volumes are encrypted to protect data at rest |
| 5 | IAM | `iam_account_password_policy` | Medium | Ensure IAM account password policy meets requirements |
| 6 | IAM | `iam_password_policy_char_combination` | Medium | Ensure password policy enforces character combination |
| 7 | IAM | `iam_password_policy_expires_passwords` | Medium | Ensure password policy enforces password expiration |
| 8 | IAM | `iam_password_policy_minimum_age` | Low | Ensure password policy enforces minimum password age |
| 9 | IAM | `iam_password_policy_reuse_prevention` | Medium | Ensure password policy prevents recent password reuse |
| 10 | IAM | `iam_root_hardware_mfa_enabled` | Critical | Ensure root account has hardware MFA enabled |
| 11 | IAM | `iam_user_disabled` | Low | Ensure disabled IAM user accounts are removed |
| 12 | IAM | `iam_user_mfa_enabled` | High | Ensure IAM users have MFA enabled |
| 13 | KMS | `kms_key_not_pending_deletion` | Medium | Ensure KMS keys are not in pending deletion state |
| 14 | KMS | `kms_key_rotation_enabled` | Medium | Ensure KMS keys have automatic rotation enabled |
| 15 | OBS | `obs_bucket_encryption` | High | Ensure OBS buckets have server-side encryption enabled |
| 16 | OBS | `obs_bucket_public_access` | Critical | Ensure OBS buckets are not publicly accessible |
| 17 | RDS | `rds_backup_enabled` | High | Ensure RDS instances have automated backup enabled |
| 18 | RDS | `rds_public_access` | Critical | Ensure RDS instances do not have public IP addresses |
| 19 | VPC | `vpc_default_security_group_restricts_all_traffic` | High | Ensure default security groups restrict all traffic |
| 20 | VPC | `vpc_security_group_open_ingress` | High | Ensure security groups don't allow open ingress on sensitive ports |
| 21 | WAF | `waf_enabled` | Medium | Ensure WAF is enabled to protect web applications |

### Severity Distribution

| Severity | Count |
|----------|-------|
| Critical | 4 |
| High | 7 |
| Medium | 8 |
| Low | 2 |

## CIS Compliance Benchmark

This provider includes a CIS Huawei Cloud 1.0 compliance benchmark that maps all 21 checks to 21 requirements across 8 sections:

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

Run a compliance scan:

```bash
prowler huaweicloud \
    --access-key-id YOUR_AK \
    --secret-access-key YOUR_SK \
    --region la-south-2 \
    --compliance cis_1.0_huaweicloud
```

List compliance checks:

```bash
prowler huaweicloud --compliance cis_1.0_huaweicloud --list-checks
```

## Provider Structure

```
prowler/providers/huaweicloud/
├── __init__.py
├── huaweicloud_provider.py      # Main provider class (HuaweicloudProvider)
├── models.py                     # Pydantic v1 models (credentials, session, identity)
├── config.py                     # Region list and constants
├── exceptions/
│   ├── __init__.py
│   └── exceptions.py
├── lib/
│   ├── arguments/arguments.py    # CLI argument parser
│   ├── mutelist/mutelist.py      # Mutelist support
│   └── service/service.py        # Base service class with threading
└── services/
    ├── cts/                      # Cloud Trace Service
    ├── ecs/                      # Elastic Cloud Server
    ├── elb/                      # Elastic Load Balance
    ├── evs/                      # Elastic Volume Service
    ├── iam/                      # Identity and Access Management
    ├── kms/                      # Key Management Service
    ├── obs/                      # Object Storage Service
    ├── rds/                      # Relational Database Service
    ├── vpc/                      # Virtual Private Cloud
    └── waf/                      # Web Application Firewall
```

Each service directory contains:
- `<service>_client.py` — SDK client wrapper
- `<service>_service.py` — Service model and data extraction
- `<check_name>/` — One directory per check with `<check_name>.py` and `<check_name>.metadata.json`

## Supported Regions

All Huawei Cloud regions are supported, including:
- `la-south-2` — Chile (Santiago)
- `sa-brazil-1` — Brazil (Sao Paulo)
- `na-mexico-1` — Mexico (Mexico City)
- `cn-north-4` — China (Beijing 4)
- `ap-southeast-1` — Singapore
- `ap-southeast-2` — Sydney
- `ap-southeast-3` — Jakarta
- `eu-west-101` — Ireland
- And more (see `config.py`)

## Prerequisites

### Huawei Cloud SDK Dependencies

```bash
pip install huaweicloudsdkcore huaweicloudsdkcts huaweicloudsdkecs huaweicloudsdkelb \
    huaweicloudsdkevs huaweicloudsdkiam huaweicloudsdkkms huaweicloudsdkobs \
    huaweicloudsdkrds huaweicloudsdkvpc huaweicloudsdkwaf
```

### Credentials

You need a Huawei Cloud IAM account with an Access Key ID and Secret Access Key. Create them in the Huawei Cloud console under **My Credentials**.

## Usage

### CLI

```bash
prowler huaweicloud \
    --access-key-id YOUR_AK \
    --secret-access-key YOUR_SK \
    --region la-south-2
```

### Prowler API/UI

Register the provider through the Prowler API or UI by providing:
- **Access Key ID**
- **Secret Access Key**
- **Region** (optional)

## Testing

Tests are located in `tests/` and use pytest. Each check has 3 test cases (PASS, FAIL, and edge cases).

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Set up prowler with provider + patches
bash scripts/setup-prowler.sh python

# Run tests
pytest -v
```

### CI/CD

GitHub Actions workflows run automatically on push and PR to `main`:
- **test** — Installs prowler, applies provider + patches, runs all 23 tests
- **lint** — Runs ruff on provider and test code

## Docker Deployment

The provider is deployed as part of a Prowler Docker stack. The Dockerfile copies the provider and patches after `uv sync`, and `docker-compose-dev.yml` mounts the provider as a volume for hot reload.

### Core File Modifications (Patches)

Five Prowler core files are patched to add Huawei Cloud support. These are stored in `patches/` and applied by `scripts/setup-prowler.sh`:

| Patch File | Modification |
|------------|-------------|
| `lib/check/check.py` | Add `_huaweicloud_checks` property |
| `lib/check/models.py` | Add `CheckReportHuaweiCloud` model |
| `lib/outputs/finding.py` | Add Huawei Cloud finding mapping |
| `lib/outputs/outputs.py` | Add Huawei Cloud output support |
| `providers/common/provider.py` | Add Huawei Cloud to provider registry |

Additionally, the Prowler API backend requires modifications (not included as patches since they're Django-specific):
- `backend/api/models.py` — Add `HUAWEICLOUD` to `Provider.ProviderChoices` enum
- `backend/api/v1/serializers.py` — Add `HuaweiCloudProviderSecret` serializer
- `backend/api/utils.py` — Add provider import and connection test

## Integration with Prowler Core

This provider follows the official Prowler developer guidelines:
- https://docs.prowler.com/developer-guide/introduction
- https://docs.prowler.com/developer-guide/provider

## License

This project is licensed under the Apache License 2.0 — same as Prowler.
