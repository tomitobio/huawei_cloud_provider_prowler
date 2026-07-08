#!/usr/bin/env bash
set -euo pipefail

PYTHON=${1:-python}
PROWLER_PKG=$($PYTHON -c "import prowler; import os; print(os.path.dirname(prowler.__file__))")

echo "Prowler package at: $PROWLER_PKG"

# Copy huaweicloud provider into installed prowler
cp -r prowler/providers/huaweicloud "$PROWLER_PKG/providers/"
echo "Provider copied."

# Copy compliance benchmark into installed prowler
mkdir -p "$PROWLER_PKG/compliance/huaweicloud"
cp prowler/compliance/huaweicloud/*.json "$PROWLER_PKG/compliance/huaweicloud/"
cp prowler/compliance/huaweicloud/__init__.py "$PROWLER_PKG/compliance/huaweicloud/"
echo "Compliance copied."

# Apply patches to prowler core files
cp patches/lib/check/check.py "$PROWLER_PKG/lib/check/check.py"
cp patches/lib/check/models.py "$PROWLER_PKG/lib/check/models.py"
cp patches/lib/outputs/finding.py "$PROWLER_PKG/lib/outputs/finding.py"
cp patches/lib/outputs/outputs.py "$PROWLER_PKG/lib/outputs/outputs.py"
cp patches/providers/common/provider.py "$PROWLER_PKG/providers/common/provider.py"
echo "Patches applied."

echo "Setup complete."
