import { Control } from "react-hook-form";

import { WizardInputField } from "@/components/providers/workflow/forms/fields";
import { ProviderCredentialFields } from "@/lib/provider-credentials/provider-credential-fields";
import { HuaweiCloudCredentials } from "@/types";

export const HuaweiCloudStaticCredentialsForm = ({
  control,
}: {
  control: Control<HuaweiCloudCredentials>;
}) => {
  return (
    <>
      <div className="flex flex-col">
        <div className="text-md text-default-foreground leading-9 font-bold">
          Connect via Access Keys
        </div>
        <div className="text-default-500 text-sm">
          Provide an IAM user Access Key ID and Secret Access Key with read
          access to the resources you want Prowler to assess.
        </div>
      </div>
      <WizardInputField
        control={control}
        name={ProviderCredentialFields.HUAWEICLOUD_ACCESS_KEY_ID}
        type="text"
        label="Access Key ID"
        labelPlacement="inside"
        placeholder="e.g. AKxxxxxxxxxxxx"
        variant="bordered"
        isRequired
      />
      <WizardInputField
        control={control}
        name={ProviderCredentialFields.HUAWEICLOUD_SECRET_ACCESS_KEY}
        type="password"
        label="Secret Access Key"
        labelPlacement="inside"
        placeholder="Enter the secret access key"
        variant="bordered"
        isRequired
      />
      <WizardInputField
        control={control}
        name={ProviderCredentialFields.HUAWEICLOUD_REGION}
        type="text"
        label="Region"
        labelPlacement="inside"
        placeholder="e.g. cn-north-4 (defaults to cn-north-4)"
        variant="bordered"
      />
      <WizardInputField
        control={control}
        name={ProviderCredentialFields.HUAWEICLOUD_PROJECT_ID}
        type="text"
        label="Project ID"
        labelPlacement="inside"
        placeholder="e.g. 0a1234567890abcdef1234567890abcd"
        variant="bordered"
      />
      <WizardInputField
        control={control}
        name={ProviderCredentialFields.HUAWEICLOUD_DOMAIN_ID}
        type="text"
        label="Domain ID"
        labelPlacement="inside"
        placeholder="e.g. 1a234567890abcdef1234567890abcd"
        variant="bordered"
      />
      <div className="text-default-400 text-xs">
        Keys never leave your browser unencrypted and are stored as secrets in
        the backend. Rotate the key from Huawei Cloud IAM console anytime if
        needed.
      </div>
    </>
  );
};
