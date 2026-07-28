# Upstream PR Plan: Submit 42 New Huawei Cloud Checks to Prowler

## Background

- **PR #11950** (merged): Added Huawei Cloud provider with 25 checks across 10 services
- **Maintainer feedback**: Future PRs should include 1 check at a time
- **Total new checks to submit**: 42 (across 17 new services + 7 existing services)
- **Only 1 new CIS-mapped check**: `obs_bucket_encryption`

### Already merged services (10)
> cts, ecs, elb, evs, iam, kms, obs, rds, vpc, waf

### Already merged checks (25)

| Service | Check |
|---------|-------|
| cts | cts_enabled |
| ecs | ecs_instance_key_pair |
| ecs | ecs_instance_no_default_security_group |
| ecs | ecs_instance_public_ip |
| ecs | ecs_instance_security_groups_attached |
| elb | elb_public_exposure |
| evs | evs_volume_encryption |
| iam | iam_account_password_policy |
| iam | iam_password_policy_char_combination |
| iam | iam_password_policy_expires_passwords |
| iam | iam_password_policy_minimum_age |
| iam | iam_password_policy_reuse_prevention |
| iam | iam_root_hardware_mfa_enabled |
| iam | iam_user_disabled |
| iam | iam_user_mfa_enabled |
| kms | kms_key_not_pending_deletion |
| kms | kms_key_rotation_enabled |
| obs | obs_bucket_public_access |
| rds | rds_backup_enabled |
| rds | rds_instance_disk_encryption |
| rds | rds_public_access |
| vpc | vpc_default_security_group_restricts_all_traffic |
| vpc | vpc_security_group_all_protocols_open |
| vpc | vpc_security_group_open_ingress |
| waf | waf_enabled |

## Phased Submission Plan

Each check = 1 PR. For **new services** (not in merged PR), the first check PR
must also include service infrastructure files:
- `prowler/providers/huaweicloud/services/<service>/__init__.py`
- `prowler/providers/huaweicloud/services/<service>/<service>_client.py`
- `prowler/providers/huaweicloud/services/<service>/<service>_service.py`

### PR Workflow (per check)
```bash
# 1. Create branch from upstream main
git checkout -b feat/huaweicloud-<check_name> prowler-cloud/main

# 2. Copy check files from feat/huaweicloud-provider branch
git checkout feat/huaweicloud-provider -- <files>

# 3. If new service, also copy service infra files

# 4. Commit and push to fork
git add <files>
git commit --no-verify -m "feat(providers/huaweicloud): add <check_name> check"
git push fork-proper feat/huaweicloud-<check_name>

# 5. Create PR via GitHub API
curl -s -H "Authorization: token $TOKEN" \
  -d '{"title":"...","head":"tomitobio:feat/huaweicloud-<check>","base":"main","body":"..."}' \
  https://api.github.com/repos/prowler-cloud/prowler/pulls
```

### Phase 1: Critical Severity (3 PRs)

| PR # | Service | Check | Severity | New Service? | CIS | Title |
|------|---------|-------|----------|-------------|-----|-------|
| 1 | dcs | dcs_instance_not_public | critical | YES |  | DCS Redis instances are not publicly accessible |
| 2 | dcs | dcs_instance_password_enabled | critical |  |  | DCS Redis instances require password authentication |
| 3 | nat | nat_dnat_sensitive_ports | critical | YES |  | NAT Gateway DNAT rules do not expose sensitive ports to the internet |

### Phase 2: High Severity (8 PRs)

| PR # | Service | Check | Severity | New Service? | CIS | Title |
|------|---------|-------|----------|-------------|-----|-------|
| 4 | cce | cce_cluster_public_endpoint | high | YES |  | CCE clusters do not expose public API endpoints |
| 5 | cfw | cfw_firewall_enabled | high | YES |  | Cloud Firewall is enabled and active |
| 6 | config | config_compliance_rules | high | YES |  | Config (RMS) compliance rules are configured and enabled |
| 7 | config | config_tracker_enabled | high |  |  | Config (RMS) tracker is enabled for compliance monitoring |
| 8 | identitycenter | identitycenter_enabled | high | YES |  | Identity Center is enabled |
| 9 | obs | obs_bucket_encryption | high |  | YES | OBS buckets have encryption enabled |
| 10 | obs | obs_bucket_encryption_and_not_public | high |  |  | OBS buckets are encrypted and not publicly accessible |
| 11 | vpn | vpn_weak_encryption | high | YES |  | VPN connections do not use weak encryption algorithms |

### Phase 3: Medium Severity (21 PRs)

