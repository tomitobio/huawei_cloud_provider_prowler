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
| #12168 | dcs | dcs_instance_not_public | critical | YES |  | DCS Redis instances are not publicly accessible |
| #12169 | dcs | dcs_instance_password_enabled | critical |  |  | DCS Redis instances require password authentication |
| #12170 | nat | nat_dnat_sensitive_ports | critical | YES |  | NAT Gateway DNAT rules do not expose sensitive ports to the internet |

### Phase 2: High Severity (8 PRs)

| PR # | Service | Check | Severity | New Service? | CIS | Title |
|------|---------|-------|----------|-------------|-----|-------|
| #12181 | cce | cce_cluster_public_endpoint | high | YES |  | CCE clusters do not expose public API endpoints |
| #12171 | cfw | cfw_firewall_enabled | high | YES |  | Cloud Firewall is enabled and active |
| #12172 | config | config_compliance_rules | high | YES |  | Config (RMS) compliance rules are configured and enabled |
| #12173 | config | config_tracker_enabled | high |  |  | Config (RMS) tracker is enabled for compliance monitoring |
| #12174 | identitycenter | identitycenter_enabled | high | YES |  | Identity Center is enabled |
| #12176 | obs | obs_bucket_encryption | high |  | YES | OBS buckets have encryption enabled |
| #12175 | obs | obs_bucket_encryption_and_not_public | high |  |  | OBS buckets are encrypted and not publicly accessible |
| #12177 | vpn | vpn_weak_encryption | high | YES |  | VPN connections do not use weak encryption algorithms |

### Phase 3: Medium Severity (21 PRs)

| PR # | Service | Check | Severity | New Service? | CIS | Title |
|------|---------|-------|----------|-------------|-----|-------|
| #12189 | bms | bms_instance_public_ip | medium | YES |  | BMS instances should not have public IP addresses directly assigned |
| #12190 | cbr | cbr_policy_retention | medium | YES |  | CBR backup policies have sufficient retention |
| #12191 | cbr | cbr_vault_resources | medium |  |  | CBR vaults have resources associated |
| #12192 | cce | cce_cluster_kubernetes_version | medium |  |  | CCE clusters run supported Kubernetes versions |
| #12193 | ces | ces_alarm_rules_configured | medium | YES |  | CES alarm rules are configured and enabled |
| #12194 | cts | cts_tracker_bucket_configured | medium |  |  | CTS tracker has an OBS bucket configured for trace file delivery |
| #12195 | cts | cts_tracker_type_system | medium |  |  | CTS system-type tracker is configured and enabled |
| #12196 | dcs | dcs_instance_ssl_enabled | medium |  |  | DCS Redis instances have SSL/TLS encryption enabled |
| #12197 | ecs | ecs_instance_vpc_configured | medium |  |  | ECS instances should be deployed within a VPC |
| #12198 | eip | eip_unassociated | medium | YES |  | All EIPs are associated with a resource |
| #12199 | evs | evs_volume_kms_key_configured | medium |  |  | Encrypted EVS volumes have a KMS key ID configured |
| #12200 | functiongraph | functiongraph_function_vpc_configured | medium | YES |  | FunctionGraph functions are configured within a VPC |
| #12201 | iam | iam_password_policy_not_username | medium |  |  | IAM password policy prevents using username in passwords |
| #12202 | iam | iam_user_password_not_expired | medium |  |  | IAM user passwords are not expired |
| #12203 | identitycenter | identitycenter_permission_sets | medium |  |  | Identity Center has permission sets configured |
| #12204 | lts | lts_log_group_retention | medium | YES |  | LTS log groups have adequate retention period |
| #12205 | rds | rds_instance_high_availability | medium |  |  | RDS instances have high availability configured |
| #12206 | rds | rds_instance_multi_az | medium |  |  | RDS instances are deployed across multiple availability zones |
| #12207 | rds | rds_instance_ssl_enabled | medium |  |  | RDS instances have SSL enabled |
| #12208 | sfs | sfs_file_system_encryption | medium | YES |  | SFS Turbo file systems have encryption enabled |
| #12209 | vpc | vpc_security_group_open_egress | medium |  |  | VPC security groups do not allow open egress to the internet |

### Phase 4: Low Severity (10 PRs)

