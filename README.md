# Huawei Cloud Provider for Prowler

A custom [Prowler](https://github.com/prowler-cloud/prowler) provider for **Huawei Cloud**, implementing 67 security best-practice checks across 27 services with a CIS compliance benchmark.

# Introduction

Hi, I am Tomas Tobio. As a student of Informatics Engineering and Huawei Cloud user, I saw the opportunity to use Prowler as I start to get into infrastructure cybersecurity. I hope this project (and repo) becomes the first of many in my professional journey.

## Services & Checks

| # | Service | Check | Severity | Description |
|---|---------|-------|----------|-------------|
| 1 | BMS | `bms_instance_public_ip` | Medium | BMS instances should not have public IP addresses directly assigned |
| 2 | BMS | `bms_instance_default_security_group` | Low | BMS instances should not use the default security group |
| 3 | CBR | `cbr_policy_retention` | Medium | CBR backup policies have sufficient retention |
| 4 | CBR | `cbr_vault_resources` | Medium | CBR vaults have resources associated |
| 5 | CCE | `cce_cluster_public_endpoint` | High | CCE clusters do not expose public API endpoints |
| 6 | CCE | `cce_cluster_kubernetes_version` | Medium | CCE clusters run supported Kubernetes versions |
| 7 | CES | `ces_alarm_rules_configured` | Medium | CES alarm rules are configured and enabled |
| 8 | CFW | `cfw_firewall_enabled` | High | Cloud Firewall is enabled and active |
| 9 | Config (RMS) | `config_compliance_rules` | High | Config (RMS) compliance rules are configured and enabled |
| 10 | Config (RMS) | `config_tracker_enabled` | High | Config (RMS) tracker is enabled for compliance monitoring |
| 11 | CTS | `cts_enabled` | Medium | CTS tracker is enabled |
| 12 | CTS | `cts_tracker_bucket_configured` | Medium | CTS tracker has an OBS bucket configured for trace file delivery |
| 13 | CTS | `cts_tracker_type_system` | Medium | CTS system-type tracker is configured and enabled |
| 14 | DCS | `dcs_instance_not_public` | Critical | DCS Redis instances are not publicly accessible |
| 15 | DCS | `dcs_instance_password_enabled` | Critical | DCS Redis instances require password authentication |
| 16 | DCS | `dcs_instance_ssl_enabled` | Medium | DCS Redis instances have SSL/TLS encryption enabled |
| 17 | DNS | `dns_public_zones_exposed` | Low | Public DNS zones do not expose internal infrastructure |
| 18 | ECS | `ecs_instance_key_pair` | High | ECS instances should use SSH key pairs for authentication |
| 19 | ECS | `ecs_instance_no_default_security_group` | Medium | ECS instances should not use the default security group |
| 20 | ECS | `ecs_instance_public_ip` | Medium | ECS instances should not have public IP addresses |
| 21 | ECS | `ecs_instance_security_groups_attached` | Medium | ECS instances should have security groups attached |
| 22 | ECS | `ecs_instance_vpc_configured` | Medium | ECS instances should be deployed within a VPC |
| 23 | ECS | `ecs_instance_enterprise_project` | Low | ECS instances should be assigned to an enterprise project |
| 24 | EIP | `eip_unassociated` | Medium | All EIPs are associated with a resource |
| 25 | ELB | `elb_public_exposure` | Medium | ELB load balancers should not have public IP addresses |
| 26 | ELB | `elb_load_balancer_configured` | Low | At least one ELB load balancer is configured |
| 27 | EVS | `evs_volume_encryption` | High | EVS volumes are encrypted |
| 28 | EVS | `evs_volume_kms_key_configured` | Medium | Encrypted EVS volumes have a KMS key ID configured |
| 29 | FunctionGraph | `functiongraph_function_vpc_configured` | Medium | FunctionGraph functions are configured within a VPC |
| 30 | IAM | `iam_root_hardware_mfa_enabled` | Critical | Root account has MFA enabled |
| 31 | IAM | `iam_user_mfa_enabled` | High | IAM users have MFA enabled |
| 32 | IAM | `iam_account_password_policy` | Medium | IAM password policy requires a minimum length of 14 or greater |
| 33 | IAM | `iam_password_policy_char_combination` | Medium | IAM password policy requires at least 3 character types |
| 34 | IAM | `iam_password_policy_expires_passwords` | Medium | IAM password policy requires passwords to expire |
| 35 | IAM | `iam_password_policy_not_username` | Medium | IAM password policy prevents using username in passwords |
| 36 | IAM | `iam_password_policy_reuse_prevention` | Medium | IAM password policy prevents reuse of at least 3 previous passwords |
| 37 | IAM | `iam_user_password_not_expired` | Medium | IAM user passwords are not expired |
| 38 | IAM | `iam_password_policy_max_consecutive_identical_chars` | Low | IAM password policy limits consecutive identical characters |
| 39 | IAM | `iam_password_policy_maximum_length` | Low | IAM password policy maximum length is 32 or greater |
| 40 | IAM | `iam_password_policy_minimum_age` | Low | IAM password policy enforces a minimum password age |
| 41 | IAM | `iam_user_disabled` | Low | IAM disabled users are reviewed and removed if stale |
| 42 | Identity Center | `identitycenter_enabled` | High | Identity Center is enabled |
| 43 | Identity Center | `identitycenter_permission_sets` | Medium | Identity Center has permission sets configured |
| 44 | KMS | `kms_key_not_pending_deletion` | Medium | KMS keys are not in pending deletion state |
| 45 | KMS | `kms_key_rotation_enabled` | Medium | KMS keys have rotation enabled |
| 46 | KMS | `kms_key_rotation_period` | Low | KMS keys with rotation enabled have a rotation period configured |
| 47 | LTS | `lts_log_group_retention` | Medium | LTS log groups have adequate retention period |
| 48 | NAT | `nat_dnat_sensitive_ports` | Critical | NAT Gateway DNAT rules do not expose sensitive ports to the internet |
| 49 | OBS | `obs_bucket_public_access` | Critical | OBS buckets are not publicly accessible |
| 50 | OBS | `obs_bucket_encryption` | High | OBS buckets have encryption enabled |
| 51 | OBS | `obs_bucket_encryption_and_not_public` | High | OBS buckets are encrypted and not publicly accessible |
| 52 | RDS | `rds_public_access` | Critical | RDS instances are not publicly accessible |
| 53 | RDS | `rds_backup_enabled` | High | RDS instances have automated backup enabled |
| 54 | RDS | `rds_instance_disk_encryption` | High | RDS instances should have disk encryption enabled |
| 55 | RDS | `rds_instance_high_availability` | Medium | RDS instances have high availability configured |
| 56 | RDS | `rds_instance_multi_az` | Medium | RDS instances are deployed across multiple availability zones |
| 57 | RDS | `rds_instance_ssl_enabled` | Medium | RDS instances have SSL enabled |
| 58 | SFS | `sfs_file_system_encryption` | Medium | SFS Turbo file systems have encryption enabled |
| 59 | SMN | `smn_topic_subscriptions` | Low | SMN topics have at least one subscription configured |
| 60 | TMS | `tms_predefined_tags_configured` | Low | TMS predefined tags should be configured |
| 61 | VPC | `vpc_default_security_group_restricts_all_traffic` | High | Default security groups restrict all traffic |
| 62 | VPC | `vpc_security_group_all_protocols_open` | High | VPC security groups should not allow ingress from 0.0.0.0/0 on all ports/protocols |
| 63 | VPC | `vpc_security_group_open_ingress` | High | VPC security groups do not allow open ingress on sensitive ports |
| 64 | VPC | `vpc_security_group_open_egress` | Medium | VPC security groups do not allow open egress to the internet |
| 65 | VPN | `vpn_weak_encryption` | High | VPN connections do not use weak encryption algorithms |
| 66 | WAF | `waf_enabled` | Medium | WAF (Web Application Firewall) is enabled |
| 67 | WAF | `waf_instance_configured` | Low | At least one WAF instance is configured |

### Severity Distribution

| Severity | Count |
|----------|-------|
| Critical | 6 |
| High | 16 |
| Medium | 33 |
| Low | 12 |

## CIS Compliance Benchmark

This provider includes a CIS Huawei Cloud 1.0 compliance benchmark that maps 21 of the 67 checks to 21 requirements across 8 sections:

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
    ├── bms/                      # Bare Metal Server
    ├── cbr/                      # Cloud Backup and Recovery
    ├── cce/                      # Cloud Container Engine
    ├── ces/                      # Cloud Eye Service
    ├── cfw/                      # Cloud Firewall
    ├── config/                   # Resource Configuration (RMS)
    ├── cts/                      # Cloud Trace Service
    ├── dcs/                      # Distributed Cache Service
    ├── dns/                      # Domain Name Service
    ├── ecs/                      # Elastic Cloud Server
    ├── eip/                      # Elastic IP
    ├── elb/                      # Elastic Load Balance
    ├── evs/                      # Elastic Volume Service
    ├── functiongraph/            # FunctionGraph
    ├── iam/                      # Identity and Access Management
    ├── identitycenter/           # Identity Center
    ├── kms/                      # Key Management Service
    ├── lts/                      # Log Tank Service
    ├── nat/                      # NAT Gateway
    ├── obs/                      # Object Storage Service
    ├── rds/                      # Relational Database Service
    ├── sfs/                      # Scalable File Service
    ├── smn/                      # Simple Message Notification
    ├── tms/                      # Tag Management Service
    ├── vpc/                      # Virtual Private Cloud
    ├── vpn/                      # Virtual Private Network
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
pip install huaweicloudsdkcore huaweicloudsdkbms huaweicloudsdkcbr huaweicloudsdkcce \
    huaweicloudsdkces huaweicloudsdkcfw huaweicloudsdkcts huaweicloudsdkdcs \
    huaweicloudsdkdns huaweicloudsdkecs huaweicloudsdkeip huaweicloudsdkelb \
    huaweicloudsdkevs huaweicloudsdkfunctiongraph huaweicloudsdkiam \
    huaweicloudsdkidentitycenter huaweicloudsdkkms huaweicloudsdklts \
    huaweicloudsdknat huaweicloudsdkobs huaweicloudsdkrds huaweicloudsdkrms \
    huaweicloudsdksfsturbo huaweicloudsdksmn huaweicloudsdktms \
    huaweicloudsdkvpc huaweicloudsdkvpn huaweicloudsdkwaf
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

Tests are located in `tests/providers/huaweicloud/` and use pytest. Each check has 3+ test cases (PASS, FAIL, and edge cases), totaling 228 tests across 116 test files.

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Set up prowler with provider + patches
bash scripts/setup-prowler.sh python

# Run tests
pytest tests/providers/huaweicloud/ -v
```

### CI/CD

GitHub Actions workflows run automatically on push and PR to `main`:
- **test** — Installs prowler, applies provider + patches, runs all 228 tests
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
