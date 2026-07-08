from unittest import mock

from tests.providers.huaweicloud.huaweicloud_fixtures import (
    set_mocked_huaweicloud_provider,
)


class TestEcsInstanceNoDefaultSecurityGroup:
    def test_no_default_sg_passes(self):
        ecs_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group.ecs_client",
                new=ecs_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group import (
                ecs_instance_no_default_security_group,
            )
            from prowler.providers.huaweicloud.services.ecs.ecs_service import (
                Instance,
            )

            ecs_client.instances = {
                "ecs-1": Instance(
                    id="ecs-1",
                    name="web-server",
                    region="la-south-2",
                    status="ACTIVE",
                    security_groups={"sg-1": "custom-sg"},
                ),
            }
            ecs_client.audited_account = "123456789012"

            check = ecs_instance_no_default_security_group()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert "does not use the default" in result[0].status_extended

    def test_default_sg_by_name_fails(self):
        ecs_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group.ecs_client",
                new=ecs_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group import (
                ecs_instance_no_default_security_group,
            )
            from prowler.providers.huaweicloud.services.ecs.ecs_service import (
                Instance,
            )

            ecs_client.instances = {
                "ecs-1": Instance(
                    id="ecs-1",
                    name="web-server",
                    region="la-south-2",
                    status="ACTIVE",
                    security_groups={"sg-default": "default"},
                ),
            }
            ecs_client.audited_account = "123456789012"

            check = ecs_instance_no_default_security_group()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert "default" in result[0].status_extended

    def test_default_sg_by_id_fails(self):
        ecs_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group.ecs_client",
                new=ecs_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group import (
                ecs_instance_no_default_security_group,
            )
            from prowler.providers.huaweicloud.services.ecs.ecs_service import (
                Instance,
            )

            ecs_client.instances = {
                "ecs-1": Instance(
                    id="ecs-1",
                    name="web-server",
                    region="la-south-2",
                    status="ACTIVE",
                    security_groups={"default": "my-sg"},
                ),
            }
            ecs_client.audited_account = "123456789012"

            check = ecs_instance_no_default_security_group()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"

    def test_no_instances(self):
        ecs_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group.ecs_client",
                new=ecs_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.ecs.ecs_instance_no_default_security_group.ecs_instance_no_default_security_group import (
                ecs_instance_no_default_security_group,
            )

            ecs_client.instances = {}
            ecs_client.audited_account = "123456789012"

            check = ecs_instance_no_default_security_group()
            result = check.execute()

            assert len(result) == 0
