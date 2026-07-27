from unittest import mock

from tests.providers.huaweicloud.huaweicloud_fixtures import (
    set_mocked_huaweicloud_provider,
)


class TestRdsInstanceDiskEncryption:
    def test_instance_with_disk_encryption_passes(self):
        rds_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.rds.rds_instance_disk_encryption.rds_instance_disk_encryption.rds_client",
                new=rds_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.rds.rds_instance_disk_encryption.rds_instance_disk_encryption import (
                rds_instance_disk_encryption,
            )
            from prowler.providers.huaweicloud.services.rds.rds_service import RDSInstance

            instance = RDSInstance(
                id="rds-1",
                name="encrypted-db",
                status="ACTIVE",
                region="la-south-2",
                disk_encryption_id="kms-key-001",
            )
            rds_client.instances = [instance]
            rds_client.audited_account = "123456789012"

            check = rds_instance_disk_encryption()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert "kms-key-001" in result[0].status_extended

    def test_instance_without_disk_encryption_fails(self):
        rds_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.rds.rds_instance_disk_encryption.rds_instance_disk_encryption.rds_client",
                new=rds_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.rds.rds_instance_disk_encryption.rds_instance_disk_encryption import (
                rds_instance_disk_encryption,
            )
            from prowler.providers.huaweicloud.services.rds.rds_service import RDSInstance

            instance = RDSInstance(
                id="rds-1",
                name="unencrypted-db",
                status="ACTIVE",
                region="la-south-2",
                disk_encryption_id="",
            )
            rds_client.instances = [instance]
            rds_client.audited_account = "123456789012"

            check = rds_instance_disk_encryption()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert "does not have disk encryption" in result[0].status_extended

    def test_no_instances(self):
        rds_client = mock.MagicMock()

        with (
            mock.patch(
                "prowler.providers.common.provider.Provider.get_global_provider",
                return_value=set_mocked_huaweicloud_provider(),
            ),
            mock.patch(
                "prowler.providers.huaweicloud.services.rds.rds_instance_disk_encryption.rds_instance_disk_encryption.rds_client",
                new=rds_client,
            ),
        ):
            from prowler.providers.huaweicloud.services.rds.rds_instance_disk_encryption.rds_instance_disk_encryption import (
                rds_instance_disk_encryption,
            )

            rds_client.instances = []
            rds_client.audited_account = "123456789012"

            check = rds_instance_disk_encryption()
            result = check.execute()

            assert len(result) == 0