| PR # | Service | Check | Severity | New Service? | CIS | Title |
|------|---------|-------|----------|-------------|-----|-------|
| 12 | bms | bms_instance_public_ip | medium | YES |  | BMS instances should not have public IP addresses directly assigned |
| 13 | cbr | cbr_policy_retention | medium | YES |  | CBR backup policies have sufficient retention |
| 14 | cbr | cbr_vault_resources | medium |  |  | CBR vaults have resources associated |
| 15 | cce | cce_cluster_kubernetes_version | medium |  |  | CCE clusters run supported Kubernetes versions |
| 16 | ces | ces_alarm_rules_configured | medium | YES |  | CES alarm rules are configured and enabled |
| 17 | cts | cts_tracker_bucket_configured | medium |  |  | CTS tracker has an OBS bucket configured for trace file delivery |
| 18 | cts | cts_tracker_type_system | medium |  |  | CTS system-type tracker is configured and enabled |
| 19 | dcs | dcs_instance_ssl_enabled | medium |  |  | DCS Redis instances have SSL/TLS encryption enabled |
| 20 | ecs | ecs_instance_vpc_configured | medium |  |  | ECS instances should be deployed within a VPC |
| 21 | eip | eip_unassociated | medium | YES |  | All EIPs are associated with a resource |
| 22 | evs | evs_volume_kms_key_configured | medium |  |  | Encrypted EVS volumes have a KMS key ID configured |
| 23 | functiongraph | functiongraph_function_vpc_configured | medium | YES |  | FunctionGraph functions are configured within a VPC |
| 24 | iam | iam_password_policy_not_username | medium |  |  | IAM password policy prevents using username in passwords |
| 25 | iam | iam_user_password_not_expired | medium |  |  | IAM user passwords are not expired |
| 26 | identitycenter | identitycenter_permission_sets | medium |  |  | Identity Center has permission sets configured |
| 27 | lts | lts_log_group_retention | medium | YES |  | LTS log groups have adequate retention period |
| 28 | rds | rds_instance_high_availability | medium |  |  | RDS instances have high availability configured |
| 29 | rds | rds_instance_multi_az | medium |  |  | RDS instances are deployed across multiple availability zones |
| 30 | rds | rds_instance_ssl_enabled | medium |  |  | RDS instances have SSL enabled |
| 31 | sfs | sfs_file_system_encryption | medium | YES |  | SFS Turbo file systems have encryption enabled |
| 32 | vpc | vpc_security_group_open_egress | medium |  |  | VPC security groups do not allow open egress to the internet |

### Phase 4: Low Severity (10 PRs)

| PR # | Service | Check | Severity | New Service? | CIS | Title |
|------|---------|-------|----------|-------------|-----|-------|
| 33 | bms | bms_instance_default_security_group | low |  |  | BMS instances should not use the default security group |
| 34 | dns | dns_public_zones_exposed | low | YES |  | Public DNS zones do not expose internal infrastructure |
| 35 | ecs | ecs_instance_enterprise_project | low |  |  | ECS instances should be assigned to an enterprise project |
| 36 | elb | elb_load_balancer_configured | low |  |  | At least one ELB load balancer is configured |
| 37 | iam | iam_password_policy_max_consecutive_identical_chars | low |  |  | IAM password policy limits consecutive identical characters |
| 38 | iam | iam_password_policy_maximum_length | low |  |  | IAM password policy maximum length is 32 or greater |
| 39 | kms | kms_key_rotation_period | low |  |  | KMS keys with rotation enabled have a rotation period configured |
| 40 | smn | smn_topic_subscriptions | low | YES |  | SMN topics have at least one subscription configured |
| 41 | tms | tms_predefined_tags_configured | low | YES |  | TMS predefined tags should be configured |
| 42 | waf | waf_instance_configured | low |  |  | At least one WAF instance is configured |

### New Services Requiring Infrastructure (17 services)

These services are not in the merged PR. The first check PR for each must include
the service `__init__.py`, `*_client.py`, and `*_service.py` files.

> bms, cbr, cce, ces, cfw, config, dcs, dns, eip, functiongraph, identitycenter, lts, nat, sfs, smn, tms, vpn

### Files Required Per Check

For each check `<check>` in service `<service>`:
```
prowler/providers/huaweicloud/services/<service>/<check>/__init__.py
prowler/providers/huaweicloud/services/<service>/<check>/<check>.py
prowler/providers/huaweicloud/services/<service>/<check>/<check>.metadata.json
tests/providers/huaweicloud/services/<service>/<check>/<check>_test.py
tests/providers/huaweicloud/services/<service>/<check>/__init__.py
```
If new service, also:
```
prowler/providers/huaweicloud/services/<service>/__init__.py
prowler/providers/huaweicloud/services/<service>/<service>_client.py
prowler/providers/huaweicloud/services/<service>/<service>_service.py
tests/providers/huaweicloud/services/<service>/__init__.py
```

## Progress Tracking