| PR # | Service | Check | Severity | New Service? | CIS | Title |
|------|---------|-------|----------|-------------|-----|-------|
| #12178 | bms | bms_instance_default_security_group | low |  |  | BMS instances should not use the default security group |
| #12179 | dns | dns_public_zones_exposed | low | YES |  | Public DNS zones do not expose internal infrastructure |
| #12180 | ecs | ecs_instance_enterprise_project | low |  |  | ECS instances should be assigned to an enterprise project |
| #12182 | elb | elb_load_balancer_configured | low |  |  | At least one ELB load balancer is configured |
| #12183 | iam | iam_password_policy_max_consecutive_identical_chars | low |  |  | IAM password policy limits consecutive identical characters |
| #12184 | iam | iam_password_policy_maximum_length | low |  |  | IAM password policy maximum length is 32 or greater |
| #12185 | kms | kms_key_rotation_period | low |  |  | KMS keys with rotation enabled have a rotation period configured |
| #12186 | smn | smn_topic_subscriptions | low | YES |  | SMN topics have at least one subscription configured |
| #12187 | tms | tms_predefined_tags_configured | low | YES |  | TMS predefined tags should be configured |
| #12188 | waf | waf_instance_configured | low |  |  | At least one WAF instance is configured |

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
| 1 | dcs_instance_not_public | feat/huaweicloud-dcs_instance_not_public | [#12168](https://github.com/prowler-cloud/prowler/pull/12168) | submitted |
| 2 | dcs_instance_password_enabled | feat/huaweicloud-dcs_instance_password_enabled | [#12169](https://github.com/prowler-cloud/prowler/pull/12169) | submitted |
| 3 | nat_dnat_sensitive_ports | feat/huaweicloud-nat_dnat_sensitive_ports | [#12170](https://github.com/prowler-cloud/prowler/pull/12170) | submitted |
| 4 | cce_cluster_public_endpoint | feat/huaweicloud-cce_cluster_public_endpoint | [#12181](https://github.com/prowler-cloud/prowler/pull/12181) | submitted |
| 5 | cfw_firewall_enabled | feat/huaweicloud-cfw_firewall_enabled | [#12171](https://github.com/prowler-cloud/prowler/pull/12171) | submitted |
| 6 | config_compliance_rules | feat/huaweicloud-config_compliance_rules | [#12172](https://github.com/prowler-cloud/prowler/pull/12172) | submitted |
| 7 | config_tracker_enabled | feat/huaweicloud-config_tracker_enabled | [#12173](https://github.com/prowler-cloud/prowler/pull/12173) | submitted |
| 8 | identitycenter_enabled | feat/huaweicloud-identitycenter_enabled | [#12174](https://github.com/prowler-cloud/prowler/pull/12174) | submitted |
| 9 | obs_bucket_encryption | feat/huaweicloud-obs_bucket_encryption | [#12176](https://github.com/prowler-cloud/prowler/pull/12176) | submitted |
| 10 | obs_bucket_encryption_and_not_public | feat/huaweicloud-obs_bucket_encryption_and_not_public | [#12175](https://github.com/prowler-cloud/prowler/pull/12175) | submitted |
| 11 | vpn_weak_encryption | feat/huaweicloud-vpn_weak_encryption | [#12177](https://github.com/prowler-cloud/prowler/pull/12177) | submitted |
| 12 | bms_instance_public_ip | feat/huaweicloud-bms_instance_public_ip | [#12189](https://github.com/prowler-cloud/prowler/pull/12189) | submitted |
| 13 | cbr_policy_retention | feat/huaweicloud-cbr_policy_retention | [#12190](https://github.com/prowler-cloud/prowler/pull/12190) | submitted |
| 14 | cbr_vault_resources | feat/huaweicloud-cbr_vault_resources | [#12191](https://github.com/prowler-cloud/prowler/pull/12191) | submitted |
| 15 | cce_cluster_kubernetes_version | feat/huaweicloud-cce_cluster_kubernetes_version | [#12192](https://github.com/prowler-cloud/prowler/pull/12192) | submitted |
| 16 | ces_alarm_rules_configured | feat/huaweicloud-ces_alarm_rules_configured | [#12193](https://github.com/prowler-cloud/prowler/pull/12193) | submitted |
| 17 | cts_tracker_bucket_configured | feat/huaweicloud-cts_tracker_bucket_configured | [#12194](https://github.com/prowler-cloud/prowler/pull/12194) | submitted |
| 18 | cts_tracker_type_system | feat/huaweicloud-cts_tracker_type_system | [#12195](https://github.com/prowler-cloud/prowler/pull/12195) | submitted |
| 19 | dcs_instance_ssl_enabled | feat/huaweicloud-dcs_instance_ssl_enabled | [#12196](https://github.com/prowler-cloud/prowler/pull/12196) | submitted |
| 20 | ecs_instance_vpc_configured | feat/huaweicloud-ecs_instance_vpc_configured | [#12197](https://github.com/prowler-cloud/prowler/pull/12197) | submitted |
| 21 | eip_unassociated | feat/huaweicloud-eip_unassociated | [#12198](https://github.com/prowler-cloud/prowler/pull/12198) | submitted |
| 22 | evs_volume_kms_key_configured | feat/huaweicloud-evs_volume_kms_key_configured | [#12199](https://github.com/prowler-cloud/prowler/pull/12199) | submitted |
| 23 | functiongraph_function_vpc_configured | feat/huaweicloud-functiongraph_function_vpc_configured | [#12200](https://github.com/prowler-cloud/prowler/pull/12200) | submitted |
| 24 | iam_password_policy_not_username | feat/huaweicloud-iam_password_policy_not_username | [#12201](https://github.com/prowler-cloud/prowler/pull/12201) | submitted |
| 25 | iam_user_password_not_expired | feat/huaweicloud-iam_user_password_not_expired | [#12202](https://github.com/prowler-cloud/prowler/pull/12202) | submitted |
| 26 | identitycenter_permission_sets | feat/huaweicloud-identitycenter_permission_sets | [#12203](https://github.com/prowler-cloud/prowler/pull/12203) | submitted |
| 27 | lts_log_group_retention | feat/huaweicloud-lts_log_group_retention | [#12204](https://github.com/prowler-cloud/prowler/pull/12204) | submitted |
| 28 | rds_instance_high_availability | feat/huaweicloud-rds_instance_high_availability | [#12205](https://github.com/prowler-cloud/prowler/pull/12205) | submitted |
| 29 | rds_instance_multi_az | feat/huaweicloud-rds_instance_multi_az | [#12206](https://github.com/prowler-cloud/prowler/pull/12206) | submitted |
| 30 | rds_instance_ssl_enabled | feat/huaweicloud-rds_instance_ssl_enabled | [#12207](https://github.com/prowler-cloud/prowler/pull/12207) | submitted |
| 31 | sfs_file_system_encryption | feat/huaweicloud-sfs_file_system_encryption | [#12208](https://github.com/prowler-cloud/prowler/pull/12208) | submitted |
| 32 | vpc_security_group_open_egress | feat/huaweicloud-vpc_security_group_open_egress | [#12209](https://github.com/prowler-cloud/prowler/pull/12209) | submitted |
| 33 | bms_instance_default_security_group | feat/huaweicloud-bms_instance_default_security_group | [#12178](https://github.com/prowler-cloud/prowler/pull/12178) | submitted |
| 34 | dns_public_zones_exposed | feat/huaweicloud-dns_public_zones_exposed | [#12179](https://github.com/prowler-cloud/prowler/pull/12179) | submitted |
| 35 | ecs_instance_enterprise_project | feat/huaweicloud-ecs_instance_enterprise_project | [#12180](https://github.com/prowler-cloud/prowler/pull/12180) | submitted |
| 36 | elb_load_balancer_configured | feat/huaweicloud-elb_load_balancer_configured | [#12182](https://github.com/prowler-cloud/prowler/pull/12182) | submitted |
| 37 | iam_password_policy_max_consecutive_identical_chars | feat/huaweicloud-iam_password_policy_max_consecutive_identical_chars | [#12183](https://github.com/prowler-cloud/prowler/pull/12183) | submitted |
| 38 | iam_password_policy_maximum_length | feat/huaweicloud-iam_password_policy_maximum_length | [#12184](https://github.com/prowler-cloud/prowler/pull/12184) | submitted |
| 39 | kms_key_rotation_period | feat/huaweicloud-kms_key_rotation_period | [#12185](https://github.com/prowler-cloud/prowler/pull/12185) | submitted |
| 40 | smn_topic_subscriptions | feat/huaweicloud-smn_topic_subscriptions | [#12186](https://github.com/prowler-cloud/prowler/pull/12186) | submitted |
| 41 | tms_predefined_tags_configured | feat/huaweicloud-tms_predefined_tags_configured | [#12187](https://github.com/prowler-cloud/prowler/pull/12187) | submitted |
| 42 | waf_instance_configured | feat/huaweicloud-waf_instance_configured | [#12188](https://github.com/prowler-cloud/prowler/pull/12188) | submitted |
