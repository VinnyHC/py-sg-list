# AWS Security Groups Exporter

This script fetches details of security groups from multiple AWS regions and exports them to a CSV file. The CSV file contains information about the inbound and outbound rules of each security group, including IP ranges and protocol details.

## Features

- Fetch security group details from multiple AWS regions.
- Extract inbound and outbound rules, including IP permissions.
- Export the details to a CSV file for easy analysis and reporting.

## Requirements

- Python 3.x
- `boto3` library

## Setup

1. **Install boto3**

   Make sure you have `boto3` installed. You can install it using pip:

   ```bash
   pip install boto3
   ```

2. **AWS Credentials**

   Ensure that your AWS credentials are configured. You can set up credentials by following the [AWS CLI configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

## Environment Variables

- `AWS_PROFILE`: The AWS profile name to use for the session.
- `REGIONS`: A space-separated list of regions to fetch the security groups from. If not provided, the script defaults to the exported variable `AWS_REGION` if that is also unset it defaults to `us-east-1`.

## Usage

1. **Set the required environment variables:**

   ```bash
   export AWS_PROFILE=your_aws_profile
   export REGIONS="us-east-1 us-west-2"
   ```

2. **Run the script:**

   ```bash
   python aws_security_groups_exporter.py
   ```

3. **Output:**

   The script generates a `security_groups.csv` file in the current directory, containing the details of the security groups.
