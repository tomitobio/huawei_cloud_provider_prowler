from unittest import mock

from tests.providers.huaweicloud.huaweicloud_fixtures import (
    set_mocked_huaweicloud_provider,
)


class TestVpcSecurityGroupAllProtocolsOpen:
    def test_all_protocols_open_fails(self):
        vpc_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open.vpc_client",
                new=vpc_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open import (
                vpc_security_group_all_protocols_open,
            )
            from prowler.providers.huaweicloud.services.vpc.vpc_service import (
                SecurityGroups,
                SecurityGroupRule,
            )

            vpc_client.security_groups = {
                "sg-1": SecurityGroups(
                    id="sg-1",
                    name="open-sg",
                    region="la-south-2",
                    vpc_id="vpc-1",
                    rules=[
                        SecurityGroupRule(
                            id="rule-1",
                            direction="ingress",
                            protocol="all",
                            ethertype="IPv4",
                            remote_ip_prefix="0.0.0.0/0",
                        ),
                    ],
                ),
            }
            vpc_client.audited_account = "123456789012"

            check = vpc_security_group_all_protocols_open()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert "all ports" in result[0].status_extended

    def test_specific_port_passes(self):
        vpc_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open.vpc_client",
                new=vpc_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open import (
                vpc_security_group_all_protocols_open,
            )
            from prowler.providers.huaweicloud.services.vpc.vpc_service import (
                SecurityGroups,
                SecurityGroupRule,
            )

            vpc_client.security_groups = {
                "sg-1": SecurityGroups(
                    id="sg-1",
                    name="restricted-sg",
                    region="la-south-2",
                    vpc_id="vpc-1",
                    rules=[
                        SecurityGroupRule(
                            id="rule-1",
                            direction="ingress",
                            protocol="tcp",
                            ethertype="IPv4",
                            remote_ip_prefix="0.0.0.0/0",
                            port_range_min=443,
                            port_range_max=443,
                        ),
                    ],
                ),
            }
            vpc_client.audited_account = "123456789012"

            check = vpc_security_group_all_protocols_open()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"

    def test_all_protocols_restricted_ip_passes(self):
        vpc_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open.vpc_client",
                new=vpc_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open import (
                vpc_security_group_all_protocols_open,
            )
            from prowler.providers.huaweicloud.services.vpc.vpc_service import (
                SecurityGroups,
                SecurityGroupRule,
            )

            vpc_client.security_groups = {
                "sg-1": SecurityGroups(
                    id="sg-1",
                    name="restricted-sg",
                    region="la-south-2",
                    vpc_id="vpc-1",
                    rules=[
                        SecurityGroupRule(
                            id="rule-1",
                            direction="ingress",
                            protocol="all",
                            ethertype="IPv4",
                            remote_ip_prefix="10.0.0.0/24",
                        ),
                    ],
                ),
            }
            vpc_client.audited_account = "123456789012"

            check = vpc_security_group_all_protocols_open()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"

    def test_no_security_groups(self):
        vpc_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open.vpc_client",
                new=vpc_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.vpc.vpc_security_group_all_protocols_open.vpc_security_group_all_protocols_open import (
                vpc_security_group_all_protocols_open,
            )

            vpc_client.security_groups = {}
            vpc_client.audited_account = "123456789012"

            check = vpc_security_group_all_protocols_open()
            result = check.execute()

            assert len(result) == 0
