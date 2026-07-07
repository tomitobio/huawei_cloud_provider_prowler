# Huawei Cloud Provider for Prowler

A custom [Prowler](https://github.com/prowler-cloud/prowler) provider for **Huawei Cloud**, implementing security best-practice checks across 10 services.

## Services & Checks

| Service | Check | Severity | Description |
|---------|-------|----------|-------------|
| CTS | `cts_enabled` | Medium | Ensure CTS tracker is enabled |
| ECS | `ecs_instance_public_ip` | Medium | Ensure ECS instances do not have public IPs |
| ELB | `elb_public_exposure` | Medium | Ensure ELB load balancers are not publicly exposed |
| EVS | `evs_volume_encryption` | Medium | Ensure EVS volumes are encrypted |
| IAM | `iam_account_password_policy` | Medium | Ensure IAM account password policy meets requirements |
| IAM | `iam_root_hardware_mfa_enabled` | Medium | Ensure root account has hardware MFA enabled |
| IAM | `iam_user_mfa_enabled` | Medium | Ensure IAM users have MFA enabled |
| KMS | `kms_key_rotation_enabled` | Medium | Ensure KMS keys have rotation enabled |
| OBS | `obs_bucket_encryption` | Medium | Ensure OBS buckets have encryption enabled |
| OBS | `obs_bucket_public_access` | Medium | Ensure OBS buckets do not allow public access |
| RDS | `rds_backup_enabled` | Medium | Ensure RDS instances have backup enabled |
| RDS | `rds_public_access` | Medium | Ensure RDS instances are not publicly accessible |
| VPC | `vpc_default_security_group_restricts_all_traffic` | Medium | Ensure default security group restricts all traffic |
| WAF | `waf_enabled` | Medium | Ensure WAF is enabled |

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

## Integration with Prowler Core

This provider follows the official Prowler developer guidelines:
- https://docs.prowler.com/developer-guide/introduction
- https://docs.prowler.com/developer-guide/provider

### Core File Modifications

To integrate this provider into a Prowler deployment, the following core files need modifications:

1. **`backend/api/models.py`** — Add `HUAWEICLOUD` to `Provider.ProviderChoices` enum and `validate_huaweicloud_uid` validator
2. **`backend/api/v1/serializers.py`** — Add `HuaweiCloudProviderSecret` serializer and provider case in `validate_secret_based_on_provider`
3. **`backend/api/utils.py`** — Add provider import in match statement, `get_prowler_provider_kwargs` case, and `prowler_provider_connection_test` case
4. **`prowler/lib/check/check.py`** — Add `_huaweicloud_checks` property
5. **`prowler/lib/check/models.py`** — Add `CheckReportHuaweiCloud` model
6. **`prowler/lib/outputs/finding.py`** — Add Huawei Cloud finding mapping
7. **`prowler/lib/outputs/outputs.py`** — Add Huawei Cloud output support
8. **`prowler/providers/common/provider.py`** — Add Huawei Cloud to provider registry

## License

This project is licensed under the Apache License 2.0 — same as Prowler.
