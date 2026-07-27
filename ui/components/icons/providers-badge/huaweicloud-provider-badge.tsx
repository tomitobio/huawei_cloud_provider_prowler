import { FC } from "react";

import { IconSvgProps } from "@/types";

export const HuaweiCloudProviderBadge: FC<IconSvgProps> = ({
  size,
  width,
  height,
  ...props
}) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true"
    fill="none"
    focusable="false"
    height={size || height}
    role="presentation"
    viewBox="0 0 256 256"
    width={size || width}
    {...props}
  >
    <g fill="none">
      <rect width="256" height="256" fill="#f4f2ed" rx="60" />
      <g transform="translate(38, 48) scale(1.8)">
        {/* Huawei petal logo - 4 curved petals */}
        <path
          fill="#CF0A2C"
          d="M50,0C50,0,50,25,50,25C50,40,40,50,25,50C25,50,0,50,0,50C0,50,0,25,0,25C0,10,10,0,25,0C25,0,50,0,50,0Z"
        />
        <path
          fill="#CF0A2C"
          d="M100,0C100,0,100,25,100,25C100,40,90,50,75,50C75,50,50,50,50,50C50,50,50,25,50,25C50,10,60,0,75,0C75,0,100,0,100,0Z"
        />
        <path
          fill="#CF0A2C"
          d="M50,50C50,50,50,75,50,75C50,90,40,100,25,100C25,100,0,100,0,100C0,100,0,75,0,75C0,60,10,50,25,50C25,50,50,50,50,50Z"
        />
        <path
          fill="#CF0A2C"
          d="M100,50C100,50,100,75,100,75C100,90,90,100,75,100C75,100,50,100,50,100C50,100,50,75,50,75C50,60,60,50,75,50C75,50,100,50,100,50Z"
        />
      </g>
    </g>
  </svg>
);
