import os
import boto3
import csv

def describe_security_groups(session, region):
    ec2_client = session.client('ec2', region_name=region)
    response = ec2_client.describe_security_groups()
    return response['SecurityGroups']


def main():
    profile_name = os.getenv("AWS_PROFILE")
    session = boto3.Session(profile_name=profile_name)
    regions = os.getenv("REGIONS", os.getenv("AWS_REGION", "us-east-1")).split(" ")
    all_security_groups = []

    for region in regions:
        print(f"Fetching security groups for region: {region}")
        security_groups = describe_security_groups(session, region)
        for sg in security_groups:
            for rule in sg['IpPermissions']:
                all_security_groups.append({
                    'Region': region,
                    'GroupId': sg['GroupId'],
                    'GroupName': sg['GroupName'],
                    'Description': sg.get('Description', ''),
                    'IpProtocol': rule.get('IpProtocol', 'N/A'),
                    'FromPort': rule.get('FromPort', 'N/A'),
                    'ToPort': rule.get('ToPort', 'N/A'),
                    'IpRanges': ','.join([r['CidrIp'] for r in rule.get('IpRanges', [])]),
                    'Ipv6Ranges': ','.join([r['CidrIpv6'] for r in rule.get('Ipv6Ranges', [])]),
                    'PrefixListIds': ','.join([r['PrefixListId'] for r in rule.get('PrefixListIds', [])]),
                    'UserIdGroupPairs': ','.join([f"{p['UserId']}:{p['GroupId']}" for p in rule.get('UserIdGroupPairs', [])]),
                    'Direction': 'Inbound'
                })
            for rule in sg['IpPermissionsEgress']:
                all_security_groups.append({
                    'Region': region,
                    'GroupId': sg['GroupId'],
                    'GroupName': sg['GroupName'],
                    'Description': sg.get('Description', ''),
                    'IpProtocol': rule.get('IpProtocol', 'N/A'),
                    'FromPort': rule.get('FromPort', 'N/A'),
                    'ToPort': rule.get('ToPort', 'N/A'),
                    'IpRanges': ','.join([r['CidrIp'] for r in rule.get('IpRanges', [])]),
                    'Ipv6Ranges': ','.join([r['CidrIpv6'] for r in rule.get('Ipv6Ranges', [])]),
                    'PrefixListIds': ','.join([r['PrefixListId'] for r in rule.get('PrefixListIds', [])]),
                    'UserIdGroupPairs': ','.join([f"{p['UserId']}:{p['GroupId']}" for p in rule.get('UserIdGroupPairs', [])]),
                    'Direction': 'Outbound'
                })

    # Write the details to a CSV file
    with open('security_groups.csv', 'w', newline='') as csvfile:
        fieldnames = ['Region', 'GroupId', 'GroupName', 'Description',
                      'IpProtocol', 'FromPort', 'ToPort', 'IpRanges',
                      'Ipv6Ranges', 'PrefixListIds', 'UserIdGroupPairs', 'Direction']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for sg in all_security_groups:
            writer.writerow(sg)


if __name__ == '__main__':
    main()
