from typing import List

from pydantic.v1 import BaseModel

from prowler.lib.logger import logger
from prowler.providers.huaweicloud.lib.service.service import HuaweiCloudService


class OBS(HuaweiCloudService):
    """
    OBS (Object Storage Service) service class for Huawei Cloud.

    This class provides methods to interact with Huawei Cloud OBS service
    to retrieve buckets and their configuration.
    """

    def __init__(self, provider):
        super().__init__(__class__.__name__, provider, global_service=True)

        self.buckets: List[Bucket] = []

        if self.session.is_mock:
            self._load_mock_data()
            return

        self._list_buckets()

    def _load_mock_data(self):
        """Load mock data for testing."""
        region = "la-south-2"
        self.buckets = [
            Bucket(
                name="mock-public-encrypted-bucket", region=region,
                is_encrypted=True, is_public=True, acl="public",
            ),
            Bucket(
                name="mock-private-unencrypted-bucket", region=region,
                is_encrypted=False, is_public=False, acl="private",
            ),
            Bucket(
                name="mock-private-encrypted-bucket", region=region,
                is_encrypted=True, is_public=False, acl="private",
            ),
        ]

    def _list_buckets(self):
        """List all OBS buckets."""
        if not self.client:
            return

        region = self.region
        client = self.client
        logger.info(f"OBS - Listing Buckets in {region}...")

        try:
            from huaweicloudsdkobs.v1 import (
                ListBucketsRequest,
                GetBucketAclRequest,
                GetBucketPublicStatusRequest,
            )

            response = self._call_with_retries(
                client.list_buckets, ListBucketsRequest()
            )

            if response and response.buckets:
                buckets_list = getattr(response.buckets, "bucket", None) or []
                for bucket_data in buckets_list:
                    bucket_name = getattr(bucket_data, "name", "")
                    bucket_region = getattr(bucket_data, "location", region)

                    is_encrypted = False
                    is_public = False
                    acl = "private"

                    try:
                        public_response = self._call_with_retries(
                            client.get_bucket_public_status,
                            GetBucketPublicStatusRequest(bucket_name=bucket_name),
                        )
                        if public_response and getattr(
                            public_response, "is_public", False
                        ):
                            is_public = True
                            acl = "public"
                    except Exception as public_error:
                        logger.error(
                            f"OBS - Public status check failed for bucket {bucket_name}: {public_error}"
                        )

                    try:
                        acl_response = self._call_with_retries(
                            client.get_bucket_acl,
                            GetBucketAclRequest(bucket_name=bucket_name),
                        )
                        if acl_response and acl_response.access_control_list:
                            grants = getattr(
                                acl_response.access_control_list, "grant", []
                            )
                            for grant in grants:
                                grantee = getattr(grant, "grantee", None)
                                if grantee:
                                    grantee_canned = getattr(grantee, "canned", "")
                                    if grantee_canned in ("AllUsers", "Everyone"):
                                        is_public = True
                                        acl = "public"
                    except Exception as acl_error:
                        logger.error(
                            f"OBS - ACL check failed for bucket {bucket_name}: {acl_error}"
                        )

                    self.buckets.append(
                        Bucket(
                            name=bucket_name,
                            region=bucket_region,
                            is_encrypted=is_encrypted,
                            is_public=is_public,
                            acl=acl,
                        )
                    )

        except Exception as error:
            logger.error(
                f"{region} -- {error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
            )


class Bucket(BaseModel):
    """OBS Bucket model."""

    name: str
    region: str = ""
    is_encrypted: bool = False
    is_public: bool = False
    acl: str = ""