| PR # | Check | Branch | PR URL | Status |
|------|-------|--------|--------|--------|
| 1 | dcs_instance_not_public | feat/huaweicloud-dcs_instance_not_public | - | pending |
| 2 | dcs_instance_password_enabled | feat/huaweicloud-dcs_instance_password_enabled | - | pending |
| 3 | nat_dnat_sensitive_ports | feat/huaweicloud-nat_dnat_sensitive_ports | - | pending |
| 4 | cce_cluster_public_endpoint | feat/huaweicloud-cce_cluster_public_endpoint | - | pending |
| 5 | cfw_firewall_enabled | feat/huaweicloud-cfw_firewall_enabled | - | pending |
| 6 | config_compliance_rules | feat/huaweicloud-config_compliance_rules | - | pending |
| 7 | config_tracker_enabled | feat/huaweicloud-config_tracker_enabled | - | pending |
| 8 | identitycenter_enabled | feat/huaweicloud-identitycenter_enabled | - | pending |
| 9 | obs_bucket_encryption | feat/huaweicloud-obs_bucket_encryption | - | pending |
| 10 | obs_bucket_encryption_and_not_public | feat/huaweicloud-obs_bucket_encryption_and_not_public | - | pending |
| 11 | vpn_weak_encryption | feat/huaweicloud-vpn_weak_encryption | - | pending |
| 12 | bms_instance_public_ip | feat/huaweicloud-bms_instance_public_ip | - | pending |
| 13 | cbr_policy_retention | feat/huaweicloud-cbr_policy_retention | - | pending |
| 14 | cbr_vault_resources | feat/huaweicloud-cbr_vault_resources | - | pending |
| 15 | cce_cluster_kubernetes_version | feat/huaweicloud-cce_cluster_kubernetes_version | - | pending |
| 16 | ces_alarm_rules_configured | feat/huaweicloud-ces_alarm_rules_configured | - | pending |
| 17 | cts_tracker_bucket_configured | feat/huaweicloud-cts_tracker_bucket_configured | - | pending |
| 18 | cts_tracker_type_system | feat/huaweicloud-cts_tracker_type_system | - | pending |
| 19 | dcs_instance_ssl_enabled | feat/huaweicloud-dcs_instance_ssl_enabled | - | pending |
| 20 | ecs_instance_vpc_configured | feat/huaweicloud-ecs_instance_vpc_configured | - | pending |
| 21 | eip_unassociated | feat/huaweicloud-eip_unassociated | - | pending |
| 22 | evs_volume_kms_key_configured | feat/huaweicloud-evs_volume_kms_key_configured | - | pending |
| 23 | functiongraph_function_vpc_configured | feat/huaweicloud-functiongraph_function_vpc_configured | - | pending |
| 24 | iam_password_policy_not_username | feat/huaweicloud-iam_password_policy_not_username | - | pending |
| 25 | iam_user_password_not_expired | feat/huaweicloud-iam_user_password_not_expired | - | pending |
| 26 | identitycenter_permission_sets | feat/huaweicloud-identitycenter_permission_sets | - | pending |
| 27 | lts_log_group_retention | feat/huaweicloud-lts_log_group_retention | - | pending |
| 28 | rds_instance_high_availability | feat/huaweicloud-rds_instance_high_availability | - | pending |
| 29 | rds_instance_multi_az | feat/huaweicloud-rds_instance_multi_az | - | pending |
| 30 | rds_instance_ssl_enabled | feat/huaweicloud-rds_instance_ssl_enabled | - | pending |
| 31 | sfs_file_system_encryption | feat/huaweicloud-sfs_file_system_encryption | - | pending |
| 32 | vpc_security_group_open_egress | feat/huaweicloud-vpc_security_group_open_egress | - | pending |
| 33 | bms_instance_default_security_group | feat/huaweicloud-bms_instance_default_security_group | - | pending |
| 34 | dns_public_zones_exposed | feat/huaweicloud-dns_public_zones_exposed | - | pending |
| 35 | ecs_instance_enterprise_project | feat/huaweicloud-ecs_instance_enterprise_project | - | pending |
| 36 | elb_load_balancer_configured | feat/huaweicloud-elb_load_balancer_configured | - | pending |
| 37 | iam_password_policy_max_consecutive_identical_chars | feat/huaweicloud-iam_password_policy_max_consecutive_identical_chars | - | pending |
| 38 | iam_password_policy_maximum_length | feat/huaweicloud-iam_password_policy_maximum_length | - | pending |
| 39 | kms_key_rotation_period | feat/huaweicloud-kms_key_rotation_period | - | pending |
| 40 | smn_topic_subscriptions | feat/huaweicloud-smn_topic_subscriptions | - | pending |
| 41 | tms_predefined_tags_configured | feat/huaweicloud-tms_predefined_tags_configured | - | pending |
| 42 | waf_instance_configured | feat/huaweicloud-waf_instance_configured | - | pending |
